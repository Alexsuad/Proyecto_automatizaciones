---
description: Flujo maestro Front-Loaded (Investigar -> Pensar -> Escribir -> Auditar). Orquesta en cascada el proceso de validación B2B, desde el Intake hasta la Validación Humana Final.
---
# File: .agent/workflows/WORKFLOW_VALIDACION_NEGOCIO.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Guía de ejecución en cascada. Evita escribir código sin investigar.
# Rol: Orquestador Principal del Bloque de Validación (Operacionalización de la Tarea 8).
# ──────────────────────────────────────────────────────────────────────

> **Advertencia Inicial:** Este workflow asume la gobernanza completa del proceso de creación del Bloque 1 B2B. El antiguo `workflow_producir_entregable.md` queda relegado estrictamente a tareas de parcheado manual aislado y no debe utilizarse en este ciclo maestro.

## Flujo Maestro en Cascada

### FASE 0: Disparo y Contexto (Gate de Arranque)
1. Recepcionar el `00_intake_proyecto.md` creado por el cliente.
2. **GATE 1 (Contexto mínimo):** Analizar si existen datos en los campos obligatorios del Intake (Problema, Cliente Objetivo, Ambición).
   - *Si falta información crítica:* Abortar la cascada y solicitar al humano los datos faltantes vía Interfaz. No continuar.

### FASE A: Investigación Estratégica
3. Invocar al conector subordinado `skill_notebooklm_research_web` pasándole los 3 Prompts Maestros definidos en `NOTEBOOKLM_PROMPTS_MASTER.md`.
4. **GATE 2 (Evidencia):** Pasar los 3 outputs devueltos por el filtro `NOTEBOOKLM_OUTPUT_CRITERIA.md`.
   - *Si hay Red Flags de Severidad B:* Hacer re-prompt inmediato indicando el fallo.
   - *Si hay Red Flags de Severidad A tras 2 re-prompts:* Detener sistema con excepción [BLOQUEADO POR FALTA DE DATOS].
5. Almacenar el research validado en NotebookLM en formato de Notas Maestras.

### FASE B: Digestión y Pensamiento (El Cerebro)
Esta fase transforma datos crudos en variables lógicas usando las skills de análisis. Para evitar ambigüedad, el output de cada skill debe generarse en formato `.json` persistido temporalmente en memoria o en una carpeta de control para alimentar la Fase C.

6. Ejecutar `skill_analisis_competitivo.md` usando de entrada el research validado del Prompt 2. Generar el payload `payload_estrategia_competitiva.json`.
7. Ejecutar `skill_diseno_propuesta_valor.md` usando de entrada el research validado del Prompt 1. Generar el payload `payload_propuesta_valor.json`.
8. *Atención Especial (Prompt 3 - Viabilidad):* Dado que su skill homóloga no está construida en esta versión, convertir la investigación validada del Prompt 3 directamente a `payload_viabilidad_cruda.md`.
9. **GATE 3 (Detección de Señal Débil):** Si alguna de las skills retorna estado de `[INSUFICIENCIA DE SEÑAL]`, amputar temporalmente el documento correspondiente (ej. no redactar `05_competencia.md`) y levantar alerta al humano.

### FASE C: Motor de Redacción (Ensamblaje final)
*Ruta crítica Front-Loaded: Queda TERMINANTEMENTE PROHIBIDO invocar o leer plantillas en la carpeta `docs_base/` si las Fases A y B no han completado los `.json` o `.md` de payload requeridos.*

**[NUEVO GATE ESTRUCTURAL - DEPENDENCIAS DE IDENTIDAD]**
Antes de redactar la primera sílaba, el Agente Redactor **DEBE** ingerir en su contexto:
1. `docs_base/PROYAUTO_DOC_A_DOSSIER_EMPRESARIAL.md` (Doc A - El proyecto).
2. `docs_base/PROYAUTO_DOC_B_REALIDAD_INTERNA.md` (Doc B - Realidad Interna).
3. `docs/ARQ_01_MARCO_RECTOR_REDACCION.md` (La Ley Anti-Deriva B2B).
*Mecanismo de Bloqueo:* Si el Agente intenta formular texto basándose puramente en su 'memoria implícita' o en cuadernos de NotebookLM históricos congelados obviando este tríptico base, debe abortar operación.

10. Ensamblar los entregables (01 a 10) inyectando la inteligencia artificial puramente en la "envoltura" de los Payloads creados en la Fase B. Emplear estrictamente las normas definidas en `ESTILO_00_guia_tono_y_voz_equipo.md` y el `ARQ_01_MARCO_RECTOR_REDACCION.md`.
11. Generar los archivos Markdown limpios dictados en el repositorio y dejarlos en `output/bloque_1/`.

### FASE D: QA Determinista y Auditoría Cualitativa
12. **GATE 4 (Scripts):** Ejecutar los scripts python obligatorios de formato como `validar_entregables.py` y resolver conflictos de conteo/títulos/múltiples negaciones asiduamente.
13. **GATE 5 (Auditoría Semántica):** Ejecutar `skill_auditar_entregable.md` individual para asegurar que los entregables generados no contengan saltos discursivos de Tono, derivas del Intake base o falta de hipótesis atadas.
14. Corregir localmente los documentos rechazados por los gates **sin re-hacer investigación NotebookLM**.
15. **GATE 6 (Coherencia Global):** Ejecutar `skill_supervisor_coherencia_global.md` en lotes leyendo todo el subdirectorio de salidas para emitir un reporte final unificado y macro-estratégico de "Bloque Consistente".

### FASE E: Cierre Organizativo
16. Redactar sintéticamente `99_resumen_bloque_1.md`.
17. Activar **VALIDACIÓN HUMANA FINAL.** Aunque el Supervisor Global (Gate 6) dictamine la coherencia del bloque como un "Aprobado Técnico", el Agente emitirá una alerta visual o notificación paralizando la transición oficial al Bloque 2 hasta confirmar que el Usuario / Emprendedor valide, interiorice y de "Luz Verde" al pivotaje o estrategia reflejada.
