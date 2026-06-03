# SPEC-003 — Especificación de repo_identity.yml

## Estado

Aprobado.

---

# 1. Relación con ADR-001, SPEC-001 y SPEC-002

SPEC-003 forma parte del bloque de gobernanza documental del framework limpio de `Proyecto_automatizaciones`.

## 1.1 Relación con ADR-001

ADR-001 define la decisión arquitectónica principal:

* repositorio madre limpio;
* proyectos vivos independientes;
* reutilización sin contaminación;
* actualización controlada desde framework;
* retención externa;
* separación entre framework, proyecto vivo, candidato extraído y archivo.

SPEC-003 no modifica ADR-001.
SPEC-003 convierte esa decisión en un contrato documental para identificar el rol operativo de un repositorio.

## 1.2 Relación con SPEC-001

SPEC-001 define el contrato de `artifact_manifest.yml`.

`artifact_manifest.yml` responde:

```text
Qué artefactos existen.
Qué categoría tiene cada artefacto.
Qué se copia.
Qué se omite.
Qué se genera vacío.
Qué bloquea.
Qué requiere auditoría.
```

SPEC-003 responde:

```text
Qué tipo de repositorio es este.
Qué rol operativo tiene.
Qué operaciones puede o no puede ejecutar.
Qué datos puede o no puede contener.
Qué restricciones globales aplican antes de interpretar sus artefactos.
```

Regla principal:

```text
repo_identity.yml identifica el repositorio.
artifact_manifest.yml clasifica los artefactos dentro del repositorio.
```

Ambos documentos deben ser coherentes.
Si `repo_identity.yml` y `artifact_manifest.yml` declaran roles incompatibles, cualquier automatización debe bloquearse.

## 1.3 Relación con SPEC-002

SPEC-002 define la estructura física estándar de repositorios y carpetas.

SPEC-002 indica qué carpetas son propias del repositorio madre, del proyecto vivo, de la retención externa o de zonas legacy.

SPEC-003 define qué identidad debe tener el repositorio para que esas carpetas sean válidas.

Ejemplo:

```text
Si repo_role = framework_mother
→ no puede contener memoria viva de caso.

Si repo_role = live_project
→ puede contener inputs, fuentes, DMV, outputs y reportes del proyecto.

Si repo_role = archive_only
→ no debe operar como workspace activo.
```

---

# 2. Propósito

El archivo `repo_identity.yml` es la declaración formal de identidad de un repositorio.

Su propósito es evitar que una herramienta, script, agente o workflow ejecute acciones peligrosas sobre el repositorio equivocado.

Sin `repo_identity.yml`, el sistema no debe asumir si está trabajando sobre:

* el repositorio madre del framework;
* un proyecto vivo;
* una base candidata extraída;
* una retención externa o archivo frío.

## 2.1 Problema que resuelve

Sin identidad explícita, podrían ocurrir errores como:

* limpiar un proyecto vivo pensando que es un temporal;
* copiar memoria viva de un proyecto real hacia el framework;
* tratar un backup como workspace editable;
* usar una base extraída no auditada como si fuera repositorio madre;
* aplicar actualizaciones del framework sobre un archivo congelado;
* ejecutar Plan A o Plan B sin saber el rol real del repositorio.

## 2.2 Regla principal

```text
Ninguna automatización de creación, extracción, limpieza, actualización, regeneración o retención debe ejecutarse si no puede determinar con claridad la identidad del repositorio.
```

---

# 3. Ubicación recomendada

El archivo debe ubicarse en la raíz del repositorio:

```text
repo_identity.yml
```

SPEC-003 define el contrato documental de este archivo.

SPEC-003 no autoriza todavía:

* crear el archivo físico real;
* activar validadores;
* implementar scripts;
* ejecutar Plan A;
* ejecutar Plan B;
* limpiar carpetas;
* migrar `docs_base/`;
* migrar `output/`.

---

# 4. Esquema mínimo v1

Este es el esquema mínimo propuesto para `repo_identity.yml` versión 1.0:

```yaml
identity_version: "1.0"
repo_id: "proyecto_automatizaciones"
repo_name: "Proyecto Automatizaciones"
repo_role: "framework_mother"
repo_status: "active"
repo_owner: "equipo_tecnico"

created_from: null
framework_source: null
framework_version: null

contains_real_data: false

allows_project_creation: true
allows_framework_updates: false
allows_case_data: false
allows_artifact_generation: false
allows_cleanup: false
allows_extraction: false
allows_retention_export: false

requires_human_approval_for:
  - cleanup
  - extraction
  - retention_export
  - role_change
  - manifest_change

notes: "Repositorio madre limpio del framework."
```

