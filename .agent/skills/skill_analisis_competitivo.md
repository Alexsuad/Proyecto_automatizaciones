---
name: skill_analisis_competitivo
description: Procesa la investigación filtrada de NotebookLM para generar un mapa táctico de posicionamiento, identificando el competidor/sustituto real, la fricción de adopción y la táctica de ataque recomendada.
---
# File: .agent/skills/skill_analisis_competitivo.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Digestor estratégico. Analiza datos de la calle para formular táctica competitiva, antes de la redacción.
# Rol: Estratega de Posicionamiento (Honestidad Analítica Estricta).
# ──────────────────────────────────────────────────────────────────────

## Objetivo
Evaluar el entorno competitivo y las alternativas actuales del cliente para determinar con quién competimos realmente por el presupuesto hoy, cuál es el grado de fricción que encontraremos, y recomendar la táctica de ataque. Esta skill es el "cerebro" analítico de la Fase 3, que produce el insumo pero no formatea el entregable final.

## Entradas Requeridas (Inputs)
Esta skill solo debe ejecutarse si se dispone de:
1. `00_intake_proyecto.md` (o el documento estructurado del negocio a montar).
2. El resultado de NotebookLM correspondiente al **Prompt 2 (Competencia y Sustitutos)**.
   - **GATE OBLIGATORIO:** El output de investigación debe estar formalmente validado por el checklist de `NOTEBOOKLM_OUTPUT_CRITERIA.md`. Esta skill tiene prohibido alimentarse de research superficial o ciego.

## Reglas de Procesamiento (Operaciones)

Al sintetizar el mapa táctico, debes operar bajo estas directrices inquebrantables de Honestidad Analítica Estricta:

1. **Anti-Complacencia del Sustituto Informal:** No subestimes el "status quo". Si la investigación devela que el cliente usa un "parche informal" (Excel, papel, no hacer nada) y le sale más barato o fácil que nuestra propuesta, decláralo fuertemente como una `friccion_de_cambio` crítica.
2. **Sustitución Fragmentada (No inventar enemigos):** Si los datos muestran que no existe un "gran competidor dominante" sino una multitud de micro-herramientas o tareas dispersas, declara explícitamente "Patrón de Sustitución Fragmentada". No inventes o eleves a la fuerza el nombre de una marca como competidor principal si no refleja la realidad de ese nicho.
3. **Manejo de Incertidumbre y Evidencias:**
   - Si la asimilación táctica que propones nace íntegramente de la categoría de `[HECHOS CON EVIDENCIA]`: procede normal.
   - Si la táctica se deriva fuertemente de `[INFERENCIAS RAZONABLES]` o hay datos faltantes: debes etiquetar obligatoriamente la parte de tu propuesta como `[HIPÓTESIS ESTRATÉGICA]`.

4. **Bloqueo por Señal Débil (No Forzar Táctica):** Si la investigación de NotebookLM vuelve con vacíos graves y es imposible deducir razonablemente la fricción o el sustituto, está PROHIBIDO inventar una estrategia. Debes devolver un estado de bloqueo explícito: `[INSUFICIENCIA DE SEÑAL COMPETITIVA]` y pedir que el bloque de investigación se repita o que el usuario aporte datos manuales de campo.

## Salida Estructurada (Outputs - CONTRATO OBLIGATORIO)

La skill **no debe redactar** ni `05_competencia.md` ni `06_estrategia_competitiva.md`. Sólo entrega este Payload Exacto como contrato de datos estructurado para alimentar el flujo posterior. 

**Formato exigido (Debe devolver exactamente estos 8 campos, ni más ni menos):**

```markdown
- **sustituto_dominante**: [Nombre de la empresa, herramienta o proceso manual/informal más usado hoy]
- **tipo_de_sustituto**: [Directo corporativo, Indirecto, Parche informal, Inacción]
- **por_que_hoy_se_usa**: [Atractivo real de ese sustituto: es gratis, inercia, única opción local]
- **vulnerabilidad_principal**: [Brecha detectada que nosotros podemos atacar: caro, ineficiente, lento]
- **friccion_de_cambio**: [Pereza, coste, riesgo o miedo que tendrá el cliente al abandonarlo]
- **tactica_recomendada**: [Recomendación base de ataque. Usa la etiqueta [HIPÓTESIS ESTRATÉGICA] si aplica]
- **nivel_de_confianza**: [ALTO / MEDIO / BAJO - según la calidad de datos de NotebookLM]
- **alertas_o_huecos_a_validar**: [1 a 3 preguntas estratégicas críticas a validar de urgencia en la calle]
```

## Relación con el Pipeline (Destino del Dato)
El bloque de salida superior alimentará:
- Al 100% como documento cartográfico para `05_competencia.md`.
- Solamente como recomendación táctica base/insumo para `06_estrategia_competitiva.md`.
