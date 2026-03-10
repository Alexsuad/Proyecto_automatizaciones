# File: ZAC_INDEX_00.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Índice principal del proyecto ZAC.
# Rol: Documentación principal y punto de entrada del repositorio.
# ──────────────────────────────────────────────────────────────────────


## Índice maestro — Proyecto ZAC (Convierte tu idea en un negocio)

**Repositorio (Fuente de verdad operativa):** este repo  
**Biblioteca / Investigación (memoria organizada):** NotebookLM (cuadernos por bloque)  
**Plan de trabajo:** CronogramaConvierteZAC.txt

---

## 1) Reglas rápidas de uso (5 líneas)
- Si el objetivo es **comunicar/explicar**, usar **Documento A** (dossier).
- Si el objetivo es **decidir/analizar/viabilidad**, usar **Documento B** (realidad interna).
- Todo entregable “válido” vive en `/output/`.
- Toda investigación profunda vive en NotebookLM, pero debe quedar referenciada aquí.
- No se avanza de bloque sin entregables y resumen ejecutivo.

---

## 2) Documentos base (docs_base/)
- Documento A: `docs_base/dossier_ampliado_proyecto_zac_operaciones_inteligentes.md`
- Documento B: `docs_base/documento_b_realidad_interna_y_marco_de_analisis_viabilidad_mercado.md`
- Cronograma: `docs_base/CronogramaConvierteZAC.txt`
- Investigación 01: `docs_base/El Ecosistema Logístico Europeo y la Transición Tecnológica.pdf`
- Investigación 02: `docs_base/Informe_ Mercado Freelance de Automatización Hiperpersonalizada en Logística (Python).pdf`
- Investigación 03: `docs_base/Proceso_Integral_Diseno_Validacion_Ejecucion_Proyectos.pdf`

---

## 3) Cuadernos NotebookLM (biblioteca)
- `ZAC_Bloque_1` — Idea, cliente, propuesta de valor, mercado inicial
- `ZAC_Bloque_2` — Legal/Jurídico (forma jurídica, RGPD, contratos, etc.)
- `ZAC_Bloque_3` — Finanzas/Precios/Fiscalidad
- `ZAC_Bloque_4` — Marca/Marketing/Ventas
- `ZAC_Tutorias` — Notas por fecha + decisiones y cambios

---

## 4) Skills NotebookLM (Herramientas del Agente)
- `.agent/skills/skill_notebooklm_bootstrap.md` — Verifica auth y crea cuadernos base.
- `.agent/skills/skill_decidir_si_requiere_investigacion.md` — Regla (Gate) para decidir si un entregable necesita investigación web.
- `.agent/skills/skill_notebooklm_research_web.md` — Orquesta la búsqueda y registra las fuentes en NotebookLM.
- `.agent/skills/skill_notebooklm_registrar_entregable.md` — Registra resúmenes estructurados de entregables finalizados en NotebookLM.
- `.agent/skills/skill_auditar_entregable.md` — Auditoría final estricta de calidad, especificidad, métricas y trazabilidad de los outputs.

---

## 4) Tablero maestro por bloque (estado y entregables)

### Convención de estado
- TODO | IN_PROGRESS | DONE | BLOCKED

### Bloque 1 — (según cronograma)
**Objetivo del bloque:** definir el corazón del proyecto + primeros análisis base.  
**Estado general:** DONE  
**Carpeta output:** `output/bloque_1/`

| Entregable | Estado | Ruta repo (output) | NotebookLM (cuaderno/sección/fecha) | Notas |
|---|---|---|---|---|
| Análisis Sectorial Logístico | DONE | output/bloque_1/00_analisis_sector_logistico_zaragoza.md | ZAC_Bloque_1 / Analisis Sectorial / 2026-03-03 | UUID inyectado. Base de la decisión estratégica |
| Mapa de Empatía (Transporte) | DONE | output/bloque_1/01_mapa_empatia_transporte.md | ZAC_Bloque_1 / Mapa Empatía Transporte / 2026-03-03 | UUID inyectado. Foco en logística terrestre pyme |
| Canvas Propuesta de Valor | DONE | output/bloque_1/02_canvas_valor.md | ZAC_Bloque_1 / Canvas Valor / 2026-03-03 | UUID inyectado. Propuesta ZAC, KPIs y segmentación Pyme de transporte |
| PESTEL | DONE | output/bloque_1/03_pestel.md | ZAC_Bloque_1 / PESTEL / 2026-03-03 | UUID inyectado. Anclas operativas |
| DAFO | DONE | output/bloque_1/04_dafo.md | ZAC_Bloque_1 / DAFO / 2026-03-03 | UUID inyectado. Anclas operativas |
| ODS (versión inicial) | DONE | output/bloque_1/05_ods_v1.md | ZAC_Bloque_1 / ODS / 2026-02-28 | ODS v1 refinado y versionado |
| Competencia y Benchmarking | DONE | output/bloque_1/06_competencia_y_benchmarking.md | ZAC_Bloque_1_Competencia / Competencia y Benchmarking / 2026-03-04 | CONVIERTE: Tipología Alta/Media/Baja. note_id: e5598ae6 |
| Estrategia Competitiva | DONE | output/bloque_1/07_estrategia_competitiva.md | ZAC_Bloque_1_Competencia / Estrategia Competitiva / 2026-03-04 | CONVIERTE: Posicionamiento. note_id: e5598ae6 |
| Curva de Valor | DONE | output/bloque_1/08_curva_valor_vs_competencia.md | ZAC_Bloque_1_Competencia / Curva de Valor / 2026-03-04 | CONVIERTE: Ejes de competencia. note_id: e5598ae6 |
| Matriz CAME | DONE | output/bloque_1/09_matriz_came.md | ZAC_Bloque_1_Competencia / Matriz CAME / 2026-03-04 | CONVIERTE: Derivada de DAFO/PESTEL. note_id: e5598ae6 |
| Business Model Canvas | DONE | output/bloque_1/10_business_model_canvas.md | ZAC_Bloque_1_Competencia / Business Model Canvas / 2026-03-04 | CONVIERTE: BMC Operativo. note_id: e5598ae6 |
| Resumen Bloque 1 (para tutor) | DONE | output/bloque_1/99_resumen_bloque_1.md | ZAC_Bloque_1 / Resumen / 2026-03-03 | UUID inyectado. |