## 4.1 Regla sobre el esquema mínimo

Los campos del esquema mínimo v1 se dividen en dos tipos:

```text
obligatorios
contextuales
```

Los campos obligatorios deben existir en todo `repo_identity.yml`.

Los campos contextuales pueden ser `null`, pero deben existir cuando ayudan a conservar trazabilidad.

---

# 5. Campos obligatorios

| Campo                         | Tipo        | Obligatorio | Descripción                                                                                        |
| ----------------------------- | ----------- | ----------: | -------------------------------------------------------------------------------------------------- |
| `identity_version`            | string      |          Sí | Versión del contrato de identidad. Ejemplo: `"1.0"`.                                               |
| `repo_id`                     | string      |          Sí | Identificador único del repositorio dentro del ecosistema gestionado por `Proyecto_automatizaciones`. Debe usar `snake_case` y puede incorporar prefijos de organización, cliente, dominio o propósito para evitar colisiones. |
| `repo_name`                   | string      |          Sí | Nombre legible del repositorio.                                                                    |
| `repo_role`                     | string      |          Sí | Rol operativo del repositorio.                                                                     |
| `repo_status`                 | string      |          Sí | Estado del ciclo de vida del repositorio.                                                          |
| `repo_owner`                  | string      |          Sí | Rol, equipo o persona responsable de aprobar cambios de identidad, rol o permisos del repositorio. |
| `created_from`                | string/null |          Sí | Repositorio o proceso desde el cual fue creado. Puede ser `null` en el repositorio madre original. |
| `framework_source`            | string/null |          Sí | Framework de origen desde el cual recibe estructura o actualizaciones. Puede ser `null`.           |
| `framework_version`           | string/null |          Sí | Versión del framework de origen. Puede ser `null`, pero es obligatorio si `framework_source` no es `null`. |
| `contains_real_data`          | boolean     |          Sí | Indica si el repositorio contiene datos reales o sensibles de un proyecto.                         |
| `allows_project_creation`     | boolean     |          Sí | Indica si el repositorio puede usarse como origen para crear proyectos vivos.                      |
| `allows_framework_updates`    | boolean     |          Sí | Indica si el repositorio puede recibir actualizaciones desde un framework madre.                   |
| `allows_case_data`            | boolean     |          Sí | Indica si el repositorio puede almacenar datos, memoria o artefactos de un caso/proyecto.          |
| `allows_artifact_generation`  | boolean     |          Sí | Indica si el repositorio puede generar artefactos de proyecto, entregables o reportes vivos.       |
| `allows_cleanup`              | boolean     |          Sí | Indica si el repositorio permite operaciones de limpieza controlada.                               |
| `allows_extraction`           | boolean     |          Sí | Indica si el repositorio puede participar en extracción de base limpia mediante Plan B.            |
| `allows_retention_export`     | boolean     |          Sí | Indica si el repositorio puede exportarse a retención externa.                                     |
| `requires_human_approval_for` | list        |          Sí | Lista de operaciones que requieren aprobación humana explícita.                                    |
| `notes`                       | string      |          Sí | Nota breve que explique el propósito o restricción principal del repositorio.                      |

---

# 6. Valores permitidos

## 6.1 Valores permitidos para `repo_role`

```text
framework_mother
live_project
extracted_candidate
archive_only
```

## 6.2 Valores permitidos para `repo_status`

```text
active
paused
frozen
archived
pending_audit
deprecated
```

Definición:

| Valor           | Significado                                                        |
| --------------- | ------------------------------------------------------------------ |
| `active`        | Repositorio en uso operativo.                                      |
| `paused`        | Repositorio temporalmente detenido.                                |
| `frozen`        | Repositorio congelado. No admite cambios sin decisión explícita.   |
| `archived`      | Repositorio archivado o retirado del ciclo operativo.              |
| `pending_audit` | Repositorio pendiente de auditoría antes de asumir rol definitivo. |
| `deprecated`    | Repositorio obsoleto, conservado solo por trazabilidad.            |

## 6.3 Valores permitidos para booleanos

Todos los campos booleanos deben ser estrictamente:

```text
true
false
```

No se permiten valores como:

```text
yes
no
1
0
"true"
"false"
```

