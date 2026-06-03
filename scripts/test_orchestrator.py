# File: scripts/test_orchestrator.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Script de prueba para el Orquestador de Fases V1.
# ──────────────────────────────────────────────────────────────────────

import sys
import os

# Añadir la raíz del proyecto al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.dmv.manager import DmvManager
from src.orchestrator.controller import PhaseOrchestrator
from src.orchestrator.states import PhaseStatus, OrchestratorEvent

def test_full_cycle():
    test_file = "cases/logistica/dmv_orchestrator_test.json"
    os.makedirs(os.path.dirname(test_file), exist_ok=True)
    
    # Limpiar
    if os.path.exists(test_file):
        os.remove(test_file)

    print("--- 1. Preparación ---")
    dmv = DmvManager(test_file)
    orchestrator = PhaseOrchestrator(dmv)
    phase = "F01"
    print(f"Estado inicial de {phase}: {orchestrator.get_current_phase_status(phase)}")

    print("\n--- 2. Inicio de Fase ---")
    orchestrator.transition(phase, OrchestratorEvent.START_PHASE)
    print(f"Estado tras START: {orchestrator.get_current_phase_status(phase)}")

    orchestrator.transition(phase, OrchestratorEvent.READY_FOR_EXEC)
    print(f"Estado tras READY_FOR_EXEC: {orchestrator.get_current_phase_status(phase)}")

    print("\n--- 3. Ejecución y Cierre de Trabajo ---")
    orchestrator.transition(phase, OrchestratorEvent.FINISH_EXEC)
    print(f"Estado tras FINISH_EXEC: {orchestrator.get_current_phase_status(phase)}")

    print("\n--- 4. Validación de Gate (Éxito) ---")
    success = orchestrator.run_simple_gate(phase, criteria=True)
    print(f"Gate superado: {success}")
    print(f"Estado tras Gate: {orchestrator.get_current_phase_status(phase)}")

    print("\n--- 5. Consolidación Final ---")
    orchestrator.transition(phase, OrchestratorEvent.COMMIT_SESSION)
    final_status = orchestrator.get_current_phase_status(phase)
    print(f"Estado FINAL: {final_status}")

    print("\n--- 6. Verificación de Atomicidad y Persistencia ---")
    if os.path.exists(test_file) and not os.path.exists(f"{test_file}.tmp"):
        print("Persistencia OK y archivo temporal eliminado (Atomicidad demostrada).")

    if final_status == PhaseStatus.CLOSED:
        print("\n--- TEST COMPLETADO EXITOSAMENTE ---")
    else:
        print("\n--- ERROR EN EL TEST ---")

if __name__ == "__main__":
    test_full_cycle()
