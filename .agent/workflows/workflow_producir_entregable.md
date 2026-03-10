---
description: Flujo operativo estándar para producir un entregable del cronograma CONVIERTE ZAC
---

# Workflow — Producir Entregable (CONVIERTE / ZAC)

Este workflow describe el proceso completo desde la selección de un entregable hasta su aprobación final.

## Pre-requisito
- La opción activa debe estar declarada y actualizada en `docs/OPCION_ACTIVA.md`.
- Si hubo pivote reciente, registrar primero en `docs/DECISION_LOG.md`.

## Pasos

### 1. Confirmar opción activa
Verificar que `docs/OPCION_ACTIVA.md` refleje el nicho, subnicho y dolor vigente. Todo el entregable debe alinearse a esta declaración.

### 2. Seleccionar entregable del cronograma
Consultar `ZAC_INDEX_00.md` → Identificar el entregable en estado `TODO` o `IN_PROGRESS` del bloque correspondiente.

### 3. Decidir si requiere investigación
Ejecutar el skill: `.agent/skills/skill_decidir_si_requiere_investigacion.md`
- **Sí →** Ejecutar `.agent/skills/skill_notebooklm_research_web.md` → importar fuentes → verificar con `research_status`.
- **No →** Avanzar directamente a redacción.

### 4. Redactar con plantilla
Usar la plantilla correspondiente de `docs/plantillas_entregables/TEMPLATE_0X.md`.
Respetar obligatoriamente:
- `docs/ESTILO_00_guia_tono_y_voz_equipo.md` (voz, tono, glosario)
- `docs/OPCION_ACTIVA.md` (enfoque)
- Sección `Hipótesis + Cómo se valida` si la plantilla lo exige

### 5. Auditoría determinista (Python — QA pipeline)
Ejecutar en orden:
```
python scripts/validar_entregables.py --bloque output/bloque_X --salida reports/reporte_validacion_bloque_X.md
python scripts/validar_estilo_equipo.py --bloque output/bloque_X --salida reports/reporte_estilo_bloque_X.md
python scripts/auditar_deriva_editorial.py --bloque output/bloque_X --salida reports/reporte_deriva_bloque_X.md
```
**Gate:** PASS obligatorio en los 3 antes de continuar.

### 6. Corregir hasta PASS
Si alguno retorna FAIL o alerta → corregir el entregable y re-ejecutar el pipeline.

### 7. Auditoría semántica (IA + evidencia obligatoria en repo)
Usar `docs/PLANTILLA_AUDITORIA_SEMANTICA.md` como guía.
Inputs: ARQ_00 + OPCION_ACTIVA + entregable.
**Validación Cualitativa:** La IA evalúa la coherencia narrativa, la tensión Hecho/Hipótesis, pertinencia operativa y solidez del argumento. (Python NO valida esto).
Veredicto: APTO / CON OBSERVACIONES → continuar. NO APTO → volver al paso 6.
**Obligatorio:** Guardar el reporte de la auditoría cualitativa como archivo en el repositorio:
`reports/auditoria_semantica_<nombre_archivo>.md`

### 8. Registrar en NotebookLM (AMBOS IDs)
Ejecutar `.agent/skills/skill_notebooklm_registrar_entregable.md`.
**Crear 2 notas separadas:**
1. **Nota HITO** (registro del entregable) → obtener UUID real (`hito_note_id`)
2. **Nota AUDITORÍA SEMÁNTICA** (Gate 7) → copiar el contenido del reporte generado en paso 7 → obtener UUID real (`auditoria_note_id`)

**Actualizar el bloque final del `.md`** con el formato estándar:
```
**Nota de Registro NotebookLM**
- **notebook_title:** <cuaderno>
- **notebook_id:** <uuid>

**Registro (HITO)**
- **hito_note_title:** HITO: <nombre>
- **hito_note_id:** <uuid>

**Auditoría semántica (Gate 7)**
- **auditoria_note_title:** AUDITORÍA SEMÁNTICA — <archivo.md>
- **auditoria_note_id:** <uuid>
- **fecha:** YYYY-MM-DD
```

### 9. Marcar READY_FOR_REVIEW
Actualizar estado en `ZAC_INDEX_00.md`: `TODO` → `READY_FOR_REVIEW`.

### 10. Aprobación del usuario
El usuario revisa y escribe: `Aprobado: [nombre] (ruta del archivo)`.

### 11. Cerrar como DONE
Actualizar estado en `ZAC_INDEX_00.md` → `DONE`.
Registrar en la sección de log de cambios del índice.

---

## Cierre de bloque completo (Gate de Coherencia Global)

Cuando todos los entregables del bloque estén en estado `DONE`:

### 1. Generar reporte automatizado de cierre (Python)
```
python scripts/generar_reporte_bloque.py --bloque output/bloque_X --salida reports/REPORTE_CIERRE_BLOQUE_X.md
```

### 2. Ejecutar Auditoría de Supervisión Global (IA)
Una vez que el QA determinista y las auditorías semánticas por entregable estén listos, **ejecutar obligatoriamente** el agente global:
`.agent/skills/skill_supervisor_coherencia_global.md`

Este agente leerá todos los entregables y reportes del bloque para emitir un informe único en:
`reports/auditoria_supervisor_global_bloque_X.md`

**Veredicto Final del Bloque:**
- **COHERENTE / CON OBSERVACIONES:** El bloque completo queda sellado y aprobado para avanzar a la siguiente fase.
- **INCOHERENTE:** El supervisor bloquea el avance hasta resolver la tensión estratégica identificada.
