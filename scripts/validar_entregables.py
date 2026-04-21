"""
scripts/validar_entregables.py

OBJETIVO
--------
Validar entregables Markdown (tanto en output/ legacy como en cases/) para evitar 
errores humanos y mantener el sistema audit-able (determinista).

Este script NO escribe contenido. Solo:
- Revisa estructura obligatoria (Nota de Registro NotebookLM con 5 campos mínimos)
- Acepta FORMATO NUEVO (hito_note_id + auditoria_note_id) y FORMATO ANTIGUO (note_id)
- Valida formatos (UUID, fecha)
- Detecta riesgos (HECHO con números sin "Fuente sólida")
- Detecta presencia mínima de métricas/KPIs (heurística simple)

FORMATO NUEVO (requerido a partir de 2026-03-05):
  notebook_title, notebook_id, hito_note_id, auditoria_note_id, fecha

USO (NUEVA ARQUITECTURA)
-----------------------
python scripts/validar_entregables.py --bloque cases/logistica/output/bloque_1 --salida cases/logistica/reports/VALIDACION.md

USO (LEGACY)
------------
python scripts/validar_entregables.py --bloque output/bloque_1 --salida reports/reporte_validacion_bloque_1.md
"""

from __future__ import annotations

import argparse
import re
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple


# ---------------------------------------------------------------------
# Configuración de patrones (simples, explícitos y fáciles de ajustar)
# ---------------------------------------------------------------------

UUID_REGEX = re.compile(
    r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b"
)

FECHA_REGEX = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")

# Detecta un bloque de trazabilidad al final. No depende de títulos exactos,
# solo busca la sección "Nota de Registro NotebookLM" y luego líneas con campos.
NOTE_BLOCK_TITLE_REGEX = re.compile(r"Nota de Registro NotebookLM", re.IGNORECASE)

# Campos obligatorios — formato nuevo (AMBOS IDs, a partir de 2026-03-05)
REQUIRED_NOTE_FIELDS_NEW = [
    "notebook_title",
    "notebook_id",
    "hito_note_id",
    "auditoria_note_id",
    "fecha",
]
# Campos — formato antiguo (compatible pero deprecado)
REQUIRED_NOTE_FIELDS_OLD = [
    "notebook_title",
    "notebook_id",
    "note_id",
    "fecha",
]
# Campo unificado para validación UUID — cualquier campo con _id en su nombre
NOTE_UUID_FIELDS = ["notebook_id", "hito_note_id", "auditoria_note_id", "note_id"]

# Detectar HECHO con números: buscamos "[HECHO]" y un número cercano.
HECHO_TAG_REGEX = re.compile(r"\[HECHO\]", re.IGNORECASE)
NUMBER_REGEX = re.compile(r"(?<!\w)(\d+([.,]\d+)?)(?!\w)")

# Detectar "Fuente sólida" cerca de un HECHO numérico
FUENTE_SOLIDA_REGEX = re.compile(r"Fuente\s+s[oó]lida\s*:", re.IGNORECASE)

# Detectar "métricas": heurística ampliada (no solo 'Métrica N:')
# Pattern 1: etiquetas explícitas de métrica
METRICA_HINT_REGEX = re.compile(r"\b(M[eé]trica|KPI|Indicador)\b", re.IGNORECASE)
# Pattern 2: patrones numéricos tipo métrica
METRICA_NUMERICA_REGEX = re.compile(
    r"("
    r"\d+\s*%"                           # 80%
    r"|>\s*\d+\s*%"                      # >80%
    r"|<\s*\d+\s*%"                      # <20%
    r"|\d+[\u2013\-]\d+\s*%"             # 30-40%
    r"|\d+[\u2013-]\d+\s*\u20ac"         # 250€–600€
    r"|\d+\s*\u20ac"                     # 500€
    r"|\d+([\u2013-]\d+)?\s*(horas|d\u00edas|semanas|entrevistas|pymes|clientes)"  # 4 horas...
    r"|>\s*\d+\s*(horas|d\u00edas|pymes|clientes)"  # >3 horas
    r"|<\s*\d+\s*(horas|d\u00edas|pymes|clientes)"  # <4 horas
    r")",
    re.IGNORECASE
)
# Pattern 3: etiquetas de validación (hipotesis con criterio)
METRICA_VALIDACION_REGEX = re.compile(
    r"\b(baseline|muestra|criterio|piloto|CÓMO SE VALIDA|cómo se valida|[Cc]ómo se validar)\b"
)


# ---------------------------------------------------------------------
# Modelos de datos para reportar resultados
# ---------------------------------------------------------------------

@dataclass
class File_validation_result:
    file_path: Path
    passed: bool
    errors: List[str]
    warnings: List[str]


