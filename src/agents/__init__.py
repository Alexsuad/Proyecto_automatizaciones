# File: src/agents/__init__.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Exportar clases y modelos del módulo de agentes de IA.
# Rol: Punto de acceso y definición pública del paquete de agentes.
# ──────────────────────────────────────────────────────────────────────

from .models import AgentRequest, AgentResponse
from .handler import AgentInterfaceHandler
from .base_adapter import BaseAgentAdapter
from .mock_adapter import MockAgentAdapter
from .adapter_factory import AgentAdapterFactory
from .factory import PromptFactory

