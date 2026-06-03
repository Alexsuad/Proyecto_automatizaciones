# File: src/dmv/manager.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Lógica de gestión del Documento Maestro Vivo (DMV).
# Rol: Controlador de lectura, escritura y validación de datos.
# ──────────────────────────────────────────────────────────────────────

import json
import os
from .models import DMVModel, ChangeMeta, RiskItem

class DmvManager:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data: DMVModel = self._load_initial()

    def _load_initial(self) -> DMVModel:
        """Carga el DMV desde disco o crea uno nuevo si no existe."""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as f:
                content = json.load(f)
                return DMVModel.model_validate(content)
        return DMVModel()

    def save(self):
        """Persiste el DMV en disco de forma atómica."""
        temp_path = f"{self.file_path}.tmp"
        try:
            with open(temp_path, 'w', encoding='utf-8') as f:
                f.write(self.data.model_dump_json(indent=2))
            # Sustitución atómica (en Windows os.replace maneja la sobrescritura)
            os.replace(temp_path, self.file_path)
        except Exception as e:
            if os.path.exists(temp_path):
                os.remove(temp_path)
            raise e

    def update_knowledge(self, key: str, value: any, role: str, phase: str):
        """
        Actualiza un campo en el knowledge_base validando permisos.
        (En esta V1 la validación de permisos es una comprobación de rol básica).
        """
        old_value = self.data.knowledge_base.get(key)
        
        # Simulación de validación de permisos definida en ARQ_07
        # Por ahora, solo registramos quién hace el cambio
        meta = ChangeMeta(updated_by=role, source_phase=phase)
        
        self.data.knowledge_base[key] = value
        self.data.add_audit_entry(f"knowledge_base.{key}", old_value, value, meta)
        
        # Actualizar estado de la fase si es necesario
        if phase in self.data.phase_control:
            self.data.phase_control[phase].status = "EXECUTING"
            self.data.phase_control[phase].last_update = meta.updated_at

    def add_risk(self, risk_id: str, level: str, description: str, phase: str):
        """Añade un riesgo al Risk Board."""
        risk = RiskItem(
            risk_id=risk_id,
            level=level,
            description=description,
            origin_phase=phase
        )
        self.data.risk_board.append(risk)
        
        # Si es crítico, se marca como potencial DANGER_ZONE
        if level == "CRITICAL":
            self.data.project_metadata["has_active_critical_risks"] = True

    def get_value(self, key: str):
        """Lectura segura del knowledge base."""
        return self.data.knowledge_base.get(key)
