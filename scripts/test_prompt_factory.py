# File: scripts/test_prompt_factory.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Prueba unitaria de la PromptFactory.
# ──────────────────────────────────────────────────────────────────────

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agents import PromptFactory

def test_factory():
    print("=== PROBANDO PROMPT FACTORY (F01 V1) ===")
    
    # Simular un contexto de DMV
    mock_dmv_context = {
        "phase_control": {
            "F01": {"status": "EXECUTING"}
        },
        "knowledge_base": {
            "business_idea": "Una plataforma de gestión logística para PYMES."
        }
    }

    # 1. Caso: Director Estratégico en F01
    prompt = PromptFactory.build_prompt(
        "ESTRATEGICO", 
        "F01", 
        mock_dmv_context,
        task_instruction="Analiza la idea test.",
        context_keys=["business_idea"]
    )
    
    print("\n--- PROMPT GENERADO (EXTRACTO) ---")
    print(prompt[:500] + "...")
    
    # Validaciones básicas
    assert "### REGLAS GLOBALES" in prompt
    assert "DIRECTOR ESTRATÉGICO" in prompt
    assert "logística" in prompt
    assert "CONTRATO DE SALIDA" in prompt
    assert "Analiza la idea test." in prompt
    
    print("\n[SUCCESS] Prompt generado contiene todas las capas necesarias.")

    # 2. Caso: Detección de falta de datos (Simulado)
    empty_context = {
        "phase_control": {"F01": {"status": "EXECUTING"}},
        "knowledge_base": {}
    }
    prompt_empty = PromptFactory.build_prompt(
        "ESTRATEGICO", 
        "F01", 
        empty_context,
        task_instruction="Analiza la idea test.",
        context_keys=["business_idea"]
    )
    
    # Verificamos que el contexto vacío esté presente para que la IA decida bloquear
    assert "'knowledge_base': {}" in prompt_empty or "CONOCIMIENTO ACTUAL: {}" in prompt_empty
    print("[SUCCESS] Contexto vacío inyectado correctamente.")

if __name__ == "__main__":
    test_factory()
