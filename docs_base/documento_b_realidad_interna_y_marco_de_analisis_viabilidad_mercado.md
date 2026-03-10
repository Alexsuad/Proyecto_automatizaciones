# DOCUMENTO B — REALIDAD INTERNA Y MARCO DE ANÁLISIS

## (Viabilidad + Mercado) — Complementario al Dossier Ampliado

**Versión:** 1.2
*Se formaliza mecánica comercial para clientes no conscientes y regla de posicionamiento del término automatización (interno).*
**Rol del documento:** Base interna (análisis honesto)
**Complementa a:** Dossier Ampliado — Proyecto ZAC (Documento A)

---

## 0. Propósito y regla de uso

Este documento existe para que el proyecto tome decisiones **reales** y no basadas en narrativa comercial.

### Pitch interno (para tutores)

Este proyecto diseña e implementa sistemas a medida para que pymes logísticas pasen de procesos manuales (Excel, correos, validaciones dispersas) a **control operativo real**: trazabilidad, alertas y evidencia. Empezamos por logística en Zaragoza como segmento inicial por cercanía y densidad del ecosistema, con plan de expansión. Internamente usamos un enfoque híbrido (Python, automatización, integraciones y, cuando aporta ROI, IA/RAG/agentes) para construir soluciones mantenibles y auditables. Hacia afuera lo comunicamos por resultados; este documento existe para analizar viabilidad, riesgos, sustitutos y decisiones con total honestidad.

### Principio interno (anti-humo)

Este proyecto evita posicionarse como “empresa de IA” o “automatización de moda”. Internamente se prioriza construir soluciones **realistas, medibles y mantenibles**, basadas en reglas del negocio, control operativo y evidencia. La IA se usa solo cuando aporta valor comprobable y bajo criterios de confiabilidad, trazabilidad y costo total. Este principio no es marketing: es una regla para filtrar proyectos, definir alcance y proteger la reputación del proyecto a largo plazo.

* **Documento A (Dossier Ampliado):** sirve para comunicar el proyecto de forma clara y sin buzzwords, centrado en resultados.
* **Documento B (este documento):** sirve para analizar viabilidad y mercado con la **realidad interna completa**: herramientas, capacidades, límites, costos, riesgos y sustitutos.

### Regla de oro

1. **Si el objetivo es vender/explicar:** usar Documento A.
2. **Si el objetivo es decidir/validar:** usar Documento B.

---

## 1. La verdad interna (qué hacemos realmente)

### 1.1 Qué ofrecemos en la práctica

Aunque externamente el proyecto se presenta como “control operativo instalado”, internamente el trabajo incluye:

* Levantar el flujo crítico y sus reglas mínimas como parte del arranque guiado (para poder implementar).
* Modelar reglas del negocio y excepciones.
* Diseñar y construir la solución.
* Integrar fuentes de datos (Excel, correo, ERP, bases de datos, APIs, PDFs, imágenes).
* Automatizar tareas repetitivas y validaciones.
* Implementar alertas, trazabilidad, evidencias, dashboards.
* Mantener y evolucionar el sistema.

### 1.2 Qué NO hacemos (límites internos)

Para que el análisis sea serio, se declaran límites:

* No prometemos automatización total de la empresa.
* No prometemos ROI sin medir datos reales.
* No competimos por ser “los más baratos”.
* No construimos “software por construir”: el foco es control/valor.

---

## 2. Caja de herramientas real (stack y medios)

**Nota:** esto NO es para marketing. Es para calcular tiempos, costos, riesgos y capacidades.

### 2.1 Tipos de soluciones que podemos implementar

* Automatizaciones y pipelines (extracción, transformación, validación, carga).
* Aplicaciones web internas / paneles de control.
* Apps ligeras para captura de evidencia/estado.
* Conectores e integraciones (APIs, bases de datos, archivos).
* Sistemas de validación documental (PDF/imagen + reglas).
* IA aplicada cuando aporta ROI (clasificación, extracción asistida, búsqueda sobre documentos, ayuda operativa).

### 2.2 Tecnologías principales (referencia interna)

**Lenguaje de programación principal**

