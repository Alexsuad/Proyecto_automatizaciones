# File: output/migracion/11_smoke_test_cases_logistica.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Evidencia de validación del flujo técnico en la nueva ruta.
# Rol: Certificación de preparación para la deprecación legacy.
# ──────────────────────────────────────────────────────────────────────

# Smoke Test: Flujo de Validación en `cases/logistica/`

## 1. Resumen de ejecución
Se ha realizado una batería de pruebas completa sobre la nueva ubicación del caso logístico para asegurar que el desacoplamiento técnico es efectivo y no existen dependencias residuales con la raíz `output/`.

- **Fecha:** 2026-04-21
- **Ubicación del Bloque:** `cases/logistica/output/bloque_1/`
- **Ubicación de Reportes:** `cases/logistica/reports/`

## 2. Comandos Ejecutados
Se utilizaron los scripts adaptados con el nuevo sistema de parámetros:

```powershell
# Validación de entregables
uv run python scripts/validar_entregables.py --bloque cases/logistica/output/bloque_1 --salida cases/logistica/reports/reporte_validacion_bloque_1.md

# Validación de estilo
uv run python scripts/validar_estilo_equipo.py --bloque cases/logistica/output/bloque_1 --salida cases/logistica/reports/reporte_estilo_bloque_1.md

# Coherencia cruzada (Gate)
uv run python scripts/gate_coherencia_cruzada.py --bloque cases/logistica/output/bloque_1 --salida cases/logistica/reports/reporte_coherencia_cruzada_bloque_1.md

# Auditoría de deriva editorial (con perfil sectorial)
uv run python scripts/auditar_deriva_editorial.py --bloque cases/logistica/output/bloque_1 --salida cases/logistica/reports/reporte_deriva_bloque_1.md --sector logistica

# Generación de reporte resumen
uv run python scripts/generar_reporte_bloque.py --bloque cases/logistica/output/bloque_1 --salida cases/logistica/reports/reporte_resumen_bloque_1.md --dir_reportes cases/logistica/reports
```

## 3. Resultados por Script
| Script | Resultado | Observaciones |
|---|---|---|
| `validar_entregables.py` | ✅ ÉXITO | Detectó los archivos. Reportó FAIL esperados (falta nota de registro en archivos de prueba). |
| `validar_estilo_equipo.py` | ✅ ÉXITO | 0 alertas de estilo detectadas. |
| `gate_coherencia_cruzada.py`| ✅ ÉXITO | Sin alertas de incoherencia. |
| `auditar_deriva_editorial.py`| ✅ ÉXITO | Detectó correctamente `TRANSPORTE` y aplicó perfil `logistica`. |
| `generar_reporte_bloque.py` | ✅ ÉXITO | Consolidó correctamente los reportes desde la nueva ruta de `--dir_reportes`. |

## 4. Dependencias Residuales
- **Detectadas**: Ninguna.
- **Validación**: Ningún script intentó acceder a la raíz `output/` ni a `reports/` general. Todos los outputs y lecturas de reportes intermedios se realizaron dentro de la jerarquía de `cases/logistica/`.

## 5. Conclusión
**Estado: LISTO PARA DEPRECACIÓN GRADUAL.**

El sistema técnico es ahora totalmente agnóstico a la ubicación de los archivos. La transición a la estructura de casos no afecta a la capacidad de auditoría y reporte del sistema. Se recomienda proceder al borrado de los activos obsoletos en la raíz.
