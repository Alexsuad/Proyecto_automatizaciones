# File: src/orchestrator/controller.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Lógica de la máquina de estados del Orquestador de Fases.
# Rol: Controlador de transiciones, gates y bloqueos.
# ──────────────────────────────────────────────────────────────────────

from typing import Optional
from src.dmv.manager import DmvManager
from .states import PhaseStatus, OrchestratorEvent

class PhaseOrchestrator:
    def __init__(self, dmv_manager: DmvManager):
        self.dmv = dmv_manager

    def get_current_phase_status(self, phase_id: str) -> str:
        """Consulta el estado de una fase en el DMV."""
        phase = self.dmv.data.phase_control.get(phase_id)
        return phase.status if phase else "IDLE"

    def transition(self, phase_id: str, event: OrchestratorEvent) -> bool:
        """
        Intenta realizar una transición de estado basada en un evento.
        Implementación V1: Transiciones lineales básicas.
        """
        current_status = self.get_current_phase_status(phase_id)
        new_status = None

        # Lógica de transición (Basada en ARQ_06)
        if event == OrchestratorEvent.START_PHASE and current_status == PhaseStatus.IDLE:
            new_status = PhaseStatus.PREPARING
        
        elif event == OrchestratorEvent.READY_FOR_EXEC and current_status == PhaseStatus.PREPARING:
            new_status = PhaseStatus.EXECUTING
            
        elif event == OrchestratorEvent.FINISH_EXEC and current_status == PhaseStatus.EXECUTING:
            new_status = PhaseStatus.AUDITING
            
        elif event == OrchestratorEvent.SUCCESS_ALL and current_status == PhaseStatus.AUDITING:
            new_status = PhaseStatus.READY
            
        elif event == OrchestratorEvent.COMMIT_SESSION and current_status == PhaseStatus.READY:
            new_status = PhaseStatus.CLOSED

        if new_status:
            self._update_dmv_status(phase_id, new_status)
            return True
        
        return False

    def run_simple_gate(self, phase_id: str, criteria: bool) -> bool:
        """
        Ejecución simplificada de un gate.
        Si criteria es True, el gate pasa.
        """
        current_status = self.get_current_phase_status(phase_id)
        if current_status != PhaseStatus.AUDITING:
            return False
            
        if criteria:
            return self.transition(phase_id, OrchestratorEvent.SUCCESS_ALL)
        else:
            self._update_dmv_status(phase_id, PhaseStatus.BLOCKED)
            return False

    def _update_dmv_status(self, phase_id: str, status: PhaseStatus):
        """Actualiza físicamente el estado en el DMV."""
        if phase_id in self.dmv.data.phase_control:
            self.dmv.data.phase_control[phase_id].status = status
            # En V1 guardamos tras cada transición para asegurar persistencia
            self.dmv.save()
