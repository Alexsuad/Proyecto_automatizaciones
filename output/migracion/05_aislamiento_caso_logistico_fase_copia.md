# File: output/migracion/05_aislamiento_caso_logistico_fase_copia.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Registro de la fase de aislamiento (Copia) del caso logístico.
# Rol: Auditoría de redundancia y preparación para el desacoplamiento final.
# ──────────────────────────────────────────────────────────────────────

# 1. Resumen de la Fase de Copia

Se ha ejecutado el aislamiento del caso logístico mediante el protocolo de **Copia Controlada**, creando una réplica operativa dentro de la estructura de casos sin alterar las rutas originales que el runtime y los scripts utilizan actualmente.

| Fecha | Ámbito | Acción | Estado |
|---|---|---|---|
| 21/04/24 | Estructura | Creación de `cases/logistica/` (output, evidencias, docs). | ✅ **DONE** |
| 21/04/24 | Contenido | Copia de `output/bloque_1/` a `cases/logistica/output/`. | ✅ **DONE** |
| 21/04/24 | Evidencias | Copia de `DRY_RUN_2_LOGISTICA_LIMPIA.md` a `cases/logistica/evidencias/`. | ✅ **DONE** |
| 21/04/24 | Docs de Contexto | Copia de `ECOSISTEMA_LOGISTICO` y `TRACKPOD` a `cases/logistica/docs/`. | ✅ **DONE** |

# 2. Análisis de Dependencias Detectadas

Tras la copia, se ha verificado que los archivos mantienen un fuerte acoplamiento con la ruta original:

- **Headers Internos**: Los archivos en `cases/logistica/output/bloque_1/` conservan la cabecera `# File: output/bloque_1/...`. 
- **Validadores**: Los scripts en `scripts/` (ej: `validar_entregables.py`) siguen apuntando a la raíz `output/`.
- **Índice Maestro**: `INDEX_MAESTRO.md` referencia exclusivamente las rutas en `output/bloque_1/`.

# 3. Riesgos y Bloqueadores Abiertos

- **Ruptura de Trazabilidad**: Si se borrara `output/bloque_1/` hoy, los scripts de validación fallarían inmediatamente.
- **Redundancia de Datos**: Actualmente existen dos versiones de los mismos entregables en el repositorio. Cualquier modificación en `output/` NO se reflejará en `cases/` sin un proceso de sincronización manual (no recomendado).

# 4. Propuesta para la Siguiente Subfase (Elegida: B)

Se recomienda proceder con la **Opción B (Ajuste de Scripts)** antes de realizar el movimiento definitivo.

**Pasos sugeridos:**
1. Modificar `scripts/` para que acepten un argumento `--base_path` o similar.
2. Validar que los scripts funcionan correctamente apuntando a `cases/logistica/output/`.
3. Actualizar `INDEX_MAESTRO.md` para que apunte a las nuevas rutas.
4. Recién entonces, proceder a la eliminación de las rutas originales en `output/` y `docs/evidencias/`.

# 5. Hallazgo de Inventario (Pendiente)

- **00_intake_proyecto.md**: No se ha localizado físicamente en el repositorio a pesar de estar referenciado en el `INDEX_MAESTRO.md`. Se requiere una búsqueda profunda o reconstrucción del activo si es necesario para el caso.
