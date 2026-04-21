# Proyecto_automatizaciones

Repositorio maestro para el diseño, validación y estructuración de una **app de acompañamiento al emprendedor** orientada a analizar proyectos, construir documentación útil por fases y llegar a un **Plan de Empresa** con trazabilidad, criterio y control.

---

## 1. Qué es este repositorio

Este repositorio **no es solo un proyecto de logística** ni un conjunto suelto de documentos.  
Es la base de trabajo de una aplicación metodológica que busca ayudar a un emprendedor a:

- entender su proyecto con claridad,
- validarlo antes de sobrediseñarlo,
- ordenar su modelo de negocio,
- aterrizar decisiones operativas, legales, comerciales y financieras,
- y consolidar todo en un Plan de Empresa útil para decidir.

La lógica central del sistema es:

**documentar primero, decidir después, y ejecutar con evidencia.**

---

## 2. Qué NO es este repositorio

Este repositorio:

- **no es todavía el producto final empaquetado**;
- **no es una app cerrada lista para producción**;
- **no está centrado exclusivamente en logística**;
- **no debe confundirse con Antigravity**, que aquí se usa como entorno de diseño, ejecución y organización interna.

La logística existe en el repositorio como **caso de prueba principal**, no como definición total del producto.

---

## 3. Qué estamos construyendo

Estamos construyendo un sistema que guía al emprendedor por una secuencia de fases para transformar una idea en una base de negocio más clara, validada y documentada.

Ese sistema combina:

- metodología por fases,
- documentación guiada,
- reglas de control,
- skills y workflows,
- trazabilidad de decisiones,
- validación híbrida (IA + lógica determinista),
- y, cuando aplica, soporte de memoria externa e investigación estructurada.

---

## 4. Principio arquitectónico clave

La arquitectura del repositorio sigue esta regla:

- **`core/`** = lógica general del producto
- **`cases/`** = casos de prueba o validación sectorial
- **`runtime/`** = entorno operativo para Antigravity
- **`research/`** = fuentes, evidencia e investigación
- **`output/`** = trazas, auditorías, migración, validaciones y resultados de trabajo

### Regla madre
El caso logístico **no define el producto**.  
`cases/logistica/` es solo un caso de prueba, igual que mañana podrían existir:

- `cases/carpinteria/`
- `cases/peluqueria/`
- `cases/restaurante/`
- `cases/servicios_profesionales/`

El objetivo del sistema es servir como base para **múltiples tipos de emprendimiento**, no solo logística.

---

## 5. Estructura actual del repositorio

