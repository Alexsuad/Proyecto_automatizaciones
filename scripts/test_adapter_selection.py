# File: scripts/test_adapter_selection.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Verificar la selección dinámica de adaptadores.
# ──────────────────────────────────────────────────────────────────────

import os
import sys
from pathlib import Path

# Añadir raíz al path
sys.path.append(str(Path(__file__).parent.parent))

from src.agents import AgentAdapterFactory, MockAgentAdapter

def test_selection():
    print("=== PRUEBA DE SELECCIÓN DE ADAPTADORES ===")

    # 1. Probar por defecto (MOCK)
    if "AGENT_ADAPTER_TYPE" in os.environ:
        del os.environ["AGENT_ADAPTER_TYPE"]
    
    adapter = AgentAdapterFactory.get_adapter()
    print(f"[TEST 1] Sin variable definida: {type(adapter).__name__}")
    assert isinstance(adapter, MockAgentAdapter)

    # 2. Probar explícitamente MOCK
    os.environ["AGENT_ADAPTER_TYPE"] = "MOCK"
    adapter = AgentAdapterFactory.get_adapter()
    print(f"[TEST 2] Con MOCK: {type(adapter).__name__}")
    assert isinstance(adapter, MockAgentAdapter)

    # 3. Probar fallback (Tipo desconocido)
    os.environ["AGENT_ADAPTER_TYPE"] = "DESCONOCIDO"
    adapter = AgentAdapterFactory.get_adapter()
    print(f"[TEST 3] Con DESCONOCIDO: {type(adapter).__name__}")
    assert isinstance(adapter, MockAgentAdapter)

    print("\n[SUCCESS] Selección de adaptadores verificada correctamente.")

if __name__ == "__main__":
    test_selection()
