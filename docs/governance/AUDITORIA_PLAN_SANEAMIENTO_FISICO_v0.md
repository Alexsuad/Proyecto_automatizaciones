# File: docs/governance/AUDITORIA_PLAN_SANEAMIENTO_FISICO_v0.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Reporte de auditoría y validación del Plan de Saneamiento Físico v0.
# Rol: Validador de gobernanza y control de calidad documental de transición.
# ──────────────────────────────────────────────────────────────────────

# AUDITORIA_PLAN_SANEAMIENTO_FISICO_v0

## 1. Estado
Propuesto / Pendiente de aprobación humana.

---

## 2. Propósito
Auditar el plan documental de clasificación de hallazgos y determinar si está listo para servir como base de un futuro dry-run de acciones propuestas.

---

## 3. Fuente auditada
- [PLAN_SANEAMIENTO_FISICO_v0.md](PLAN_SANEAMIENTO_FISICO_v0.md) (ubicado en `docs/governance/PLAN_SANEAMIENTO_FISICO_v0.md`)

---

## 4. Fuentes de contraste
- `reports/saneamiento/AUDITORIA_DRY_RUN_SANEAMIENTO_FISICO.md`
- `docs/specs/HARD_SPEC_SANEAMIENTO_FISICO.md`
- `artifact_manifest.yml`
- `repo_identity.yml`
- `docs/specs/SPEC-004_artifact_classification.md`

---

## 5. Matriz de auditoría del plan

| ID | Criterio auditado | Resultado | Evidencia | Riesgo si falla | Observación |
| -- | ----------------- | --------- | --------- | --------------- | ----------- |
| A-001 | El plan tiene estado correcto | `PASS` | Sección 1 declara "Propuesto / Pendiente de aprobación humana". | Alto | Evita la confusión de un borrador con un plan aprobado. |
| A-002 | El plan no se autoaprueba | `PASS` | El documento establece claramente la necesidad de aprobación humana formal por escrito (Sección 9 y 10). | Alto | Impide que la IA tome acciones autónomas sobre saneamientos físicos. |
| A-003 | El plan no autoriza saneamiento físico | `PASS` | Sección 3 (No objetivos) y Sección 10 (Bloqueos) prohíben de forma rotunda limpiezas físicas. | Crítico | Evita la pérdida o desestructuración del working tree de manera accidental. |
| A-004 | La matriz mantiene `Acción autorizada = Ninguna` | `PASS` | En la Sección 7, todas las filas de la matriz registran "Ninguna" en la columna de acción autorizada. | Crítico | Previene la ejecución errónea de acciones bajo supuestas autorizaciones implícitas. |
| A-005 | El plan clasifica hallazgos en grupos comprensibles | `PASS` | Sección 6 agrupa los hallazgos en 10 categorías formales de gobernanza técnica. | Medio | Facilita la toma de decisiones al organizar el volumen de hallazgos del dry-run. |
| A-006 | El plan distingue propuesta de autorización | `PASS` | La matriz contiene columnas de "Clasificación propuesta" y "Acción propuesta", separadas de "Acción autorizada". | Alto | Evita la ejecución prematura de propuestas no validadas por el usuario. |
| A-007 | El plan no ordena mover ni borrar | `PASS` | Excluido de forma explícita en Sección 3 y bloqueado en Sección 10. | Crítico | Garantiza la inmutabilidad física del repositorio durante esta fase. |
| A-008 | El plan no ordena limpiar `output/` | `PASS` | Bloqueo absoluto documentado en la Sección 10. | Crítico | Evita la eliminación de reportes y registros de logs de auditorías anteriores. |
| A-009 | El plan no ordena limpiar `docs_base/` | `PASS` | Excluido de no objetivos y bloqueado en la sección 10. | Alto | Preserva documentación histórica sujeta a análisis. |
| A-010 | El plan no ordena mover `cases/logistica/` | `PASS` | Bloqueo explícito en la Sección 10. | Alto | Evita la alteración o rotura de los casos de uso sectoriales históricos del repositorio. |
| A-011 | El plan no modifica ni exige modificar manifests | `PASS` | Sección 3 y 10 prohíben modificar `artifact_manifest.yml` o `repo_identity.yml`. | Alto | Mantiene la coherencia de la gobernanza documental inalterada. |
| A-012 | El plan no mezcla negocio/producto con gobernanza | `PASS` | El plan se enfoca estrictamente en la higiene de Git, dependencias de código y exclusiones. | Medio | Evita contaminar las reglas de gobierno con variables funcionales de producto. |
| A-013 | El plan identifica posibles falsos positivos | `PASS` | En la Sección 6 (Grupo 9) y la matriz (ID M-009) se consideran referencias informativas y de ayuda. | Bajo | Ahorra esfuerzo de refactorización en código de argparse o comentarios informativos. |
| A-014 | El plan prepara una fase posterior de dry-run de acciones | `PASS` | Sección 11 define claramente la simulación de las acciones propuestas como el siguiente paso. | Medio | Evita saltar de la planificación a la ejecución directa sin simulación de impacto. |
| A-015 | El plan mantiene bloqueo de ejecución física | `PASS` | Sección 10 enumera los bloqueos automáticos inmutables. | Crítico | Asegura que la IA se mantenga en modo de solo lectura estricto. |

