# File: docs/specs/HARD_SPEC_SANEAMIENTO_FISICO.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Especificación Técnica Dura (Hard Spec) de la verificación previa al saneamiento físico.
# Rol: Documento de gobernanza técnica y diseño de la microfase SDD.
# ──────────────────────────────────────────────────────────────────────

## Estado
Propuesto / Pendiente de aprobación humana.

---

## 1. Propósito y Declaración de Alcance

Este documento define las especificaciones técnicas para la ejecución de la microfase `Dry-run verificable de saneamiento físico v0`.

> [!IMPORTANT]
> **Declaración de No Acción Física:** No se implementa saneamiento físico. Se implementa verificación previa al saneamiento físico.
> El script de dry-run debe operar bajo estricto modo de **solo lectura**, sin realizar modificaciones, movimientos, renombrados o borrados en el repositorio real.

El objetivo es proporcionar una herramienta determinista que analice el repositorio y genere evidencia de discrepancias o contradicciones entre la gobernanza documental (definida en `repo_identity.yml` y `artifact_manifest.yml`) y el estado físico actual del repositorio.

---

## 2. No Objetivos
- Realizar limpieza, eliminación o movimiento de archivos o carpetas.
- Modificar el archivo `artifact_manifest.yml` o `repo_identity.yml`.
- Automatizar la corrección de errores sin supervisión y aprobación humana explícita.
- Modificar el código productivo o runtime existente.

---

## 3. Documentos Normativos de Referencia
El análisis se fundamenta en las reglas establecidas en:
1. `repo_identity.yml`: Identidad del repositorio y limitaciones operativas.
2. `artifact_manifest.yml`: Manifiesto defensivo que clasifica qué archivos pertenecen al framework madre y cuáles son legacy/excluidos.
3. `docs/specs/SPEC-001_artifact_manifest.md`: Especificación detallada del manifiesto de artefactos.
4. `docs/specs/SPEC-002_estructura_repositorios_carpetas.md`: Especificación de la estructura organizativa y de carpetas del repositorio.
5. `docs/specs/SPEC-003_repo_identity.md`: Especificación de identidad de repositorios en Antigravity 2.0.

---

## 4. Rutas Críticas a Revisar y Justificación de Alcance
El dry-run analizará y cruzará las siguientes rutas:
- Zonas Legacy / Transicionales (Excluidas en el Manifiesto):
  - `docs_base/`
  - `output/`
  - `cases/logistica/`
  - `core/templates/`
- Zonas del Framework Madre (Permitidas en el Manifiesto):
  - `scripts/`
  - `tests/`
  - `src/`
  - `core/` (excluyendo subruta templates)

### Justificación de Exclusión de `.agent/` (Opción B - Conservadora)
Se ha optado por **excluir `.agent/` del alcance de esta microfase** y dejarlo para una microfase posterior dedicada. La carpeta `.agent/` contiene archivos de configuración de sistema y skills críticas del runtime agéntico. Manipular o inspeccionar estas rutas en un script general de saneamiento incrementa el riesgo de efectos colaterales en la orquestación. Por tanto, aislar su análisis es el enfoque más seguro y coherente con las directrices de bajo riesgo del framework madre.

---

## 5. Reglas de Detección e Interpretación

El script de dry-run clasificará las inconsistencias bajo tres categorías:

### 5.1 Hallazgo
Se define como la presencia física de elementos o zonas clasificadas como legacy, transicionales o temporales que existen en el árbol de trabajo local, pero que no rompen necesariamente la integridad del framework si están correctamente excluidas del control de versiones (Git).
- *Ejemplo:* La carpeta `docs_base/` o `cases/logistica/` existe físicamente en el directorio, pero no tiene archivos agregados a Git.
- *Nivel de Gravedad:* Bajo / Informativo. Requiere revisión humana eventual.

