# File: docs/governance/PLAN_SANEAMIENTO_FISICO_v0.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Plan documental de clasificación de hallazgos del dry-run v0.
# Rol: Documento de gobernanza y control operativo de transición.
# ──────────────────────────────────────────────────────────────────────

# PLAN_SANEAMIENTO_FISICO_v0

## 1. Estado
Propuesto / Pendiente de aprobación humana.

---

## 2. Propósito
Clasificar los hallazgos detectados por el dry-run de saneamiento físico v0 y preparar decisiones humanas posteriores sin ejecutar ninguna acción física.

---

## 3. No objetivos
Este plan es estrictamente de carácter documental y de diagnóstico de gobernanza. No autoriza en absoluto las siguientes acciones físicas u operativas sobre el repositorio:
- mover archivos o carpetas;
- borrar archivos o carpetas;
- renombrar archivos o carpetas;
- limpiar la carpeta `docs_base/`;
- limpiar la carpeta `output/`;
- mover la carpeta `cases/logistica/`;
- tocar o alterar el runtime en `src/` o `core/`;
- modificar scripts de producción o automatizaciones en `scripts/`;
- modificar el suite de pruebas en `tests/`;
- modificar los manifiestos de gobernanza (`repo_identity.yml` o `artifact_manifest.yml`);
- ejecutar comandos destructivos de control de versiones como `git rm` o `git rm --cached`;
- ejecutar `git add`;
- ejecutar `git commit`;
- ejecutar `git push`.

---

## 4. Fuente principal
El análisis y las clasificaciones propuestas en este plan se fundamentan directamente en la evidencia registrada en:
- `reports/saneamiento/AUDITORIA_DRY_RUN_SANEAMIENTO_FISICO.md`

---

## 5. Resumen ejecutivo
- **Resultado Global del Dry-Run:** `FAIL` (Código de salida: `2`).
- **Grupos Principales de Hallazgos:** 
  1. Carpetas y archivos de zonas legacy y contaminadas registradas activamente en el control de versiones (Git).
  2. Documentación técnica de diseño o decisiones (`.md`) archivada en zonas de cuarentena no normativas.
  3. Dependencias de código activo (scripts y pruebas de runtime) referenciando de manera rígida estructuras sectoriales o históricas (`cases/logistica/`).
- **Razón de No Ejecución Física:** La gobernanza documental establecida en `repo_identity.yml` prohíbe de forma explícita la ejecución autónoma de limpiezas físicas (`allows_cleanup: false`) y exige que cualquier acción de saneamiento sea precedida de un análisis minucioso de clasificación de destino y cuente con aprobación humana formal escrita.

---

## 6. Grupos de hallazgos
Los elementos analizados se han organizado bajo las siguientes categorías de gobernanza:
1. **Legacy trackeado en Git:** Carpetas enteras como `docs_base/`, `output/` o `cases/logistica/` que contienen archivos bajo control de versiones.
2. **Documentos Markdown en zonas no normativas:** Archivos de decisiones de diseño o inventarios ubicados bajo carpetas legacy en lugar de `docs/`.
3. **Output histórico:** Reportes e informes acumulados en la carpeta `output/`.
4. **Caso logístico histórico:** Estructura sectorial real de pruebas en `cases/logistica/` que no pertenece al framework base limpio.
5. **Templates transicionales:** Plantillas antiguas en `core/templates/` que violan la asignación de la ruta canónica del manifest.
6. **Referencias operativas reales a rutas legacy:** Código en scripts generales y de prueba que realiza importaciones o lecturas duras de archivos en `cases/logistica/` o dependencias de `output/`.
7. **Referencias informativas o de auditoría:** Comentarios explicativos, docstrings o cadenas de ayuda en argparse que mencionan de forma puramente informativa las zonas legacy.
8. **Temporales y cachés:** Directorios locales de desarrollo físico como `.venv/` o carpetas temporales locales de casos.
9. **Posibles falsos positivos:** Cadenas de texto en utilidades de prueba que coinciden con los patrones pero no representan una dependencia operativa real del framework.
10. **Elementos que requieren decisión humana:** Archivos críticos que no tienen un destino evidente y requieren la intervención directa del operador para decidir si conservarse o excluirse.

---

## 7. Matriz de clasificación y decisión