# ---------------------------------------------------------------------
# Utilidades de validación
# ---------------------------------------------------------------------

def is_valid_uuid(value: str) -> bool:
    """Valida si un string es un UUID real."""
    try:
        uuid.UUID(value)
        return True
    except ValueError:
        return False


def extract_note_block(text: str) -> str | None:
    """
    Extrae el bloque 'Nota de Registro NotebookLM' (si existe).
    Estrategia:
    - Encuentra el título
    - Toma desde ahí hasta el final del archivo
    """
    match = NOTE_BLOCK_TITLE_REGEX.search(text)
    if not match:
        return None

    return text[match.start():].strip()


def parse_note_fields(note_block: str) -> dict:
    """
    Extrae campos del bloque de trazabilidad NotebookLM.
    Acepta formato nuevo (hito_note_id + auditoria_note_id) y antiguo (note_id).
    """
    # Lista unificada de todos los campos posibles (formato nuevo + antiguo)
    all_known_fields = [
        "notebook_title", "notebook_id",
        "hito_note_title", "hito_note_id",
        "auditoria_note_title", "auditoria_note_id",
        "note_title", "note_id",
        "fecha",
    ]
    fields: dict = {}
    for field_name in all_known_fields:
        # Captura de forma tolerante al formato markdown con ** **
        pattern = re.compile(
            rf"{field_name}\s*:\s*(.+)",
            re.IGNORECASE
        )
        m = pattern.search(note_block)
        if m:
            fields[field_name.lower()] = m.group(1).strip()

    return fields



def count_metrics(text: str) -> int:
    """
    Cuenta métricas usando una heurística ampliada (Gate 3 mejorado).
    Combina 3 fuentes:
      1. Etiquetas explícitas: 'Métrica', 'KPI', 'Indicador'.
      2. Patrones numéricos tipo métrica: '80%', '>4 horas', '250€–600€', '5 entrevistas'...
      3. Etiquetas de validación: 'baseline', 'criterio', 'CÓMO SE VALIDA'...
    Agrega todas las coincidencias únicas (por posición) para evitar doble conteo.
    El resultado es una estimación; el reporte lo indica como 'heurística ampliada'.
    """
    hits_explicitas = len(METRICA_HINT_REGEX.findall(text))
    hits_numericas = len(METRICA_NUMERICA_REGEX.findall(text))
    hits_validacion = len(METRICA_VALIDACION_REGEX.findall(text))
    # La suma NO es solo los 3 contadores: usamos máx(etiquetas, numéricas) + validación
    # para no inflar el total cuando un documento tiene muchos % sin hipótesis
    return max(hits_explicitas, hits_numericas) + hits_validacion


def find_hecho_numeric_without_fuente_solida(text: str) -> List[str]:
    """
    Detecta casos donde:
    - existe [HECHO]
    - hay un número cerca
    - y no aparece "Fuente sólida:" en un rango cercano

    Devuelve fragmentos cortos para reportar.
    """
    findings: List[str] = []

    # Recorremos ocurrencias de [HECHO]
    for hecho_match in HECHO_TAG_REGEX.finditer(text):
        start = max(0, hecho_match.start() - 250)
        end = min(len(text), hecho_match.end() + 350)
        window = text[start:end]

        # Si no hay número cerca, no nos preocupa
        if not NUMBER_REGEX.search(window):
            continue

        # Si hay número, exigimos "Fuente sólida" cerca
        if not FUENTE_SOLIDA_REGEX.search(window):
            snippet = window.strip().replace("\n", " ")
            findings.append(snippet[:280] + ("..." if len(snippet) > 280 else ""))

    return findings


