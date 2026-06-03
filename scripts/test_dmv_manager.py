# File: scripts/test_dmv_manager.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Script de prueba para el DMV Manager.
# ──────────────────────────────────────────────────────────────────────

import sys
import os

# Añadir la raíz del proyecto al path para poder importar src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.dmv.manager import DmvManager
from pydantic import ValidationError

def test_dmv_ops():
    test_file = "cases/logistica/dmv_test.json"
    
    # Asegurar que el directorio existe
    os.makedirs(os.path.dirname(test_file), exist_ok=True)
    
    # Limpiar archivo previo si existe
    if os.path.exists(test_file):
        os.remove(test_file)

    print("--- 1. Inicialización ---")
    manager = DmvManager(test_file)
    print("DMV cargado/creado con éxito.")

    print("\n--- 2. Escritura de Conocimiento ---")
    manager.update_knowledge(
        key="business_idea",
        value="Servicio de optimización de rutas con IA",
        role="ESTRATEGICO",
        phase="F01"
    )
    print(f"Campo 'business_idea' actualizado: {manager.get_value('business_idea')}")

    print("\n--- 3. Gestión de Riesgos ---")
    manager.add_risk(
        risk_id="R001",
        level="CRITICAL",
        description="Falta de datos históricos del cliente",
        phase="F01"
    )
    print(f"Riesgos en tablero: {len(manager.data.risk_board)}")
    print(f"¿Tiene riesgos críticos?: {manager.data.project_metadata.get('has_active_critical_risks')}")

    print("\n--- 4. Persistencia ---")
    manager.save()
    if os.path.exists(test_file):
        print(f"Archivo guardado en {test_file}")
    
    print("\n--- 5. Validación de Audit Log ---")
    last_log = manager.data.audit_log[-1]
    print(f"Último cambio registrado: {last_log['field']} por {last_log['meta']['updated_by']}")

    print("\n--- 6. Prueba de Fallo de Validación (Simulada) ---")
    try:
        # Intentar forzar un tipo incorrecto en un campo estructurado (si lo hubiera en el modelo)
        # Como knowledge_base es dict[str, Any], probaremos a cargar un JSON corrupto
        with open(test_file, 'w') as f:
            f.write('{"invalid": json}')
        DmvManager(test_file)
    except Exception as e:
        print(f"Capturado error esperado al cargar JSON inválido: {type(e).__name__}")

    print("\n--- TEST FINALIZADO CON ÉXITO ---")

if __name__ == "__main__":
    test_dmv_ops()
