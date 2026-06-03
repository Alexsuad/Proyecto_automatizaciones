# File: src/agents/prompts/phase_prompts.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Registro central de tareas y alcances de contexto por fase.
# Rol: Desacoplar las directivas específicas de la factoría genérica.
# ──────────────────────────────────────────────────────────────────────

from typing import Dict, List, TypedDict

class PhaseConfig(TypedDict):
    task_instruction: str
    context_keys: List[str]

# Registro principal de configuraciones por fase
PHASE_REGISTRY: Dict[str, PhaseConfig] = {
    "F01": {
        "task_instruction": (
            "Analiza el conocimiento actual en F01. Si la idea de negocio es válida, "
            "propone campos iniciales. Si es insuficiente, bloquea y pide lo que falta."
        ),
        "context_keys": ["idea_description"]  # Contexto súper reducido para F01
    }
}
