# File: output/migracion/01_matriz_de_rutas_y_referencias_a_actualizar.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Matriz de impacto de rutas para la migración.
# Rol: Inventario anticipado de "broken links" y redirecciones.
# ──────────────────────────────────────────────────────────────────────

# 1. Scripts con Rutas Hardcoded (Prioridad ALTA)

| Script | Ruta Detectada | Tipo | Impacto |
|---|---|---|---|
| `scripts/validar_entregables.py` | `--bloque output/bloque_1` | Argumento/Docs | Romperá la validación si se mueve la logística. |
| `scripts/generar_reporte_bloque.py`| `output/` | Argumento/Docs | Desajuste en la generación de reportes consolidados. |
| `scripts/__pycache__/` | N/A | Binario | Debe eliminarse antes de migrar. |

# 2. Documentos con Hipervínculos Relativos (Prioridad MEDIA)

| Documento Origen | Referencia a | Tipo de Vínculo | Prioridad de Ajuste |
|---|---|---|---|
| `INDEX_MAESTRO.md` | `docs/fases_marketing/` | Relativo (`[link](path)`) | ALTA (Indice inutilizable). |
| `docs/ARQ_00_...md` | `docs/ARQ_01_...md` | Relativo | BAJA (Es legacy). |
| `docs/fases_marketing/*.md` | `00_Tabla_maestra_...md`| Relativo intra-carpeta | MEDIA (Si se mueve la carpeta). |
| `output/bloque_1/*.md` | `docs/evidencias/` | Trazabilidad | MEDIA (Pruebas de auditabilidad). |

# 3. Referencias en Antigravity Runtime (Prioridad ALTA)

| Pieza Configuración | Referencia Sensible | Impacto |
|---|---|---|
| `RULE_OPERATIVO_SISTEMA.md` | Referencias a `output/` y `docs/` | Desorientación del agente sobre dónde leer/escribir. |
| `WORKFLOW_VALIDACION_NEGOCIO` | Referencias a `docs/fases_marketing` | El workflow fallará al intentar cargar pasos. |
| `skill_auditar_entregable.md` | Referencia a manuales en `docs/` | Pérdida de capacidad de auditoría semántica. |

# 4. Estrategia de Actualización

- **Scripts**: Se debe modificar para que acepten la ruta base como variable de entorno o argumento obligatorio relativo a la raíz del repo.
- **Documentos**: Usar una búsqueda y reemplazo masiva (`sed` o similar) basada en la tabla origen->destino de ARQ_04.
- **Runtime**: Actualizar los prompts maestros para que apunten a la nueva carpeta `core/` como fuente de verdad metodológica.