* **Python**: base para scripts, automatización, ETL, validación, servicios e integraciones.
* **JavaScript / React**: se mencionan como complemento posible cuando el caso lo exige, pero la estrategia interna prioriza Python para acelerar prototipos y MVPs sin depender de un stack web complejo.

**Frameworks para construir productos con Python (UI / apps)**

* **Streamlit**: dashboards y paneles interactivos.
* **Gradio**: interfaces visuales rápidas para prototipos con IA.
* **NiceGUI**: aplicaciones web internas de gestión.
* **Flet**: apps móviles (iOS/Android) y de escritorio multiplataforma.
* **Reflex**: aplicaciones web full-stack y MVPs.

**Inteligencia Artificial y Machine Learning (cuando aporta ROI)**

* Integración con modelos y APIs (por ejemplo, GPT, Claude, Gemini; y generación de imágenes como DALL·E cuando aplique).
* **RAG (Retrieval-Augmented Generation)**: para que la IA consulte y responda sobre documentos del cliente (PDFs, bases de datos, manuales).
* **Agentes de IA**: sistemas autónomos que usan herramientas (siempre con control, trazabilidad y límites).
* Asistentes de código (uso interno) para acelerar desarrollo.

**Librerías de datos, automatización y backend**

* **Pandas** y **Polars**: procesamiento y análisis de datos.
* **Plotly**: visualización interactiva.
* **FastAPI**: backend y servicios para integraciones.
* **Asyncio**: concurrencia cuando aplica.
* **Selenium** y **Playwright**: automatización de navegador cuando no hay APIs.
* Integraciones de alertas/mensajería (por ejemplo, **Telegram APIs**) y otras según el caso.

### 2.3 Regla de selección tecnológica (criterio interno)

Siempre elegir la opción que maximice:

* **Confiabilidad** (que no falle en operación real)
* **Trazabilidad** (evidencia y auditoría)
* **Mantenibilidad** (que se pueda sostener en el tiempo)
* **Costo total** (desarrollo + operación + soporte)

---

## 3. Capacidades núcleo (lo que sí es replicable)

Para no convertirnos en “hacemos de todo”, el proyecto se sostiene en 3 capacidades replicables:

1. **Validación y auditoría de datos/documentos**

   * reglas del negocio, discrepancias, control previo al pago, alertas

2. **Trazabilidad y control de proceso**

   * estados, evidencias, incidencias, responsables, tiempos

3. **Tableros de control operativos**

   * centralización de información, KPIs accionables, visibilidad de margen/desviaciones

Estas capacidades definen:

* qué proyectos aceptamos primero,
* qué proyectos rechazamos o derivamos,
* y cómo escalamos a “nicho replicable”.

---

## 4. Mercado: competidores y sustitutos (mapa real)

### 4.1 Competidores directos (por resultado)

Actores que también entregan “control operativo” o soluciones similares:

* Desarrolladores/estudios de software a medida B2B.
* Integradores de ERP/TMS/WMS que implementan módulos y reportes.
* Consultoras boutique que además de analizar, implementan herramientas.
* Empresas especializadas en auditoría documental / facturas / compliance (aunque lo llamen distinto).

### 4.2 Sustitutos (los que compiten aunque no parezcan)

Esto es clave para la viabilidad. Sustitutos típicos:

* No-code / low-code (automatizaciones con herramientas estándar).
* “Freelancers baratos” que entregan scripts puntuales.
* Software estándar (ERP/TMS/WMS + módulos) que el cliente ya paga.
* Excel “bien gestionado” + disciplina (aunque sea frágil, es el sustituto real más común).
* Agencias de “IA” genéricas (promesas rápidas; pueden confundir al cliente).

### 4.3 Qué nos diferencia de forma defendible

* Enfoque en **control + evidencia**, no solo automatización.
* Soluciones **adoptables** (UX y operación real).
* Capacidad híbrida: entender la operación y traducirla a sistema.
* Selección de herramientas por confiabilidad (no por moda).

### 4.4 Segmento inicial (Zaragoza) y expansión

El segmento inicial será **pymes logísticas ubicadas en Zaragoza** por cercanía, acceso y densidad del ecosistema.

Aun así, Zaragoza es un mercado **acotado**, por lo que el análisis de mercado y la estrategia de crecimiento deben contemplar expansión por etapas:

