# File: output/arquitectura/00_inventario_actual_del_repositorio.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Inventario detallado y clasificación operativa del repo.
# Rol: Mapa de calor para la migración y blindaje del runtime.
# ──────────────────────────────────────────────────────────────────────

# 1. Clasificación del Inventario por Carpetas y Archivos

| Ruta | Clasificación Operativa | Sensible? | Notas |
|---|---|---|---|
| `.agent/` | **antigravity_runtime** | ✅ SÍ | Motor del sistema; no mover sin reconfigurar orquestación. |
| `.agent/rules/` | **antigravity_runtime** | ✅ SÍ | Define el comportamiento ético y técnico del agente. |
| `.agent/rules/RULE_NO_SESGO_SECTORIAL_EN_CORE.md` | **antigravity_runtime** | ✅ SÍ | Blindaje del core contra sesgo de casos de prueba. |
| `.agent/skills/` | **antigravity_runtime** | ✅ SÍ | Capacidades específicas de redacción y auditoría. |
| `.agent/workflows/` | **antigravity_runtime** | ✅ SÍ | Flujos que unen skills con fases. |
| `docs/` | **programa_incubadora** | ⚠️ PARCIAL| Contiene el Marco Rector y políticas de calidad. |
| `docs/adrs/` | **antigravity_runtime** | No | Registro de decisiones técnicas históricas. |
| `docs/evidencias/` | **caso_de_prueba** | No | Logs de ejecuciones pasadas (logística). |
| `docs/fases_marketing/` | **obsoleto/vacío** | No | Directorio de origen (Migrado a `core/`). |
| `core/` | **core_app** | ✅ SÍ | Núcleo del sistema (Metodología y Datos). |
| `docs/plantillas_entregables/` | **programa_incubadora**| No | Esquemas vacíos para generar outputs. |
| `docs/ARQ_00_...` | **documentacion_heredada**| No | Arquitectura antigua enfocada en ProyectoAuto Logística. |
| `docs/ARQ_01_MARCO...` | **programa_incubadora**| ⚠️ SÍ | Define cómo debe redactar el sistema (Audit-Mode). |
| `docs_base/` | **documentacion_heredada**| No | Fuentes externas y cronogramas de programas anteriores. |
| `output/bloque_1/` | **caso_de_prueba** | No | Entregables reales de la fase de logística. |
| `scripts/` | **validacion_determinista**| ✅ SÍ | Validadores Python que aseguran el cumplimiento de Gates. |
| `INDEX_MAESTRO.md` | **caso_de_prueba** | No | Indice actual (100% logística). Debe ser reemplazado. |
| `README.md` | **documentacion_heredada**| No | Introducción descriptiva del estado actual. |
| `pyproject.toml` | **antigravity_runtime** | ⚠️ SÍ | Dependencias y entorno de ejecución. |

# 2. Piezas Sensibles (Blindaje Temporal)

Estas piezas **NO deben moverse ni modificarse** en la primera fase de migración para asegurar que el sistema siga respondiendo:

1. **`.agent/` (Completo)**: Es el cerebro del runtime. Cualquier cambio de ruta rompería la carga de skills.
2. **`scripts/`**: Los scripts tienen rutas hardcoded relativas que dependen de la ubicación de los archivos en `output/` y `docs/`.
3. **`core/dmv/00_Tabla_maestra_de_campos_DMV.md`**: Fuente de verdad de datos (MIGRADOS).
4. **`docs/ARQ_01_MARCO_RECTOR_REDACCION.md`**: Es la instrucción suprema para la redacción de entregables.

# 3. Identificación de Duplicidades y Ruido

- **`docs/ARQ_00_sistema_proyectoauto.md`**: Contradice el nuevo enfoque de Core App. Debe ser marcado como heredado.
- **`README.md`**: Mezcla la misión del sistema con el caso logístico.
- **`docs_base/`**: Contiene material PDF/Word que ya ha sido procesado o que no pertenece al core de la app.
