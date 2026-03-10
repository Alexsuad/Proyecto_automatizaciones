"""
scripts/gate_coherencia_cruzada.py
# File: scripts/gate_coherencia_cruzada.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Detectar incoherencias de clasificación HECHO/HIPÓTESIS entre documentos del mismo bloque.
# Rol: Gate de coherencia cruzada (alerta, no bloquea).
# ──────────────────────────────────────────────────────────────────────

OBJETIVO
--------
Detectar que la misma afirmación o entidad clave no aparezca clasificada como
[HECHO] en un documento e [HIPÓTESIS] en otro.

Este gate SOLO ALERTA. No bloquea el pipeline.
Las alertas deben revisarse manualmente y corregir en la tanda de contenido correspondiente.

USO
---
uv run python scripts/gate_coherencia_cruzada.py --bloque output/bloque_1 --salida reports/reporte_coherencia_cruzada_bloque_1.md
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Tuple


# ---------------------------------------------------------------------
# Configuración
# ---------------------------------------------------------------------

# Entidades clave a rastrear entre documentos.
# Se añaden entidades conocidas del proyecto + cualquier que aparezca en un [HECHO] numérico
ENTIDADES_CLAVE = [
    "Fenadismer",
    "MITMA",
    "DBK",
    "IRU",
    "CETM",
    "PLAZA",
    "Kit Digital",
    "Dashdoc",
    "SAP",
    "Track-POD",
    "Igarle",
    "ICLE",
    "IAF",
]

# Regex para capturar fragmentos con [HECHO] o [HIPÓTESIS] y texto circundante
HECHO_REGEX = re.compile(
    r"\[HECHO\].{0,200}",
    re.IGNORECASE | re.DOTALL
)
HIPOTESIS_REGEX = re.compile(
    r"\[HIP[OÓ]TESIS\].{0,200}",
    re.IGNORECASE | re.DOTALL
)


# ---------------------------------------------------------------------
# Modelos
# ---------------------------------------------------------------------

@dataclass
class EntidadOcurrencia:
    archivo: str
    clasificacion: str  # "HECHO" o "HIPÓTESIS"
    fragmento: str


@dataclass
class AlertaCoherencia:
    entidad: str
    ocurrencias: List[EntidadOcurrencia] = field(default_factory=list)

    @property
    def tiene_conflicto(self) -> bool:
        """Retorna True si la misma entidad aparece como HECHO en un doc e HIPÓTESIS en otro."""
        clasificaciones = {o.clasificacion for o in self.ocurrencias}
        return "HECHO" in clasificaciones and "HIPÓTESIS" in clasificaciones


# ---------------------------------------------------------------------
# Lógica de extracción
# ---------------------------------------------------------------------

def extraer_ocurrencias_entidad(
    text: str, archivo: str, entidad: str
) -> List[EntidadOcurrencia]:
    """
    Para una entidad dada, busca si aparece en el contexto de un [HECHO] o [HIPÓTESIS].
    Devuelve la lista de ocurrencias con su clasificación.
    """
    ocurrencias: List[EntidadOcurrencia] = []
    entidad_regex = re.compile(re.escape(entidad), re.IGNORECASE)

    # Buscar en fragmentos HECHO
    for m in HECHO_REGEX.finditer(text):
        frag = m.group(0)
        if entidad_regex.search(frag):
            ocurrencias.append(EntidadOcurrencia(
                archivo=archivo,
                clasificacion="HECHO",
                fragmento=frag.strip().replace("\n", " ")[:200]
            ))

    # Buscar en fragmentos HIPÓTESIS
    for m in HIPOTESIS_REGEX.finditer(text):
        frag = m.group(0)
        if entidad_regex.search(frag):
            ocurrencias.append(EntidadOcurrencia(
                archivo=archivo,
                clasificacion="HIPÓTESIS",
                fragmento=frag.strip().replace("\n", " ")[:200]
            ))

    return ocurrencias


def extraer_hechos_numericos_con_fuente(text: str) -> List[Tuple[str, str]]:
    """
    Extrae pares (cifra, fuente) de los [HECHO] que contienen números.
    Útil para detectar si la misma cifra aparece como HECHO en un doc y HIPÓTESIS en otro.
    """
    resultado: List[Tuple[str, str]] = []
    for m in HECHO_REGEX.finditer(text):
        frag = m.group(0)
        # Buscar números en el fragmento
        numeros = re.findall(r"\d+[\.,]?\d*\s*(?:%|€|días|horas)?", frag)
        # Buscar entidades de fuente cercanas
        fuente = ""
        fuente_m = re.search(r"Fuente\s+s[oó]lida\s*:\s*([^,\.\n]+)", frag, re.IGNORECASE)
        if fuente_m:
            fuente = fuente_m.group(1).strip()
        for num in numeros:
            if len(num.strip()) > 1:  # Ignorar dígitos triviales (ej. "1", "2")
                resultado.append((num.strip(), fuente))
    return resultado


def analizar_bloque(bloque_path: Path) -> Tuple[List[AlertaCoherencia], List[str]]:
    """
    Analiza todos los .md del bloque y detecta incoherencias de clasificación.
    Devuelve: (alertas, log_de_proceso)
    """
    md_files = sorted(bloque_path.glob("*.md"))
    log: List[str] = []

    # Mapa: entidad -> lista de ocurrencias en todos los archivos
    mapa: Dict[str, List[EntidadOcurrencia]] = defaultdict(list)

    for fp in md_files:
        text = fp.read_text(encoding="utf-8", errors="replace")
        nombre = fp.name
        log.append(f"Procesando: {nombre}")

        for entidad in ENTIDADES_CLAVE:
            ocurrencias = extraer_ocurrencias_entidad(text, nombre, entidad)
            if ocurrencias:
                mapa[entidad].extend(ocurrencias)
                log.append(
                    f"  {entidad}: {len(ocurrencias)} ocurrencia(s) — "
                    f"{', '.join(o.clasificacion for o in ocurrencias)}"
                )

    # Construir alertas
    alertas: List[AlertaCoherencia] = []
    for entidad, ocurrencias in mapa.items():
        alerta = AlertaCoherencia(entidad=entidad, ocurrencias=ocurrencias)
        if alerta.tiene_conflicto:
            alertas.append(alerta)

    return alertas, log


# ---------------------------------------------------------------------
# Generador de reporte
# ---------------------------------------------------------------------

def build_markdown_report(
    alertas: List[AlertaCoherencia],
    log: List[str],
    bloque_path: Path
) -> str:
    lines: List[str] = []
    lines.append("# Reporte Gate — Coherencia Cruzada de Clasificaciones")
    lines.append("")
    lines.append(f"- **Bloque analizado:** `{bloque_path.as_posix()}`")
    lines.append(f"- **Entidades rastreadas:** {len(ENTIDADES_CLAVE)}")
    lines.append(f"- **Alertas de incoherencia:** {len(alertas)}")
    lines.append("")
    lines.append("> Este gate SOLO ALERTA, no bloquea.")
    lines.append("> Las alertas deben revisarse manualmente y corregirse en la tanda de contenido correspondiente.")
    lines.append("")
    lines.append("---")
    lines.append("")

    if not alertas:
        lines.append("## ✅ Sin alertas de incoherencia")
        lines.append("")
        lines.append("Ninguna entidad clave aparece clasificada de forma contradictoria entre documentos.")
    else:
        lines.append("## ⚠️ Alertas detectadas")
        lines.append("")
        for alerta in alertas:
            lines.append(f"### Entidad: `{alerta.entidad}`")
            lines.append("")
            # Agrupar por clasificación
            hechos = [o for o in alerta.ocurrencias if o.clasificacion == "HECHO"]
            hipotesis = [o for o in alerta.ocurrencias if o.clasificacion == "HIPÓTESIS"]
            lines.append(f"- **Aparece como [HECHO] en:**")
            for o in hechos:
                lines.append(f"  - `{o.archivo}`: ...{o.fragmento[:120]}...")
            lines.append(f"- **Aparece como [HIPÓTESIS] en:**")
            for o in hipotesis:
                lines.append(f"  - `{o.archivo}`: ...{o.fragmento[:120]}...")
            lines.append("")
            lines.append("**Acción recomendada:** revisar cuál clasificación es correcta y estandarizar en todos los documentos.")
            lines.append("")
            lines.append("---")
            lines.append("")

    lines.append("")
    lines.append("## Log de proceso")
    lines.append("")
    lines.append("```")
    lines.extend(log)
    lines.append("```")
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Gate de coherencia cruzada — detecta HECHO/HIPÓTESIS contradictorios entre documentos."
    )
    parser.add_argument(
        "--bloque", default="output/bloque_1",
        help="Ruta al bloque (ej. output/bloque_1)"
    )
    parser.add_argument(
        "--salida", default="reports/reporte_coherencia_cruzada_bloque_1.md",
        help="Ruta del reporte MD de salida"
    )
    args = parser.parse_args()

    bloque_path = Path(args.bloque).resolve()
    output_path = Path(args.salida).resolve()

    if not bloque_path.exists():
        raise SystemExit(f"Bloque no encontrado: {bloque_path}")

    alertas, log = analizar_bloque(bloque_path)
    report_md = build_markdown_report(alertas, log, bloque_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report_md, encoding="utf-8")

    if alertas:
        print(f"⚠️  {len(alertas)} alerta(s) de incoherencia detectada(s). Reporte en: {output_path}")
    else:
        print(f"✅ Sin alertas de incoherencia. Reporte en: {output_path}")


if __name__ == "__main__":
    main()
