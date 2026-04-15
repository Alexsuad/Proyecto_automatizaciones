# Criterios de Calidad de Salida para NotebookLM

**Contexto del Sistema:** Este documento define el *checklist* (Gate de Calidad) mediante el cual el sistema debe evaluar el output crudo (investigación) devuelto por NotebookLM antes de inyectarlo en el motor de redacción.

> **Alcance Universal:** Estos criterios aplican por igual a proyectos B2B tecnológicos, negocios locales, servicios profesionales presenciales y modelos híbridos producto-servicio.

---

## 🚩 Categorías de Evaluación (Red Flags)
El sistema debe procesar la salida de NotebookLM y evaluar si cae en alguno de estos escenarios, clasificados por severidad:

### A. Fallos Críticos (RECHAZO AUTOMÁTICO)
*Si la investigación incumple alguno de estos puntos, no es válida como fuente.*

**1. Superficialidad o "Efecto Wikipedia"**
- **Red Flag:** El análisis solo ofrece definiciones generales del sector sin datos empíricos ni análisis de la *urgencia* específica del problema.
- **Criterio:** Debe contener datos tangibles y evaluar si el dolor es crítico o un problema de "segundo orden".

**2. Listas de datos sin interpretación estratégica**
- **Red Flag:** NotebookLM entrega listas (leyes, competidores) sin explicar cómo afectan al proyecto actual y sin usar la categoría `[INFERENCIAS RAZONABLES]`.

**3. Ausencia de Sustitutos Informales**
- **Red Flag:** Omite cómo resuelve el cliente su problema HOY de forma casera o analógica (Excel, papel, WhatsApp, hacerlo él mismo). Si asume que "no existen sustitutos", se rechaza.

**4. Mezcla Tóxica de Hechos e Inferencias**
- **Red Flag:** Presenta afirmaciones lógicas, estimaciones o esperanzas de éxito futuro como si fueran `[HECHOS CON EVIDENCIA]`.

### B. Fallos Importantes (DEVOLVER PARA REVISIÓN)
*Si la investigación falla aquí, el sistema debe lanzar un prompt correctivo (re-prompt) exigiendo que se complete la información faltante.*

**5. Ausencia de Fricción de Cambio o Adopción**
- **Fallo:** La salida asume que, como hay un problema, el cliente automáticamente adoptará la nueva solución sin resistencia.
- **Corrección requerida:** Debe detallar la fricción de cambio (curva de aprendizaje, coste de migración, pérdida de proveedores de confianza, etc.).

**6. Ausencia de Preguntas de Validación en Campo**
- **Fallo:** La salida no incluye la sección obligatoria `[PREGUNTAS DE CAMPO]`.
- **Corrección requerida:** Obligar al modelo a declarar qué datos no pudo probar y qué debe preguntarse a un cliente en la vida real.

**7. Sesgo Complaciente (Validación Automática)**
- **Fallo:** El tono adula al equipo ("idea altamente innovadora") o asume viabilidad comercial sin datos de Disposición a Pagar (WTP).
- **Corrección requerida:** Aplicar "Honestidad Analítica Estricta". Si no hay evidencia de WTP, declarar el riesgo.

---

## ⚖️ Veredicto de Evaluación

Todo agente o skill que consuma output de NotebookLM emitirá uno de estos tres veredictos:

- ✅ **APTO:** Cumple todo. Avanza al flujo de redacción.
- 🟡 **DEVOLVER PARA REVISIÓN:** Falla en la categoría B. Se lanza un prompt correctivo automático señalando el fallo.
- 🔴 **RECHAZADO:** Falla en la categoría A. Se bloquea la rama de investigación ("Bloqueado por falta de datos base").
