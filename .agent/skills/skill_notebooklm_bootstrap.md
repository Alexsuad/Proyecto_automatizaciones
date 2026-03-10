---
name: skill_notebooklm_bootstrap
description: Verifica autenticación y crea cuadernos base de NotebookLM
---
# File: .agent/skills/skill_notebooklm_bootstrap.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Inicializar el entorno de NotebookLM para el proyecto ZAC.
# Rol: Asegurar que los cuadernos base existan para la trazabilidad y la investigación documental.
# ──────────────────────────────────────────────────────────────────────

## Objetivo
Implementar el uso real del MCP de NotebookLM inicializando la estructura base del proyecto ZAC.

## Pasos de la Skill

1. **Verificar Autenticación**:
   - Ejecuta la herramienta `mcp_notebooklm_refresh_auth`.
   - Llama a `mcp_notebooklm_notebook_list` para listar cuadernos existentes.

2. **Crear Cuadernos Base**:
   - Revisa si ya existen los siguientes cuadernos. Si no existen, los crea usando `mcp_notebooklm_notebook_create`:
     - `ZAC_Base_Documentos_A_B`
     - `ZAC_Bloque_1`
     - `ZAC_Bloque_1_Investigacion_Sector`

3. **Registrar Nota Inicial**:
   - Para cada uno de los cuadernos anteriores, usa `mcp_notebooklm_note` con `action="create"` para añadir una nota titulada `00_Registro_Inicial`.
   - Contenido de la nota: "Inicialización del cuaderno para el proyecto ZAC. Creado por Antigravity."

4. **Output**:
   - Debes retornar una **evidencia con los IDs de los notebooks** creados o encontrados, confirmando su disponibilidad para los siguientes entregables.
