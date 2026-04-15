---
name: skill_notebooklm_research_web
description: Envoltorio técnico MCP para enviar los Prompts Maestros a NotebookLM e importar las fuentes al cuaderno destino.
---
# File: .agent/skills/skill_notebooklm_research_web.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Único vehículo autorizado para hablar con NotebookLM. No investiga por libre.
# Rol: Conector Técnico Subordinado (MCP Wrapper).
# ──────────────────────────────────────────────────────────────────────

## Objetivo
Ejecutar la consulta a NotebookLM usando estrictamente los Prompts Maestros preaprobados, monitorear el progreso y asegurar que las fuentes queden importadas en el cuaderno correspondiente, sin alterar la estructura de la consulta.

## Regla de Subordinación Estricta (Antideriva)
Tienes **PROHIBIDO** inventar consultas ("queries"), decidir el nivel de profundidad, o inferir qué preguntar. Cuando se invoque esta skill durante el `WORKFLOW_VALIDACION_NEGOCIO.md`, debes inyectar fiel y literalmente el Prompt Maestro 1, 2 o 3 (ubicados en `docs/NOTEBOOKLM_PROMPTS_MASTER.md`), reemplazando solo las variables de contexto por los datos del Intake.

## Pasos de la Skill (El Envoltorio)

1. **Recuperar y Formatear Prompt:**
   - Lee el Prompt Maestro correspondiente en `docs/NOTEBOOKLM_PROMPTS_MASTER.md`.
   - Inyecta la variable mínima de contexto del proyecto basándote en el Intake.
2. **Iniciar Búsqueda**:
   - Llama a `mcp_notebooklm_research_start`.
   - *Argumento obligatorio*: `query` (El prompt maestro exacto), `mode` ("deep" por defecto para validación B2B y competidores), `source` ("web"), y el `notebook_id` destino.
3. **Monitorear**:
   - Llama cíclicamente a `mcp_notebooklm_research_status` proveyendo el `notebook_id` hasta que la investigación finalice.
4. **Importar Fuentes**:
   - Extraer el `task_id` e importar usando la herramienta `mcp_notebooklm_research_import`.
5. **Output Final** (Para el GATE 2 - Calidad):
   - Entregar la investigación textual devuelta por el LLM y el reporte de fuentes importadas.
   - El texto devuelto será luego sometido obligatoriamente al escrutinio del checklist en `docs/NOTEBOOKLM_OUTPUT_CRITERIA.md`.
