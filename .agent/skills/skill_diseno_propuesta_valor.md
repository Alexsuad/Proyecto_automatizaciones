---
name: skill_diseno_propuesta_valor
description: Procesa la urgencia validada del mercado y la mecánica del proyecto para formular los componentes estratégicos de la propuesta de valor sin sesgo tecnológico por defecto.
---
# File: .agent/skills/skill_diseno_propuesta_valor.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Digestor estratégico. Conecta lógicamente el dolor urgido con la mecánica de la solución B2B.
# Rol: Arquitecto de Propuesta de Valor (Honestidad Analítica Estricta).
# ──────────────────────────────────────────────────────────────────────

## Objetivo
Analizar la urgencia real del problema del cliente detectada por NotebookLM y armar los bloques lógicos de la propuesta de valor (Aliviadores y Diferenciadores). Esta skill actúa como "digestor": no redacta el documento final (.md formateado), sino que produce el esqueleto lógico para evitar derivas temáticas, sesgos a palabras de moda o promesas imposibles.

## Entradas Requeridas (Inputs)
Esta skill solo debe ejecutarse si se dispone de:
1. `00_intake_proyecto.md` (o el documento estructurado del negocio a montar).
2. El resultado de NotebookLM correspondiente al **Prompt 1 (Investigación de Mercado y Entorno)**.
   - **GATE OBLIGATORIO:** El output de investigación debe estar formalmente validado por el checklist de `NOTEBOOKLM_OUTPUT_CRITERIA.md`. Esta skill no puede alimentarse de research crudo sin filtrar.

## Reglas de Procesamiento (Operaciones)

Al sintetizar la propuesta, el agente debe operar bajo estas directrices:

1. **Anti-Humo Tecnológico (Cero SaaS por defecto):** Tienes expresamente prohibido usar jerga técnica ("módulos", "orquestación", "plataforma multi-tenant", "SaaS") para describir el servicio, **a menos que** el Intake diga literalmente "somos una empresa de software/SaaS". Presenta la propuesta como un mecanismo de atención al dolor (ej. "servicio de consultoría", "sistema llave en mano", "equipo externo", "operativa delegada").
2. **Dependencia Causal Estricta:** No inventes aliviadores "bonitos" que no ataquen directamente un dolor que el Prompt 1 demostró que existe. Cada beneficio prometido debe ser la medicina exacta a una herida real.
3. **Control de Certeza (Marcaje de Hipótesis):**
   - Si un logro (ej. "ahorraremos un 30% de costo") no está avalado por pilotos terminados o datos confirmados explícitamente en el Intake/NotebookLM, debe marcarse irremediablemente como `[HIPÓTESIS VALORATIVA]`.

## Salida Estructurada (Outputs - CONTRATO OBLIGATORIO)

La skill **no debe redactar** el archivo `02_canvas_valor.md`. Sólo entrega este Payload Exacto como contrato de datos estructurado para alimentar el flujo de redacción posterior:

**Formato exigido (Debe devolver exactamente estos 6 campos, ni más ni menos):**

```markdown
- **problema_validado**: [El dolor más agudo extraído de NotebookLM que vamos a resolver]
- **intensidad_del_dolor**: [Crítico (amenaza de muerte del negocio) / Moderado / De Segundo Orden]
- **game_changer**: [La diferencia nuclear de nuestra oferta vs el status quo. Máximo 2 líneas]
- **aliviadores_clave**: [Lista de 1 a 3 mecanismos precisos mediante los cuales nuestra solución cura el dolor]
- **enfoque_de_entrega**: [Cómo percibe el cliente el servicio: Ej. Suscripción SaaS, Consultoría 1-a-1, Taller Físico, Servicio Delegado]
- **beneficios_hipoteticos**: [1 a 3 declaraciones de valor que asumen el éxito pero requieren pruebas de calle. Marcados como HIPÓTESIS VALORATIVA]
```

## Relación con el Pipeline (Destino del Dato)
El bloque de salida superior alimentará:
- Al 100% como arquitectura base para la creación del **Canvas de Propuesta de Valor** (`02_canvas_valor.md`).
- Como insumo correctivo estructural para el **Mapa de Empatía** (`01_mapa_empatia.md`).
