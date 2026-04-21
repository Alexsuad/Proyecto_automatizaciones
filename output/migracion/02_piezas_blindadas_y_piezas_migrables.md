# File: output/migracion/02_piezas_blindadas_y_piezas_migrables.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Lista de control de activos para la ejecución de la Fase 1.
# Rol: Selector quirúrgico de archivos para el movimiento físico.
# ──────────────────────────────────────────────────────────────────────

# 1. Piezas Blindadas (NO TOCAR en Fase 1)

| Recurso | Tipo | Motivo de Blindaje |
|---|---|---|
| `.agent/*` | Carpeta | Corazón del runtime; riesgo de desconexión total. |
| `scripts/*.py` | Archivo | Riesgo de ruptura de lógica determinista hasta que se validen los nuevos paths. |
| `pyproject.toml`, `uv.lock` | Config | Gestión de dependencias y runtime Python. |

# 2. Piezas Migrables en Fase 1 (SÍ se pueden mover)

| Recurso Origen | Destino Propuesto | Acción |
|---|---|---|
| `core/fases/` | `core/fases/` | ✅ **MIGRADAS (Fase 1)** |
| `core/dmv/00_Tabla_maestra...`| `core/dmv/` | ✅ **MIGRADOS (Fase 1)** |
| `docs/plantillas_entregables/`| `core/contratos/` | **Mover**. |
| `output/bloque_1/` | `cases/logistica/output/` | **Mover** (Caso de prueba). |
| `docs/evidencias/` | `cases/logistica/evidencias/` | **Mover**. |

# 3. Piezas que requieren COPIA antes de Mover (Seguridad)

| Recurso | Motivo | Destino de la Copia |
|---|---|---|
| `INDEX_MAESTRO.md` | Mantener histórico operativo de logística mientras se crea el nuevo. | `cases/logistica/INDEX_LOGISTICA_V1.md` |
| `docs/ARQ_01_MARCO...` | Es el manual más importante; debe copiarse para auditoría. | `core/fases/ARQ_01_MARCO_RECTOR.md` |

# 4. Piezas a Deprecar (Eliminar al final de la migración)

| Recurso | Estado actual | Acción final |
|---|---|---|
| `docs/ARQ_00_...md` | Superado por ARQ_01/02. | Eliminar (o mover a legacy). |
| `docs_base/` | Ruido informativo. | Archivar en carpeta externa o eliminar. |
| `README.md` (actual) | Obsoleto ante el nuevo enfoque. | Sobrescribir con el nuevo README agnóstico. |
