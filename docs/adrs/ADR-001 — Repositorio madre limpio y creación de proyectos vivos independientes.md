# ADR-001 — Repositorio madre limpio y creación de proyectos vivos independientes

## Estado

Aprobado.

Este ADR queda aprobado como decisión arquitectónica para definir el repositorio madre limpio, la creación de proyectos vivos independientes, la actualización controlada desde framework, la retención externa y las reglas de reutilización sin contaminación. Su implementación técnica queda pendiente para una especificación posterior.

## Contexto

`Proyecto_automatizaciones` debe funcionar como un sistema reutilizable para crear y operar proyectos agénticos. En este caso inicial, el sistema se está aplicando a planes de negocio, pero la arquitectura debe servir también para otros sistemas agénticos futuros.

El problema detectado es que un repositorio usado para desarrollar un caso real puede contaminarse con información específica del proyecto: outputs, fuentes, DMV, reportes, documentos generados, decisiones de negocio, memoria externa, hipótesis, cambios, versiones y material histórico.

Si esa información queda mezclada con el framework base, el sistema deja de ser reutilizable. Al crear un nuevo proyecto, podría arrastrar datos, reglas, prompts, fuentes o decisiones de un proyecto anterior.

También se identificó que cada plan de negocio o proyecto real debe seguir vivo durante meses o años. Por tanto, no debe tratarse como un archivo muerto. Puede tener versiones, hitos, entregas y backups, pero el repositorio del proyecto debe seguir siendo editable y evolutivo.

Este ADR resuelve únicamente el primer problema: cómo crear proyectos limpios e independientes desde una base madre reutilizable.

La gestión de cambios internos dentro de un proyecto vivo, como feedback, pivotes, reapertura de fases, regeneración documental y control de no-maquillaje, queda fuera de este ADR y se tratará en ADR-002.

## Decisión

Se adopta el modelo de **Repositorio Madre Seguro + Proyecto Vivo Independiente**.

`Proyecto_automatizaciones` tendrá un repositorio madre limpio, protegido y reutilizable. Este repositorio funcionará como framework base para crear nuevos proyectos agénticos.

Cada proyecto real creado desde el framework madre vivirá en su propio repositorio independiente.

Nunca debe existir más de un proyecto real dentro del mismo repositorio.

El repositorio madre no se usará para trabajar casos reales. Solo contendrá la base del sistema, configuración general, reglas, scripts, plantillas, documentación técnica y ejemplos sintéticos mínimos.

Cada proyecto vivo tendrá identidad propia, DMV propio, entradas propias, outputs propios, reportes propios, cambios propios y versiones propias.

La reutilización no se basará en borrar manualmente contaminación, sino en crear nuevas instancias limpias desde una base aprobada y clasificada.

### Definiciones operativas

Para este ADR se aplican las siguientes definiciones:

**Repositorio madre:** repositorio limpio, protegido y reutilizable que contiene el framework base del sistema. No contiene proyectos reales ni información específica de un caso.

**Proyecto real:** repositorio vivo e independiente que contiene identidad propia, DMV, entradas del usuario, fuentes, decisiones, outputs, reportes, cambios, versiones o evidencias asociadas a un caso concreto.

**Artefacto de framework:** elemento reutilizable del sistema base, como código, reglas generales, plantillas, validadores, documentación técnica, tests, scripts o workflows generales. No debe contener datos, fuentes, decisiones ni documentos generados de un proyecto real.

**Proyecto vivo:** proyecto real que sigue siendo editable, versionable y evolutivo. Puede recibir cambios, mejoras, feedback, pivotes y nuevas versiones durante meses o años.

**Retención externa:** conservación fuera del repositorio activo de snapshots, backups, entregas publicadas o paquetes de evidencia. La retención externa no convierte el proyecto vivo en proyecto muerto.

## Reglas obligatorias

### 1. Repositorio madre limpio

El repositorio madre debe contener únicamente componentes reutilizables del sistema.

Puede contener:

* código base del framework;
* core metodológico;
* scripts generales;
* tests generales;
* documentación de gobernanza;
* documentación técnica;
* reglas generales;
* skills generales;
* workflows generales;
* plantillas vacías;
* ejemplos sintéticos mínimos.

No puede contener:

* proyectos reales;
* planes de negocio reales;
* outputs de casos reales;
* DMV de casos reales;
* fuentes aportadas por usuarios;
* reportes de un proyecto real;
* cambios o pivotes de un proyecto real;
* documentos finales de un caso real;
* memoria externa contaminada;
* secretos, claves o archivos locales sensibles.

### 2. Repositorio madre protegido

El repositorio madre debe tener una identidad explícita que advierta que es el framework base.

Debe existir un mecanismo de confirmación antes de permitir cambios estructurales sobre él.

El objetivo de esta confirmación no es seguridad criptográfica, sino prevenir errores humanos o de agentes automáticos.

#### Protección mínima obligatoria

El repositorio madre debe contar, como mínimo, con cuatro capas de protección:

1. Un archivo de identidad del repositorio, por ejemplo `repo_identity.yml`, que declare explícitamente que el repositorio es de tipo `framework_madre`.
2. Una confirmación explícita antes de realizar cambios estructurales sobre el framework.
3. Una protección externa en GitHub, mediante Branch Protection o Rulesets sobre la rama principal.
4. Una regla documental que prohíba trabajar proyectos reales dentro del repositorio madre.

Estas protecciones no buscan impedir todo cambio. El repositorio madre sí puede evolucionar, pero solo mediante mejoras generales del sistema, nunca mediante contenido específico de un proyecto real.

Ejemplo conceptual de confirmación:

```text
Este es el REPOSITORIO MADRE del framework.

No debe usarse para trabajar proyectos reales.

Solo se permite editarlo para mejorar el sistema base.

Para continuar, confirma explícitamente que estás modificando el framework y no un proyecto vivo.
```

Toda modificación al repositorio madre debe responder a una mejora general del sistema, no a una necesidad específica de un caso real.

### 3. Un proyecto real por repositorio

Cada plan de negocio o proyecto real debe tener su propio repositorio independiente.

Ejemplos:

```text
plan_negocio_logistica/
plan_negocio_carpinteria/
plan_negocio_panaderia_don_jaime/
```

No se permite almacenar varios proyectos reales dentro del mismo repositorio.

Esta regla evita contaminación, crecimiento excesivo del repositorio, confusión de contexto y reutilización accidental de información de un caso anterior.

### 4. Proyecto vivo, no proyecto muerto

Un proyecto creado desde el repositorio madre es un repositorio vivo.

Puede cambiar, evolucionar, recibir feedback, pivotar, generar nuevas versiones y actualizar sus documentos.

El proyecto vivo no se envía a un archivo muerto. El repositorio del proyecto sigue siendo editable y evolutivo mientras el proyecto tenga vida.

Lo que sí puede conservarse fuera o dentro del repositorio son snapshots, backups, entregas publicadas, paquetes de evidencia o versiones concretas del proyecto.

El término “archivo frío” no debe usarse como destino principal del proyecto vivo.

Ejemplos:

```text
versions/
  v0_1_diagnostico_inicial/
  v0_2_entrega_banco/
  v0_3_post_feedback_jurado/
```

El repositorio del proyecto sigue vivo aunque una versión específica quede registrada como hito.

#### Retención externa sin desactivar el proyecto vivo

El repositorio del proyecto real sigue siendo el espacio vivo, editable y evolutivo del plan de negocio o sistema agéntico derivado.

Sin embargo, para mantener el repositorio lean y evitar acumulación innecesaria de históricos pesados, se permite conservar fuera del repositorio activo ciertos estados concretos del proyecto.

Esta retención externa no reemplaza el repositorio vivo, no desactiva el proyecto y no convierte el proyecto en un archivo muerto.

La retención externa puede incluir:

* snapshots del proyecto;
* backups completos o parciales;
* entregas publicadas;
* paquetes de evidencia;
* versiones exportadas para banco, jurado, cliente, auditoría o revisión externa;
* manifiestos de estado;
* reportes finales asociados a una entrega concreta.