---

## 6. Observaciones bloqueantes
- **No se detectan observaciones bloqueantes.** El plan cumple de forma rigurosa y alineada con los criterios establecidos en las Hard Specs y la gobernanza documental aprobada del repositorio.

---

## 7. Observaciones no bloqueantes
- **Deuda Técnica de Fixtures:** Las dependencias identificadas en la matriz en `scripts/test_dmv_manager.py` y `scripts/test_orchestrator.py` demuestran que las pruebas generales del framework están acopladas con el caso sectorial real de `cases/logistica/`. Se recomienda priorizar la creación de fixtures sintéticos mínimos dentro de `tests/` para eliminar este acoplamiento.
- **Transición de `core/templates/`:** La presencia de plantillas antiguas bajo `core/templates/` debe resolverse en fases posteriores promoviendo o unificando las plantillas de manera canónica en `templates/` tal como especifica `SPEC-002`.

---

## 8. Decisión de auditoría
- **`APROBADO PARA SIGUIENTE MICROFASE`**

---

## 9. Siguiente microfase recomendada
Se propone como la siguiente microfase del proyecto:
- **`DRY_RUN_ACCIONES_SANEAMIENTO_FISICO_v0`**

*Nota aclaratoria:* Esta futura fase debe estructurar un script de simulación que muestre de forma determinista qué archivos cambiarían y de qué manera se realizaría el desacoplamiento técnico (por ejemplo, mostrando diffs de código y simulación de comandos Git), sin realizar ningún tipo de modificación, borrado, movimiento o git push en el working tree real.

---

## 10. Bloqueos explícitos
Para asegurar la inmutabilidad física del repositorio madre, se declaran los siguientes bloqueos:
- No se autoriza saneamiento físico real.
- No se autoriza `git rm`.
- No se autoriza mover carpetas.
- No se autoriza borrar archivos.
- No se autoriza limpiar `output/`.
- No se autoriza limpiar `docs_base/`.
- No se autoriza tocar `cases/logistica/`.
- No se autoriza modificar runtime en `src/` o `core/`.
- No se autoriza modificar manifests (`repo_identity.yml` o `artifact_manifest.yml`).
- No se autoriza modificar scripts ni tests existentes.

---

## 11. Criterio de cierre
Esta microfase de auditoría se considerará completada con éxito cuando el documento de auditoría sea registrado en el control de versiones local de manera selectiva, garantizando que el plan original no ha sido modificado y que ninguna acción física ha sido autorizada ni ejecutada.
