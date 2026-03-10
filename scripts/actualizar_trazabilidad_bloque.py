"""
File: scripts/actualizar_trazabilidad_bloque.py
──────────────────────────────────────────────────────────────────────
Propósito: Actualizar el bloque de trazabilidad NotebookLM en todos los
           entregables de output/bloque_1/ con el formato estándar AMBOS IDs
           (HITO + Auditoría Semántica), usando UUIDs reales extraídos de NotebookLM.
Rol: Herramienta de mantenimiento determinista (no modifica cuerpo del documento).
──────────────────────────────────────────────────────────────────────
! [ALERTA]: Solo debe ejecutarse una vez por ciclo de estandarización.
             El script hace backup previo de cada archivo tocado.
"""

from __future__ import annotations

import re
import shutil
from datetime import datetime
from pathlib import Path

# ─────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN: Mapa de trazabilidad real por entregable
# Fuente: extraído directamente de NotebookLM vía MCP el 2026-03-05
# ─────────────────────────────────────────────────────────────────────

BLOQUE_1_DIR = Path("output/bloque_1")
ARCHIVE_DIR = BLOQUE_1_DIR / "archive"
FECHA_HOY = datetime.now().strftime("%Y-%m-%d")

# Cuadernos
NB_INVESTIGACION = {
    "title": "ZAC_Bloque_1_Investigacion_Sector",
    "id": "a9776342-15b0-4d0d-9280-86fb060e7027",
}
NB_COMPETENCIA = {
    "title": "ZAC_Bloque_1_Competencia",
    "id": "7aee3bc4-233d-4b2d-9941-04b53fa270ca",
}

ENTREGABLES: dict[str, dict] = {
    "00_analisis_sector_logistico_zaragoza.md": {
        "notebook": NB_INVESTIGACION,
        "hito_note_title": "HITO: Análisis Sector Logístico Zaragoza",
        "hito_note_id": "120e9e71-7715-4b8f-892d-53df90d860eb",
        "auditoria_note_title": "AUDITORÍA SEMÁNTICA — 00_analisis_sector_logistico_zaragoza.md",
        "auditoria_note_id": "35e62822-a4e8-4d93-b426-e01b577d33b0",
    },
    "01_mapa_empatia_transporte.md": {
        "notebook": NB_INVESTIGACION,
        "hito_note_title": "HITO: Mapa Empatía Transporte",
        "hito_note_id": "1d695db6-dd3f-46aa-a290-141eb47a5790",
        "auditoria_note_title": "AUDITORÍA SEMÁNTICA — 01_mapa_empatia_transporte.md",
        "auditoria_note_id": "cc459270-3406-4947-88e5-f142e0c9cfd5",
    },
    "02_canvas_valor.md": {
        "notebook": NB_INVESTIGACION,
        "hito_note_title": "HITO: Canvas Propuesta de Valor",
        "hito_note_id": "ff2aa51a-0ab0-46c0-b313-bc64ee7d5589",
        "auditoria_note_title": "AUDITORÍA SEMÁNTICA — 02_canvas_valor.md",
        "auditoria_note_id": "c7d8a63e-4e6b-4e0c-a798-45b74d99a693",
    },
    "03_pestel.md": {
        "notebook": NB_INVESTIGACION,
        "hito_note_title": "HITO: PESTEL Logístico ZAC",
        "hito_note_id": "df35622f-84f9-4a69-b154-cb4961c50aa6",
        "auditoria_note_title": "AUDITORÍA SEMÁNTICA — 03_pestel.md",
        "auditoria_note_id": "d4ebb514-a105-4fc9-8917-d15b3827748b",
    },
    "04_dafo.md": {
        "notebook": NB_INVESTIGACION,
        "hito_note_title": "HITO: DAFO Logístico ZAC",
        "hito_note_id": "03a382db-aedb-445f-9d06-38b53005cd4b",
        "auditoria_note_title": "AUDITORÍA SEMÁNTICA — 04_dafo.md",
        "auditoria_note_id": "32355f67-0d64-4f42-b1f7-dccce92a3685",
    },
    "05_ods_v1.md": {
        "notebook": NB_INVESTIGACION,
        "hito_note_title": "HITO: ODS Version 1",
        "hito_note_id": "c1a419fb-fc35-47f9-987d-2dc5cdccb40b",
        "auditoria_note_title": "AUDITORÍA SEMÁNTICA — 05_ods_v1.md",
        "auditoria_note_id": "c7461ac3-2fda-49bc-b6ef-0dae328c9b3a",
    },
    "06_competencia_y_benchmarking.md": {
        "notebook": NB_COMPETENCIA,
        # TODO: Nota HITO no existe aún. Crear con skill_notebooklm_registrar_entregable.
        "hito_note_title": "HITO: Competencia y Benchmarking (PENDIENTE)",
        "hito_note_id": "pendiente-crear-con-skill-notebooklm",
        "auditoria_note_title": "AUDITORÍA SEMÁNTICA — 06_competencia_y_benchmarking.md",
        "auditoria_note_id": "6d5178b4-edc6-49a5-883f-3f07756fb9ff",
    },
    "07_estrategia_competitiva.md": {
        "notebook": NB_COMPETENCIA,
        "hito_note_title": "HITO: Estrategia Competitiva (PENDIENTE)",
        "hito_note_id": "pendiente-crear-con-skill-notebooklm",
        "auditoria_note_title": "AUDITORÍA SEMÁNTICA — 07_estrategia_competitiva.md",
        "auditoria_note_id": "3307040d-aa4b-4086-b890-acd89b2cf863",
    },
    "08_curva_valor_vs_competencia.md": {
        "notebook": NB_COMPETENCIA,
        "hito_note_title": "HITO: Curva de Valor vs Competencia (PENDIENTE)",
        "hito_note_id": "pendiente-crear-con-skill-notebooklm",
        "auditoria_note_title": "AUDITORÍA SEMÁNTICA — 08_curva_valor_vs_competencia.md",
        "auditoria_note_id": "cc0cabb2-492f-41a0-9d9e-0ba0eac26711",
    },
    "09_matriz_came.md": {
        "notebook": NB_COMPETENCIA,
        "hito_note_title": "HITO: Matriz CAME (PENDIENTE)",
        "hito_note_id": "pendiente-crear-con-skill-notebooklm",
        "auditoria_note_title": "AUDITORÍA SEMÁNTICA — 09_matriz_came.md",
        "auditoria_note_id": "8d208e19-fff5-412b-99a3-7d0d4380fdd4",
    },
    "10_business_model_canvas.md": {
        "notebook": NB_COMPETENCIA,
        "hito_note_title": "HITO: Business Model Canvas (PENDIENTE)",
        "hito_note_id": "pendiente-crear-con-skill-notebooklm",
        "auditoria_note_title": "AUDITORÍA SEMÁNTICA — 10_business_model_canvas.md",
        "auditoria_note_id": "762498a3-9cad-4163-ac83-9e642da7c3af",
    },
    "99_resumen_bloque_1.md": {
        "notebook": NB_INVESTIGACION,
        "hito_note_title": "HITO: Resumen Bloque 1",
        "hito_note_id": "ff268584-be4f-4c2d-ac73-1f2c4daf6090",
        "auditoria_note_title": "AUDITORÍA SEMÁNTICA — 99_resumen_bloque_1.md",
        "auditoria_note_id": "5d99964a-1ca7-41e8-bb9f-c731288fbbc2",
    },
}

