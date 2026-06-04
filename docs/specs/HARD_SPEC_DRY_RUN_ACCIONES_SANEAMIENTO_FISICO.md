# File: docs/specs/HARD_SPEC_DRY_RUN_ACCIONES_SANEAMIENTO_FISICO.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Especificación formal (Hard Spec) para el dry-run de acciones.
# Rol: Definición del marco normativo y contrato de simulación.
# ──────────────────────────────────────────────────────────────────────

# HARD_SPEC_DRY_RUN_ACCIONES_SANEAMIENTO_FISICO

## 1. Estado
Propuesto / Pendiente de aprobación humana.

## 2. Propósito
Definir el contrato documental para simular acciones de saneamiento físico propuestas, sin ejecutar ninguna acción real sobre el repositorio.

## 3. No objetivos
Esta microfase documental es estrictamente simulada y de diagnóstico lógico. No autoriza, permite ni instruye a la realización de ninguna de las siguientes acciones físicas o de control de cambios sobre el repositorio:
- mover archivos o carpetas;
- borrar archivos o carpetas;
- renombrar archivos o carpetas;
- ejecutar comandos Git de desindexación (incluyendo la remoción de la caché del índice);
- ejecutar comandos Git de movimiento;
- limpiar `output/`;
- limpiar `docs_base/`;
- mover `cases/logistica/`;
- modificar runtime en `src/` o `core/`;
- modificar scripts existentes en `scripts/`;
- modificar tests existentes en `tests/`;
- modificar los archivos de manifiestos (`repo_identity.yml` o `artifact_manifest.yml`);
- hacer `git add`;
- hacer commit;
- hacer push.

## 4. Fuentes normativas
- `docs/governance/PLAN_SANEAMIENTO_FISICO_v0.md`
- `docs/governance/AUDITORIA_PLAN_SANEAMIENTO_FISICO_v0.md`
- `reports/saneamiento/AUDITORIA_DRY_RUN_SANEAMIENTO_FISICO.md`
- `artifact_manifest.yml`
- `repo_identity.yml`
- `docs/specs/SPEC-004_artifact_classification.md`
- `docs/specs/SPEC-005_agent_skills_workflows_contract.md`

## 5. Tipos de acción simulada
Se definen formalmente las siguientes tipologías de acciones conceptuales que pueden proponerse para la matriz:
- **conservar como histórico:** Aislamiento en rama o repositorio histórico de transición.
- **archivar fuera del framework madre:** Reubicación en repositorio externo del caso sectorial.
- **excluir del baseline:** Incorporación a reglas de ignore (`.gitignore`) y desindexación de Git.
- **promover parcialmente:** Extraer contenido con valor de diseño/especificación a `docs/` y descartar el resto.
- **dejar en cuarentena:** Mantener intacto y sin indexar en el árbol de trabajo local.
- **eliminar solo con aprobación humana posterior:** Programación de borrado definitivo condicionado a una firma humana.
- **revisar como falso positivo:** Confirmación de que el elemento no representa acoplamiento o desviación.
- **convertir en deuda técnica:** Registro sistemático en la especificación para resolución futura.
- **convertir en futura regla del auditor:** Automatización en scripts de validación del baseline.
- **bloquear por riesgo:** Congelamiento de cualquier propuesta por riesgo de regresión en dependencias.

## 6. Reglas de simulación
- **Simulación absoluta:** Toda acción descrita o listada tiene carácter puramente documental y simulado.
- **Prohibición de comandos activos:** No se permite escribir comandos en un formato de instrucción ejecutable directa por consola (ej. no escribir líneas sueltas de shell). Los comandos simulados deben constar como texto aclaratorio conceptual o ejemplos.
- **No ejecución por defecto:** Ninguna acción de la matriz queda autorizada para ser ejecutada en el repositorio.
- **Aprobación obligatoria posterior:** Cualquier ejecución física requerirá una microfase técnica posterior, un nuevo plan con SDD aprobado y una decisión formal humana explícita.
- **Invariabilidad de manifiestos y runtime:** No se alterará ningún comportamiento activo ni manifiesto de control del repositorio en esta microfase.

## 7. Matriz mínima de acción simulada
Toda matriz de dry-run de acciones debe poseer y cumplimentar de forma acumulativa las siguientes columnas obligatorias:

| ID | Grupo | Ruta / patrón | Hallazgo origen | Acción simulada | Riesgo | Evidencia | Comando simulado / textual | Acción ejecutada | Requiere aprobación humana | Estado |
| -- | ----- | ------------- | --------------- | --------------- | ------ | --------- | -------------------------- | ---------------- | -------------------------- | ------ |

### Reglas para columnas de control:
1. **Acción ejecutada:** Debe declararse obligatoriamente como `Ninguna` en todas las filas de la matriz.
2. **Requiere aprobación humana:** Debe declararse obligatoriamente como `Sí` en todas las filas de la matriz.
3. **Estado:** Debe reflejar uno de los siguientes valores de control documental: `Propuesto`, `Bloqueado`, `Requiere análisis`, `Posible falso positivo`.

## 8. Códigos de resultado documental
- **PASS:** El dry-run de acciones propuesto es consistente y no autoriza ni ejecuta ninguna acción física.
- **WARN:** Se detectan ambigüedades en las rutas propuestas o posibles falsos positivos que requieren una evaluación más profunda.
- **FAIL:** El documento contiene instrucciones redactadas como comandos ejecutables directos o fórmulas que induzcan a la acción física inmediata.
- **ERROR_TECNICO:** Falta alguna de las fuentes normativas de entrada indispensables para realizar la simulación documental.

## 9. Criterio de aceptación
La especificación de dry-run de acciones propuestas será aceptable si y solo si:
- No autoriza de ninguna forma operaciones de escritura, borrado o traslado en el sistema de archivos del repositorio.
- Excluye expresamente la presencia de comandos como código ejecutable.
- Garantiza que la columna `Acción ejecutada` se mantenga en `Ninguna` y `Requiere aprobación humana` en `Sí`.
- Define un entorno claro de auditoría y validación documental previa a cualquier decisión futura.
