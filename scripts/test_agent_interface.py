# File: scripts/test_agent_interface.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Script de prueba para el Agent Interface Handler.
# ──────────────────────────────────────────────────────────────────────

import sys
import os

# Añadir la raíz del proyecto al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.agents import AgentInterfaceHandler, AgentRequest, MockAgentAdapter

def test_interface_scenarios():
    adapter = MockAgentAdapter()
    handler = AgentInterfaceHandler(adapter, max_retries=2)
    
    dummy_request = AgentRequest(
        request_id="REQ_001",
        phase_id="F01",
        active_profile="ESTRATEGICO",
        command="ANALYZE",
        dmv_snapshot={"test": True}
    )

    print("--- ESCENARIO 1: Éxito Inmediato ---")
    res1 = handler.invoke(dummy_request)
    print(f"Status: {res1.status}, Reason: {res1.reason}")
    assert res1.status == "SUCCESS"

    print("\n--- ESCENARIO 2: Reintento Exitoso ---")
    adapter.set_fail_sequence(1) # Fallará una vez
    res2 = handler.invoke(dummy_request)
    print(f"Status: {res2.status}, Reason: {res2.reason}")
    assert res2.status == "SUCCESS"

    print("\n--- ESCENARIO 3: Agotamiento de Reintentos ---")
    adapter.set_fail_sequence(5) # Fallará hasta agotar reintentos (max=2)
    res3 = handler.invoke(dummy_request)
    print(f"Status: {res3.status}, Reason: {res3.reason}")
    assert res3.status == "BLOCKED"
    assert "reintentos" in res3.reason

    print("\n--- TODOS LOS ESCENARIOS PROBADOS CON ÉXITO ---")

if __name__ == "__main__":
    test_interface_scenarios()
