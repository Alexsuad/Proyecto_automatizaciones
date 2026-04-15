---
name: skill_auditar_entregable
description: Auditoría de calidad estricta para entregables. Verifica consistencia de HECHOS mediante fuentes sólidas, especificidad del dominio logístico, presencia de métricas y trazabilidad obligatoria con NotebookLM (exigiendo note_id).
---
# File: .agent/skills/skill_auditar_entregable.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Gate de calidad automatizado para aprobar o bloquear entregables del Proyecto_automatizaciones.
# Rol: Auditor (Anti-vaguedad y control de calidad de fuentes sólidas).
# ──────────────────────────────────────────────────────────────────────

## Objetivo
Analizar de forma crítica cualquier entregable finalizado en la carpeta `output/` antes de que se marque como `DONE` en el índice. Se asegura de que no se publiquen afirmaciones débiles camufladas como hechos, que el lenguaje no sea genérico, y que todo esté respaldado en NotebookLM con su Note ID correspondiente.

## Entradas Requeridas (Inputs)
Para ejecutar esta auditoría, el Agente debe tener a la vista o solicitar:
- `ruta_entregable`: Ruta relativa del archivo a auditar (ej. `output/bloque_1/01_mapa_empatia.md`).
- `notebook_id`: El ID del cuaderno de NotebookLM asignado a este bloque/tarea.
- `referencia_nota`: El `note_id` exacto de la nota de registro en NotebookLM.

## Reglas de Auditoría (Responsabilidad de la IA)

IMPORTANTE: Esta skill **NO** valida formatos, conteos, sintaxis ni presencia de campos UUID. Toda la validación estructural se delega a los scripts de Python del pipeline QA.
El rol de esta skill es una evaluación **puramente cualitativa, semántica y estratégica**.

Al ejecutar esta skill, el Agente debe leer el entregable completo y evaluarlo bajo estos 4 pilares:

### Pilar 1: Coherencia con OPCION_ACTIVA
- ¿El documento respeta el nicho y el alcance declarados en `OPCION_ACTIVA.md`?
- **Riesgo:** Inclusión de temas fuera de alcance (ej. aduanas, transitarios, marítimo, DUA) como tema principal.
- **Validación:** El documento debe sentirse estrictamente escrito para el target (ej. pymes de transporte terrestre, ciclo doc-to-cash).

### Pilar 2: Tensión entre Hipótesis y Hechos
- ¿El documento promete cosas como hechos absolutos cuando no hay datos empíricos del piloto?
- **Riesgo:** Confundir "lo que queremos que pase" con "lo que ya demostramos que pasa".
- **Validación:** Afirmaciones sobre comportamiento futuro del cliente, impacto sin validar, o cifras de ingresos/costes deben estar formuladas explícitamente como hipótesis.

### Pilar 3: Claridad y Fortaleza del Argumento de Negocio
- ¿Es el dolor descrito un "nice-to-have" o un problema crítico para la supervivencia/rentabilidad de la empresa?
- **Riesgo:** Resolver problemas genéricos de gestión en lugar de atacar el flujo de caja o el coste oculto.
- **Validación:** Las métricas operativas mencionadas (aunque sean hipotéticas) deben apuntar al corazón del negocio del cliente.

### Pilar 4: Continuidad Narrativa del Bloque
- ¿Este documento encaja orgánicamente con los entregables anteriores del mismo bloque?
- **Riesgo:** Un documento brillante que contradice la estrategia o la propuesta de valor fijada en otro documento.
- **Validación:** La propuesta, los recursos, las debilidades y la competencia deben tejer una historia única y coherente.

## Salida de la Auditoría (Outputs)

Tras revisar el documento, el Agente no debe detenerse en una simple respuesta de chat. Debe obligatoriamente **generar el reporte de auditoría semántica real** siguiendo la `docs/PLANTILLA_AUDITORIA_SEMANTICA.md`.

### Pasos de Salida Obligatorios:
1. Redactar el análisis basándose en los 4 Pilares descritos arriba.
2. Formatear la salida como un documento de reporte completo (Identificación, Propósito, Hallazgos positivos, Hallazgos débiles, Coherencia, Veredicto y Correcciones).
3. Escribir el documento en `reports/auditoria_semantica_<nombre_archivo>.md`.
4. Devolver al flujo el Veredicto Final:
   - **APTO / APTO CON OBSERVACIONES:** El entregable puede avanzar al pipeline QA de Python.
   - **NO APTO:** El entregable debe iterarse antes de continuar.
