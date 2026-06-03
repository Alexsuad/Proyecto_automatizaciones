# AGENTS.md — Instrucciones para agentes técnicos

Este documento define el protocolo de comportamiento, los límites operativos y las reglas de diseño para cualquier agente o herramienta de IA de desarrollo que interactúe con este repositorio.

---

## 1. Rol del Agente

Usted actúa como **agente técnico de desarrollo** dentro de un repositorio madre limpio (`framework_mother`). Su labor se limita a tareas de codificación, auditoría documental, validaciones técnicas y documentación en un entorno estructurado de bajo riesgo.
*   **No actúa como orquestador estratégico ni toma decisiones arquitectónicas por cuenta propia.**
*   Si una tarea resulta ambigua, deténgase y solicite aclaración al usuario.

---

## 2. Lectura obligatoria

Antes de proponer o realizar cualquier modificación en el repositorio, es estrictamente obligatorio leer los siguientes archivos para comprender la gobernanza y los límites vigentes:
*   `README.md` (Documento de entrada).
*   `repo_identity.yml` (Manifiesto de identidad del repositorio).
*   `artifact_manifest.yml` (Clasificación de artefactos).
*   `docs/specs/SPEC-001_artifact_manifest.md`
*   `docs/specs/SPEC-002_estructura_repositorios_carpetas.md`
*   `docs/specs/SPEC-003_repo_identity.md`
*   `.agent/skills/audit_repo_baseline/SKILL.md` (Protocolo del skill auditor).

---

## 3. Ejecución del Auditor Baseline

Antes de consolidar o preparar cambios estructurales, es obligatorio verificar el estado del repositorio mediante:
```bash
python scripts/audit_repo_baseline.py
```
*   El agente debe interpretar el resultado y actuar de acuerdo a las directrices de `SKILL.md`.
*   Cualquier veredicto de `FAIL` (exit code 2) bloquea de inmediato la operación y debe ser reportado.

---

## 4. Prohibiciones operativas

*   **No use staging masivo** (`git add .`, `git add -A` o equivalentes).
*   **No modifique ni haga staging** de archivos dentro de las zonas transicionales `docs_base/` y `output/` a menos que exista una instrucción directa y explícita del usuario.
*   **No altere decisiones arquitectónicas ni especificaciones aprobadas** (ADRs o SPECs) sin autorización.
*   **No crear, sobrescribir ni modificar** `repo_identity.yml` o `artifact_manifest.yml` sin instrucción explícita.
*   **No guarde credenciales, API keys ni secretos** (`.env`) en el control de versiones.

---

## 5. Reglas de Git y Commits

*   **Staging selectivo:** Agregue únicamente los archivos específicos autorizados para la tarea:
    ```bash
    git add ruta/al/archivo_especifico.ext
    ```
*   **Mensajes de commit en español:** Use mensajes profesionales en español que expliquen de forma clara qué problema corrige, dónde está el cambio y qué se reemplaza.
*   **Verificación previa:** Ejecute `git status --short` y `git diff --cached --name-only` antes de ejecutar cualquier commit para garantizar que no se introducen archivos ajenos a la tarea.

---

## 6. Regla 14 de Documentación y Comentarios

Todo archivo nuevo o modificado sustancialmente por el agente debe incluir el encabezado estándar:
```python
# File: ruta/relativa.py
# ──────────────────────────────────────────────────────────────────────
# Propósito: Descripción breve del módulo.
# Rol: Función dentro del sistema.
# ──────────────────────────────────────────────────────────────────────
```

### Comentarios permitidos:
*   `! [ALERTA]:` Riesgos técnicos graves o advertencias de deuda técnica.
*   `? [PREGUNTA]:` Dudas conceptuales o de diseño para revisión humana.
*   `TODO [fecha]:` Pendientes de implementación futura.
*   `* [NOTA]:` Aclaraciones técnicas o decisiones de diseño importantes.

### Comentarios prohibidos:
Se prohíbe dejar explicaciones redundantes o informales de desarrollo en el código final (como "corrección aplicada", "arreglo temporal", "esto fallaba", etc.). Mantenga los comentarios profesionales y concisos.

---

## 7. Criterio de parada ante dudas

Si la duda implica modificar contratos, tocar zonas legacy, ejecutar limpieza, hacer push, cambiar identidad/manifiesto o afectar datos reales, deténgase y pida aprobación explícita.