def validate_one_file(file_path: Path) -> File_validation_result:
    """
    Valida un archivo markdown y retorna resultados estructurados.
    Acepta el formato nuevo (hito_note_id + auditoria_note_id) y el antiguo (note_id).
    """
    text = file_path.read_text(encoding="utf-8", errors="replace")

    errors: List[str] = []
    warnings: List[str] = []

    # 1) Validar que exista bloque NotebookLM
    note_block = extract_note_block(text)
    if note_block is None:
        errors.append("Falta el bloque final: 'Nota de Registro NotebookLM'.")
        return File_validation_result(file_path=file_path, passed=False, errors=errors, warnings=warnings)

    # 2) Detectar formato (nuevo vs antiguo) y validar campos obligatorios
    fields = parse_note_fields(note_block)

    # Determinar si usa formato nuevo (hito_note_id presente)
    is_new_format = "hito_note_id" in fields or "auditoria_note_id" in fields

    if is_new_format:
        # Formato nuevo: requiere hito_note_id + auditoria_note_id
        for field_name in REQUIRED_NOTE_FIELDS_NEW:
            if field_name not in fields:
                errors.append(f"[Formato nuevo] Falta el campo obligatorio: {field_name}")
    else:
        # Formato antiguo: FALLA (Gate 4 real) — ya no es solo warning
        errors.append(
            "[Gate 4 FAIL] Trazabilidad en FORMATO ANTIGUO (note_id único). "
            "Debe migrarse al formato nuevo con hito_note_id + auditoria_note_id. "
            "El entregable queda BLOQUEADO hasta completar la migración."
        )
        # Verificar que los campos del formato antiguo estén presentes
        for field_name in REQUIRED_NOTE_FIELDS_OLD:
            if field_name not in fields:
                errors.append(f"[Formato antiguo] Falta además el campo: {field_name}")

    # 3) Validar todos los UUIDs presentes
    for uuid_field in NOTE_UUID_FIELDS:
        val = fields.get(uuid_field, "")
        if not val:
            continue
        # Ignorar placeholders explícitos
        if "pendiente" in val.lower():
            warnings.append(f"{uuid_field} marcado como pendiente: {val[:60]}")
            continue
        uuid_match = UUID_REGEX.search(val)
        if not uuid_match or not is_valid_uuid(uuid_match.group(0)):
            errors.append(f"{uuid_field} no es UUID válido: {val}")

    # 4) Validar fecha
    fecha_value = fields.get("fecha", "")
    if fecha_value:
        fecha_match = FECHA_REGEX.search(fecha_value)
        if not fecha_match:
            errors.append(f"fecha no cumple formato YYYY-MM-DD: {fecha_value}")

    # 5) Gate 1 determinista: HECHO numérico sin Fuente sólida
    hecho_findings = find_hecho_numeric_without_fuente_solida(text)
    if hecho_findings:
        errors.append("Se detectaron [HECHO] con números sin 'Fuente sólida:' cerca.")
        for i, snippet in enumerate(hecho_findings, start=1):
            errors.append(f"  - Caso {i}: {snippet}")

    # 6) Métricas mínimas (warning si no llega a 3 — usando heurística ampliada)
    metrics_count = count_metrics(text)
    if metrics_count < 3:
        warnings.append(
            f"Métricas/KPIs detectadas (heurística ampliada): {metrics_count}. "
            "Verificar manualmente si el documento tiene menos de 3 métricas operativas."
        )

    passed = len(errors) == 0
    return File_validation_result(file_path=file_path, passed=passed, errors=errors, warnings=warnings)


def build_markdown_report(results: List[File_validation_result], bloque_path: Path) -> str:
    """
    Construye reporte Markdown con PASS/FAIL por archivo.
    """
    total = len(results)
    fails = sum(1 for r in results if not r.passed)

    lines: List[str] = []
    lines.append("# Reporte de Validación Determinista (Entregables)")
    lines.append("")
    lines.append(f"- **Bloque revisado:** `{bloque_path.as_posix()}`")
    lines.append(f"- **Archivos revisados:** {total}")
    lines.append(f"- **FAIL:** {fails}")
    lines.append(f"- **PASS:** {total - fails}")
    lines.append("")
    lines.append("---")
    lines.append("")

    for r in results:
        status = "PASS ✅" if r.passed else "FAIL ❌"
        lines.append(f"## {status} — {r.file_path.name}")
        lines.append("")
        if r.errors:
            lines.append("**Errores (bloquea cierre):**")
            for e in r.errors:
                lines.append(f"- {e}")
            lines.append("")
        if r.warnings:
            lines.append("**Warnings (revisar):**")
            for w in r.warnings:
                lines.append(f"- {w}")
            lines.append("")
        if not r.errors and not r.warnings:
            lines.append("Sin observaciones.")
            lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bloque", required=True, help="Ruta al bloque a validar (ej. cases/logistica/output/bloque_1)")
    parser.add_argument("--salida", required=True, help="Ruta del reporte resultante (ej. cases/logistica/reports/VALIDACION.md)")
    args = parser.parse_args()

    bloque_path = Path(args.bloque).resolve()
    output_path = Path(args.salida).resolve()

    if not bloque_path.exists():
        raise SystemExit(f"Bloque no encontrado: {bloque_path}")

    md_files = sorted(bloque_path.glob("*.md"))
    if not md_files:
        raise SystemExit(f"No se encontraron .md en: {bloque_path}")

    results = [validate_one_file(fp) for fp in md_files]
    report_md = build_markdown_report(results, bloque_path=bloque_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report_md, encoding="utf-8")
    print(f"OK: reporte generado en {output_path}")


if __name__ == "__main__":
    main()
