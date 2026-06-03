import json
from .base_adapter import BaseAgentAdapter
from .models import AgentRequest

class MockAgentAdapter(BaseAgentAdapter):
    def __init__(self):
        self.fail_next_count = 0

    def call(self, request: AgentRequest) -> str:
        """Simula la respuesta de una IA en formato string/JSON."""
        
        # En el Mock ignoramos el request.assembled_prompt, pero un adapter real lo usaría.
        
        # Simulación de error de formato (Retry Loop Trigger)
        
        # Simulación de error de formato (Retry Loop Trigger)
        if self.fail_next_count > 0:
            self.fail_next_count -= 1
            return "RESPUESTA_INVALIDA_Y_SIN_JSON"

        # Respuesta genérica válida
        response = {
            "status": "SUCCESS",
            "reason": "Análisis completado satisfactoriamente según el snapshot del DMV.",
            "user_message": "He revisado tu idea de negocio y parece viable.",
            "internal_narrative": "Validación exitosa de precondiciones de fase.",
            "proposed_updates": {"target_market": "Logística B2B"},
            "confidence_score": 0.95,
            "risk_flags": [],
            "gate_signal": True
        }
        return json.dumps(response)

    def set_fail_sequence(self, count: int):
        """Prepara al mock para fallar las próximas N veces."""
        self.fail_next_count = count