## 6.4 Valores permitidos para `requires_human_approval_for`

```text
cleanup
extraction
retention_export
update_from_framework
project_creation
artifact_generation
role_change
manifest_change
destructive_operation
external_provider_use
```

Si una acción no aparece en esta lista, no debe asumirse como permitida.

## 6.5 Regla de aprobación humana auditable

La presencia de una acción en `requires_human_approval_for` no basta por sí sola para considerar aprobada una operación.

Para SPEC-003, una aprobación humana válida debe ser verificable y trazable. Como mínimo, debe dejar evidencia en uno de estos formatos:

1. Registro documental en `changes/`, `reports/official/` o documento equivalente aprobado.
2. Commit o pull request donde conste la decisión y el alcance aprobado.
3. Acta, reporte o manifest de operación con:
   * identificador de aprobación;
   * fecha;
   * persona o rol aprobador;
   * operación aprobada;
   * alcance exacto;
   * archivos o carpetas afectados;
   * motivo;
   * restricciones;
   * evidencia de revisión.

Regla:
```text
Si una operación aparece en `requires_human_approval_for`, ningún script, agente o workflow debe ejecutarla si no existe evidencia verificable de aprobación.
```

Esta regla no implementa todavía el mecanismo técnico de aprobación. Solo define el estándar documental mínimo que deberá respetar una automatización futura.

## 6.6 Invariantes globales para repositorios con datos reales

Cuando un repositorio declare:
```yaml
contains_real_data: true
```

deben cumplirse siempre estas reglas, sin importar el rol:

1. `repo_role` no puede ser `framework_mother`.
2. `allows_extraction` debe ser `false`, salvo excepción futura formalmente documentada y aprobada.
3. `requires_human_approval_for` debe incluir siempre:
   * `destructive_operation`
   * `external_provider_use`
4. Cualquier limpieza, exportación, envío a proveedor externo, retención o migración debe requerir aprobación humana auditable.
5. El repositorio no puede usarse como base limpia reutilizable.
6. Si el repositorio declara `contains_real_data: false`, pero se detectan datos reales, debe bloquearse con `REAL_DATA_CONTRADICTION`.

Regla:
```text
La presencia de datos reales activa protecciones globales, aunque el rol del repositorio permita otras operaciones.
```

---

# 7. Roles de repositorio

SPEC-003 reconoce cuatro roles operativos.

## 7.1 `framework_mother`

Repositorio madre limpio del framework.

Contiene:

* documentación normativa;
* ADRs;
* SPECs;
* runtime reutilizable;
* plantillas;
* ejemplos sintéticos;
* tests;
* scripts generales aprobados.

No contiene:

* datos reales de proyectos;
* memoria viva de casos;
* inputs reales;
* outputs de negocio reales;
* `case_config.yml` de proyecto vivo;
* `origin_manifest.yml` de proyecto vivo;
* `.env` versionado.

## 7.2 `live_project`

Repositorio vivo de un proyecto específico.

Puede contener:

* datos reales del proyecto;
* fuentes;
* inputs;
* DMV;
* outputs;
* reportes;
* versiones;
* decisiones;
* cambios;
* evidencias.

No debe actuar como framework madre.

No debe copiar su memoria viva a otros proyectos.

## 7.3 `extracted_candidate`

Repositorio candidato extraído mediante un proceso de recuperación o limpieza.

Representa una posible base limpia, pero aún no aprobada.

Debe permanecer en estado:

```text
pending_audit
```

hasta que pase controles documentales y técnicos.

No puede actuar como `framework_mother` automáticamente.

## 7.4 `archive_only`

Repositorio o paquete de retención externa.

Contiene evidencia fría, snapshot, backup o entrega cerrada.

No es workspace activo.

No debe recibir actualizaciones desde framework.

No debe ejecutar regeneración, limpieza o edición evolutiva.

---

# 8. Reglas por rol

## 8.1 Reglas para `framework_mother`

Un repositorio con `repo_role: framework_mother` debe cumplir:

```yaml
contains_real_data: false
allows_project_creation: true
allows_framework_updates: false
allows_case_data: false
allows_artifact_generation: false
allows_cleanup: false
allows_extraction: false
allows_retention_export: false
```

Reglas:

1. No puede contener datos reales de proyectos.
2. No puede contener memoria viva de proyectos.
3. No puede contener `case_config.yml`.
4. No puede contener `origin_manifest.yml`.
5. No puede contener `.env` versionado.
6. Puede contener plantillas reutilizables.
7. Puede contener ejemplos sintéticos.
8. Puede ser origen de creación de proyectos vivos mediante Plan A.
9. No debe ejecutarse Plan B sobre él como si fuera una base contaminada.
10. Debe requerir aprobación humana para cambios de rol, cambios de manifiesto y operaciones destructivas.

## 8.2 Reglas para `live_project`

Un repositorio con `repo_role: live_project` normalmente debe cumplir:

```yaml
contains_real_data: true
allows_project_creation: false
allows_framework_updates: true
allows_case_data: true
allows_artifact_generation: true
allows_cleanup: true
allows_extraction: false
allows_retention_export: true
```

Reglas:

1. Puede contener datos reales del proyecto.
2. Puede contener `case_config.yml`.
3. Puede contener `origin_manifest.yml`.
4. Puede recibir actualizaciones controladas desde framework.
5. Puede generar outputs, reportes y entregables del proyecto.
6. Puede exportarse a retención externa.
7. No puede actuar como framework madre.
8. No debe copiar su memoria viva a otros proyectos.
9. No debe activar extracción de base limpia salvo decisión explícita y auditoría previa.
10. Toda limpieza debe ser controlada, trazable y con aprobación humana si afecta datos o outputs.

## 8.3 Reglas para `extracted_candidate`

Un repositorio con `repo_role: extracted_candidate` debe cumplir:

```yaml
repo_status: "pending_audit"
contains_real_data: false
allows_project_creation: false
allows_framework_updates: false
allows_case_data: false
allows_artifact_generation: false
allows_cleanup: false
allows_extraction: false
allows_retention_export: false
```

Reglas:

1. Es una base candidata, no una base aprobada.
2. No puede crear proyectos nuevos.
3. No puede operar como framework madre.
4. No puede recibir datos reales de proyectos.
5. No puede activar automatizaciones de producción.
6. Debe someterse a auditoría antes de cambiar de rol.
7. Solo puede convertirse en `framework_mother` mediante aprobación humana formal y cambio controlado de identidad.

## 8.4 Reglas para `archive_only`

Un repositorio con `repo_role: archive_only` debe cumplir:

```yaml
repo_status: "archived"
allows_project_creation: false
allows_framework_updates: false
allows_artifact_generation: false
allows_cleanup: false
allows_extraction: false
allows_retention_export: false
```

Reglas:

1. No es workspace activo.
2. No debe recibir actualizaciones desde framework.
3. No debe generar nuevos entregables.
4. No debe ejecutar limpieza destructiva.
5. No debe ser fuente para crear proyectos.
6. No debe ser fuente para Plan B.
7. Puede contener datos reales si es snapshot o backup, pero debe tratarse como evidencia fría.
8. Si contiene datos reales, debe marcar `contains_real_data: true`.

---

# 9. Relación con artifact_manifest.yml

## 9.1 Diferencia funcional

`repo_identity.yml` define la identidad global del repositorio.

`artifact_manifest.yml` define la clasificación de artefactos dentro del repositorio.

Ejemplo:

```text
repo_identity.yml:
Este repositorio es un framework madre.

artifact_manifest.yml:
Estos archivos son framework base, plantillas, ejemplos sintéticos o legacy.
```

## 9.2 Coincidencia obligatoria de rol

Si existe `artifact_manifest.yml`, su campo `repo_role` debe coincidir con `repo_identity.yml`.

Ejemplo válido:

```yaml
# repo_identity.yml
repo_role: "framework_mother"

# artifact_manifest.yml
repo_role: "framework_mother"
```

Ejemplo inválido:

```yaml
# repo_identity.yml
repo_role: "live_project"

# artifact_manifest.yml
repo_role: "framework_mother"
```

## 9.3 Regla de bloqueo

Si hay contradicción entre ambos documentos, la automatización debe bloquearse con:

```text
ROLE_MANIFEST_MISMATCH
```

## 9.4 Precedencia de validación

La validación debe ejecutarse en este orden:

1. Validar existencia y estructura de `repo_identity.yml`.
2. Validar el rol y permisos declarados en `repo_identity.yml`.
3. Validar existencia y estructura de `artifact_manifest.yml`, si aplica.
4. Validar coherencia cruzada entre `repo_identity.yml` y `artifact_manifest.yml`.
5. Validar rutas y artefactos según el rol declarado.

Regla:

```text
La identidad del repositorio se valida antes que el manifiesto de artefactos.
```

Motivo:

```text
Primero se debe saber qué tipo de repositorio se está evaluando.
Después se interpretan sus artefactos.
```

---

# 10. Relación con estructura de carpetas

SPEC-003 utiliza las reglas físicas de SPEC-002.

## 10.1 Carpetas incompatibles con `framework_mother`

Un repositorio `framework_mother` no debe contener como estructura viva:

```text
inputs/
sources/ con datos reales
dmv/
output/ con entregables reales
reports/tmp/
reports/official/ de proyectos reales
changes/ de proyecto vivo
versions/ de proyecto vivo
case_config.yml
origin_manifest.yml
```

Puede contener:

```text
docs/
docs/adrs/
docs/specs/
core/
src/
scripts/
templates/
examples/ sintéticos
tests/
```

## 10.2 Carpetas compatibles con `live_project`

Un repositorio `live_project` puede contener:

```text
inputs/
sources/
dmv/
output/
reports/official/
changes/
impact_assessments/
versions/
case_config.yml
origin_manifest.yml
```

`reports/tmp/` puede existir solo como runtime temporal y debe estar ignorado por Git.

## 10.3 Carpetas compatibles con `archive_only`

Un repositorio `archive_only` puede contener:

```text
README_ARCHIVE.md
MANIFEST_FREEZE.md
checksums/
output/
reports/official/
versions/
artifact_manifest.yml
repo_identity.yml
```

No debe operar como workspace activo.

---

# 11. Validaciones obligatorias

Un futuro validador deberá comprobar, como mínimo:

## 11.1 Validaciones de existencia

1. `repo_identity.yml` existe en la raíz cuando una operación lo requiere.
2. El archivo puede parsearse como YAML.
3. El archivo contiene todos los campos obligatorios.
4. No contiene campos críticos vacíos.

## 11.2 Validaciones de rol

1. `repo_role` existe.
2. `repo_role` pertenece a los valores permitidos.
3. `repo_status` pertenece a los valores permitidos.
4. La combinación `repo_role` + `repo_status` es válida.
5. Los permisos `allows_*` son coherentes con el rol.

## 11.3 Validaciones para `framework_mother`

Debe bloquearse si:

1. `contains_real_data: true`.
2. `allows_case_data: true`.
3. `allows_artifact_generation: true` para outputs de proyecto.
4. Existe `case_config.yml`.
5. Existe `origin_manifest.yml`.
6. Existe `.env` versionado.
7. Existen carpetas de proyecto vivo con datos reales.
8. Se intenta ejecutar limpieza destructiva sobre casos reales.
9. Se intenta ejecutar Plan B sobre el framework madre.

## 11.4 Validaciones para `live_project`

Debe bloquearse si:

1. Intenta actuar como framework madre.
2. Intenta crear otros proyectos vivos.
3. Intenta exportar memoria viva a otro proyecto sin retención o anonimización.
4. Intenta modificar documentación normativa del framework sin actualización controlada.
5. Ejecuta limpieza destructiva sin aprobación humana cuando haya datos reales.

## 11.5 Validaciones para `extracted_candidate`

Debe bloquearse si:

1. Tiene `repo_status` distinto de `pending_audit`.
2. Intenta crear proyectos vivos.
3. Intenta operar como `framework_mother`.
4. Contiene datos reales.
5. Declara `allows_project_creation: true`.
6. Declara `allows_artifact_generation: true`.

## 11.6 Validaciones para `archive_only`

Debe bloquearse si:

1. Tiene `repo_status: active`.
2. Declara `allows_framework_updates: true`.
3. Declara `allows_project_creation: true`.
4. Declara `allows_artifact_generation: true`.
5. Declara `allows_cleanup: true`.
6. Declara `allows_extraction: true`.

## 11.7 Validaciones cruzadas

Debe bloquearse si:

1. `repo_identity.yml` y `artifact_manifest.yml` tienen `repo_role` diferente.
2. `artifact_manifest.yml` permite una acción que `repo_identity.yml` prohíbe.
3. `repo_identity.yml` permite una acción pero `artifact_manifest.yml` bloquea los artefactos requeridos.
4. Existen datos reales en un repositorio que declara `contains_real_data: false`.
5. `framework_source` no es `null` pero `framework_version` está vacío o no existe.

---

# 12. Errores bloqueantes