| ID | Grupo | Ruta / patrón | Tipo | Riesgo | Clasificación propuesta | Acción propuesta | Acción autorizada | Requiere aprobación humana | Observaciones |
| -- | ----- | ------------- | ---- | ------ | ---------------------- | ---------------- | ----------------- | -------------------------- | ------------- |
| M-001 | Legacy trackeado | `docs_base/` | Directorio | Alto | archivar fuera del framework madre | Mantener en cuarentena física local; programar exclusión en rama transicional. | Ninguna | Sí | Contiene archivos trackeados en Git. |
| M-002 | Output histórico | `output/` | Directorio | Alto | excluir del baseline | Dejar en cuarentena y archivar fuera del framework madre. | Ninguna | Sí | Contiene reportes históricos generados. |
| M-003 | Caso logístico | `cases/logistica/` | Directorio | Alto | conservar como histórico | Archivar fuera del framework madre y aislar en rama separada. | Ninguna | Sí | Caso de uso sectorial real. |
| M-004 | Templates transic. | `core/templates/` | Directorio | Alto | promover parcialmente | Clasificar destino antes de cualquier acción para migrar a `templates/` canónico. | Ninguna | Sí | Ubicación no recomendada en SPEC-002. |
| M-005 | Markdown no normat. | `docs_base/*.md` | Archivo | Medio | clasificar destino antes de cualquier acción | Promover parcialmente a `docs/` o `docs/specs/` si aporta valor normativo; si no, archivar. | Ninguna | Sí | Documentos de diseño fuera de `docs/`. |
| M-006 | Markdown no normat. | `output/**/*.md` | Archivo | Medio | clasificar destino antes de cualquier acción | Promover parcialmente a `docs/` o archivar fuera del framework. | Ninguna | Sí | Evidencias y reportes generados. |
| M-007 | Ref. operativas reales | `scripts/audit_repo_baseline.py` | Código | Alto | documentar como deuda técnica | Refactorizar dependencias a rutas duras usando fixtures sintéticos. | Ninguna | Sí | Referencias en código activo a `cases/logistica`. |
| M-008 | Ref. operativas reales | `scripts/test_dmv_manager.py` | Código | Alto | documentar como deuda técnica | Refactorizar test para usar fixtures sintéticos independientes. | Ninguna | Sí | Depende de dmv_test.json en caso logístico. |
| M-009 | Ref. informativas | `scripts/auditar_deriva_editorial.py` | Código | Bajo | conservar como histórico | Mantener comentario o documentación informativa sin alterar. | Ninguna | Sí | Referencia informativa de argparse. |
| M-010 | Temporales y cachés | `cases/tmp_*/` | Directorio | Bajo | excluir del baseline | Asegurar exclusión en Git y mantener en cuarentena física local. | Ninguna | Sí | Carpetas de desarrollo local temporales. |

---

## 8. Clasificaciones permitidas
Para toda toma de decisiones sobre el repositorio se usarán de forma exclusiva las siguientes clasificaciones neutrales:
- **conservar como histórico:** Mantener el elemento en un repositorio o rama histórica de transición, reconociendo su valor de archivo pero fuera del framework limpio.
- **archivar fuera del framework madre:** Extraer del working tree y guardarlo en un almacenamiento o repositorio externo dedicado a casos sectoriales.
- **excluir del baseline:** Asegurar que la ruta esté declarada en `.gitignore` y no forme parte de los archivos trackeados por el framework.
- **promover parcialmente:** Evaluar qué elementos del contenido (por ejemplo, partes de un Markdown) tienen valor normativo real y reubicarlos en la carpeta canónica correspondiente de `docs/`.
- **dejar en cuarentena:** Mantener el archivo o carpeta sin tocar, aislado en el árbol de trabajo local actual sin integrarse a Git.
- **eliminar solo con aprobación humana posterior:** Programar el borrado del elemento del sistema de archivos local únicamente tras confirmación explícita y escrita del operador humano.
- **revisar como falso positivo:** Analizar si la coincidencia de texto en código no representa un acoplamiento real y puede ignorarse de manera segura.
- **convertir en regla futura del auditor:** Incorporar la validación como una verificación fija en scripts de integración futura.
- **documentar como deuda técnica:** Registrar el acoplamiento en la especificación técnica general del framework para su posterior resolución por parte del equipo de desarrollo.

---

## 9. Checklist de decisión humana
Antes de autorizar cualquier acción física sobre un hallazgo de la matriz, el operador humano debe evaluar las siguientes preguntas de gobernanza:
- ¿Este archivo contiene valor normativo real para el framework madre limpio?
- ¿Es evidencia histórica de la ejecución que deba preservarse?
- ¿Su contenido pertenece al ámbito de producto/negocio y no al framework base de gobernanza?
- ¿Debe conservarse fuera del repositorio del framework madre (ej. en un repositorio de proyecto vivo)?
- ¿Debe excluirse de Git de forma permanente mediante reglas de ignore?
- ¿Debe promoverse parcialmente alguna parte de su contenido a una zona normativa aprobada?
- ¿Debe quedar temporalmente en cuarentena local sin alteración?
- ¿Requiere validación final por parte del responsable técnico (Alex)?
- ¿Requiere validación técnica adicional de impacto antes de ser reubicado?
- ¿Puede eliminarse definitivamente de forma segura solo después de haber realizado un respaldo externo y contar con aprobación expresa?

---

## 10. Bloqueos
Se declaran los siguientes bloqueos operativos automáticos de seguridad en esta versión del plan:
- **No se autoriza saneamiento físico** (eliminación, borrado o movimiento).
- **No se autoriza `git rm`** ni operaciones destructivas de indexado.
- **No se autoriza mover carpetas** a otras rutas físicas.
- **No se autoriza limpiar `output/`**.
- **No se autoriza limpiar `docs_base/`**.
- **No se autoriza tocar ni alterar `cases/logistica/`**.
- **No se autoriza modificar el runtime** (`src/` o `core/`).
- **No se autoriza modificar los manifiestos** de gobernanza ni roles.

---

## 11. Salida esperada de la siguiente fase
La siguiente fase aprobada del cronograma consistirá en el desarrollo de un **dry-run de acciones propuestas** (simulación detallada del plan de migración de dependencias de código y documentación) sin ejecutar ningún cambio físico real en el working tree.

---

## 12. Criterio de cierre
Esta microfase documental se considerará cerrada exitosamente solo si:
- se clasifican formalmente todos los hallazgos en la matriz;
- no se autoriza ninguna acción física o comando destructivo en el repositorio;
- se diferencian claramente los niveles de riesgo y tipos de hallazgo;
- se definen las decisiones humanas a través del checklist de gobernanza;
- no se mezclan aspectos de producto/negocio con reglas de gobernanza;
- se establecen los límites para que los datos legacy queden fuera de la base limpia;
- se proyecta la siguiente simulación sin alterar el sistema de archivos actual.