La retención externa no debe incluir:

* secretos;
* `.env` con credenciales reales;
* `.venv`;
* cachés;
* temporales;
* archivos locales no trazables;
* artefactos no clasificados por el manifiesto;
* material que no pueda auditarse.

Regla obligatoria:

```text
El proyecto vive en su repositorio.
Las versiones e hitos pueden vivir dentro del proyecto.
Los backups, snapshots y paquetes de evidencia pueden vivir fuera.
Nada de eso convierte el proyecto en muerto.
```

### 5. Taxonomía obligatoria de artefactos

Todo archivo o carpeta relevante debe clasificarse por ciclo de vida.

La decisión de copiar, inicializar, regenerar, bloquear o excluir un artefacto no debe depender solo del nombre de la carpeta, sino de su categoría.

Categorías base:

| Categoría                | Descripción                                           | Se copia a nuevo proyecto | Puede contener datos reales | Puede actualizarse desde framework |
| ------------------------ | ----------------------------------------------------- | ------------------------: | --------------------------: | ---------------------------------: |
| `FRAMEWORK_BASE`         | Código, core, scripts, tests, dependencias base       |                        Sí |                          No |                                 Sí |
| `FRAMEWORK_CONFIG`       | Reglas, skills, workflows y configuración general     |                        Sí |                          No |                                 Sí |
| `TEMPLATE_CASE`          | Plantillas vacías para crear nuevos casos             |                        Sí |                          No |                                 Sí |
| `PROJECT_IDENTITY`       | Identidad del nuevo proyecto                          |           Se genera nueva |                          Sí |                                 No |
| `USER_INPUT`             | Información aportada por el usuario                   |                        No |                          Sí |                                 No |
| `PROJECT_MEMORY`         | DMV, decisiones, conocimiento vivo del proyecto       |                        No |                          Sí |                                 No |
| `AGENT_GENERATED_OUTPUT` | Documentos y salidas generadas por el sistema         |                        No |                          Sí |                                 No |
| `PROJECT_REPORTS`        | Auditorías, validaciones y reportes del caso          |                        No |                          Sí |                                 No |
| `PROJECT_CHANGES`        | Feedback, solicitudes de cambio y pivotes             |                        No |                          Sí |                                 No |
| `PROJECT_VERSIONS`       | Hitos y versiones internas del proyecto vivo          |                        No |                          Sí |                                 No |
| `TEMP_RUNTIME`           | Cachés, temporales y archivos técnicos descartables   |                        No |                          No |                                 No |
| `LOCAL_SECRETS`          | `.env`, claves, tokens y configuración local sensible |                        No |         Sí, pero solo local |                                 No |
| `LEGACY_OR_CONTAMINATED` | Material heredado, dudoso o no clasificado            |                        No |              Puede contener |                                 No |
| `SYNTHETIC_EXAMPLES`     | Ejemplos falsos, mínimos y seguros                    |                  Opcional |                          No |                                 No |

Regla madre:

```text
No se copia por nombre de carpeta.
Se copia por categoría aprobada.
```

#### Contrato operativo por categoría

Cada categoría de artefacto debe tener consecuencias operativas explícitas. No basta con nombrar la categoría.

Para cada categoría se debe definir, como mínimo:

* si se copia al crear un nuevo proyecto;
* si se genera vacía;
* si puede contener datos reales;
* si puede vivir dentro del repositorio madre;
* si puede actualizarse desde el framework madre;
* si puede regenerarse automáticamente;
* si requiere auditoría previa;
* quién es responsable de modificarla.

Esta regla evita que la taxonomía se convierta en una lista descriptiva sin efecto práctico.

### 6. Manifiesto único de taxonomía

Debe existir un manifiesto único que actúe como fuente de verdad para clasificar artefactos del repositorio.

Nombre conceptual sugerido:

```text
artifact_manifest.yml
```

Este manifiesto debe existir antes de implementar cualquier generador, extractor, limpieza automática o actualización desde framework.

#### Esquema mínimo v1 del `artifact_manifest.yml`