| Código                                   | Motivo                                                                   |
| ---------------------------------------- | ------------------------------------------------------------------------ |
| `MISSING_REPO_IDENTITY`                  | Falta `repo_identity.yml` cuando la operación lo requiere.               |
| `INVALID_REPO_IDENTITY_SCHEMA`           | El archivo no cumple el esquema mínimo.                                  |
| `INVALID_REPO_ROLE`                      | `repo_role` no pertenece a los valores permitidos.                       |
| `INVALID_REPO_STATUS`                    | `repo_status` no pertenece a los valores permitidos.                     |
| `INVALID_ROLE_STATUS_COMBINATION`        | La combinación rol + estado es inválida.                                 |
| `ROLE_MANIFEST_MISMATCH`                 | `repo_identity.yml` y `artifact_manifest.yml` declaran roles diferentes. |
| `FRAMEWORK_CONTAINS_REAL_DATA`           | Un framework madre declara o contiene datos reales.                      |
| `FRAMEWORK_ALLOWS_CASE_DATA`             | Un framework madre permite datos de caso.                                |
| `FRAMEWORK_ALLOWS_PROJECT_OUTPUTS`       | Un framework madre permite generación de outputs de proyecto.            |
| `FORBIDDEN_CASE_CONFIG_IN_FRAMEWORK`     | Existe `case_config.yml` en repositorio madre.                           |
| `FORBIDDEN_ORIGIN_MANIFEST_IN_FRAMEWORK` | Existe `origin_manifest.yml` en repositorio madre.                       |
| `ARCHIVE_MARKED_ACTIVE`                  | Un repositorio `archive_only` aparece como `active`.                     |
| `ARCHIVE_ALLOWS_MUTATION`                | Un archivo frío permite actualización, limpieza o generación.            |
| `EXTRACTED_CANDIDATE_NOT_APPROVED`       | Un candidato extraído intenta operar como framework sin aprobación.      |
| `UNAUTHORIZED_OPERATION_FOR_ROLE`        | La acción solicitada no está permitida para el rol.                      |
| `LOCAL_SECRETS_VERSIONED`                | Se detectan secretos versionados.                                        |
| `REAL_DATA_CONTRADICTION`                | El repositorio contiene datos reales pero declara que no los contiene.   |
| `MISSING_FRAMEWORK_VERSION`              | `framework_source` no es `null` pero `framework_version` está vacío o no existe. |

---

# 13. Ejemplos válidos

Todos los ejemplos de esta sección son completos según el esquema mínimo v1.

## 13.1 `framework_mother`

```yaml
identity_version: "1.0"
repo_id: "proyecto_automatizaciones"
repo_name: "Proyecto Automatizaciones"
repo_role: "framework_mother"
repo_status: "active"
repo_owner: "equipo_tecnico"

created_from: null
framework_source: null
framework_version: null

contains_real_data: false

allows_project_creation: true
allows_framework_updates: false
allows_case_data: false
allows_artifact_generation: false
allows_cleanup: false
allows_extraction: false
allows_retention_export: false

requires_human_approval_for:
  - cleanup
  - extraction
  - retention_export
  - role_change
  - manifest_change

notes: "Repositorio madre limpio del framework."
```

## 13.2 `live_project`

```yaml
identity_version: "1.0"
repo_id: "proyecto_vivo_demo_001"
repo_name: "Proyecto Vivo Demo 001"
repo_role: "live_project"
repo_status: "active"
repo_owner: "responsable_proyecto"

created_from: "proyecto_automatizaciones"
framework_source: "proyecto_automatizaciones"
framework_version: "1.0"

contains_real_data: true

allows_project_creation: false
allows_framework_updates: true
allows_case_data: true
allows_artifact_generation: true
allows_cleanup: true
allows_extraction: false
allows_retention_export: true

requires_human_approval_for:
  - cleanup
  - retention_export
  - update_from_framework
  - destructive_operation
  - external_provider_use

notes: "Repositorio vivo de proyecto demo con datos de caso."
```

## 13.3 `extracted_candidate`

```yaml
identity_version: "1.0"
repo_id: "base_extraida_candidata_001"
repo_name: "Base Extraída Candidata 001"
repo_role: "extracted_candidate"
repo_status: "pending_audit"
repo_owner: "equipo_tecnico"

created_from: "proyecto_vivo_demo_001"
framework_source: "proyecto_automatizaciones"
framework_version: "1.0"

contains_real_data: false

allows_project_creation: false
allows_framework_updates: false
allows_case_data: false
allows_artifact_generation: false
allows_cleanup: false
allows_extraction: false
allows_retention_export: false

requires_human_approval_for:
  - extraction
  - role_change
  - manifest_change

notes: "Base candidata extraída. No puede operar como framework hasta aprobación."
```

