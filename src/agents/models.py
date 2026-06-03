# File: src/agents/models.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Modelos de datos para la comunicación con agentes.
# Rol: Esquemas Pydantic para Request y Response (ARQ_10).
# ──────────────────────────────────────────────────────────────────────

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class AgentRequest(BaseModel):
    """Contrato de entrada para invocar a un perfil/agente."""
    request_id: str
    phase_id: str
    active_profile: str
    command: str
    dmv_snapshot: Dict[str, Any]
    constraints: List[str] = Field(default_factory=list)
    assembled_prompt: str = ""

class AgentResponse(BaseModel):
    """Contrato de respuesta obligatoria de un perfil/agente."""
    status: str  # SUCCESS, FAIL, BLOCKED, NEEDS_INPUT
    reason: str  # Justificación obligatoria (ARQ_10)
    user_message: str
    internal_narrative: str
    proposed_updates: Dict[str, Any] = Field(default_factory=dict)
    confidence_score: float = Field(default=1.0, ge=0.0, le=1.0)
    risk_flags: List[str] = Field(default_factory=list)
    gate_signal: bool = False
