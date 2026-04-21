# REPORTE DE CIERRE — BLOQUE

- **Bloque:** `C:/Mis Documentos/Proyectos_Wds/Proyecto_automatizaciones/cases/logistica/output/bloque_1`
- **Nombre del bloque detectado:** `bloque_1`
- **Cantidad de entregables (.md):** 3

## 1) Entregables detectados

- 06_competencia_y_benchmarking.md
- 07_estrategia_competitiva.md
- 08_curva_valor_vs_competencia.md

## 2) Reporte de Validación Determinista

> Buscando en: `C:/Mis Documentos/Proyectos_Wds/Proyecto_automatizaciones/cases/logistica/reports/reporte_validacion_bloque_1.md`

# Reporte de Validación Determinista (Entregables)

- **Bloque revisado:** `C:/Mis Documentos/Proyectos_Wds/Proyecto_automatizaciones/cases/logistica/output/bloque_1`
- **Archivos revisados:** 3
- **FAIL:** 3
- **PASS:** 0

---

## FAIL ❌ — 06_competencia_y_benchmarking.md

**Errores (bloquea cierre):**
- Falta el bloque final: 'Nota de Registro NotebookLM'.

---

## FAIL ❌ — 07_estrategia_competitiva.md

**Errores (bloquea cierre):**
- Falta el bloque final: 'Nota de Registro NotebookLM'.

---

## FAIL ❌ — 08_curva_valor_vs_competencia.md

**Errores (bloquea cierre):**
- Falta el bloque final: 'Nota de Registro NotebookLM'.

---


## 3) Reporte Anti-Deriva Editorial

> Buscando en: `C:/Mis Documentos/Proyectos_Wds/Proyecto_automatizaciones/cases/logistica/reports/reporte_deriva_bloque_1.md`

# Reporte Anti-Deriva Editorial

- **Bloque revisado:** `C:/Mis Documentos/Proyectos_Wds/Proyecto_automatizaciones/cases/logistica/output/bloque_1`
- **Sector configurado:** `logistica`
- **Opción activa detectada:** `TRANSPORTE`

Reglas usadas:
- Riesgo de genérico: menos de 5 menciones totales de términos ancla del sector.
- Riesgo contextual: aparece cualquier término de riesgo para la opción activa.

---

## GENÉRICO ⚠️ — 06_competencia_y_benchmarking.md

- **Total términos ancla:** 3
- **Detalle anclas (top):**
  - POD: 1
  - conciliación: 1
  - doc-to-cash: 1
- **Términos de riesgo contextual detectados:** 0

---

## OK ✅ — 07_estrategia_competitiva.md

- **Total términos ancla:** 5
- **Detalle anclas (top):**
  - conciliación: 2
  - doc-to-cash: 2
  - cobro: 1
- **Términos de riesgo contextual detectados:** 0

---

## GENÉRICO ⚠️ — 08_curva_valor_vs_competencia.md

- **Total términos ancla:** 2
- **Detalle anclas (top):**
  - conciliación: 1
  - doc-to-cash: 1
- **Términos de riesgo contextual detectados:** 0

---


## 4) Acción recomendada

- Si el reporte determinista contiene **FAIL**, el bloque está **BLOCKED** hasta corregir.
- Si no hay FAIL, pero hay alertas de deriva (FUERA_DE_FOCO), corregir antes de cerrar.
- Si todo está OK, los entregables quedan en **READY_FOR_REVIEW** hasta que el usuario apruebe.
