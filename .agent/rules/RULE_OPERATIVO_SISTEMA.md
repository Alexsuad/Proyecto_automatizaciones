---
description: Reglas operativas críticas del Proyecto_automatizaciones que el agente debe respetar siempre
---

# Regla Operativa Sistema_ProyectoAuto

## 1. Opción activa manda
- La fuente de verdad es `docs/OPCION_ACTIVA.md`.
- Todo entregable en `output/` debe alinearse con la opción activa declarada.
- Si hay cambio de opción → primero registrar en `docs/DECISION_LOG.md`, luego actualizar `docs/OPCION_ACTIVA.md`.

## 2. Output vs Exploración
- `output/` = entregables oficiales del cronograma (un solo camino activo).
- `exploracion/` = comparativos, opciones descartadas, pivotes.
- Nunca mezclar ambos propósitos en el mismo archivo.

## 3. Voz institucional obligatoria
- Siempre voz de equipo: "nosotros", "el equipo", "se propone", "se valida".
- Prohibida primera persona singular.
- Prohibida jerga bélica/grandilocuente (ver glosario en `docs/ESTILO_00_guia_tono_y_voz_equipo.md`).
- Prohibido adjetivar negativamente a la competencia.
- Promesas absolutas → siempre como `[HIPÓTESIS]` + `[CÓMO SE VALIDA]`.

## 4. Gates de calidad (Pipeline Python vs IA)

**A. Responsabilidad de Scripts Python (Determinista, Estructural, Riguroso):**
- **Gate 0:** Estilo y voz (`scripts/validar_estilo_equipo.py`). Cero primera persona, métricas anti-humo.
- **Gate 1:** Fuentes y veracidad (`scripts/validar_entregables.py`). HECHOS numéricos exigen fuente sólida.
- **Gate 2.1:** Anti-deriva (`scripts/auditar_deriva_editorial.py`). Alineación de dominio.
- **Gate 3:** Densidad de Métricas (`scripts/validar_entregables.py`).
- **Gate 4:** Trazabilidad NotebookLM (`scripts/validar_entregables.py`). **Formato AMBOS IDs obligatorios.**
- **Gate 5:** Coherencia cruzada (`scripts/gate_coherencia_cruzada.py`). Clasificaciones HECHO/HIPÓTESIS consistentes entre documentos.

**B. Responsabilidad de la IA (Cualitativa, Estratégica, Semántica):**
- **Gate 7:** Auditoría Semántica Estricta (`skill_auditar_entregable.md`).
- Evalúa riesgo narrativo, alineación real del dolor, validez del argumento por entregable.
- Emite un veredicto y guarda el reporte real en `reports/auditoria_semantica_<archivo>.md`.
- **Gate 8:** Supervisor de Coherencia Global (`skill_supervisor_coherencia_global.md`).
- Capa final de revisión del bloque completo. No repite QA individual.
- Detecta contradicciones entre documentos (ej. cliente cambia, BMC contradice DAFO, etc).
- Documenta en `reports/auditoria_supervisor_global_bloque_<N>.md`. Emite el OK final para sellar un bloque.

## 5. NotebookLM obligatorio
- Todo HECHO numérico debe tener fuente sólida importada en NotebookLM.
- **1 entregable = 2 notas dedicadas** (HITO de registro + Auditoría Semántica Gate 7).
- Prohibido reutilizar UUID entre entregables distintos.
- El reporte Gate 7 **debe guardarse en `reports/`** con nombre estándar: `auditoria_semantica_<nombre_archivo>.md`.

## 6. No DONE sin aprobación explícita
- El agente no puede mover documentos a DONE sin que el usuario escriba: `Aprobado: [nombre] (ruta)`.
- Estados: TODO → IN_PROGRESS → READY_FOR_REVIEW → DONE | BLOCKED.

## 7. Regla de Familiaridad Técnica (Pedagogía de Equipo)
- Es obligatorio aplicar el formato `término (explicación sencilla)` para tecnicismos no evidentes, según se detalla en la sección 7 de `docs/ESTILO_00_guia_tono_y_voz_equipo.md`.
- Objetivo: Alinear el lenguaje interno con el del negocio y facilitar el aprendizaje progresivo del equipo.
