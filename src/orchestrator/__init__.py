# File: src/orchestrator/__init__.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Exportar clases y enums del orquestador de fases de negocio.
# Rol: Punto de acceso y definición pública del paquete del orquestador.
# ──────────────────────────────────────────────────────────────────────

from .controller import PhaseOrchestrator
from .states import PhaseStatus, OrchestratorEvent

