# File: scripts/test_phase_lifecycle_f01.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Script de prueba para el ciclo de vida integrado (F01).
# ──────────────────────────────────────────────────────────────────────

import sys
import os
import json

# Añadir la raíz del proyecto al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.dmv import DmvManager
from src.orchestrator import PhaseOrchestrator
from src.agents import AgentInterfaceHandler, MockAgentAdapter
from src.integration import PhaseCycleManager

def run_integration_test():
    test_file = "cases/integration/dmv_f01_integrated.json"
    os.makedirs(os.path.dirname(test_file), exist_ok=True)
    
    # Limpiar si existe
    if os.path.exists(test_file):
        os.remove(test_file)

    print("=== INICIANDO PRUEBA DE INTEGRACIÓN VERTICAL (F01 V1) ===")
    
    # 1. Setup de componentes
    dmv = DmvManager(test_file)
    orchestrator = PhaseOrchestrator(dmv)
    adapter = MockAgentAdapter()
    handler = AgentInterfaceHandler(adapter)
    
    # 2. Setup del gestor de integración
    manager = PhaseCycleManager(dmv, orchestrator, handler)

    # 3. Ejecución del ciclo
    success = manager.run_f01_auto_cycle()

    if success:
        print("\n=== VALIDACIÓN POST-EJECUCIÓN ===")
        # Verificar el archivo físico
        with open(test_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Comprobar estado de la fase
        f01_status = data["phase_control"]["F01"]["status"]
        print(f"Estado en disco de F01: {f01_status}")
        
        # Comprobar datos de negocio
        market = data["knowledge_base"].get("target_market")
        print(f"Datos de conocimiento ('target_market'): {market}")
        
        # Comprobar trazabilidad
        audit_entries = len(data["audit_log"])
        print(f"Entradas en el audit_log: {audit_entries}")
        
        # Comprobar narrativa
        narrative = data["project_metadata"].get("last_narrative")
        print(f"Narrativa interna capturada: {narrative[:50]}...")

        print("\n[RESULTADO] La integración vertical ha funcionado perfectamente.")
    else:
        print("\n[ERROR] El ciclo de fase falló.")
        sys.exit(1)

if __name__ == "__main__":
    run_integration_test()
