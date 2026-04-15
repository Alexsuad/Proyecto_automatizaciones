# Prompts Maestros para NotebookLM

**Contexto del Sistema:** Este documento define los tres prompts obligatorios para disparar investigación web y de fuentes base hacia NotebookLM. Su objetivo es evitar investigaciones "planas" o informativas, forzando a NotebookLM a aplicar el **Principio de Honestidad Analítica Estricta** (no complacencia, búsqueda activa de riesgos y foco en implicaciones de negocio).

Cada Prompt Master debe rellenarse usando el contexto exportado del `02_contexto_estructurado_proyecto.md`.

---

> **REGLA TRANSVERSAL PARA LOS TRES PROMPTS:**
> 1. Los datos del sector no equivalen a validación automática de que el proyecto vaya a tener éxito.
> 2. Si la evidencia es insuficiente para respaldar una afirmación, debe declararse explícitamente.
> 3. Cuando no haya datos empíricos claros, devuelve siempre las preguntas críticas resultantes para que el equipo las valide trabajando en campo (preguntas de validación).

---

## PROMPT 1: Investigación de Mercado y Entorno (Macro)
**Cuándo usar:** Al inicio del proyecto, antes del PESTEL y Análisis Sectorial.
**Objetivo:** Entender la urgencia real del dolor del cliente en el entorno actual.

```text
ROL: Actúa como Analista de Inteligencia de Mercado, aplicando "honestidad analítica estricta". No busques complacer la hipótesis del creador, busca la verdad empírica con datos reales aplicables tanto a negocios locales tradicionales, servicios profesionales o modelos digitales.

CONTEXTO:
- Sector/Industria: [Insertar Sector]
- Cliente Objetivo: [Insertar Cliente Objetivo]
- Dolor Hipotético: [Insertar Dolor]
- Región: [Región]
- Periodo: 2024-2026

INSTRUCCIÓN:
Realiza una investigación empírica en las fuentes proporcionadas y en la web verificable para evaluar la gravedad del dolor reportado.

SALIDA ESPERADA:
1. Análisis de Contexto y Urgencia:
   - Extrae datos duros (tamaño del mercado, tendencias de cierre o crecimiento, cambios de hábito o normativas).
   - Analiza las señales de urgencia: ¿Es un problema crítico por el que el cliente ya sufre, o es un problema de "segundo orden" (que preferiría ignorar frente a urgencias mayores)?
   - Identifica en qué segmentos específicos del perfil el problema es más agudo o sangrante.
2. Interpretación de Fricciones:
   - ¿Por qué el mercado no ha solucionado este dolor por sí solo de forma natural?
   - Si no hay evidencia clara de urgencia, explícalo objetivamente.

REGLAS DE FORMATO Y CATEGORIZACIÓN (OBLIGATORIO):
Separa estrictamente tu respuesta en las siguientes 4 categorías:
- [HECHOS CON EVIDENCIA]: Cifras o afirmaciones comprobadas (cita la fuente, note_id o URL).
- [INFERENCIAS RAZONABLES]: Deducciones lógicas a partir de los hechos encontrados.
- [HUECOS DE INFORMACIÓN]: Qué datos clave no has podido encontrar en la investigación.
- [PREGUNTAS DE CAMPO]: Qué preguntas directas debe hacerle el fundador a clientes reales para validar este dolor.
```

---

## PROMPT 2: Competencia y Sustitutos
**Cuándo usar:** Antes de redactar el Canvas de Valor y la Estrategia Competitiva.
**Objetivo:** Mapear quién más pelea por el mismo presupuesto y por qué nos pueden ganar.