* **Aragón** (plataformas y corredores cercanos).
* **España** (otros hubs logísticos y transitarios).
* **Europa** (mercados donde la presión regulatoria y la transición tecnológica acelera la demanda).

### 4.5 Fuentes internas obligatorias para análisis

Además del Documento A, para investigaciones profundas y estudios (mercado/viabilidad) se deben usar como base:

* **Informe_ Mercado Freelance de Automatización Hiperpersonalizada en Logística (Python)**
* **El Ecosistema Logístico Europeo y la Transición Tecnológica**
* **Proceso_Integral_Diseno_Validacion_Ejecucion_Proyectos**

4.6 Estrategia de entrada: “Producto 1” (wedge) + piloto medible

Para evitar un posicionamiento difuso (“hacemos de todo”) y reducir el riesgo comercial y técnico, la entrada al mercado se realizará mediante un wedge: un primer caso acotado que permita demostrar valor con datos reales, sin requerir despliegues extensos.

Producto 1 (wedge propuesto): Control Doc-to-Cash (Viaje → Evidencia → Factura → Cobro).
Este wedge es consistente con las capacidades núcleo del proyecto (validación/auditoría, trazabilidad/control, tableros) 

documento_b_realidad_interna_y_…

 y ataca un dolor directamente relacionado con caja/operación (bloqueos por documentación y falta de visibilidad), lo que aumenta probabilidad de decisión por parte de gerencia.

Objetivo del piloto (qué debe validar)

El piloto no busca “demostrar tecnología”, sino validar que el sistema:

Reduce bloqueos por falta o mala calidad de evidencia (POD/CMR/albarán).

Es adoptable por operación/backoffice (uso real, sin fricción excesiva).

Puede operar con datos sucios y canales reales del cliente (condición típica del sector). 

documento_b_realidad_interna_y_…

Permite medición del impacto (sin métricas no hay viabilidad). 

documento_b_realidad_interna_y_…

Diseño del piloto (alcance acotado)

Para evitar dependencia de proyectos largos (riesgo B2B) 

documento_b_realidad_interna_y_…

, el piloto debe acotarse a:

Un subconjunto de viajes (muestra controlada).

1–3 tipos de documento (POD/CMR/albarán).

Reglas mínimas de aceptación (completitud/legibilidad mínima).

Un tablero básico con estados por viaje (OK / bloqueado / causa).

Métricas mínimas (criterio de éxito)

El piloto se considera exitoso si permite medir, al menos:

% de viajes con evidencia completa dentro del plazo objetivo.

# de casos bloqueados por documentación (línea base vs. durante piloto).

Tiempo medio de resolución de bloqueos (documento faltante / inválido).

Estas métricas conectan directamente con el enfoque defendible de “control + evidencia” y con la necesidad de tableros accionables. 

documento_b_realidad_interna_y_…

Regla de consistencia (narrativa externa vs realidad interna)

En narrativa externa, el wedge se describe como “control de bloqueos y evidencia por viaje” (resultado).
En realidad interna (este documento), se acepta que pueden usarse herramientas diversas (Python, integraciones, automatización, componentes de IA si aportan confiabilidad y medición), manteniendo la regla de selección tecnológica por confiabilidad y trazabilidad. 

chat02_Antigravity

---

## 5. Hipótesis críticas (lo que debemos validar sí o sí)

Estas hipótesis determinan si el negocio es viable:

1. Existe dolor pagable en pymes logísticas (tiempo/dinero/riesgo) que no está resuelto con su sistema actual.
2. El cliente paga más por una solución instalada y mantenida que por “un script”.
3. Podemos demostrar valor con un MVP corto sin entrar en proyectos interminables.
4. La adopción del equipo es alcanzable (UX + quick wins).
5. Podemos construir un núcleo replicable sin que cada proyecto sea totalmente único.

---

## 6. Riesgos reales (y cómo afectan decisiones)

### 6.1 Riesgos comerciales

* Cliente no prioriza control (prefiere “apagar incendios”).
* Ciclos de venta largos en B2B.
* Cliente compara con “freelancer barato”.

### 6.2 Riesgos operativos

* Datos incompletos o sucios.
* Cambios de formatos/documentos frecuentes.
* Dependencia de proveedores externos.