### 5.2 Contradicción
Ocurre cuando la estructura o el comportamiento del repositorio viola directamente las directrices de la gobernanza documental aprobada.
- *Ejemplo 1:* Un archivo dentro de una zona excluida (`docs_base/`, `output/`, `cases/logistica/`) está trackeado en Git (está en el control de versiones, violando su `copy_policy: exclude` y `allowed_in_framework: false`).
- *Ejemplo 2:* Un script del runtime general (en `scripts/` o `src/`) o un test general (en `tests/`) importa o referencia de manera dura archivos de rutas legacy (como `cases/logistica/`) en lugar de utilizar datos o fixtures sintéticos autocontenidos.
- *Ejemplo 3:* Presencia de documentos Markdown de diseño técnico o decisiones arquitectónicas (`.md`) dentro de zonas no normativas (`docs_base/` u `output/`) en lugar de `docs/`.
- *Ejemplo 4:* El rol del repositorio (`repo_role`) difiere entre `repo_identity.yml` y `artifact_manifest.yml`.
- *Nivel de Gravedad:* Alto. Genera un fallo en la auditoría (`FAIL`).

### 5.3 Bloqueo
Situaciones de error técnico que impiden la ejecución confiable de la verificación previa.
- *Ejemplo:* Ausencia física de `repo_identity.yml` o `artifact_manifest.yml`, o corrupción de su estructura que impida la lectura.
- *Nivel de Gravedad:* Crítico. Provoca una salida de error inmediato (`ERROR_TECNICO`).

---

## 6. Comportamiento Restringido del Dry-Run
El dry-run **NUNCA** debe:
- Modificar, renombrar, mover o borrar ningún archivo.
- Hacer `git add`, `git commit` o `git push`.
- Modificar variables de entorno o configuraciones del sistema.

---

## 7. Códigos de Salida

El script devolverá los siguientes códigos numéricos a la consola:
- **`0` (PASS):** El repositorio está en perfecto estado, no existen zonas legacy físicas y no hay ninguna contradicción.
- **`1` (WARN):** El dry-run se ejecutó exitosamente. No hay contradicciones graves, pero se detectaron hallazgos físicos (carpetas legacy existentes en el working tree que están correctamente excluidas en Git) o referencias informativas (comentarios, docstrings, o textos de ayuda en argparse).
  - *Restricción:* `WARN` indica estado transicional y **no autoriza** la eliminación física.
- **`2` (FAIL):** Se detectaron contradicciones graves (dependencias operativas reales o archivos legacy trackeados en Git) que violan la gobernanza del framework madre.
  - *Restricción:* `FAIL` **no autoriza** correcciones automáticas; obliga a la intervención humana para resolver las inconsistencias detectadas.
- **`3` (ERROR_TECNICO):** El dry-run no pudo ejecutarse de manera confiable debido a que no es un repositorio Git válido o por falta de archivos normativos u otros problemas del sistema.
  - *Restricción:* **No autoriza** continuar el pipeline de integración o desarrollo.

---

## 8. Formato del Reporte de Evidencia
El script generará el reporte Markdown en la ruta:
`reports/saneamiento/AUDITORIA_DRY_RUN_SANEAMIENTO_FISICO.md`

El reporte deberá contener de forma estructurada:
1. **Resumen Ejecutivo:** Resultado global y código de salida.
2. **Metadatos de Ejecución:** Fecha/hora y contexto.
3. **Documentos Normativos Analizados:** Lista de archivos de configuración leídos.
4. **Matriz de Hallazgos y Contradicciones:** Tabla detallada con los campos:
   `| ID | Ruta | Zona detectada | Clasificación normativa | Hallazgo | Riesgo | Acción propuesta | Requiere aprobación humana | Resultado |`
5. **Decisiones Humanas Pendientes:** Detalle de qué requiere la intervención del usuario bajo la siguiente regla de decisión:
   > "Clasificar destino antes de cualquier acción: promover, archivar, conservar como histórico, excluir, dejar en cuarentena o eliminar solo con aprobación humana posterior."
6. **Confirmación de Seguridad:** Declaración explícita de que no se ha modificado ningún archivo.

---

## 9. Criterios de Aceptación
1. El script finaliza con `0`, `1`, `2` o `3` de forma consistente.
2. Se analiza la presencia física y el trackeo en Git de las rutas críticas.
3. Se detectan referencias duras a `cases/logistica/` en scripts y tests generales.
4. Se genera el reporte en Markdown en la ruta correcta con toda la información requerida.
5. Los tests de pytest corren con fixtures sintéticos independientes de `cases/logistica/`.