```text
Proyecto_automatizaciones/
│
├── .agent/
│   ├── rules/
│   ├── skills/
│   └── workflows/
│
├── core/
│   ├── fases/
│   ├── dmv/
│   ├── contratos/
│   └── prompts/
│
├── cases/
│   └── logistica/
│       ├── output/
│       ├── evidencias/
│       └── docs/
│
├── research/
│   ├── fuentes/
│   ├── notebooklm/
│   └── evidencia/
│
├── scripts/
│   ├── validadores/
│   └── utilidades/
│
├── output/
│   ├── arquitectura/
│   ├── migracion/
│   ├── validaciones/
│   └── pruebas/
│
├── INDEX_MAESTRO.md
└── README.md

6. Núcleo metodológico (core/)

La carpeta core/ contiene la fuente principal de verdad metodológica del sistema.

core/fases/

Aquí viven las fases oficiales del proyecto.
Estas fases estructuran el avance del emprendedor desde la comprensión inicial de su proyecto hasta la integración final del Plan de Empresa.

core/dmv/

Aquí vive el Documento Maestro Vivo (DMV), que funciona como contrato de datos y memoria estructurada del proyecto.

El DMV permite:

acumular lo aprendido,
mantener coherencia entre fases,
registrar hipótesis, riesgos y decisiones,
y evitar rehacer trabajo innecesariamente.
core/contratos/

Espacio para plantillas, estructuras base y contratos metodológicos que luego puedan ser usados por skills, validadores o futuras capas de software.

core/prompts/

Reservado para prompts oficiales o instrucciones estabilizadas cuando el sistema las requiera como parte formal de la arquitectura.

7. Casos de prueba (cases/)

La carpeta cases/ contiene ejemplos reales o simulados usados para validar si la metodología funciona correctamente en distintos tipos de negocio.

cases/logistica/

Es el caso de prueba actualmente más desarrollado.

Su función es:

probar la robustez de la metodología,
detectar sesgos sectoriales,
evaluar si el sistema genera entregables útiles,
y comprobar si las reglas, fases y validadores se sostienen en un caso con complejidad operativa real.
Importante

Los contenidos dentro de cases/ no definen el producto.
Solo validan su comportamiento en contextos concretos.

8. Runtime de Antigravity (.agent/)

La carpeta .agent/ contiene piezas operativas del entorno de trabajo, como:

rules/
skills/
workflows/

Estas piezas ayudan a ejecutar y mantener el sistema dentro del entorno de Antigravity, pero no deben confundirse con el producto final.

Distinción importante

Antigravity es aquí un entorno de construcción, organización y ejecución.
No es, por sí mismo, la arquitectura final de la app que se quiere construir.

9. Investigación y memoria (research/)

Esta capa existe para organizar mejor la evidencia del proyecto.

Incluye:

fuentes base,
materiales importados,
notas de investigación,
referencias de NotebookLM,
y soporte documental para decisiones estratégicas.
Regla importante

Toda afirmación fuerte de mercado, regulación, competencia o datos externos debe poder trazarse a una fuente concreta.

10. Salidas y trazabilidad (output/)

La carpeta output/ no es el producto.
Es el espacio de trabajo donde quedan:

auditorías,
planes de migración,
verificaciones,
reportes,
y documentación temporal o de control.

Es útil para:

seguir el rastro de cambios,
auditar el proceso,
y evitar perder decisiones tomadas durante el desarrollo del sistema.
11. Estado actual del proyecto

En este momento el repositorio está en una fase de reorganización y consolidación arquitectónica.

Ya se ha avanzado en:
separación entre core/ y cases/;
consolidación del núcleo metodológico;
creación del DMV en su nueva ubicación;
migración de fases al núcleo del sistema;
creación de reglas para evitar sesgo sectorial;
documentación de arquitectura y migración;
aislamiento inicial del caso logístico por copia controlada.
Aún queda por cerrar:
alineación completa de scripts con la nueva arquitectura;
saneamiento final de rutas heredadas;
refinamiento de documentación raíz;
estabilización de validadores;
y, más adelante, aterrizar esta arquitectura en una capa de software más ejecutable.
12. Cómo debe leerse este repositorio

La forma correcta de entender el repositorio es esta:

core/ dice cómo piensa el sistema
cases/ demuestra si eso funciona en un negocio real
.agent/ ayuda a operarlo dentro del entorno
research/ sostiene la evidencia
output/ deja trazabilidad del trabajo
13. Principios de trabajo

Este proyecto se rige por estos principios:

no rehacer sin necesidad;
no mover piezas sensibles sin plan previo;
no mezclar producto con caso de prueba;
no introducir lógica sectorial en el núcleo;
no dar por cerrado algo que sigue en transición;
usar IA para pensar y proponer;
usar validación determinista cuando la exactitud importa;
y documentar los cambios antes de ejecutar transformaciones delicadas.
14. Enfoque del producto

La app que se está diseñando debe ayudar al emprendedor a:

pensar mejor su proyecto,
no saltarse fases críticas,
identificar hipótesis, riesgos y vacíos,
construir documentación útil y ordenada,
y tomar decisiones con más claridad antes de invertir tiempo, dinero o esfuerzo en dirección equivocada.

El valor no está en “usar IA” por sí sola.
El valor está en combinar:

estructura,
criterio,
trazabilidad,
y apoyo real a la toma de decisiones.
15. Nota final

Este repositorio debe evolucionar hacia una arquitectura más clara, portable y mantenible.
Por eso se está separando cuidadosamente:

el método,
los casos,
la evidencia,
el runtime,
y la futura capa de software.

La meta no es tener muchos documentos.
La meta es construir una base sólida para una app que realmente ayude a emprendedores a entender, validar y estructurar mejor sus negocios.