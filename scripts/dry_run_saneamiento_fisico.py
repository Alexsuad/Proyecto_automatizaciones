# File: scripts/dry_run_saneamiento_fisico.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Script de solo lectura para la verificación previa al saneamiento físico.
# Rol: Auditor determinista de gobernanza contra la estructura física real.
# ──────────────────────────────────────────────────────────────────────

import os
import sys
import json
import subprocess
import glob
import fnmatch
from datetime import datetime

def parse_repo_identity(filepath):
    """Parsea de forma mínima repo_identity.yml."""
    if not os.path.exists(filepath):
        return None
    data = {}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if ":" in line:
                    key, val = line.split(":", 1)
                    key = key.strip()
                    val = val.strip()
                    if "#" in val:
                        val = val.split("#", 1)[0].strip()
                    val = val.strip("'\"")
                    if val.lower() == "true":
                        val = True
                    elif val.lower() == "false":
                        val = False
                    elif val.lower() == "null":
                        val = None
                    data[key] = val
    except Exception:
        return None
    return data

def parse_artifact_manifest(filepath):
    """Parsea de forma estructurada artifact_manifest.yml."""
    if not os.path.exists(filepath):
        return None
    artifacts = []
    current_artifact = {}
    repo_role = None
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line_str = line.strip()
                if not line_str or line_str.startswith("#"):
                    continue
                
                if line_str.startswith("repo_role:"):
                    repo_role = line_str.split(":", 1)[1].strip().strip("'\"")
                    continue
                    
                if line_str.startswith("- path:"):
                    if current_artifact:
                        artifacts.append(current_artifact)
                    current_artifact = {
                        "path": line_str.split(":", 1)[1].strip().strip("'\"")
                    }
                elif current_artifact and ":" in line_str:
                    parts = line_str.split(":", 1)
                    key = parts[0].strip()
                    val = parts[1].strip().strip("'\"")
                    if val.lower() == "true":
                        val = True
                    elif val.lower() == "false":
                        val = False
                    elif val.lower() == "null":
                        val = None
                    current_artifact[key] = val
                    
            if current_artifact:
                artifacts.append(current_artifact)
    except Exception:
        return None
        
    return {
        "repo_role": repo_role,
        "artifacts": artifacts
    }

def is_git_repo(workspace_dir):
    """Valida si la ruta pertenece a un repositorio Git activo."""
    try:
        res = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=workspace_dir,
            check=False
        )
        return res.returncode == 0 and res.stdout.strip() == "true"
    except Exception:
        return False

def get_tracked_files(path, workspace_dir):
    """Devuelve la lista de archivos registrados en Git bajo una ruta específica usando el cwd correcto."""
    try:
        res = subprocess.run(
            ["git", "ls-files", path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=workspace_dir,
            check=False
        )
        if res.returncode == 0:
            return [line.strip() for line in res.stdout.splitlines() if line.strip()]
        return []
    except Exception:
        return []

def classify_line_dependency(line, pattern):
    """Separa dependencias en operativas (FAIL) e informativas/comentarios/help/docstrings (WARN)."""
    stripped = line.strip()
    
    # Comentario puro
    if stripped.startswith("#"):
        return "WARN"
        
    # Mensaje de ayuda o descripción típica de parser / argparse
    if "help=" in stripped or "help =" in stripped or "description=" in stripped:
        return "WARN"
        
    # Docstring o bloque multilínea de comentario
    if stripped.startswith('"""') or stripped.startswith("'''") or stripped.endswith('"""') or stripped.endswith("'''"):
        return "WARN"
        
    # Comentario inline
    if "#" in stripped:
        before_comment = stripped.split("#", 1)[0]
        if pattern not in before_comment:
            return "WARN"
            
    # Si parece código operativo real
    return "FAIL"

def check_file_dependencies(filepath, workspace_dir):
    """Detecta dependencias hacia rutas legacy en un archivo python."""
    filename = os.path.basename(filepath)
    if filename in ["dry_run_saneamiento_fisico.py", "test_dry_run_saneamiento_fisico.py"]:
        return []
    if "fixtures" in filepath:
        return []
        
    dependencies = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, 1):
                line_lower = line.lower()
                for pattern in ["cases/logistica", "docs_base", "output/"]:
                    if pattern in line_lower:
                        classification = classify_line_dependency(line, pattern)
                        dependencies.append((i, line.strip(), pattern, classification))
    except Exception:
        pass
    return dependencies

