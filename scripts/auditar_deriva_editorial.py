"""
scripts/auditar_deriva_editorial.py

OBJETIVO
--------
Detectar "deriva editorial" (documentos que se vuelven genéricos o se van a temas
secundarios que no corresponden a la opción activa).

Este script NO corrige contenido. Solo marca riesgos.

USO
---
python scripts/auditar_deriva_editorial.py --bloque output/bloque_1 --salida reports/reporte_deriva_bloque_1.md
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import List, Dict


# ---------------------------------------------------------------------
# Perfiles Sectoriales (Desacoplamiento temática)
# ---------------------------------------------------------------------

DEFAULT_SECTOR_PROFILES = {
    "logistica": {
        "anchor_terms": [
            "CMR", "eCMR", "POD", "albarán", "incidencia", "subcontrata", "peaje",
            "ventana", "conciliación", "doc-to-cash", "factura", "cobro", "trazabilidad"
        ],
        "risk_terms": [
            "DUA", "arancel", "packing list", "incoterm", "despacho aduanero",
            "operador aduanero", "agente de aduanas", "gestor aduanero"
        ],
        "legal_context_pattern": (
            r"(normativa|ley|cumplimiento|regulación|control|inspección|obligación).{0,60}aduan"
            r"|aduan.{0,60}(normativa|ley|cumplimiento|regulación|control|inspección|obligación)"
        )
    }
}


@dataclass
class Drift_result:
    file_path: Path
    anchor_hits: Dict[str, int]
    contextual_hits: Dict[str, int]
    is_generic_risk: bool
    is_contextual_risk: bool


def read_option_active(option_file: Path) -> str:
    """
    Lee el archivo de opción activa (por defecto docs/OPCION_ACTIVA.md).
    """
    if not option_file.exists():
        # Fallback silencioso si no existe para no romper el script si se parametriza mal,
        # pero avisando que el nicho activo no se pudo determinar.
        return "Opción activa (nicho): DESCONOCIDO"
    return option_file.read_text(encoding="utf-8", errors="replace")


def detect_active_nicho(option_text: str) -> str:
    """
    Extrae el nicho activo de forma simple.
    """
    m = re.search(r"Opción activa\s*\(nicho\)\s*:\s*(.+)", option_text, re.IGNORECASE)
    if not m:
        return "DESCONOCIDO"
    return m.group(1).replace("*", "").strip().upper()


def count_term_hits(text: str, terms: List[str]) -> Dict[str, int]:
    """
    Cuenta ocurrencias por término.
    """
    hits: Dict[str, int] = {}
    for t in terms:
        pattern = re.compile(rf"\b{re.escape(t)}\b", re.IGNORECASE)
        hits[t] = len(pattern.findall(text))
    return hits


def audit_one_file(file_path: Path, active_nicho: str, profile: dict) -> Drift_result:
    text = file_path.read_text(encoding="utf-8", errors="replace")

    anchor_terms = profile.get("anchor_terms", [])
    risk_terms = profile.get("risk_terms", [])
    legal_pattern_str = profile.get("legal_context_pattern", "")

    anchor_hits = count_term_hits(text, anchor_terms)

    contextual_terms = []
    # En logística, la deriva es hacia aduanas cuando el nicho es transporte
    if "TRANSPORTE" in active_nicho:
        contextual_terms = risk_terms

    # Conteo de riesgo y filtrado por contexto legal si existe patrón
    raw_contextual_hits = count_term_hits(text, contextual_terms) if contextual_terms else {}
    contextual_hits: dict = {}
    
    legal_regex = re.compile(legal_pattern_str, re.IGNORECASE) if legal_pattern_str else None

    for term, count in raw_contextual_hits.items():
        if term.lower() == "aduana" and count > 0 and legal_regex:
            legal_matches = len(legal_regex.findall(text))
            aduana_pattern = re.compile(r"\baduana\b", re.IGNORECASE)
            total_aduana = len(aduana_pattern.findall(text))
            contextual_hits[term] = max(0, total_aduana - legal_matches)
        else:
            contextual_hits[term] = count

    # Reglas de riesgo
    total_anchor_hits = sum(anchor_hits.values())
    is_generic_risk = total_anchor_hits < 5
    is_contextual_risk = any(v > 0 for v in contextual_hits.values())

    return Drift_result(
        file_path=file_path,
        anchor_hits=anchor_hits,
        contextual_hits=contextual_hits,
        is_generic_risk=is_generic_risk,
        is_contextual_risk=is_contextual_risk
    )


def build_markdown_report(results: List[Drift_result], bloque_path: Path, active_nicho: str, sector: str) -> str:
    lines: List[str] = []
    lines.append("# Reporte Anti-Deriva Editorial")
    lines.append("")
    lines.append(f"- **Bloque revisado:** `{bloque_path.as_posix()}`")
    lines.append(f"- **Sector configurado:** `{sector}`")
    lines.append(f"- **Opción activa detectada:** `{active_nicho}`")
    lines.append("")
    lines.append("Reglas usadas:")
    lines.append("- Riesgo de genérico: menos de 5 menciones totales de términos ancla del sector.")
    lines.append("- Riesgo contextual: aparece cualquier término de riesgo para la opción activa.")
    lines.append("")
    lines.append("---")
    lines.append("")

    for r in results:
        status_parts = []
        if r.is_generic_risk:
            status_parts.append("GENÉRICO ⚠️")
        if r.is_contextual_risk:
            status_parts.append("REVISAR_CONTEXTO ⚠️")
        status = "OK ✅" if not status_parts else " + ".join(status_parts)

        lines.append(f"## {status} — {r.file_path.name}")
        lines.append("")

        total_anchor = sum(r.anchor_hits.values())
        lines.append(f"- **Total términos ancla:** {total_anchor}")
        lines.append("- **Detalle anclas (top):**")
        for term, count in sorted(r.anchor_hits.items(), key=lambda x: x[1], reverse=True):
            if count > 0:
                lines.append(f"  - {term}: {count}")
        if total_anchor == 0:
            lines.append("  - (sin menciones)")

        if r.contextual_hits:
            contextual_total = sum(r.contextual_hits.values())
            lines.append(f"- **Términos de riesgo contextual detectados:** {contextual_total}")
            for term, count in r.contextual_hits.items():
                if count > 0:
                    lines.append(f"  - {term}: {count}")
            if contextual_total > 0:
                lines.append("")
                lines.append(f"  > **NOTA:** Aparecen menciones de riesgo específicas para `{sector}`. Verificar si corresponden al objetivo del documento.")

        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bloque", required=True, help="Ruta al bloque (ej. output/bloque_1)")
    parser.add_argument("--salida", required=True, help="Ruta del reporte MD (ej. reports/reporte_deriva_bloque_1.md)")
    parser.add_argument("--sector", default="logistica", help="Perfil sectorial a usar (default: logistica)")
    parser.add_argument("--opcion_activa", default="docs/OPCION_ACTIVA.md", help="Ruta al archivo OPCION_ACTIVA.md")
    args = parser.parse_args()

    bloque_path = Path(args.bloque).resolve()
    output_path = Path(args.salida).resolve()
    option_file = Path(args.opcion_activa).resolve()

    sector = args.sector.lower()
    profile = DEFAULT_SECTOR_PROFILES.get(sector, {})
    if not profile and sector != "desconocido":
        print(f"Advertencia: Sector '{sector}' no tiene perfil interno. Se usará auditoría básica.")

    option_text = read_option_active(option_file)
    active_nicho = detect_active_nicho(option_text)

    md_files = sorted(bloque_path.glob("*.md"))
    results = [audit_one_file(fp, active_nicho=active_nicho, profile=profile) for fp in md_files]

    report_md = build_markdown_report(results, bloque_path=bloque_path, active_nicho=active_nicho, sector=sector)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report_md, encoding="utf-8")
    print(f"OK: reporte generado en {output_path}")


if __name__ == "__main__":
    main()

