---
name: skill_decidir_si_requiere_investigacion
description: Regla para decidir si un entregable requiere investigación web y bajo qué modalidad (FAST o DEEP) obligatoriamente en NotebookLM.
---
# File: .agent/skills/skill_decidir_si_requiere_investigacion.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Evaluar el contenido de un entregable para determinar si se deben buscar fuentes y la profundidad de estas.
# Rol: Actuar como un Gate de Investigación y Evidencia.
# ──────────────────────────────────────────────────────────────────────

## Objetivo
Analizar la naturaleza de un entregable para decidir de manera explícita si precisa de fuentes verificables usando NotebookLM, y definir la profundidad (FAST o DEEP) justificando la decisión.

## Política obligatoria NotebookLM
- Si se requiere investigación externa, **SIEMPRE** se debe ejecutar el ciclo de NotebookLM:
  1. `mcp_notebooklm_research_start(...)`
  2. `mcp_notebooklm_research_status(...)`
  3. `mcp_notebooklm_research_import(...)`
- **PROHIBIDO**: No se permite "investigar fuera" (usar navegadores independientes o buscar sin registro) y solo pegar conclusiones. Toda fuente externa debe terminar importada en el cuaderno correspondiente.

## Árbol de Decisión

Antes de redactar la versión final de un entregable o análisis, ejecuta este árbol:

### Paso 1: Clasificar el tipo de afirmación del entregable

- **HECHO verificable** (cifra, ranking, normativa, tendencia temporal 2024-2026, nombre de competidor con claims) -> **Requiere investigación.** (Avanzar al Paso 2).
- **HIPÓTESIS** (basada en supuestos, conjeturas, experiencia o proyecciones estimadas) -> **Permitido, pero no requiere investigación profunda si es evidente.** Debe quedar explícitamente etiquetado en el documento ("Hipótesis", "Supuesto interno") y generar preguntas de validación (cosas pendientes por probar en calle).
- **MARCO/OPINIÓN** (definiciones internas del proyecto, metodología, enfoques teóricos) -> **No requiere investigación.**

### Paso 2: Si requiere investigación, decidir FAST o DEEP usando el "Impacto"

- **FAST (Modo por defecto)**: Usado para contexto, soporte, cifras generales, llenar PESTEL/DAFO con base, y obtener 5-10 fuentes iniciales.
- **DEEP (Excepción obligatoria)**: Usado cuando el resultado determina una decisión irreversible o de alto impacto.

**Criterios explícitos para DEEP:**
DEEP es obligatorio si el output afecta o requiere datos concluyentes sobre cualquiera de estos puntos:
1. Selección de segmento/nicho objetivo (ej. decantar entre transporte vs. transitario).
2. Decisión GO/NO-GO del modelo de negocio.
3. Pricing (modelos value-based, fees, setup) o estimación de ROI con soporte cuantitativo.
4. Competencia directa (mapeo competitivo preciso, productos sustitutos de alto riesgo, barreras de entrada).
5. Marco legal/regulatorio crítico (normativa de aduanas, transporte de mercancías, laboral del sector, protección de datos).
6. Riesgos financieros o reputacionales graves (multas, sanciones, régimen de incumplimientos).

## Justificación Obligatoria
Antes de ejecutar `research_start`, el Agente debe escribir/declarar explícitamente en su proceso, y dejar evidencia:
- **Modo elegido:** [FAST / DEEP]
- **Motivo:** [1-2 frases justificando según los criterios del Paso 2]

## Plantilla de query NotebookLM
Para mantener la consistencia en los prompts enviados a `research_start`, se debe seguir este patrón:
```text
Contexto: [Zaragoza / Aragón / España / UE], periodo [2023-2026].
Objetivo: Necesito datos/verificaciones sobre [tema] para decidir/soportar [argumento].
Destino: [Archivo o entregable output/... donde se usará].
Requisitos:
- Citar fuente original + año de publicación.
- Evitar blogs o fuentes no confiables salvo que sea estrictamente necesario.
Salida esperada: Resumen estructurado en bullets (y tabla si es relevante).
```

## Salida del Skill (Resultado esperado)
Tras completar la evaluación y (si aplicaba) la investigación, se debe reportar:
- `notebook_id` destino donde se importaron las fuentes.
- `task_id` (el ID temporal de la investigación).
- **Cantidad de fuentes importadas** al cuaderno.
- **Lista corta** de las 5 fuentes principales usadas (Títulos + Tipo de fuente/URL si está disponible).
- **Hipótesis o supuestos** (si el entregable incluye puntos clasificados como Hipótesis que quedan a la espera de validación de campo).

## Resultado de Verificación
El uso correcto de esta skill asegura:
- [x] Que el flujo mínimo de control de NotebookLM (`start` -> `status` -> `import`) sea obligatorio.
- [x] Que FAST sea el modo por defecto y DEEP se use bajo criterios estrictos y justificados.
- [x] Que cualquier dato "sacado de fuera" termine convertido en un asset indexado en la Biblioteca del usuario.
