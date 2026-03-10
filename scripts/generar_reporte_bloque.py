"""
scripts/generar_reporte_bloque.py

OBJETIVO
--------
Generar un reporte final de cierre de bloque:
- Lista de archivos del bloque
- Resultado de validación determinista (si existe el reporte previo)
- Resultado de deriva editorial (si existe el reporte previo)
- Siguiente acción recomendada: READY_FOR_REVIEW / BLOCKED

Este script NO cambia el índice. Solo genera reporte consolidado.

USO
---
python scripts/generar_reporte_bloque.py --bloque output/bloque_1 --salida reports/REPORTE_CIERRE_BLOQUE_1.md
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import List


def read_if_exists(path: Path) -> str:
    if path.exists():
        return path.read_text(encoding="utf-8", errors="replace")
    return "(No existe aún este reporte. Ejecuta primero los scripts previos.)"


def build_report(bloque_path: Path) -> str:
    md_files = sorted(bloque_path.glob("*.md"))

    lines: List[str] = []
    lines.append("# REPORTE DE CIERRE — BLOQUE")
    lines.append("")
    lines.append(f"- **Bloque:** `{bloque_path.as_posix()}`")
    lines.append(f"- **Cantidad de entregables (.md):** {len(md_files)}")
    lines.append("")
    lines.append("## 1) Entregables detectados")
    lines.append("")
    for fp in md_files:
        lines.append(f"- {fp.name}")
    lines.append("")

    lines.append("## 2) Reporte de Validación Determinista")
    lines.append("")
    lines.append(read_if_exists(Path("reports/reporte_validacion_bloque_1.md")))
    lines.append("")

    lines.append("## 3) Reporte Anti-Deriva Editorial")
    lines.append("")
    lines.append(read_if_exists(Path("reports/reporte_deriva_bloque_1.md")))
    lines.append("")

    lines.append("## 4) Acción recomendada")
    lines.append("")
    lines.append("- Si el reporte determinista contiene **FAIL**, el bloque está **BLOCKED** hasta corregir.")
    lines.append("- Si no hay FAIL, pero hay alertas de deriva (FUERA_DE_FOCO), corregir antes de cerrar.")
    lines.append("- Si todo está OK, los entregables quedan en **READY_FOR_REVIEW** hasta que el usuario apruebe.")
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bloque", required=True, help="Ruta al bloque (ej. output/bloque_1)")
    parser.add_argument("--salida", required=True, help="Ruta del reporte final MD")
    args = parser.parse_args()

    bloque_path = Path(args.bloque).resolve()
    output_path = Path(args.salida).resolve()

    if not bloque_path.exists():
        raise SystemExit(f"Bloque no encontrado: {bloque_path}")

    report_md = build_report(bloque_path=bloque_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report_md, encoding="utf-8")
    print(f"OK: reporte generado en {output_path}")


if __name__ == "__main__":
    main()
