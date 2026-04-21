# File: output/arquitectura/ARQ_04_plan_de_migracion_del_repositorio.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Guía de ejecución para el reajuste estructural del repo.
# Rol: Plan maestro de movimientos y blindaje de dependencias.
# ──────────────────────────────────────────────────────────────────────

# 1. Comparativa de Estructuras

| Estructura Actual | Estructura Destino (Propuesta) | Categoría |
|---|---|---|
| `docs/fases_marketing/` | `core/fases/` y `core/dmv/` | core_app |
| `.agent/` | `.agent/` (con subcarpetas `core/` y `cases/`) | antigravity_runtime |
| `output/bloque_1/` | `cases/logistica/output/` | caso_de_prueba |
| `scripts/` | `core/validation/` o `scripts/` (generalizado) | validacion_determinista |
| `docs/plantillas_entregables/`| `core/templates/` | programa_incubadora |
| `docs/evidencias/` | `cases/logistica/evidencias/` | caso_de_prueba |

# 2. Tabla de Migración Detallada (Origen -> Destino)

| Recurso Origen | Recurso Destino | Acción | Riesgo |
|---|---|---|---|
| `docs/fases_marketing/` | `core/fases/` | **Mover** | Medio (actualizar hipervínculos). |
| `.agent/skills/` | `.agent/skills/` | **Mantener** | Nulo (solo limpieza editorial). |
| `output/bloque_1/` | `cases/logistica/` | **Mover** | Bajo (histórico). |
| `scripts/` | `scripts/` | **Mantener** | Alto (rutas hardcoded). |
| `INDEX_MAESTRO.md` | `cases/logistica/INDEX_LOG.md` | **Mover** | Bajo. |
| `docs/ARQ_00_...` | `docs/legacy/` | **Mover** | Bajo. |
| `-` | `/INDEX_MAESTRO.md` | **Crear** | Nuevo índice agnóstico. |

# 3. Orden Exacto de Migración (Estado actual)

1. **Fase 0 (Preparación)**: Creación de la estructura base. ✅ **DONE**
2. **Fase 1 (Elevación del Core)**: Mover DMV a `core/dmv/` y Fases a `core/fases/`. ✅ **DONE**
3. **Fase 2 (Aislamiento de Casos)**: Mover contenido de Logística a `cases/logistica/`. 🟢 **PENDIENTE**
4. **Fase 3 (Limpieza del Runtime)**: Purga de sesgo en prompts y skills. 🟢 **PENDIENTE**
5. **Fase 4 (Nuevo Panel de Control)**: Nuevo `INDEX_MAESTRO.md` agnóstico. 🟢 **PENDIENTE**

# 4. Lo que NO debe tocarse en la primera migración

- **Configuración de Entorno**: `.python-version`, `pyproject.toml`, `uv.lock`.
- **Identidad del Agente**: `.agent/rules/RULE_OPERATIVO_SISTEMA.md` (salvo menciones a ruta).
- **Git Config**: `.git`, `.gitignore`.

# 5. Dependencias y Riesgos de Ruptura

- **Hipervínculos**: Casi todos los manuales en `docs/` se referencian entre sí con rutas relativas. La migración requiere un escaneo y reemplazo de rutas masivo.
- **Paths de Validación**: Los scripts en `scripts/` asumen que los archivos a validar están en `output/`. Si movemos la logística a `cases/logistica/`, los scripts fallarán si no se les pasa la nueva ruta como argumento.
- **Trazabilidad NotebookLM**: Las notas existentes en NotebookLM apuntan a rutas de archivos que van a cambiar. Se debe decidir si se actualiza la nota en NotebookLM o se acepta la ruptura histórica.