### 6.3 Riesgos técnicos

* Dependencia de herramientas de terceros.
* Costos variables de IA si se usa sin control.
* Seguridad y protección de datos.

---

## 7. Criterios internos para aceptar proyectos (filtro anti-caos)

Se priorizan proyectos que:

* se alineen con las 3 capacidades núcleo (validación, trazabilidad, dashboards)
* tengan un proceso crítico repetitivo
* permitan MVP en tiempo razonable
* tengan acceso a datos reales
* tengan decisor claro

Se evitan proyectos que:

* sean “citas y reservas” genéricas (commodity)
* sean “todo el ERP desde cero”
* tengan dependencia total de terceros sin control
* no permitan medir impacto

---

## 8. Modelo de servicio real (cómo trabajamos por dentro)

### 8.1 Fase 1 — Arranque guiado + definición del MVP

* captura de proceso real
* lista de reglas
* priorización
* estimación conservadora (tiempo/dinero/riesgo)
* piloto corto si aplica

### 8.2 Fase 2 — Implementación

* construcción
* integraciones
* pruebas con datos reales
* puesta en funcionamiento

### 8.3 Fase 3 — Acompañamiento

* soporte
* ajustes
* mejoras

### 8.4 Mecánica comercial para clientes “no conscientes” (sin consultoría)

En pymes logísticas es común que el cliente no perciba que tiene un “problema de automatización”. Lo que sí percibe es el costo del descontrol: cobros bloqueados, incidencias sin evidencia, reprocesos y falta de visibilidad.

Por eso la venta NO se basa en explicar tecnología. Se basa en hacer visible el costo operativo y demostrar valor con un piloto corto.

**Secuencia estándar (replicable):**
1) **Chequeo corto (15–30 min):** preguntas y checklist sobre un flujo crítico (cobro, incidencias o margen).
2) **Arranque guiado (90 min):** definición del flujo elegido, reglas mínimas, evidencias, entradas y salida esperada.
3) **Piloto con datos reales (72h–7 días):** implementación mínima para mostrar el “antes vs después”.
4) **Implementación del MVP:** si el piloto demuestra valor, se formaliza alcance y se construye.
5) **Acompañamiento:** soporte y mejoras.

**Regla anti-consultoría:**
- No vendemos diagnósticos abiertos ni informes como producto final.
- El resultado de la fase inicial debe ser un piloto funcional o un MVP definido para implementación.
- Si el cliente pide “revisar toda la empresa”, se vuelve a enfocar en un flujo crítico primero.

### 8.5 Posicionamiento estratégico del término “automatización”

Internamente, el proyecto utiliza automatización, integración de sistemas y, cuando aporta valor real, componentes de inteligencia artificial.

Sin embargo, en la comunicación externa el término “automatización” no se utiliza como eje principal del discurso comercial.

La razón es estratégica:
Las pymes logísticas no compran “automatización”.
Compran control, reducción de bloqueos de cobro, evidencia ante incidencias y mejora visible del margen operativo.

Por tanto:
- La automatización es el mecanismo interno.
- El mensaje externo es control operativo y resultado tangible.
- El discurso comercial comienza por el dolor operativo y termina en herramienta funcionando.

---

## 9. Cómo se conecta con el Documento A (para no contradicirnos)

* Documento A describe el “qué” en lenguaje de negocio.
* Documento B define el “cómo” real, los riesgos y el mapa de mercado.

**Regla de consistencia:**

* Nada de lo dicho en A debe ser falso frente a B.
* B puede tener detalles que A omite por estrategia de comunicación.

---

## 10. Plantillas internas (para futuros análisis)

### Plantilla 1 — Ficha de proceso candidato

* Proceso:
* Dolor:
* Entradas:
* Salidas:
* Reglas:
* Frecuencia:
* Riesgo:
* MVP posible:

### Plantilla 2 — Mapa de sustitutos

* Sustituto actual (Excel/ERP/no-code):
* Por qué no resuelve:
* Qué se rompe:
* Qué mejoraría con sistema:

### Plantilla 3 — Riesgos por cliente

* Datos:
* Adopción:
* Seguridad:
* Dependencias:

---