# ─────────────────────────────────────────────────────────────────────
# Patrón para detectar el bloque de trazabilidad existente (cualquier formato)
# ─────────────────────────────────────────────────────────────────────
NOTE_BLOCK_REGEX = re.compile(
    r"\*\*Nota de Registro NotebookLM\*\*.*$",
    re.DOTALL | re.IGNORECASE,
)


def build_trace_block(data: dict) -> str:
    """Construye el bloque de trazabilidad estándar con ambos IDs."""
    nb = data["notebook"]
    return (
        f"**Nota de Registro NotebookLM**\n"
        f"- **notebook_title:** {nb['title']}\n"
        f"- **notebook_id:** {nb['id']}\n"
        f"\n"
        f"**Registro (HITO)**\n"
        f"- **hito_note_title:** {data['hito_note_title']}\n"
        f"- **hito_note_id:** {data['hito_note_id']}\n"
        f"\n"
        f"**Auditoría semántica (Gate 7)**\n"
        f"- **auditoria_note_title:** {data['auditoria_note_title']}\n"
        f"- **auditoria_note_id:** {data['auditoria_note_id']}\n"
        f"- **fecha:** {FECHA_HOY}\n"
    )


def actualizar_archivo(filepath: Path, data: dict) -> bool:
    """
    Reemplaza el bloque de trazabilidad existente por el formato estándar.
    Hace backup previo del archivo original.
    Retorna True si hubo cambio, False si no se encontró el bloque.
    """
    texto = filepath.read_text(encoding="utf-8")

    if not NOTE_BLOCK_REGEX.search(texto):
        print(f"  [WARN] No se encontró bloque 'Nota de Registro' en: {filepath.name}")
        return False

    # Backup antes de modificar
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = ARCHIVE_DIR / f"{filepath.stem}_trazabilidad_backup_{ts}.md"
    shutil.copy2(filepath, backup)
    print(f"  [BACKUP] {backup.name}")

    nuevo_bloque = build_trace_block(data)
    nuevo_texto = NOTE_BLOCK_REGEX.sub(nuevo_bloque, texto)
    filepath.write_text(nuevo_texto, encoding="utf-8")
    print(f"  [OK] Actualizado: {filepath.name}")
    return True


def main() -> None:
    print("======================================================")
    print("  ACTUALIZACIÓN DE TRAZABILIDAD — BLOQUE 1 (AMBOS IDs)")
    print("======================================================\n")

    actualizados = 0
    for nombre, datos in ENTREGABLES.items():
        ruta = BLOQUE_1_DIR / nombre
        if not ruta.exists():
            print(f"[SKIP] No existe: {ruta}")
            continue
        print(f"Procesando: {nombre}")
        ok = actualizar_archivo(ruta, datos)
        if ok:
            actualizados += 1
        print()

    print(f"\n✅ Actualizados: {actualizados}/{len(ENTREGABLES)} entregables.")
    print("Backups guardados en: output/bloque_1/archive/")


if __name__ == "__main__":
    main()
