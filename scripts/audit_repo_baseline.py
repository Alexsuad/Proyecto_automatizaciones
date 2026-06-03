# File: scripts/audit_repo_baseline.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: MVP de auditoría determinista del repositorio madre.
# Rol: Validador técnico de hechos de identidad, estructura y reglas del baseline.
# ──────────────────────────────────────────────────────────────────────

import os
import sys
import json
import subprocess

def parse_yaml_minimal(filepath):
    """Parsea de forma mínima un YAML plano con claves escalares.

    Este parser está diseñado para el MVP de auditoría y no pretende cubrir
    toda la especificación YAML. Soporta claves simples con valores string,
    booleanos y null. Las listas se detectan de forma básica solo cuando
    la validación específica lo requiere.

    No debe usarse como parser YAML general para validadores finales.
    """
    data = {}
    if not os.path.exists(filepath):
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ":" in line:
                key, val = line.split(":", 1)
                key = key.strip()
                val = val.strip()
                # Limpiar comillas y comentarios en la misma línea
                if "#" in val:
                    val = val.split("#", 1)[0].strip()
                val = val.strip("'\"")
                if val.lower() == "true":
                    val = True
                elif val.lower() == "false":
                    val = False
                elif val.lower() == "null":
                    val = None
                elif val.startswith("-"):
                    # Procesamiento simplificado para listas si es necesario
                    continue
                data[key] = val
    return data

def parse_yaml_list(filepath, list_key):
    """Extrae una lista YAML simple asociada a una clave de primer nivel."""
    values = []
    if not os.path.exists(filepath):
        return values

    inside_list = False

    with open(filepath, "r", encoding="utf-8") as file:
        for raw_line in file:
            line = raw_line.rstrip()

            if not line.strip() or line.strip().startswith("#"):
                continue

            if line.startswith(f"{list_key}:"):
                inside_list = True
                continue

            if inside_list:
                stripped = line.strip()

                if stripped.startswith("- "):
                    values.append(stripped[2:].strip().strip("'\""))
                    continue

                if not line.startswith(" ") and ":" in line:
                    break

    return values

def parse_spec_status(filepath):
    """Busca el estado de la especificación leyendo la línea de cabecera '## Estado'."""
    if not os.path.exists(filepath):
        return None
    status = None
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if "## Estado" in line:
                for j in range(i + 1, min(i + 5, len(lines))):
                    content = lines[j].strip()
                    if content:
                        status = content.rstrip(".")
                        break
                break
    return status