def scan_dependencies_in_dir(directory, workspace_dir):
    """Escanea un directorio buscando archivos Python con dependencias legacy."""
    dependencies = {}
    if not os.path.exists(directory):
        return dependencies
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                file_deps = check_file_dependencies(filepath, workspace_dir)
                if file_deps:
                    dependencies[filepath] = file_deps
    return dependencies

def find_markdown_in_legacy_zones(legacy_zones, workspace_dir):
    """Busca archivos Markdown en zonas legacy resolviendo comodines físicamente."""
    md_files = []
    for zone in legacy_zones:
        # Resolver comodín usando glob
        search_path = os.path.join(workspace_dir, zone.rstrip("/"))
        matched_paths = glob.glob(search_path)
        for path in matched_paths:
            if os.path.exists(path) and os.path.isdir(path):
                for root, _, files in os.walk(path):
                    for file in files:
                        if file.endswith(".md"):
                            md_files.append(os.path.join(root, file))
            elif os.path.exists(path) and os.path.isfile(path) and path.endswith(".md"):
                md_files.append(path)
    return md_files

def run_dry_run(workspace_dir="."):
    print("=== INICIANDO DRY-RUN VERIFICABLE DE SANEAMIENTO FÍSICO v0 ===")
    
    # 1. Comprobar que sea un repositorio Git válido
    if not is_git_repo(workspace_dir):
        print(f"[ERROR_TECNICO]: El directorio '{workspace_dir}' no es un repositorio Git válido.")
        return 3
        
    # 2. Comprobar bloqueos por archivos normativos obligatorios
    identity_path = os.path.join(workspace_dir, "repo_identity.yml")
    manifest_path = os.path.join(workspace_dir, "artifact_manifest.yml")
    
    if not os.path.exists(identity_path) or not os.path.exists(manifest_path):
        print("[ERROR_TECNICO]: Falta un archivo normativo obligatorio (repo_identity.yml o artifact_manifest.yml).")
        return 3
        
    identity = parse_repo_identity(identity_path)
    manifest = parse_artifact_manifest(manifest_path)
    
    if identity is None or manifest is None:
        print("[ERROR_TECNICO]: Error al parsear los archivos normativos obligatorios.")
        return 3
        
    # 3. Validar coherencia de roles
    identity_role = identity.get("repo_role")
    manifest_role = manifest.get("repo_role")
    
    has_role_contradiction = False
    if identity_role != "framework_mother" or manifest_role != "framework_mother" or identity_role != manifest_role:
        print(f"[CONTRADICCIÓN GRAVE]: Discrepancia de roles. Identidad: {identity_role}, Manifiesto: {manifest_role}")
        has_role_contradiction = True
        
    # 4. Obtener zonas legacy dinámicamente del manifiesto (soportando comodines)
    manifest_patterns = []
    if manifest and "artifacts" in manifest:
        for art in manifest["artifacts"]:
            if art.get("allowed_in_framework") is False and art.get("copy_policy") == "exclude":
                manifest_patterns.append(art.get("path"))
                
    # Fallback si no se detectan rutas
    if not manifest_patterns:
        manifest_patterns = ["docs_base/", "output/", "cases/logistica/", "core/templates/"]
        
    # 5. Resolver patrones con comodines en el sistema de archivos
    resolved_legacy_zones = []
    for pattern in manifest_patterns:
        clean_pattern = pattern.rstrip("/")
        full_glob_pattern = os.path.join(workspace_dir, clean_pattern)
        matched_paths = glob.glob(full_glob_pattern)
        
        if matched_paths:
            for path in matched_paths:
                rel_path = os.path.relpath(path, workspace_dir).replace("\\", "/")
                resolved_legacy_zones.append((rel_path, pattern))
        else:
            # Si no existe físicamente pero es una ruta definida, la mantenemos para validación Git potencial
            resolved_legacy_zones.append((clean_pattern, pattern))
            
    # 6. Analizar rutas críticas y construir matriz de hallazgos
    hallazgos = []
    id_counter = 1
    
    for zone_rel, manifest_pattern in resolved_legacy_zones:
        zone_path = os.path.join(workspace_dir, zone_rel)
        exists_physically = os.path.exists(zone_path)
        
        if exists_physically:
            # Comprobar si está trackeado en Git con cwd=workspace_dir
            tracked_files = get_tracked_files(zone_rel, workspace_dir)
            is_tracked = len(tracked_files) > 0
            
            if is_tracked:
                hallazgos.append({
                    "id": f"DRY-{id_counter:03d}",
                    "ruta": zone_rel,
                    "zona": "Legacy / Contaminada",
                    "clasificacion": f"Excluida (Patrón: {manifest_pattern})",
                    "hallazgo": f"Zona legacy '{zone_rel}' coincide con patrón '{manifest_pattern}' y tiene {len(tracked_files)} archivos registrados en Git.",
                    "riesgo": "Alto",
                    "accion": "Clasificar destino antes de cualquier acción: promover, archivar, conservar como histórico, excluir, dejar en cuarentena o eliminar solo con aprobación humana posterior.",
                    "aprobacion": "Sí",
                    "resultado": "FAIL"
                })
                id_counter += 1
            else:
                hallazgos.append({
                    "id": f"DRY-{id_counter:03d}",
                    "ruta": zone_rel,
                    "zona": "Legacy / Contaminada",
                    "clasificacion": f"Excluida (Patrón: {manifest_pattern})",
                    "hallazgo": f"Carpeta legacy '{zone_rel}' coincide con patrón '{manifest_pattern}' y existe local sin registro en Git.",
                    "riesgo": "Bajo",
                    "accion": "Clasificar destino antes de cualquier acción: promover, archivar, conservar como histórico, excluir, dejar en cuarentena o eliminar solo con aprobación humana posterior.",
                    "aprobacion": "Sí",
                    "resultado": "WARN"
                })
                id_counter += 1
                
    # 7. Buscar documentos arquitectónicos (.md) en zonas legacy
    legacy_mds = find_markdown_in_legacy_zones(manifest_patterns, workspace_dir)
    for md_file in legacy_mds:
        rel_md = os.path.relpath(md_file, workspace_dir).replace("\\", "/")
        tracked = len(get_tracked_files(rel_md, workspace_dir)) > 0
        res = "FAIL" if tracked else "WARN"
        hallazgos.append({
            "id": f"DRY-{id_counter:03d}",
            "ruta": rel_md,
            "zona": "Legacy / Documentación",
            "clasificacion": "Excluida en manifest",
            "hallazgo": f"Documento Markdown '{os.path.basename(md_file)}' detectado en zona no normativa.",
            "riesgo": "Medio",
            "accion": "Clasificar destino antes de cualquier acción: promover, archivar, conservar como histórico, excluir, dejar en cuarentena o eliminar solo con aprobación humana posterior.",
            "aprobacion": "Sí",
            "resultado": res
        })
        id_counter += 1

    # 8. Detectar scripts o tests que dependan de rutas legacy (clasificando en FAIL o WARN)
    framework_dirs = ["scripts", "tests", "src", "core"]
    for f_dir in framework_dirs:
        dir_path = os.path.join(workspace_dir, f_dir)
        # Excluir core/templates
        if f_dir == "core":
            if os.path.exists(dir_path):
                for item in os.listdir(dir_path):
                    if item != "templates":
                        item_path = os.path.join(dir_path, item)
                        if os.path.isdir(item_path):
                            deps = scan_dependencies_in_dir(item_path, workspace_dir)
                            for filepath, file_deps in deps.items():
                                rel_path = os.path.relpath(filepath, workspace_dir).replace("\\", "/")
                                for line_num, line_content, pattern, classification in file_deps:
                                    hallazgos.append({
                                        "id": f"DRY-{id_counter:03d}",
                                        "ruta": f"{rel_path}:{line_num}",
                                        "zona": "Framework / Código",
                                        "clasificacion": "Permitida",
                                        "hallazgo": f"Referencia a ruta legacy '{pattern}' en código: '{line_content}'",
                                        "riesgo": "Alto" if classification == "FAIL" else "Bajo",
                                        "accion": "Refactorizar código para usar fixtures sintéticos" if classification == "FAIL" else "Conservar comentario o ajustar texto de ayuda.",
                                        "aprobacion": "Sí",
                                        "resultado": classification
                                    })
                                    id_counter += 1
                        elif item.endswith(".py"):
                            file_deps = check_file_dependencies(item_path, workspace_dir)
                            if file_deps:
                                rel_path = os.path.relpath(item_path, workspace_dir).replace("\\", "/")
                                for line_num, line_content, pattern, classification in file_deps:
                                    hallazgos.append({
                                        "id": f"DRY-{id_counter:03d}",
                                        "ruta": f"{rel_path}:{line_num}",
                                        "zona": "Framework / Código",
                                        "clasificacion": "Permitida",
                                        "hallazgo": f"Referencia a ruta legacy '{pattern}' en código: '{line_content}'",
                                        "riesgo": "Alto" if classification == "FAIL" else "Bajo",
                                        "accion": "Refactorizar código para usar fixtures sintéticos" if classification == "FAIL" else "Conservar comentario o ajustar texto de ayuda.",
                                        "aprobacion": "Sí",
                                        "resultado": classification
                                    })
                                    id_counter += 1
        else:
            deps = scan_dependencies_in_dir(dir_path, workspace_dir)
            for filepath, file_deps in deps.items():
                rel_path = os.path.relpath(filepath, workspace_dir).replace("\\", "/")
                for line_num, line_content, pattern, classification in file_deps:
                    hallazgos.append({
                        "id": f"DRY-{id_counter:03d}",
                        "ruta": f"{rel_path}:{line_num}",
                        "zona": "Framework / Código",
                        "clasificacion": "Permitida",
                        "hallazgo": f"Referencia a ruta legacy '{pattern}' en código: '{line_content}'",
                        "riesgo": "Alto" if classification == "FAIL" else "Bajo",
                        "accion": "Refactorizar código para usar fixtures sintéticos" if classification == "FAIL" else "Conservar comentario o ajustar texto de ayuda.",
                        "aprobacion": "Sí",
                        "resultado": classification
                    })
                    id_counter += 1

    # Agregar contradicción de rol si existe
    if has_role_contradiction:
        hallazgos.append({
            "id": f"DRY-{id_counter:03d}",
            "ruta": "repo_identity.yml / artifact_manifest.yml",
            "zona": "Gobernanza / Raíz",
            "clasificacion": "Obligatoria",
            "hallazgo": f"Discrepancia en el rol asignado al repositorio. Identidad define '{identity_role}' y Manifiesto define '{manifest_role}'.",
            "riesgo": "Alto",
            "accion": "Alinear identidad y manifiesto para que coincidan en 'framework_mother'.",
            "aprobacion": "Sí",
            "resultado": "FAIL"
        })
        id_counter += 1

    # 9. Determinar código de salida
    final_result = "PASS"
    exit_code = 0
    
    has_fail = any(h["resultado"] == "FAIL" for h in hallazgos)
    has_warn = any(h["resultado"] == "WARN" for h in hallazgos)
    
    if has_fail:
        final_result = "FAIL"
        exit_code = 2
    elif has_warn:
        final_result = "WARN"
        exit_code = 1

    # 10. Generar reporte Markdown con enlaces relativos seguros
    report_dir = os.path.join(workspace_dir, "reports/saneamiento")
    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, "AUDITORIA_DRY_RUN_SANEAMIENTO_FISICO.md")
    
    # Construcción de la matriz en formato tabla Markdown
    matrix_rows = []
    for h in hallazgos:
        matrix_rows.append(
            f"| {h['id']} | {h['ruta']} | {h['zona']} | {h['clasificacion']} | {h['hallazgo']} | {h['riesgo']} | {h['accion']} | {h['aprobacion']} | `{h['resultado']}` |"
        )
        
    matrix_table = "\n".join(matrix_rows)
    if not matrix_rows:
        matrix_table = "| - | - | - | - | No se encontraron discrepancias o hallazgos. | - | - | - | - |"

    report_content = f"""# File: reports/saneamiento/AUDITORIA_DRY_RUN_SANEAMIENTO_FISICO.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Reporte de evidencia del dry-run de saneamiento físico.
# Rol: Registro documental de auditoría y análisis de integridad.
# ──────────────────────────────────────────────────────────────────────

# Reporte de Auditoría: Dry-run de Saneamiento Físico v0

## Resumen Ejecutivo
- **Resultado Global:** `{final_result}` (Código de salida: `{exit_code}`)
- **Fecha de Ejecución:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Ámbito:** Verificación determinista previa al saneamiento físico del repositorio madre.

> [!WARNING]
> **Confirmación de Seguridad:** Este análisis ha operado estrictamente en modo de **solo lectura**. No se ha modificado, borrado, renombrado ni movido ningún archivo o directorio del repositorio.

---

## Documentos Normativos Leídos
- [repo_identity.yml](repo_identity.yml)
- [artifact_manifest.yml](artifact_manifest.yml)

---

## Rutas Analizadas
- Zonas Excluidas (Patrones de Manifiesto): {", ".join(f"`{z}`" for z in manifest_patterns)}
- Zonas Permitidas (Framework): `scripts/`, `tests/`, `src/`, `core/` (excluyendo subruta templates)

---

## Matriz de Hallazgos y Contradicciones

| ID | Ruta | Zona detectada | Clasificación normativa | Hallazgo | Riesgo | Acción propuesta | Requiere aprobación humana | Resultado |
| -- | ---- | -------------- | ----------------------- | -------- | ------ | ---------------- | -------------------------- | --------- |
{matrix_table}

---

## Decisiones Humanas Requeridas
1. **Aprobación de Saneamiento Físico Real:** 
   - De acuerdo a `repo_identity.yml`, cualquier limpieza de archivos requiere aprobación humana explícita.
   - Las carpetas legacy detectadas físicamente deben evaluarse bajo la siguiente regla neutral:
     > "Clasificar destino antes de cualquier acción: promover, archivar, conservar como histórico, excluir, dejar en cuarentena o eliminar solo con aprobación humana posterior."
2. **Refactorización de Dependencias Técnicas:**
   - Para las contradicciones de tipo `FAIL` detectadas en código activo, se propone refactorizar para usar fixtures sintéticos independientes.
   - Para las advertencias `WARN` en comentarios o textos de ayuda, se propone conservar como histórico o archivar/ajustar la documentación.
3. **Reubicación de Documentos:**
   - Para los archivos `.md` en zonas legacy, se debe clasificar destino antes de cualquier acción: promover, archivar, conservar como histórico, excluir, dejar en cuarentena o eliminar solo con aprobación humana posterior.

> [!IMPORTANT]
> **Sin Autorización Automática:** Ninguna acción propuesta en la matriz queda autorizada para ejecución autónoma. Se requiere la frase explícita de aprobación del operador humano.

---
Fin del Reporte.
"""

    try:
        with open(report_path, "w", encoding="utf-8") as rf:
            rf.write(report_content)
        print(f"[OK] Reporte de auditoría generado en: {report_path}")
    except Exception as e:
        print(f"[ERROR]: No se pudo escribir el reporte Markdown. {e}")
        return 3

    print(f"Resultado final: {final_result} (Exit code: {exit_code})")
    return exit_code

if __name__ == "__main__":
    sys.exit(run_dry_run())
