# File: output/arquitectura/ARQ_02_catalogo_de_skills_y_workflows.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Catálogo operativo y técnico de las capacidades del agente.
# Rol: Plan de acción para la limpieza y generalización del runtime.
# ──────────────────────────────────────────────────────────────────────

# 1. Catálogo Operativo de Capacidades (Antigravity Runtime)

| Nombre | Tipo | Propósito | Dep. Logística | Decisión | Motivo |
|---|---|---|---|---|---|
| `skill_analisis_competitivo.md` | Skill | Realizar Benchmarking y Curva de Valor. | No | **Mantener** | Es una herramienta metodológica pura. |
| `skill_auditar_entregable.md` | Skill | Verificar cumplimiento de manuales de redacción. | No | **Mantener** | Núcleo del rol de "auditor de incubadora". |
| `skill_diseno_propuesta_valor.md`| Skill | Estructurar el encaje cliente-solución. | No | **Mantener** | Habilidad central del Programa Convierte. |
| `skill_notebooklm_bootstrap.md` | Skill | Iniciar/vincular notebooks y fuentes. | No | **Mantener** | Infraestructura técnica necesaria. |
| `skill_notebooklm_registrar...` | Skill | Guardar notas con IDs de trazabilidad. | No | **Generalizar** | Debe asegurar soporte para los 142 campos DMV. |
| `skill_notebooklm_research_web` | Skill | Búsqueda profunda de evidencia externa. | No | **Mantener** | Herramienta de rigor investigativo. |
| `skill_supervisor_coherencia...`| Skill | Auditoría de "hilo conductor" del proyecto. | No | **Mantener** | Asegura que la Fase 10 no contradiga a la 03. |
| `RULE_OPERATIVO_SISTEMA.md` | Rule | Reglas de comportamiento global de Antigravity. | No | **Mantener** | Define el contrato ético y operativo. |
| `WORKFLOW_VALIDACION_NEGOCIO.md`| Wkflow| Flujo maestro desde Intake a Validación. | Parcial | **Generalizar** | Cambiar referencias a "sector logística" por "nicho". |
| `workflow_producir_entregable.md`| Wkflow| Producción lineal de un entregable MD. | No | **Mantener** | Es el "brazo ejecutor" estándar. |

# 2. Análisis de Generalización Necesaria

Actualmente, el Runtime es técnicamente agnóstico a la logística, pero existen "filtros mentales" en los prompts que asumen un entorno B2B industrial.

- **Acción Inmediata**: Revisar los ejemplos internos en las skills (especialmente en `skill_analisis_competitivo`) para que no fuercen analogías logísticas si el usuario es, por ejemplo, un emprendedor de servicios digitales.
- **Acción en Workflows**: El workflow `VALIDACION_NEGOCIO` debe ser renombrado internamente o referenciado como `WORKFLOW_CORE_PROGRAMA` para desacoplarlo de la idea de "Validación de Negocio Logístico".

# 3. Estado de Deprecación

No se detectan skills obsoletas, pero se sugiere **deprecar la skill `skill_notebooklm_registrar_entregable.md`** si se decide migrar a una gestión de DMV centralizada (JSON) que automatice este registro mediante el script de validación determinista.