El `artifact_manifest.yml` debe tener un esquema mínimo obligatorio. Este esquema no implementa la automatización, pero sí define el contrato que cualquier generador, extractor, limpiador o actualizador deberá respetar.

Campos obligatorios por entrada:

```yaml
path:
category:
copy_policy:
allowed_in_framework:
contains_real_data:
can_update_from_framework:
requires_audit:
can_regenerate:
owner:
notes:
```

Valores permitidos para `copy_policy`:

```text
copy
skip
generate_empty
regenerate
ask_before_copy
```

Reglas mínimas del esquema v1:

* `path` identifica una ruta o patrón de ruta dentro del repositorio.
* `category` debe usar una categoría aprobada por este ADR.
* `copy_policy` define si el artefacto se copia, se omite, se genera vacío, se regenera o requiere confirmación.
* `allowed_in_framework` indica si la ruta puede existir dentro del repositorio madre.
* `contains_real_data` indica si puede contener información real de un proyecto.
* `can_update_from_framework` indica si puede recibir cambios desde el framework madre.
* `requires_audit` indica si requiere revisión antes de copiar, extraer, actualizar o regenerar.
* `can_regenerate` indica si el artefacto puede volver a generarse por el sistema.
* `owner` indica el responsable lógico de la categoría.
* `notes` permite documentar restricciones o aclaraciones.

Ejemplo conceptual para una ruta de framework:

```yaml
- path: "src/"
  category: "FRAMEWORK_BASE"
  copy_policy: "copy"
  allowed_in_framework: true
  contains_real_data: false
  can_update_from_framework: true
  requires_audit: false
  can_regenerate: false
  owner: "equipo_tecnico"
  notes: "Código base reutilizable del sistema."
```

Ejemplo conceptual para memoria viva del proyecto:

```yaml
- path: "dmv/"
  category: "PROJECT_MEMORY"
  copy_policy: "generate_empty"
  allowed_in_framework: false
  contains_real_data: true
  can_update_from_framework: false
  requires_audit: true
  can_regenerate: false
  owner: "proyecto_vivo"
  notes: "Memoria viva del caso. Nunca se copia desde otro proyecto ni se sobrescribe desde framework."
```

Regla obligatoria:

```text
Sin `artifact_manifest.yml` aprobado con esquema mínimo v1, queda prohibido implementar scripts de creación, limpieza, extracción, regeneración o actualización.
```

### 7. Plan A — Crear proyecto desde repositorio madre

La ruta principal para crear un proyecto nuevo será partir del repositorio madre limpio.

Flujo conceptual:

```text
Repositorio Madre Seguro
→ crear nuevo proyecto
→ generar identidad del proyecto
→ inicializar estructura viva
→ crear DMV inicial vacío
→ generar origin_manifest
→ dejar repositorio listo para trabajar
```

El nuevo proyecto debe registrar su origen.

Ejemplo conceptual:

```yaml
framework_source: proyecto_automatizaciones_framework
framework_version: v0.1
project_name: panaderia_don_jaime
created_at: 2026-06-03
repo_type: proyecto_vivo
```

### 8. Plan B — Extraer base limpia desde repositorio existente

Además del repositorio madre, debe existir una ruta alternativa para reconstruir una base limpia desde un repositorio existente.

Esta ruta es excepcional y debe usarse cuando:

* el repositorio madre no existe;
* el repositorio madre quedó obsoleto;
* se necesita rescatar una arquitectura útil desde un proyecto terminado;
* un proyecto derivado contiene mejoras estructurales que podrían convertirse en base general.

El extractor no debe copiar todo y limpiar después.

Debe copiar únicamente lo clasificado como base reutilizable.

Debe excluir outputs, DMV, inputs, fuentes, reportes, versiones, cambios, secretos, temporales y material contaminado.

Debe generar un reporte de extracción.

#### Gate: `gate_base_extraible_limpia`

El Plan B solo puede ejecutarse si supera el gate `gate_base_extraible_limpia`.

Este gate tiene resultado binario:

```text
PASS
FAIL
```

Si el gate devuelve `FAIL`, queda prohibido extraer la base limpia desde el repositorio existente.