**Gate Bloque 1 (no se avanza si falta):**
- [x] Todos los entregables anteriores están en DONE
- [x] Cada entregable tiene: Resultado + Fuentes + Insights + Próximos pasos
- [x] Resumen Bloque 1 listo para entregar

**Artefactos de Exploración (no entregables):**
- Mapa de Empatía (Comparativo): `exploracion/comparativos/artefactos/01_mapa_empatia_comparativo.md`
- Mapa de Empatía (Transitario): `exploracion/transitarios/artefactos/01_mapa_empatia_transitario.md`

---

### Bloque 2 — (según cronograma)
**Objetivo del bloque:** legal/jurídico y requisitos para operar sin riesgos.  
**Estado general:** TODO  
**Carpeta output:** `output/bloque_2/`

| Entregable | Estado | Ruta repo (output) | NotebookLM | Notas |
|---|---|---|---|---|
| [Definir según cronograma] | TODO | output/bloque_2/01_[nombre].md | ZAC_Bloque_2 / [sección] / [FECHA] |  |

**Gate Bloque 2:**
- [ ] Entregables legales completos
- [ ] Riesgos y mitigaciones documentados

---

### Bloque 3 — (según cronograma)
**Objetivo del bloque:** precios, finanzas, viabilidad económica.  
**Estado general:** TODO  
**Carpeta output:** `output/bloque_3/`

| Entregable | Estado | Ruta repo (output) | NotebookLM | Notas |
|---|---|---|---|---|
| [Definir según cronograma] | TODO | output/bloque_3/01_[nombre].md | ZAC_Bloque_3 / [sección] / [FECHA] |  |

**Gate Bloque 3:**
- [ ] Modelo de ingresos validado (hipótesis y rangos)
- [ ] Supuestos claros y conservadores

---

### Bloque 4 — (según cronograma)
**Objetivo del bloque:** marca, marketing, ventas, adquisición de clientes.  
**Estado general:** TODO  
**Carpeta output:** `output/bloque_4/`

| Entregable | Estado | Ruta repo (output) | NotebookLM | Notas |
|---|---|---|---|---|
| [Definir según cronograma] | TODO | output/bloque_4/01_[nombre].md | ZAC_Bloque_4 / [sección] / [FECHA] |  |

**Gate Bloque 4:**
- [ ] Posicionamiento y mensaje coherentes con Documento A
- [ ] Estrategia comercial realista y ejecutable

---

### Entrega final — (según cronograma)
**Objetivo:** plan final coherente con todo lo anterior.  
**Estado general:** TODO  
**Carpeta output:** `output/final/`

| Entregable | Estado | Ruta repo (output) | NotebookLM | Notas |
|---|---|---|---|---|
| Documento final / Plan | TODO | output/final/plan_final.md | ZAC_Tutorias / Consolidado / [FECHA] |  |

---

## 5) Registro de tutorías y cambios (log)
| Fecha | Qué cambió | Impacta a | Acción |
|---|---|---|---|
| 2026-03-04 | Aprobado Análisis Sectorial | Bloque 1 | Estado en índice → DONE |
| 2026-03-04 | Aprobado Mapa de Empatía Transporte | Bloque 1 | Estado en índice → DONE |
| 2026-03-04 | Aprobado Canvas Propuesta de Valor | Bloque 1 | Estado en índice → DONE |
| 2026-03-04 | Aprobado PESTEL Bloque 1 (Gates PASS) | Bloque 1 | Estado en índice → DONE |
| 2026-03-04 | Aprobado DAFO Bloque 1 (Gates PASS) | Bloque 1 | Estado en índice → DONE |
| 2026-03-04 | Aprobado ODS Bloque 1 (Gates PASS) | Bloque 1 | Estado en índice → DONE |
| 2026-03-04 | Aprobado Resumen Bloque 1 | Bloque 1 | Estado en índice → DONE |
| [FECHA] | [Cambio] | [Bloque/Docs] | [Acción concreta] |
