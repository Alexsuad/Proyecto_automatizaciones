---
name: skill_notebooklm_registrar_entregable
description: Registra en NotebookLM un resumen de los entregables finalizados
---
# File: .agent/skills/skill_notebooklm_registrar_entregable.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Mantener la Biblioteca (NotebookLM) actualizada con los hitos del proyecto.
# Rol: Cierre documental y sincronización del conocimiento maestro.
# ──────────────────────────────────────────────────────────────────────

## Objetivo
Crear una memoria organizada en el cuaderno respectivo cada vez que un entregable (ej. Mapa de Empatía, Análisis Sectorial) se finaliza e ingresa a `output/`.

## Pasos de la Skill

1. **Preparar el Contenido**:
   - Identifica el **nombre del entregable**.
   - Redacta un **resumen conciso**.
   - Clasifica los datos en **hipótesis vs. evidencia factual**.
   - Añade 1 o 2 **preguntas de validación** (cosas que queden por comprobar o probar en calle).
   - Anota la **ruta relativa del archivo** en el repo local (ej. `output/bloque_1/01_mapa_empatia.md`).

2. **Registrar la Nota**:
   - Ejecuta la herramienta `mcp_notebooklm_note` con `action="create"`.
   - Asigna el contexto preparado al `content` de la nota y dale un `title` representativo.
   - Pásale el `notebook_id` correcto (ej. el ID de ProyAuto_Sector_Logistica u otro).

3. **Output**:
   - Devuelve la confirmación de la acción y el `note_id`.
   - Asegura la consistencia actualizando la columna correspondiente de NotebookLM en `INDEX_MAESTRO.md`.