def run_audit():
    result = "PASS"
    blocking_errors = []
    warnings = []
    info = []
    checks = {}

    print("=== AUDITORÍA AGÉNTICA DEL BASELINE: MVP ===")
    print("Iniciando validaciones deterministas...\n")

    # A. Identidad del repositorio
    identity_path = "repo_identity.yml"
    if not os.path.exists(identity_path):
        blocking_errors.append("MISSING_REPO_IDENTITY: repo_identity.yml no existe en la raíz.")
        result = "FAIL"
        checks["identity"] = "MISSING"
    else:
        identity = parse_yaml_minimal(identity_path)
        checks["identity"] = "PRESENT"
        
        expected_fields = {
            "identity_version": "1.0",
            "repo_id": "proyecto_automatizaciones",
            "repo_name": "Proyecto Automatizaciones",
            "repo_role": "framework_mother",
            "repo_status": "active",
            "repo_owner": "equipo_tecnico",
            "contains_real_data": False,
            "allows_project_creation": True,
            "allows_framework_updates": False,
            "allows_case_data": False,
            "allows_artifact_generation": False,
            "allows_cleanup": False,
            "allows_extraction": False,
            "allows_retention_export": False,
        }

        for key, expected in expected_fields.items():
            actual = identity.get(key)
            if actual != expected:
                blocking_errors.append(f"IDENTITY_MISMATCH: campo {key} esperado '{expected}', real '{actual}'")
                result = "FAIL"

        required_approvals = {
            "cleanup",
            "extraction",
            "retention_export",
            "role_change",
            "manifest_change",
            "destructive_operation",
        }

        actual_approvals = set(parse_yaml_list(identity_path, "requires_human_approval_for"))
        missing_approvals = sorted(required_approvals - actual_approvals)

        if missing_approvals:
            blocking_errors.append(
                "MISSING_REQUIRED_APPROVALS: faltan aprobaciones requeridas: "
                + ", ".join(missing_approvals)
            )
            result = "FAIL"

        checks["required_approvals"] = {
            "expected": sorted(required_approvals),
            "actual": sorted(actual_approvals),
            "missing": missing_approvals,
        }

    # B. Documentos normativos (SPECs)
    specs = {
        "SPEC-001": "docs/specs/SPEC-001_artifact_manifest.md",
        "SPEC-002": "docs/specs/SPEC-002_estructura_repositorios_carpetas.md",
        "SPEC-003": "docs/specs/SPEC-003_repo_identity.md",
    }
    
    checks["specs"] = {}
    for spec_name, spec_path in specs.items():
        if not os.path.exists(spec_path):
            blocking_errors.append(f"MISSING_{spec_name}: archivo {spec_path} no existe.")
            result = "FAIL"
            checks["specs"][spec_name] = "MISSING"
        else:
            status = parse_spec_status(spec_path)
            if status != "Aprobado":
                blocking_errors.append(f"SPEC_NOT_APPROVED: {spec_name} tiene estado '{status}', esperado 'Aprobado'.")
                result = "FAIL"
                checks["specs"][spec_name] = f"NOT_APPROVED ({status})"
            else:
                checks["specs"][spec_name] = "APPROVED"

    # C. Estado esperado del manifiesto de artefactos
    manifest_path = "artifact_manifest.yml"
    if os.path.exists(manifest_path):
        manifest_data = parse_yaml_minimal(manifest_path)
        if not manifest_data:
            blocking_errors.append("INVALID_ARTIFACT_MANIFEST: El archivo existe pero está vacío o no se puede leer.")
            result = "FAIL"
            checks["manifest"] = "INVALID"
        else:
            checks["manifest"] = "PRESENT"
            info.append("ARTIFACT_MANIFEST_PRESENT: artifact_manifest.yml existe en la raíz del repositorio.")
            
            # Validación de coincidencia de rol
            role = manifest_data.get("repo_role")
            if role != "framework_mother":
                blocking_errors.append(f"ROLE_MANIFEST_MISMATCH: repo_role en manifest es '{role}', esperado 'framework_mother'.")
                result = "FAIL"
    else:
        warnings.append("MANIFEST_NOT_FOUND: artifact_manifest.yml no existe.")
        checks["manifest"] = "MISSING"

    # D. Zonas legacy o pendientes
    legacy_zones = [
        "docs_base",
        "output",
        "cases/logistica",
        "core/templates",
    ]
    checks["legacy_zones"] = {}
    for zone in legacy_zones:
        if os.path.exists(zone):
            warnings.append(f"LEGACY_ZONE_DETECTED: La carpeta '{zone}' existe en el working tree.")
            checks["legacy_zones"][zone] = "PRESENT"
        else:
            checks["legacy_zones"][zone] = "ABSENT"

    # E. Zonas temporales
    temporal_zones = [
        "reports/tmp",
        "_workspace_cases",
    ]
    # Buscar patrones como cases/tmp_*
    has_cases_tmp = False
    if os.path.exists("cases"):
        for item in os.listdir("cases"):
            if item.startswith("tmp_") and os.path.isdir(os.path.join("cases", item)):
                has_cases_tmp = True
                warnings.append(f"TEMPORAL_ZONE_DETECTED: La carpeta 'cases/{item}' existe.")
    
    checks["temporal_zones"] = {
        "cases_tmp": "PRESENT" if has_cases_tmp else "ABSENT"
    }
    
    for zone in temporal_zones:
        if os.path.exists(zone):
            info.append(f"TEMPORAL_ZONE_DETECTED: La carpeta '{zone}' existe.")
            checks["temporal_zones"][zone] = "PRESENT"
        else:
            checks["temporal_zones"][zone] = "ABSENT"

    # F. Prohibiciones fuertes
    forbidden_items = [
        ".env",
        ".venv",
        "__pycache__",
    ]
    checks["forbidden_items"] = {}
    
    # Comprobar si están trackeados por Git (versionados)
    def is_tracked(path):
        try:
            # git ls-files retornará contenido si está en el repositorio de Git
            res = subprocess.run(
                ["git", "ls-files", path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False
            )
            return len(res.stdout.strip()) > 0
        except Exception:
            return False

    for item in forbidden_items:
        found_tracked = is_tracked(item)
        if found_tracked:
            blocking_errors.append(f"FORBIDDEN_ITEM_VERSIONED: Se detectó '{item}' trackeado en Git (debe excluirse).")
            result = "FAIL"
            checks["forbidden_items"][item] = "PRESENT"
        else:
            # Si solo existe pero no está trackeado
            if os.path.exists(item):
                # .env no debería existir en absoluto en la raíz de framework_mother para evitar descuidos, pero es WARNING
                if item == ".env":
                    warnings.append("LOCAL_SECRETS_PRESENT: .env existe localmente (aunque está fuera de Git).")
                else:
                    info.append(f"LOCAL_EXCLUSION_ACTIVE: '{item}' existe localmente pero está correctamente excluido de Git.")
            checks["forbidden_items"][item] = "ABSENT"

    # Establecer resultado final si hay warnings pero no fallos bloqueantes
    if result == "PASS" and warnings:
        result = "PASS_WITH_WARNINGS"

    # Salida por consola
    print(f"RESULTADO DE AUDITORÍA: {result}")
    print("Exit codes: 0=PASS, 1=PASS_WITH_WARNINGS, 2=FAIL")
    print("───────────────────────────────────────")
    
    print("\n[OK] Validaciones Exitosas:")
    if result != "FAIL" and not blocking_errors:
        print("  - Identidad del repositorio válida para framework_mother.")
        print("  - Documentos normativos SPEC-001, SPEC-002 y SPEC-003 existen y están aprobados.")
    else:
        print("  - Algunas validaciones fallaron (ver sección de Bloqueos).")

    print("\n[WARNINGS] Advertencias:")
    for warn in warnings:
        print(f"  - {warn}")

    print("\n[INFO] Información General:")
    for i in info:
        print(f"  - {i}")

    print("\n[FAIL] Bloqueos Detectados:")
    if blocking_errors:
        for err in blocking_errors:
            print(f"  - {err}")
    else:
        print("  - Ninguno.")

    print("\n=== JSON_START ===")
    report_json = {
        "result": result,
        "blocking_errors": blocking_errors,
        "warnings": warnings,
        "info": info,
        "checks": checks
    }
    print(json.dumps(report_json, indent=2))
    print("=== JSON_END ===")
    
    if result == "FAIL":
        sys.exit(2)
    elif result == "PASS_WITH_WARNINGS":
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    run_audit()
