---
name: skill_notebooklm_research_web
description: Orquesta la búsqueda y registro de fuentes de investigación en NotebookLM
---
# File: .agent/skills/skill_notebooklm_research_web.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Ejecutar deep o fast research integrando los resultados a NotebookLM.
# Rol: Investigador base y sincronizador de pruebas.
# ──────────────────────────────────────────────────────────────────────

## Objetivo
Realizar búsquedas estructuradas en la web (cuando sea requerido) y consolidar las fuentes y el conocimiento dentro de los cuadernos de NotebookLM.

## Pasos de la Skill

1. **Iniciar Búsqueda**:
   - Dependiendo del nivel de profundidad solicitado, llama a `mcp_notebooklm_research_start`.
   - *Argumentos importantes*: `query`, `mode` ("fast" o "deep"), `source` ("web"), y el `notebook_id` destino donde se alojarán los resultados.

2. **Monitorear**:
   - Llama cíclicamente a `mcp_notebooklm_research_status` proveyendo el `notebook_id` hasta que la investigación finalice.

3. **Importar Fuentes**:
   - Extraer el `task_id` e importar usando la herramienta `mcp_notebooklm_research_import`.
   - Estas fuentes se adjuntarán al cuaderno para sustentar el conocimiento derivado.

4. **Output Final**:
   - Entregar un reporte que liste las **fuentes importadas**, los links de origen (si aplica) y el **notebook_id** actualizado, para usar esta lista en las referencias (por ejemplo: "Referencia NotebookLM" al pie de los .md de salida).