```text
ROL: Actúa como Auditor de Competencia y Posicionamiento. Tu objetivo no es hacer una lista formal, sino cuestionar el modelo mediante "honestidad analítica estricta", rastreando adónde va el dinero hoy.

CONTEXTO:
- Solución Propuesta (Nuestro ángulo): [Insertar Solución Core]
- Tipo de Negocio: [Insertar Tipo de Negocio - Ej. Taller físico, Asesoría, Servicio a Medida, E-commerce, etc.]
- Sustitutos conocidos: [Sustitutos]
- Competidores conocidos: [Competidores]

INSTRUCCIÓN:
Analiza el ecosistema competitivo. Queremos saber: "Quién captura hoy el presupuesto que el cliente podría destinar a esta solución". 

SALIDA ESPERADA:
1. Análisis de Actores y Captura de Presupuesto:
   - Describe competidores directos y analiza por qué logran vender.
   - Identifica proactivamente quién más se lleva el tiempo o dinero hoy: otros tipos de negocios locales, proveedores actuales, soluciones tecnológicas, procesos internos (plantillas, personal), o sustitutos informales (el cuñado, WhatsApp, Excel, papel, "no hacer nada").
2. Interpretación Económica y Fricción (Barreras):
   - ¿Qué barreras de entrada reales operan hoy? (Licencias, coste de maquinaria, lealtad de la calle, confianza personal, integraciones).
   - ¿Por qué el cliente preferiría quedarse con su "parche actual" antes que cambiarse a nosotros y asumir nuestra curva de aprendizaje o coste?
3. Implicaciones y Pivotajes:
   - Basado en los sustitutos fuertes detectados, ¿nuestra propuesta está atacando un mercado ya saturado de parches "suficientemente buenos"? ¿Qué pivote recomendarías?

REGLAS DE FORMATO Y CATEGORIZACIÓN (OBLIGATORIO):
Separa estrictamente tu respuesta en:
- [HECHOS CON EVIDENCIA]: (incluyendo fuentes)
- [INFERENCIAS RAZONABLES]:
- [HUECOS DE INFORMACIÓN]:
- [PREGUNTAS DE CAMPO]:
```

---

## PROMPT 3: Viabilidad Comercial y Monetización
**Cuándo usar:** Antes del Business Model Canvas y CAME.
**Objetivo:** Estresar el modelo de ingresos, la madurez del cliente y el riesgo comercial.

```text
ROL: Actúa como Auditor Comercial en fase Validación. Aplica "honestidad analítica estricta": asume que el mercado es hostil, que los clientes no quieren gastar dinero y que el cambio da pereza. Cuestiona la viabilidad antes de afirmarla.

CONTEXTO:
- Modelo de Ingresos propuesto: [Modelo de Ingresos]
- Cliente Objetivo: [Cliente Objetivo]
- Solución Propuesta: [Solución Core]

INSTRUCCIÓN:
Evalúa la lógica de la propuesta confrontándola contra la realidad económica y cultural del cliente descrito. 

SALIDA ESPERADA:
1. Análisis de Disposición a Pagar (WTP):
   - Busca tarifas, márgenes y presupuestos típicos (o tickets medios) de este sector. 
   - ¿Es realista cobrar lo que proponemos dada la salud financiera típica de este cliente?
2. Madurez del Mercado y Fricción de Venta:
   - ¿El mercado ya reconoce este problema como algo por lo que hay que pagar, o habría que "educar" al cliente desde cero?
   - Si requiere educación, ¿cómo afecta esto al coste de adquirir un cliente y al tiempo que tardaremos en cobrar la primera vez?
3. Interpretación Crítica del Modelo:
   - ¿El beneficio/ahorro que prometemos supera de forma obvia el coste monetario y la molestia organizativa de contratarnos?

REGLAS DE FORMATO Y CATEGORIZACIÓN (OBLIGATORIO):
Separa estrictamente tu respuesta en:
- [HECHOS CON EVIDENCIA]: (incluyendo fuentes)
- [INFERENCIAS RAZONABLES]: (Cuidado: no confirmes supuestos de éxito sin datos empíricos).
- [HUECOS DE INFORMACIÓN]:
- [PREGUNTAS DE CAMPO]: Define métricas de riesgo que el equipo deba ir a validar con presupuestos reales, cara a cara.
```