## 13.4 `archive_only`

```yaml
identity_version: "1.0"
repo_id: "archivo_proyecto_demo_001"
repo_name: "Archivo Proyecto Demo 001"
repo_role: "archive_only"
repo_status: "archived"
repo_owner: "responsable_proyecto"

created_from: "proyecto_vivo_demo_001"
framework_source: "proyecto_automatizaciones"
framework_version: "1.0"

contains_real_data: true

allows_project_creation: false
allows_framework_updates: false
allows_case_data: false
allows_artifact_generation: false
allows_cleanup: false
allows_extraction: false
allows_retention_export: false

requires_human_approval_for:
  - destructive_operation
  - external_provider_use

notes: "Retención externa de proyecto demo. Evidencia fría no operativa."
```

---

# 14. Ejemplos inválidos

## 14.1 Framework madre con datos reales

```yaml
repo_role: "framework_mother"
contains_real_data: true
```

Motivo:

```text
FRAMEWORK_CONTAINS_REAL_DATA
```

## 14.2 Framework madre permitiendo datos de caso

```yaml
repo_role: "framework_mother"
allows_case_data: true
```

Motivo:

```text
FRAMEWORK_ALLOWS_CASE_DATA
```

## 14.3 Framework madre con generación de outputs de proyecto

```yaml
repo_role: "framework_mother"
allows_artifact_generation: true
```

Motivo:

```text
FRAMEWORK_ALLOWS_PROJECT_OUTPUTS
```

## 14.4 Archive activo

```yaml
repo_role: "archive_only"
repo_status: "active"
```

Motivo:

```text
ARCHIVE_MARKED_ACTIVE
```

## 14.5 Archive editable

```yaml
repo_role: "archive_only"
allows_cleanup: true
allows_artifact_generation: true
```

Motivo:

```text
ARCHIVE_ALLOWS_MUTATION
```

## 14.6 Candidato extraído actuando como framework

```yaml
repo_role: "extracted_candidate"
repo_status: "pending_audit"
allows_project_creation: true
```

Motivo:

```text
EXTRACTED_CANDIDATE_NOT_APPROVED
```

## 14.7 Discrepancia entre identidad y manifiesto

```yaml
# repo_identity.yml
repo_role: "live_project"

# artifact_manifest.yml
repo_role: "framework_mother"
```

Motivo:

```text
ROLE_MANIFEST_MISMATCH
```

---

# 15. Relación con Plan A

Plan A consiste en crear un proyecto vivo nuevo desde el repositorio madre limpio.

## 15.1 Regla de identidad en Plan A

El `repo_identity.yml` del repositorio madre no debe copiarse literalmente al proyecto vivo.

En su lugar, el proceso debe generar una nueva identidad para el repositorio destino.

Ejemplo:

```yaml
repo_role: "live_project"
created_from: "proyecto_automatizaciones"
framework_source: "proyecto_automatizaciones"
framework_version: "1.0"
```

## 15.2 Condiciones mínimas para Plan A

Plan A solo puede ejecutarse si:

1. El repositorio origen tiene `repo_role: framework_mother`.
2. El repositorio origen tiene `contains_real_data: false`.
3. El repositorio origen tiene `allows_project_creation: true`.
4. El repositorio destino no existe o está vacío.
5. El repositorio destino recibe un nuevo `repo_identity.yml`.
6. El repositorio destino queda como `live_project`.
7. El repositorio destino no hereda memoria viva ni outputs de otro proyecto.

---

# 16. Relación con Plan B

Plan B consiste en extraer una base limpia candidata desde un repositorio existente contaminado o evolucionado.

## 16.1 Regla de identidad en Plan B

El resultado de Plan B nunca debe declararse directamente como `framework_mother`.

Debe declararse primero como:

```yaml
repo_role: "extracted_candidate"
repo_status: "pending_audit"
```

## 16.2 Condiciones mínimas para Plan B

Plan B solo puede avanzar si:

1. Existe `repo_identity.yml`.
2. Existe `artifact_manifest.yml`.
3. El manifiesto identifica qué artefactos son copiables.
4. No hay artefactos `LEGACY_OR_CONTAMINATED` entre candidatos de extracción.
5. No hay datos reales en artefactos destinados a la base limpia.
6. El resultado queda como `extracted_candidate`.
7. La promoción a `framework_mother` requiere aprobación humana posterior.

## 16.3 Regla de no promoción automática

```text
Un extracted_candidate no puede convertirse automáticamente en framework_mother.
```

La promoción debe ser una tarea posterior, auditada y aprobada.

---

# 17. Relación con actualización desde framework

Un repositorio solo puede recibir actualizaciones desde framework si cumple:

```yaml
repo_role: "live_project"
allows_framework_updates: true
```

Además:

1. La actualización debe respetar SPEC-001.
2. La actualización debe respetar SPEC-002.
3. No debe sobrescribir memoria viva.
4. No debe sobrescribir inputs reales.
5. No debe sobrescribir outputs del proyecto.
6. No debe modificar datos reales sin aprobación humana.
7. Debe registrar evidencia de qué cambió.

Repositorios que no pueden recibir actualización desde framework:

```text
framework_mother
extracted_candidate
archive_only
```

---

# 18. Relación con retención externa

Una exportación de retención externa debe generar identidad:

```yaml
repo_role: "archive_only"
repo_status: "archived"
```

## 18.1 Reglas de retención externa

1. La retención externa es evidencia fría.
2. No es workspace activo.
3. No debe recibir actualizaciones desde framework.
4. No debe ejecutar regeneración.
5. No debe ejecutar limpieza destructiva.
6. No debe crear proyectos.
7. Puede contener datos reales si representa snapshot o backup.
8. Si contiene datos reales, debe declararlo con `contains_real_data: true`.

---

# 19. Criterios de aceptación

SPEC-003 será aceptable si cumple:

1. Define claramente qué es `repo_identity.yml`.
2. Define claramente para qué sirve.
3. Define su ubicación en la raíz del repositorio.
4. Define roles de repositorio permitidos.
5. Define campos obligatorios completos.
6. Define valores permitidos.
7. Define reglas por rol.
8. Distingue `allows_project_creation` de `allows_extraction`.
9. No permite que `framework_mother` contenga datos reales.
10. No permite que `framework_mother` almacene datos de caso.
11. No permite que `archive_only` actúe como workspace activo.
12. No permite que `extracted_candidate` opere como framework sin aprobación.
13. Define la relación con `artifact_manifest.yml`.
14. Define la precedencia de validación.
15. Define validaciones obligatorias.
16. Define errores bloqueantes.
17. Incluye ejemplos válidos completos.
18. Incluye ejemplos inválidos.
19. No crea `repo_identity.yml` real.
20. No crea `artifact_manifest.yml`.
21. No implementa scripts.
22. No implementa validadores.
23. No ejecuta Plan A.
24. No ejecuta Plan B.
25. No limpia ni migra `docs_base/`.
26. No limpia ni migra `output/`.

---

# 20. Fuera de alcance

SPEC-003 no implementa:

* `repo_identity.yml` real;
* `artifact_manifest.yml` real;
* scripts;
* validadores;
* CLI;
* Plan A;
* Plan B;
* actualización desde framework;
* retención externa real;
* limpieza física de carpetas;
* migración de `docs_base/`;
* migración de `output/`;
* ADR-002;
* reglas de cambios internos del proyecto vivo;
* regeneración documental;
* políticas de pivote.

SPEC-003 tampoco decide todavía:

* cuándo se creará físicamente `repo_identity.yml`;
* si el primer `repo_identity.yml` se creará antes o junto con `artifact_manifest.yml`;
* cómo se implementará el validador;
* cómo se hará la promoción de `extracted_candidate` a `framework_mother`;
* qué hacer con los pendientes locales `docs_base/` y `output/`.

---

# 21. Decisiones pendientes

## 21.1 Prioridad inmediata

1. Auditar y aprobar SPEC-003.
2. Definir cuándo se creará físicamente `repo_identity.yml`.
3. Definir si `repo_identity.yml` se crea antes o junto con `artifact_manifest.yml`.

## 21.2 Pendientes posteriores

1. Crear `artifact_manifest.yml` real.
2. Implementar validador de identidad y manifiesto.
3. Definir procedimiento de promoción de `extracted_candidate` a `framework_mother`.
4. Definir política operativa de retención externa.
5. Definir política de migración o descarte de `docs_base/`.
6. Definir política de migración o descarte de `output/`.