##### Checklist mínimo del gate

El gate solo puede devolver `PASS` si confirma todos estos puntos:

* existe `artifact_manifest.yml` aprobado;
* todos los artefactos candidatos a extracción están clasificados en el manifiesto;
* solo se extraen artefactos `FRAMEWORK_BASE`, `FRAMEWORK_CONFIG` o `TEMPLATE_CASE`, salvo excepción documentada;
* no se extraen DMV reales;
* no se extraen outputs reales;
* no se extraen inputs de usuario;
* no se extraen fuentes reales;
* no se extraen reportes propios de un caso;
* no se extraen cambios, pivotes o feedback de un proyecto real;
* no se extraen versiones internas del proyecto vivo;
* no se extraen secretos ni configuraciones locales;
* no se extraen temporales, cachés ni entornos virtuales;
* no se extraen reglas, prompts, skills o workflows contaminados por un sector o caso específico;
* la extracción genera un reporte de aprobación o bloqueo.

##### Criterio de bloqueo

Si cualquiera de los puntos del checklist falla, el gate devuelve `FAIL` y la extracción queda bloqueada.

El Plan B no puede operar bajo criterio informal, intuición del agente o limpieza posterior. Solo puede operar sobre artefactos clasificados, auditados y permitidos.

### 9. Actualización futura desde framework madre

Se adopta como decisión arquitectónica que los proyectos vivos podrán recibir actualizaciones controladas desde el framework madre.

Esta actualización solo podrá afectar artefactos clasificados como `FRAMEWORK_BASE`, `FRAMEWORK_CONFIG` y `TEMPLATE_CASE`.

Queda prohibido que una actualización desde el framework madre sobrescriba, sustituya o regenere directamente artefactos clasificados como `PROJECT_IDENTITY`, `USER_INPUT`, `PROJECT_MEMORY`, `PROJECT_CHANGES`, `AGENT_GENERATED_OUTPUT`, `PROJECT_REPORTS`, `PROJECT_VERSIONS`, `LOCAL_SECRETS` o cualquier material marcado como `LEGACY_OR_CONTAMINATED`.

Copier queda como herramienta candidata principal para evaluar esta capacidad de actualización controlada. GitHub Template queda como opción simple o complementaria para creación inicial. El extractor Python propio queda como plan B de recuperación, no como mecanismo principal.

La herramienta final para actualización desde framework madre se decidirá en la especificación técnica derivada de este ADR, antes de implementar cualquier flujo real de actualización.

Hasta ese hito, Copier queda como candidata principal porque se alinea mejor con actualizaciones controladas desde una plantilla versionada. GitHub Template queda como opción simple o complementaria para creación inicial. El extractor Python queda reservado como Plan B de recuperación desde repositorios existentes.

## Consecuencias

### Consecuencias positivas

* El framework madre se mantiene limpio.
* Cada proyecto real tiene identidad propia.
* Se evita mezclar varios planes de negocio en un mismo repositorio.
* Se reduce la contaminación entre proyectos.
* El sistema puede reutilizarse en otros dominios agénticos, no solo planes de negocio.
* La taxonomía permite decidir qué se copia y qué no con criterios claros.
* El manifiesto único evita depender de memoria humana.
* Se define la actualización controlada desde el framework madre como capacidad arquitectónica prevista.
* Se mantiene la naturaleza viva de cada proyecto creado.

### Consecuencias negativas o costes

* Exige disciplina documental.
* Requiere mantener un manifiesto de artefactos.
* Requiere separar con claridad framework y proyecto vivo.
* Puede exigir trabajo adicional para proteger el repositorio madre.
* Si se usa Copier u otra herramienta similar, habrá que aprender y mantener su flujo.
* Si no se clasifica bien, el extractor de base limpia puede copiar contaminación.

### Riesgos

* Que el equipo técnico empiece a implementar scripts antes de cerrar el manifiesto.
* Que se copie información de un caso real al framework madre.
* Que se use un proyecto real como plantilla sin auditoría previa.
* Que se confunda backup o snapshot con “proyecto muerto”.
* Que una actualización del framework sobrescriba memoria viva del proyecto.

