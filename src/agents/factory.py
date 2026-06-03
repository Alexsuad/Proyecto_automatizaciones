# File: src/agents/factory.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Ensamblado dinámico de prompts.
# Rol: Factoría de instrucciones para los agentes.
# ──────────────────────────────────────────────────────────────────────

from typing import Dict, Any
from .prompts.global_layer import GLOBAL_RULES, JSON_SCHEMA_CONTRACT
from .prompts.ceo_layer import CEO_IDENTITY

class PromptFactory:
    """Clase encargada de construir el prompt final para la IA."""

    @staticmethod
    def build_prompt(profile_id: str, phase_id: str, dmv_context: Dict[str, Any], task_instruction: str = "", context_keys: list = None) -> str:
        """Ensambla las capas de prompt según el perfil y contexto."""
        
        # 1. Obtener ADN del perfil
        profile_dna = ""
        if profile_id == "ESTRATEGICO":
            profile_dna = CEO_IDENTITY
        else:
            profile_dna = f"### PERFIL: {profile_id}\nActúa según las directrices de tu rol."

        # 2. Filtrar Contexto del DMV (Snapshot)
        # Solo pasamos metadatos y la fase actual para evitar sobrecarga
        phase_data = dmv_context.get("phase_control", {}).get(phase_id, {})
        knowledge = dmv_context.get("knowledge_base", {})
        
        # Filtrado básico de contexto por scope
        filtered_knowledge = {k: v for k, v in knowledge.items() if k in context_keys} if context_keys else knowledge
        
        context_block = f"""
### CONTEXTO DEL PROYECTO (DMV SNAPSHOT)
- FASE ACTUAL: {phase_id}
- ESTADO DE FASE: {phase_data.get('status', 'IDLE')}
- CONOCIMIENTO ACTUAL: {filtered_knowledge}
"""

        # 3. Ensamblado final
        prompt = f"""
{GLOBAL_RULES}

{profile_dna}

{context_block}

{JSON_SCHEMA_CONTRACT}

### TAREA ESPECÍFICA
{task_instruction}
"""
        return prompt.strip()
