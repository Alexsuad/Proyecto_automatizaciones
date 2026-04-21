# File: output/migracion/00_estado_fase_0_preparacion.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Control de estado de la Fase 0 (Preparación Estructural).
# Rol: Asegurar que los cimientos de la nueva arquitectura están listos.
# ──────────────────────────────────────────────────────────────────────

# 1. Registro de Carpetas Creadas (Estructura Destino)

| Carpeta | Estado | Clasificación Operativa |
|---|---|---|
| `core/` | ✅ Creada | Nucleo de la Core App |
| `core/fases/` | ✅ Creada | Definición de pasos del programa |
| `core/dmv/` | ✅ Creada | Contrato de datos persistente |
| `core/contratos/` | ✅ Creada | ADAs y acuerdos operativos |
| `core/prompts/` | ✅ Creada | Base de instrucciones metodológicas |
| `runtime/` | ✅ Creada | Motor Antigravity |
| `runtime/antigravity/`| ✅ Creada | Configuración del Agente |
| `cases/` | ✅ Creada | Instancias de aplicación |
| `cases/logistica/` | ✅ Creada | Caso de prueba (histórico) |
| `programa_convierte/` | ✅ Creada | Materiales educativos y metodológicos |
| `research/` | ✅ Creada | Capa de evidencia y NotebookLM |
| `scripts/validadores/`| ✅ Creada | Capa determinista técnica |
| `output/migracion/` | ✅ Creada | Control de este proceso |

# 2. Carpetas NO Tocadas (Blindadas)

Las siguientes carpetas **mantienen su ubicación original** para no comprometer el runtime activo en esta fase:

- `.agent/` (Toda la carpeta raíz del agente)
- `scripts/` (Contenido raíz actual)
- `output/bloque_1/` (Resultados de logística activos)
- `docs/fases_marketing/` (Metodología activa)

# 3. Riesgos Abiertos

- **Inconsistencia de Referencias**: Aunque las carpetas existen, el sistema sigue buscando en las rutas viejas. La Fase 1 debe ser quirúrgica para no "romper el hilo conductor".
- **Scripts Hardcoded**: Se ha identificado que `scripts/validar_entregables.py` asume rutas relativas que fallarán si se mueve el script o el output prematuramente.

# 4. Traza de Auditoría de Movimientos

| 21/04/24 | `docs/fases_marketing/Fase07-12`| `core/fases/` | Movimiento Tanda 2 | ✅ **DONE** |
| 21/04/24 | `docs/fases_marketing/Fase07-12`| `output/migracion/backups/fase_1_tanda_2/`| Backup Tanda 2 | ✅ **DONE** |
| 21/04/24 | `docs/fases_marketing/Fase01-06`| `core/fases/` | Movimiento Tanda 1 | ✅ **DONE** |
| 21/04/24 | `docs/fases_marketing/Fase01-06`| `output/migracion/backups/fase_1_tanda_1/`| Backup Tanda 1 | ✅ **DONE** |

# 5. Notas de Ejecución
- **Fase 1 - Elevación Metodológica**: Completada al 100% (12 fases en `core/fases/`).
- **Fase 1 - Paso 1/2**: DMV migrado con éxito a `core/dmv/`.
- **Estado**: Las 12 fases metodológicas residen ahora en la estructura core del sistema.
