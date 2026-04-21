# File: output/migracion/09_plan_ajuste_scripts_para_nueva_arquitectura.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Plan de ajuste de scripts para soporte de arquitectura agnóstica.
# Rol: Hoja de ruta para el desacoplamiento técnico del runtime.
# ──────────────────────────────────────────────────────────────────────

# 1. Resumen de Análisis de Scripts

Se han auditado los 5 scripts principales en `scripts/`. El nivel de acoplamiento con la estructura "legacy" varía desde meros valores por defecto hasta lógica hardcodeada de rutas de reportes.

| Script | Riesgo | Dependencia Detectada | Propuesta de Ajuste |
|---|---|---|---|
| `generar_reporte_bloque.py` | **ALTO** | Rutas de lectura de reportes hardcodeadas (`reports/reporte_validacion_bloque_1.md`). | Parametrizar las rutas de los reportes de entrada o derivarlas del nombre del bloque. |
| `auditar_deriva_editorial.py` | **ALTO** | Sesgo sectorial (términos de logística en el código) y ruta fija a `docs/OPCION_ACTIVA.md`. | Pasar términos ancla por archivo de configuración o argumento. Parametrizar ruta de opciones. |
| `gate_coherencia_cruzada.py` | **MEDIO** | Argumentos por defecto apuntando a `output/bloque_1`. | Eliminar valores por defecto o hacerlos relativos al contexto de ejecución. |
| `validar_entregables.py` | **BAJO** | Solo en la documentación de uso (`--bloque output/bloque_1`). | Actualizar documentación de ayuda (`--help`) y ejemplos. |
| `validar_estilo_equipo.py` | **BAJO** | Solo en la documentación de uso. | Actualizar documentación de ayuda. |

# 2. Detalle quirúrgico por Script

## A. `generar_reporte_bloque.py`
- **Ubicación:** `scripts/generar_reporte_bloque.py`
- **Problema:** Las líneas 49 y 54 cargan reportes específicos de "Bloque 1" sin importar el argumento `--bloque`.
- **Ajuste:** Modificar la función `build_report` para que acepte las rutas de los reportes previos como argumentos o los busque en la subcarpeta del bloque correspondiente.

## B. `auditar_deriva_editorial.py`
- **Ubicación:** `scripts/auditar_deriva_editorial.py`
- **Problema:** El núcleo del script tiene "miedo" a palabras como "Incoterm" o "DUA" porque asume que el universo es transporte interurbano FTL. Además, la `OPCION_ACTIVA.md` está fija en `docs/`.
- **Ajuste:** 1) Mover `ANCHOR_TERMS` a un JSON externo (ej. `cases/logistica/config/anchors.json`). 2) Añadir `--config` al script. 3) Añadir `--opcion_activa` para evitar el hardcoding de `docs/`.

## C. `gate_coherencia_cruzada.py`
- **Ubicación:** `scripts/gate_coherencia_cruzada.py`
- **Problema:** Si se ejecuta sin argumentos, el `default` de `argparse` busca una carpeta que vamos a eliminar.
- **Ajuste:** Hacer que los argumentos sean obligatorios (`required=True`) para forzar la declaración de la ruta real (`cases/logistica/output/...`).

# 3. Compatibilidad Retroactiva

Para garantizar una transición suave, los scripts seguirán este orden de búsqueda:
1. **Prioridad 1**: Ruta explícita pasada por argumento (`--bloque`).
2. **Prioridad 2 (Legacy)**: Si falla la ruta 1, buscar en las rutas `output/...` (solo mientras dure la fase de transición).
3. **Reportes**: Los nombres de los reportes generados deberán incluir el nombre del bloque para evitar colisiones (ej. `REPORTE_VALIDACION_LOGISTICA_BLOQUE_1.md`).

# 4. Orden Recomendado de Intervención

1. **`generar_reporte_bloque.py`**: Es el que más "rompe" la visualización cruzada si se usa para un nuevo caso.
2. **`gate_coherencia_cruzada.py`**: Limpieza de defaults.
3. **`auditar_deriva_editorial.py`**: Es el cambio más complejo por la extracción de configuración, pero vital para el principio de "No Sesgo Sectorial".
4. **Validadores**: Actualización de ayuda y strings de salida.

# 5. Hallazgos Adicionales

- No se han detectado sub-scripts en `validadores/` o `utilidades/`.
- Se requiere crear una carpeta `config/` dentro de cada caso (ej. `cases/logistica/config/`) para alojar los términos ancla y las opciones específicas, eliminando así el sesgo en el runtime (`scripts/`).

# 6. Decisión de Arquitectura (ADR)

**¿Hace falta ADR?** No se considera necesario un nuevo ADR (Document de Decisión de Arquitectura) ya que estas acciones derivan directamente del **ADR-01** y de la nueva **RULE_NO_SESGO_SECTORIAL_EN_CORE.md**. Es un ajuste de implementación, no un cambio de política.
