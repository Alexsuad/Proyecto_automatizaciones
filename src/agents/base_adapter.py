# File: src/agents/base_adapter.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Definición del contrato común para adaptadores de IA.
# Rol: Interfaz abstracta (Protocolo) para multi-proveedor.
# ──────────────────────────────────────────────────────────────────────

from abc import ABC, abstractmethod
from .models import AgentRequest

class BaseAgentAdapter(ABC):
    """
    Clase base abstracta para todos los adaptadores de agentes.
    Define el contrato mínimo que debe cumplir cualquier motor de IA.
    """

    @abstractmethod
    def call(self, request: AgentRequest) -> str:
        """
        Envía una petición al motor de IA y devuelve la respuesta cruda (JSON string).
        
        Args:
            request (AgentRequest): El objeto con el prompt ensamblado y metadatos.
            
        Returns:
            str: Respuesta cruda del modelo (debe ser un JSON parseable).
        """
        pass
