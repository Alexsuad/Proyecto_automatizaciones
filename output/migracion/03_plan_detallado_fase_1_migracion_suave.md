# File: output/migracion/03_plan_detallado_fase_1_migracion_suave.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Guía quirúrgica para la ejecución de la Fase 1 (Reordenada).
# Rol: Plan de vuelo detallado con enfoque en la seguridad del DMV.
# ──────────────────────────────────────────────────────────────────────

# 1. Alcance de la Fase 1 (Actualizado)

| Estado | Elementos | Justificación |
|---|---|---|
| **IN (Etapa 1)** | **Tabla Maestra DMV**, Metodología de Fases. | Elevación del núcleo de datos y metodología. |
| **IN (Etapa 2)** | Plantillas, Caso Logístico (Output), Evidencias. | Aislamiento del caso de prueba. |
| **OUT (Pendiente)** | .agent/ (Completo), Scripts/ (Completo). | Requieren validación de rutas en Fase 2. |
| **BLINDADO** | Reglas de comportamiento, Identidad del Agente. | Protección del runtime. |

# 2. Tabla de Migración Analítica

| Origen | Destino | Acción | Motivo | Riesgo | Referencias a actualizar | Prioridad |
|---|---|---|---|---|---|---|
| `docs/fases_marketing/00_Tabla_maestra...` | `core/dmv/` | **Mover** | Centralizar contrato de datos. | Mínimo | Inventario, Plan Migración | ALTA (Paso 1) |
| `docs/fases_marketing/FaseXX.md` | `core/fases/` | **Mover** | Desacoplar metodología. | Medio | INDEX, Referencias DMV | ALTA (Paso 2) |
| `output/bloque_1/` | `cases/logistica/output/` | **Mover** | Aislar caso de prueba. | Alto | Scripts, INDEX | MEDIA (Paso 3) |

# 3. Referencias Concretas a Actualizar por Movimiento DMV

Al mover `00_Tabla_maestra_de_campos_DMV.md` a `core/dmv/`, deben actualizarse:
1. **Documentación de Arquitectura Nueva**: `output/arquitectura/ARQ_03_contrato_operativo_del_DMV.md` y `output/arquitectura/ARQ_04_plan_de_migracion_del_repositorio.md`.
2. **Inventario del Repo**: `output/arquitectura/00_inventario_actual_del_repositorio.md`.
3. **Piezas Migrables**: `output/migracion/02_piezas_blindadas_y_piezas_migrables.md`.
4. **Fases (conceptualmente)**: Las fases en `core/fases/` deberán referenciar al DMV en `../dmv/`.

# 4. Orden Exacto de Ejecución (NUEVA SECUENCIA)

### Paso 1: Protección y Seguridad
- Crear backup de todo el estado actual en `output/migracion/backups/fase_1_pre_dmv/`.

### Paso 2: Elevación del Núcleo de Datos (EL PRIMER MOVIMIENTO)
- **Acción**: Mover `docs/fases_marketing/00_Tabla_maestra_de_campos_DMV.md` a `core/dmv/`.
- **Estado**: ✅ **DONE** (21/04/2026).
- **Verificación**: Realizada con éxito.

### Paso 3: Elevación Metodológica
- **Acción**: Mover los archivos de fases (`Fase01...` a `Fase12...`) a `core/fases/`.
- **Estado**: ✅ **COMPLETADO** (21/04/2026).
- **Control de Referencias**: 
  - Pendiente: Saneamiento de hipervínculos relativos hacia el DMV (ahora en `../dmv/`).

### Paso 4: Aislamiento del Caso de Prueba
- **Acción**: Mover `output/bloque_1/` a `cases/logistica/output/`.
- **Nota**: Se deja para el final de la Fase 1 por su alto acoplamiento con los scripts de validación.

# 5. Gate de Cierre de Fase 1 (Actualizado)

- [ ] El DMV reside en `core/dmv/`.
- [ ] Las 12 fases residen en `core/fases/`.
- [ ] La logística reside en `cases/logistica/`.
- [ ] **Validación**: El agente puede explicar un campo del DMV leyéndolo desde `core/dmv/`.
- [ ] **Validación**: Las rutas en los documentos de control de `output/migracion/` han sido actualizadas.
