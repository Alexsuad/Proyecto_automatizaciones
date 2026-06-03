# File: scripts/validate_case.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Validar de forma no destructiva y determinista la estructura
#            mínima de un Caso de Negocio según la especificación v0.2.
# Rol: Herramienta de solo lectura para diagnóstico de integridad.
# ──────────────────────────────────────────────────────────────────────

import argparse
import sys
from pathlib import Path

# Elementos obligatorios definidos en la SPEC v0.2
obligatory_files = [
    "case_config.yml",
    "README.md"
]

obligatory_dirs = [
    "inputs",
    "sources",
    "dmv",
    "output",
    "reports",
    "reports/tmp",
    "reports/official"
]

def validate_case_structure(case_path_str: str) -> int:
    """
    Inspecciona la ruta de un caso y reporta el estado de su estructura.
    Retorna:
      - 0 si es PASS (estructura completa)
      - 1 si es FAIL (faltan elementos obligatorios)
      - 2 en caso de errores inesperados (ej. ruta inexistente)
    """
    case_path = Path(case_path_str).resolve()
    
    # 1. Protección básica: Existencia y tipo
    if not case_path.exists():
        print(f"ERROR: La ruta especificada no existe: {case_path}")
        return 2
        
    if not case_path.is_dir():
        print(f"ERROR: La ruta especificada no es un directorio: {case_path}")
        return 2

    # 2. Protección: Evitar validar la raíz del repositorio
    # Si la ruta parece ser la raíz del repositorio, se bloquea para evitar
    # validar accidentalmente el proyecto completo como si fuera un caso.
    config_file = case_path / "case_config.yml"
    
    # Si la ruta parece ser la raíz (tiene pyproject.toml y no tiene case_config.yml), abortar
    if (case_path / "pyproject.toml").exists() and not config_file.exists():
        print("ERROR: Se detectó la raíz del repositorio. No es un directorio de caso válido.")
        return 2

    print("======================================================================")
    print(f"REPORTE DE VALIDACIÓN DE ESTRUCTURA DE CASO")
    print(f"Ruta analizada: {case_path}")
    print("======================================================================\n")

    elements_found = []
    elements_missing = []

    # 3. Validar archivos obligatorios
    for file_name in obligatory_files:
        file_path = case_path / file_name
        if file_path.is_file():
            elements_found.append(f"[ARCHIVO] {file_name}")
        else:
            elements_missing.append(f"[ARCHIVO] {file_name}")

    # 4. Validar directorios obligatorios
    for dir_name in obligatory_dirs:
        dir_path = case_path / dir_name
        if dir_path.is_dir():
            elements_found.append(f"[DIR]     {dir_name}")
        else:
            elements_missing.append(f"[DIR]     {dir_name}")

    # 5. Analizar archivo case_config.yml si existe (sin dependencias externas)
    config_status = "No verificado (archivo no encontrado)"
    if config_file.is_file():
        try:
            content = config_file.read_text(encoding="utf-8").strip()
            if content:
                config_status = "Existe (no vacío)"
            else:
                config_status = "Existe (vacío - ALERTA)"
                elements_missing.append("[CONTENIDO] case_config.yml está vacío")
        except Exception as e:
            config_status = f"Error de lectura: {str(e)}"
            elements_missing.append(f"[CONTENIDO] Error al leer case_config.yml: {str(e)}")

    # 6. Validar estado de archive_manifest.yml (Opcional)
    manifest_file = case_path / "archive_manifest.yml"
    archive_status = "NO ARCHIVADO (sin archive_manifest.yml)"
    if manifest_file.is_file():
        archive_status = "ARCHIVADO (archive_manifest.yml presente)"

    # 7. Imprimir reporte detallado
    print("--- ELEMENTOS ENCONTRADOS ---")
    if elements_found:
        for item in elements_found:
            print(f"  ✅ {item}")
    else:
        print("  Ninguno")
    print("")

    print("--- ELEMENTOS FALTANTES ---")
    if elements_missing:
        for item in elements_missing:
            print(f"  ❌ {item}")
    else:
        print("  Ninguno")
    print("")

    print("--- INFORMACIÓN EXTRA ---")
    print(f"  - Configuración: {config_status}")
    print(f"  - Archivamiento: {archive_status}")
    print("")

    # 8. Evaluación de resultado final
    print("======================================================================")
    if not elements_missing:
        print("RESULTADO DE VALIDACIÓN: PASS ✅")
        print("El caso cumple con todas las directrices de la SPEC v0.2.")
        print("======================================================================")
        return 0
    else:
        print("RESULTADO DE VALIDACIÓN: FAIL ❌")
        print("Faltan componentes obligatorios en la estructura del caso.")
        print("======================================================================")
        return 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validador estructural de casos (SPEC v0.2)")
    parser.add_argument("--case-path", required=True, help="Ruta al directorio del caso")
    args = parser.parse_args()
    
    try:
        exit_code = validate_case_structure(args.case_path)
        sys.exit(exit_code)
    except Exception as e:
        print(f"ERROR INESPERADO: {str(e)}")
        sys.exit(2)
