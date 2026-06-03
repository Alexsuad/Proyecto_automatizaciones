# File: scripts/init_case.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Inicializar un nuevo caso de negocio copiando la plantilla
#            maestra y sustituyendo los metadatos correspondientes.
# Rol: Herramienta de escritura no destructiva para despliegue de casos.
# ──────────────────────────────────────────────────────────────────────

import argparse
import sys
import shutil
import re
from datetime import datetime
from pathlib import Path

# Añadimos el directorio raíz para permitir importar el módulo de validación
sys.path.append(str(Path(__file__).resolve().parent))
from validate_case import validate_case_structure

def is_valid_snake_case(case_id: str) -> bool:
    """Valida que el case_id sea un snake_case simple (letras, números y guiones bajos)."""
    return bool(re.match(r"^[a-z0-9_]+$", case_id))

def init_new_case(case_id: str, case_name: str, sector: str, description: str, target_root_str: str) -> int:
    """
    Copia la plantilla de caso a la ruta destino, reemplaza los placeholders en la
    configuración y el README, y valida la estructura creada.
    """
    # 1. Validar formato de case_id
    if not is_valid_snake_case(case_id):
        print(f"ERROR: El case_id '{case_id}' no es un snake_case válido (solo minúsculas, números y '_').")
        return 1

    template_path = Path(__file__).resolve().parent.parent / "core" / "templates" / "case_template"
    target_root = Path(target_root_str).resolve()
    target_path = target_root / case_id

    print(f"Plantilla origen: {template_path}")
    print(f"Destino:          {target_path}")

    # 2. Validaciones iniciales de rutas
    if not template_path.is_dir():
        print(f"ERROR: La plantilla origen no existe o no es un directorio: {template_path}")
        return 2

    if target_path.exists():
        print(f"ERROR: El directorio de destino ya existe: {target_path}. Cancelando inicialización para evitar sobrescrituras.")
        return 1

    try:
        # 3. Crear árbol de directorios y copiar contenidos de la plantilla
        print("\nCopiando estructura de plantilla...")
        shutil.copytree(template_path, target_path)
        print("Estructura copiada con éxito.")

        # 4. Preparar metadatos para reemplazo
        created_at_iso = datetime.now().isoformat()
        
        replacements = {
            "__case_id__": case_id,
            "__case_name__": case_name,
            "__sector__": sector,
            "__description__": description,
            "__created_at__": created_at_iso
        }

        # 5. Modificar case_config.yml y README.md
        files_to_process = ["case_config.yml", "README.md"]
        for file_name in files_to_process:
            file_path = target_path / file_name
            if file_path.is_file():
                content = file_path.read_text(encoding="utf-8")
                # Sustituir todos los placeholders
                for placeholder, replacement in replacements.items():
                    content = content.replace(placeholder, replacement)
                file_path.write_text(content, encoding="utf-8")
                print(f"  Modificado: {file_name}")

        # 6. Validar estructura del caso creado
        print("\nEjecutando validación estructural sobre el caso creado...")
        exit_code = validate_case_structure(str(target_path))
        return exit_code

    except Exception as e:
        print(f"ERROR INESPERADO durante la copia/inicialización: {str(e)}")
        print("No se realizó limpieza automática para evitar borrados no autorizados.")
        if target_path.exists():
            print(f"Revisa manualmente el directorio destino: {target_path}")
        return 2

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inicializador estructural de nuevos casos (SPEC v0.2)")
    parser.add_argument("--case-id", required=True, help="Identificador del caso en snake_case")
    parser.add_argument("--case-name", required=True, help="Nombre legible del caso")
    parser.add_argument("--sector", required=True, help="Sector del negocio analizado")
    parser.add_argument("--description", required=True, help="Breve descripción del caso")
    parser.add_argument("--target-root", default="cases", help="Directorio raíz destino para el caso")
    args = parser.parse_args()

    sys.exit(init_new_case(
        case_id=args.case_id,
        case_name=args.case_name,
        sector=args.sector,
        description=args.description,
        target_root_str=args.target_root
    ))
