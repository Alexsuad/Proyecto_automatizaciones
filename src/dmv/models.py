# File: src/dmv/models.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Modelos de datos para el Documento Maestro Vivo (DMV).
# Rol: Esquemas de validación determinista mediante Pydantic.
# ──────────────────────────────────────────────────────────────────────

from datetime import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, ConfigDict

class ChangeMeta(BaseModel):
    """Metadatos de trazabilidad para cada cambio."""
    updated_at: str = Field(default_factory=lambda: datetime.now().isoformat())
    updated_by: str  # ROLE_ID (ej: "ESTRATEGICO", "MERCADO")
    source_phase: str  # F01-F12
    confidence_score: float = Field(default=1.0, ge=0.0, le=1.0)

class RiskItem(BaseModel):
    """Ítem de riesgo persistente en el Risk Board."""
    risk_id: str
    level: str  # ANNOTATED, WARNING, CRITICAL (DANGER_ZONE)
    description: str
    origin_phase: str
    status: str = "ACTIVE"
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())

class PhaseState(BaseModel):
    """Estado de una fase específica."""
    status: str = "IDLE"  # IDLE, EXECUTING, AUDITING, CLOSED, PAUSED
    last_update: Optional[str] = None

class DMVModel(BaseModel):
    """Esquema completo del Documento Maestro Vivo."""
    model_config = ConfigDict(extra='allow') # Permitir campos extra de negocio

    project_metadata: Dict[str, Any] = Field(default_factory=lambda: {
        "name": "Nuevo Proyecto",
        "sector": "General"
    })
    
    phase_control: Dict[str, PhaseState] = Field(default_factory=lambda: {
        f"F{i:02d}": PhaseState() for i in range(1, 13)
    })
    
    knowledge_base: Dict[str, Any] = Field(default_factory=dict)
    
    risk_board: List[RiskItem] = Field(default_factory=list)
    
    audit_log: List[Dict[str, Any]] = Field(default_factory=list)

    def add_audit_entry(self, field: str, old_value: Any, new_value: Any, meta: ChangeMeta):
        """Registra un cambio en el audit log."""
        self.audit_log.append({
            "field": field,
            "old_value": old_value,
            "new_value": new_value,
            "meta": meta.model_dump()
        })
