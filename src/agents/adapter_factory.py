# File: src/agents/adapter_factory.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Selector dinámico de adaptadores de IA.
# Rol: Factory Pattern para instanciar el motor configurado.
# ──────────────────────────────────────────────────────────────────────

import os
from typing import Type
from .base_adapter import BaseAgentAdapter
from .mock_adapter import MockAgentAdapter

class AgentAdapterFactory:
    """Gestiona la instanciación del adaptador configurado en el entorno."""

    @staticmethod
    def get_adapter() -> BaseAgentAdapter:
        """
        Lee la variable de entorno AGENT_ADAPTER_TYPE y devuelve el adaptador correspondiente.
        Por defecto devuelve MockAgentAdapter si no está definida o es desconocida.
        """
        adapter_type = os.getenv("AGENT_ADAPTER_TYPE", "MOCK").upper()

        if adapter_type == "MOCK":
            return MockAgentAdapter()
        
        # Próximamente: GEMINI, ANTIGRAVITY, etc.
        # elif adapter_type == "GEMINI":
        #     return GeminiAdapter()
        
        print(f"[WARNING] Tipo de adaptador '{adapter_type}' no soportado. Usando MOCK por defecto.")
        return MockAgentAdapter()