#### Mitigaciones mínimas

| Riesgo                                                                | Mitigación mínima                                                                                                                                       |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Implementar scripts antes de cerrar el manifiesto                     | Queda prohibido crear generadores, extractores, limpiadores, regeneradores o actualizadores sin `artifact_manifest.yml` aprobado con esquema mínimo v1. |
| Extraer una base desde repositorio contaminado                        | El Plan B solo puede ejecutarse si `gate_base_extraible_limpia` devuelve `PASS`.                                                                        |
| Interpretar el manifiesto de forma distinta por cada persona o agente | El `artifact_manifest.yml` debe tener esquema mínimo v1 con campos obligatorios y valores permitidos para `copy_policy`.                                |
| Sobrescribir memoria viva al actualizar desde framework               | Las categorías de proyecto vivo deben tener `can_update_from_framework: false`.                                                                         |
| Confundir retención externa con proyecto muerto                       | El ADR debe mantener que el proyecto vivo permanece editable en su propio repositorio; solo se exportan snapshots, backups o paquetes de evidencia.     |
| Contaminar el framework con contenido de un caso real   | Todo cambio al repositorio madre debe pasar por revisión de categoría y confirmar que no introduce artefactos de proyecto vivo.                                                    |
| Editar el repositorio madre por accidente               | El repositorio madre debe tener `repo_identity.yml`, confirmación explícita y protección externa en GitHub.                                                                        |
| El repositorio del proyecto vivo se vuelve pesado por acumulación de históricos | Definir retención externa para snapshots, backups, entregas publicadas y paquetes de evidencia, sin convertir el proyecto vivo en proyecto muerto. |

## Fuera de alcance

Este ADR no define todavía cómo se gestionan cambios internos dentro de un proyecto vivo.

Queda fuera:

* feedback de banco, jurado o cliente;
* solicitudes de cambio;
* evaluación de impacto;
* reapertura de fases;
* regeneración documental;
* control de no-maquillaje;
* cambios menores, parciales, críticos o invalidantes;
* política de baseline dentro del proyecto vivo.

Ese problema será tratado en:

```text
ADR-002 — Gestión de cambios, pivotes y regeneración dentro de un proyecto vivo
```

La retención externa definida en este ADR no resuelve cambios internos, pivotes, reapertura de fases ni regeneración documental. Esos temas corresponden al ADR-002.

## Criterio de aceptación del ADR-001

Este ADR se considera aceptado cuando queden aprobadas estas reglas:

* existe un repositorio madre limpio y protegido;
* cada proyecto real vive en su propio repositorio independiente;
* nunca habrá más de un proyecto real dentro del mismo repositorio;
* existe decisión explícita de permitir actualización controlada desde framework madre;
* Copier queda como herramienta candidata principal;
* GitHub Template queda como opción simple o complementaria;
* extractor Python queda como Plan B;
* existe protección mínima del repositorio madre;
* existe exigencia de `artifact_manifest.yml`;
* existe contrato operativo por categoría;
* existe `gate_base_extraible_limpia` para Plan B;
* se prohíbe implementar scripts antes del manifiesto aprobado;
* se corrige la idea de archivo frío: el proyecto vivo no se manda a un archivo muerto;
* ADR-002 queda explícitamente fuera de alcance;
* existe esquema mínimo v1 del `artifact_manifest.yml`;
* el `artifact_manifest.yml` define campos obligatorios y valores permitidos para `copy_policy`;
* la taxonomía indica si una categoría puede actualizarse desde framework;
* existe gate formal `gate_base_extraible_limpia`;
* el gate `gate_base_extraible_limpia` tiene resultado `PASS` / `FAIL`;
* el gate `gate_base_extraible_limpia` tiene checklist mínimo;
* si el gate falla, el Plan B queda bloqueado;
* la herramienta final para updates se decidirá en especificación técnica posterior antes de implementar actualización real;
* Copier queda como candidata principal para updates controlados desde framework;
* la retención externa queda separada del concepto de proyecto muerto.
