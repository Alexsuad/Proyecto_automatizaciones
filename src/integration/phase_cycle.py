# File: src/integration/phase_cycle.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Orquestación del ciclo de vida de una fase integrada.
# Rol: Pegamento (Glue) entre DMV, Orchestrator y Agents.
# ──────────────────────────────────────────────────────────────────────

from src.dmv import DmvManager
from src.orchestrator import PhaseOrchestrator, OrchestratorEvent, PhaseStatus
from src.agents import AgentInterfaceHandler, AgentRequest, PromptFactory
from src.agents.prompts.phase_prompts import PHASE_REGISTRY

class PhaseCycleManager:
    def __init__(self, dmv: DmvManager, orchestrator: PhaseOrchestrator, agent_handler: AgentInterfaceHandler):
        self.dmv = dmv
        self.orchestrator = orchestrator
        self.agent_handler = agent_handler

    def run_f01_auto_cycle(self) -> bool:
        """Ejecuta el ciclo vertical completo para la Fase 01."""
        phase_id = "F01"
        print(f"\n[CYCLE] Iniciando ciclo automatizado para {phase_id}")

        # 1. Preparación e Inicio
        if not self.orchestrator.transition(phase_id, OrchestratorEvent.START_PHASE):
            print("[ERROR] No se pudo iniciar la fase.")
            return False
        
        self.orchestrator.transition(phase_id, OrchestratorEvent.READY_FOR_EXEC)
        print(f"[STEP] Fase en estado: {self.orchestrator.get_current_phase_status(phase_id)}")

        # 2. Generación de Prompt y Petición
        phase_config = PHASE_REGISTRY.get(phase_id, {"task_instruction": "", "context_keys": []})
        
        print("\n--- [PROMPT GENERADO POR FACTORY] ---")
        generated_prompt = PromptFactory.build_prompt(
            profile_id="ESTRATEGICO",
            phase_id=phase_id,
            dmv_context=self.dmv.data.dict(),
            task_instruction=phase_config["task_instruction"],
            context_keys=phase_config["context_keys"]
        )
        # Mostrar extracto para observabilidad
        print(generated_prompt[:400] + "...")
        print("--------------------------------------\n")

        request = AgentRequest(
            request_id="INT_F01_001",
            phase_id=phase_id,
            active_profile="ESTRATEGICO",
            command="ANALYZE_IDEA",
            dmv_snapshot=self.dmv.data.project_metadata,
            constraints=["Idioma: Español", "Ser conciso"],
            assembled_prompt=generated_prompt
        )
        
        print("[STEP] Invocando Agent Interface Handler...")
        response = self.agent_handler.invoke(request)
        
        if response.status != "SUCCESS":
            print(f"[ERROR] El agente no pudo procesar la solicitud: {response.reason}")
            return False

        print(f"[STEP] Agente respondió SUCCESS. Razón: {response.reason}")

        # 3. Consolidación de Datos en el DMV
        print("[STEP] Consolidando propuestas del agente en el DMV...")
        for key, value in response.proposed_updates.items():
            self.dmv.update_knowledge(
                key=key,
                value=value,
                role=request.active_profile,
                phase=phase_id
            )
        
        # Inyectar también la narrativa interna en los metadatos del proyecto o log
        self.dmv.data.project_metadata["last_narrative"] = response.internal_narrative

        # 4. Auditoría y Cierre
        print("[STEP] Preparando auditoría (Transición a AUDITING)...")
        self.orchestrator.transition(phase_id, OrchestratorEvent.FINISH_EXEC)

        print("[STEP] Ejecutando Gate de validación...")
        # En V1 el gate es satisfactorio si el agente dio luz verde (gate_signal)
        gate_passed = self.orchestrator.run_simple_gate(phase_id, criteria=response.gate_signal)
        
        if not gate_passed:
            print("[ERROR] La fase no superó el gate de validación.")
            return False

        print("[STEP] Gate superado. Cerrando fase...")
        self.orchestrator.transition(phase_id, OrchestratorEvent.COMMIT_SESSION)
        
        final_status = self.orchestrator.get_current_phase_status(phase_id)
        print(f"[SUCCESS] Ciclo F01 finalizado. Estado final: {final_status}")
        
        return final_status == PhaseStatus.CLOSED
