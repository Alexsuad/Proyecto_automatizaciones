# File: output/arquitectura/ARQ_03_contrato_operativo_del_DMV.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Contrato de datos detallado (DMV) para la Core App.
# Rol: Especificación de persistencia y visibilidad metodológica.
# ──────────────────────────────────────────────────────────────────────

# 1. Clasificación de Campos: Metodológicos vs Técnicos

El DMV se divide en información de alto valor estratégico (Metodológica) e información de control/proceso (Técnica).

| Categoría | Naturaleza | Visibilidad | Ejemplo |
|---|---|---|---|
| **Metodológico** | Información estratégica del negocio aportada por el emprendedor o deducida por la IA. | **Siempre Visible** | `narrativa_emprendedor`, `propuesta_valor`, `huecos_detectados`. |
| **Técnico** | Metadatos de control, estados de proceso e indicadores de auditoría. | **Compactable** | `proyecto_id`, `ultima_actualizacion`, `note_id`, `state_gate`. |

# 2. Blindaje contra la Compactación (No comprimir todavía)

Para no perder el "hilo conductor" del acompañamiento, los siguientes campos **no deben ser resumidos o comprimidos** en las primeras 6 fases:

- **Narrativa y Motivación**: Los matices originales del emprendedor son críticos para que la IA no se vuelva genérica.
- **Hipótesis Vivas**: Deben mantenerse literales hasta que se marquen como validadas o descartadas.
- **Alertas Tempranas**: Cada alerta debe persistirse íntegra para asegurar que se resuelve en fases posteriores.

# 3. Relación Campo DMV <-> Entregable por Fase

Cada entregable oficial es una "proyección" de los campos del DMV.

| Fase | Entregable (Output) | Campos DMV Origen |
|---|---|---|
| 01 | Informe de Diagnóstico Early | `narrativa_emprendedor`, `motivacion_principal`, `diagnostico_inicial_claridad`. |
| 02 | Definición de Dirección | `alcance_inicial`, `foco_inicial`, `direccion_inicial_validada`. |
| 03 | Canvas de Propuesta de Valor | `cliente_inicial`, `necesidad_relevante`, `propuesta_valor_inicial`, `encaje`. |
| 04 | Reporte de Validación | `mapa_senales`, `diagnostico_madurez_validacion`, `senales_favor/contra`. |
| 05 | Modelo de Negocio (BMC) | `que_vende_realmente`, `logica_ingreso`, `actividades_clave`. |
| 06 | Análisis PESTEL/Entorno | `factores_externos`, `tendencias_detectadas`, `oportunidades_externas`. |
| 07 | Mapa Competitivo | `competidores_directos`, `alternativas_reales`, `huecos_detectados`. |
| 08 | Síntesis DAFO/CAME | `fortalezas_principales`, `debilidades_principales`, `decision_rumbo`. |

# 4. Gestión de la "Memoria Viva"

El DMV asegura que la Fase 08 (Síntesis) tenga acceso a la "Narrativa Inicial" de la Fase 01, permitiendo al sistema detectar si el proyecto ha derivado excesivamente de su misión original o si los cambios están debidamente justificados por la evidencia de mercado.
