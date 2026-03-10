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
# Configuración base (anclas típicas de logística operativa)
# ---------------------------------------------------------------------

ANCHOR_TERMS_DEFAULT = [
    "CMR", "eCMR", "POD", "albarán", "incidencia", "subcontrata", "peaje",
    "ventana", "conciliación", "doc-to-cash", "factura", "cobro", "trazabilidad"
]

# Términos que indican deriva temática real hacia transitarios/aduanas como tema principal
TERMINOS_RIESGO_CONTEXTUAL = [
    "DUA", "arancel", "packing list", "incoterm", "despacho aduanero",
    "operador aduanero", "agente de aduanas", "gestor aduanero"
]

# Términos de aduanas permitidos en contexto legal (NO generan alerta de deriva)
# Si 'aduana' aparece junto a estas palabras en una ventana de 200 caracteres, se permite
CONTEXTO_LEGAL_ADUANAS = [
    "normativa aduanera", "ley aduanera", "cumplimiento aduanero",
    "regulación aduanera", "control aduanero", "obligación aduanera",
    "normativa", "incumplimiento", "cumplimiento", "regulación", "inspección"
]
CONTEXTO_LEGAL_REGEX = re.compile(
    r"(normativa|ley|cumplimiento|regulación|control|inspección|obligación).{0,60}aduan"
    r"|aduan.{0,60}(normativa|ley|cumplimiento|regulación|control|inspección|obligación)",
    re.IGNORECASE
)


@dataclass
class Drift_result:
    file_path: Path
    anchor_hits: Dict[str, int]
    contextual_hits: Dict[str, int]
    is_generic_risk: bool
    is_contextual_risk: bool


def read_option_active(option_file: Path) -> str:
    """
    Lee docs/OPCION_ACTIVA.md y retorna el contenido.
    """
    if not option_file.exists():
        raise SystemExit(f"No existe {option_file}. Debes crear docs/OPCION_ACTIVA.md primero.")
    return option_file.read_text(encoding="utf-8", errors="replace")


def detect_active_nicho(option_text: str) -> str:
    """
    Extrae el nicho activo (TRANSPORTE / TRANSITARIOS / OTRO) de forma simple.
    """
    m = re.search(r"Opción activa\s*\(nicho\)\s*:\s*(.+)", option_text, re.IGNORECASE)
    if not m:
        return "DESCONOCIDO"
    return m.group(1).replace("*", "").strip().upper()


def count_term_hits(text: str, terms: List[str]) -> Dict[str, int]:
    """
    Cuenta ocurrencias por término (case-insensitive, con límites de palabra).
    """
    hits: Dict[str, int] = {}
    for t in terms:
        pattern = re.compile(rf"\b{re.escape(t)}\b", re.IGNORECASE)
        hits[t] = len(pattern.findall(text))
    return hits


def audit_one_file(file_path: Path, active_nicho: str) -> Drift_result:
    text = file_path.read_text(encoding="utf-8", errors="replace")

    anchor_hits = count_term_hits(text, ANCHOR_TERMS_DEFAULT)

    contextual_terms = []
    if "TRANSPORTE" in active_nicho:
        contextual_terms = TERMINOS_RIESGO_CONTEXTUAL

    # Conteo bruto de términos de riesgo
    raw_contextual_hits = count_term_hits(text, contextual_terms) if contextual_terms else {}

    # Filtrar 'aduana' si aparece únicamente en contexto legal (no como tema principal)
    # Si el texto tiene aduana pero TODAS las apariciones son en contexto legal, no se alerta
    contextual_hits: dict = {}
    for term, count in raw_contextual_hits.items():
        if term.lower() == "aduana" and count > 0:
            # Verificar si la mención es de contexto legal
            legal_matches = len(CONTEXTO_LEGAL_REGEX.findall(text))
            # Mención total de aduana
            aduana_pattern = re.compile(r"\baduana\b", re.IGNORECASE)
            total_aduana = len(aduana_pattern.findall(text))
            if legal_matches >= total_aduana:
                # Todas las menciones son en contexto legal — no es deriva
                contextual_hits[term] = 0
            else:
                # Hay menciones fuera de contexto legal — posible deriva
                contextual_hits[term] = total_aduana - legal_matches
        else:
            contextual_hits[term] = count

    # Regla simple:
    # - riesgo de genérico si tiene menos de 5 hits totales de términos ancla
    total_anchor_hits = sum(anchor_hits.values())
    is_generic_risk = total_anchor_hits < 5

    # - riesgo contextual si aparece cualquier término de riesgo (después del filtro legal) al menos 1 vez
    is_contextual_risk = any(v > 0 for v in contextual_hits.values())

    return Drift_result(
        file_path=file_path,
        anchor_hits=anchor_hits,
        contextual_hits=contextual_hits,
        is_generic_risk=is_generic_risk,
        is_contextual_risk=is_contextual_risk
    )


def build_markdown_report(results: List[Drift_result], bloque_path: Path, active_nicho: str) -> str:
    lines: List[str] = []
    lines.append("# Reporte Anti-Deriva Editorial")
    lines.append("")
    lines.append(f"- **Bloque revisado:** `{bloque_path.as_posix()}`")
    lines.append(f"- **Opción activa detectada:** `{active_nicho}`")
    lines.append("")
    lines.append("Reglas usadas:")
    lines.append("- Riesgo de genérico: menos de 5 menciones totales de términos ancla.")
    lines.append("- Riesgo contextual: aparece cualquier término de riesgo contextual para la opción activa.")
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
        # Mostrar solo los que tienen hits, para no llenar el reporte
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
                lines.append("  > **NOTA:** Aparecen términos de aduanas (DUA, aduana, packing list…). Verificar si aportan al objetivo del documento según Opción Activa y el tipo de entregable.")

        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bloque", required=True, help="Ruta al bloque (ej. output/bloque_1)")
    parser.add_argument("--salida", required=True, help="Ruta del reporte MD (ej. reports/reporte_deriva_bloque_1.md)")
    args = parser.parse_args()

    bloque_path = Path(args.bloque).resolve()
    output_path = Path(args.salida).resolve()

    option_file = Path("docs/OPCION_ACTIVA.md").resolve()
    option_text = read_option_active(option_file)
    active_nicho = detect_active_nicho(option_text)

    md_files = sorted(bloque_path.glob("*.md"))
    results = [audit_one_file(fp, active_nicho=active_nicho) for fp in md_files]

    report_md = build_markdown_report(results, bloque_path=bloque_path, active_nicho=active_nicho)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report_md, encoding="utf-8")
    print(f"OK: reporte generado en {output_path}")


if __name__ == "__main__":
    main()
