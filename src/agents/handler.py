# File: src/agents/handler.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Gestor de la interfaz de comunicación con agentes.
# Rol: Orquestar invocación, validación y reintentos (ARQ_10).
# ──────────────────────────────────────────────────────────────────────

import json
from .models import AgentRequest, AgentResponse
from .base_adapter import BaseAgentAdapter
from pydantic import ValidationError

class AgentInterfaceHandler:
    def __init__(self, adapter: BaseAgentAdapter, max_retries: int = 2):
        self.adapter = adapter
        self.max_retries = max_retries

    def invoke(self, request: AgentRequest) -> AgentResponse:
        """Invoca a un agente con lógica de reintento ante fallos de esquema."""
        attempts = 0
        last_error = ""

        while attempts <= self.max_retries:
            raw_response = self.adapter.call(request)
            
            try:
                # Intentar parsear y validar
                response_data = json.loads(raw_response)
                return AgentResponse.model_validate(response_data)
            
            except (json.JSONDecodeError, ValidationError) as e:
                attempts += 1
                last_error = str(e)
                print(f"[RETRY_LOOP] Intento {attempts} fallido. Error: {type(e).__name__}")
                # Aquí se añadiría un prompt de corrección en una V2 real

        # Si agotamos reintentos, devolvemos un objeto de fallo técnico
        return AgentResponse(
            status="BLOCKED",
            reason=f"Fallo crítico de comunicación tras {self.max_retries} reintentos. Error: {last_error}",
            user_message="Lo siento, el sistema de análisis ha tenido un error técnico. Por favor, reintenta en unos momentos.",
            internal_narrative=f"MAX_RETRIES_EXCEEDED: {last_error}",
            confidence_score=0.0
        )
