# SPEC-001 — Especificación del `artifact_manifest.yml`

## Estado

Aprobado.

## Relación con ADR-001

Esta especificación deriva de ADR-001 — Repositorio madre limpio y creación de proyectos vivos independientes.

ADR-001 ya define la decisión arquitectónica principal:

* existe un repositorio madre limpio;
* cada proyecto real vive en un repositorio independiente;
* el repositorio madre no debe contener proyectos reales;
* la reutilización no se basa en borrar contaminación manualmente, sino en crear instancias limpias desde una base aprobada;
* todo artefacto relevante debe clasificarse por ciclo de vida;
* `artifact_manifest.yml` será la fuente de verdad para clasificar artefactos;
* sin manifiesto aprobado queda prohibido implementar scripts de creación, limpieza, extracción, regeneración o actualización.

SPEC-001 no modifica ADR-001. Solo desarrolla el contrato técnico-documental del manifiesto.

---

# 1. Propósito del `artifact_manifest.yml`

El `artifact_manifest.yml` es el contrato que clasifica los archivos y carpetas relevantes del repositorio según su ciclo de vida.

Su propósito es evitar que agentes, scripts o personas decidan informalmente qué copiar, excluir, regenerar o actualizar.

El manifiesto debe responder, para cada ruta relevante:

* qué tipo de artefacto es;
* si pertenece al framework;
* si puede existir en el repositorio madre;
* si puede copiarse a un proyecto nuevo;
* si debe generarse vacío;
* si puede contener datos reales;
* si puede actualizarse desde el framework;
* si puede regenerarse automáticamente;
* si requiere auditoría;
* quién es responsable de modificarlo.

Regla central:

```text
No se copia por nombre de carpeta.
Se copia por categoría aprobada.
```

---

# 2. Ubicación recomendada

## 2.1 Ubicación principal

El manifiesto debe ubicarse en la raíz del repositorio:

```text
artifact_manifest.yml
```

Motivo:

* debe ser visible para humanos y agentes;
* debe poder leerse antes de ejecutar cualquier script;
* debe actuar como contrato de gobierno del repositorio completo;
* debe estar versionado junto con el framework.

## 2.2 Ubicaciones no recomendadas

No debe ubicarse en:

```text
core/artifact_manifest.yml
```

porque el manifiesto gobierna todo el repositorio, no solo el core.

No debe ubicarse en:

```text
scripts/artifact_manifest.yml
```

porque no es una herramienta, sino un contrato.

No debe ubicarse en:

```text
output/artifact_manifest.yml
```

porque `output/` puede ser una zona generada o histórica, no una fuente normativa.

---

# 3. Esquema mínimo v1

El manifiesto debe tener una versión explícita y una lista de artefactos.

Esquema mínimo:

```yaml
manifest_version: "1.0"
manifest_status: "draft"
adr_source: "ADR-001"
spec_source: "SPEC-001"
repo_role: "framework_mother"

artifacts:
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

---

# 4. Campos obligatorios

## 4.1 Campos raíz obligatorios

| Campo              |   Tipo | Obligatorio | Descripción                         |
| ------------------ | -----: | ----------: | ----------------------------------- |
| `manifest_version` | string |          Sí | Versión del esquema del manifiesto. |
| `manifest_status`  | string |          Sí | Estado del manifiesto.              |
| `adr_source`       | string |          Sí | ADR que origina el contrato.        |
| `spec_source`      | string |          Sí | SPEC que define el contrato.        |
| `repo_role`        | string |          Sí | Rol del repositorio.                |
| `artifacts`        |   list |          Sí | Lista de entradas de artefactos.    |

## 4.2 Campos obligatorios por artefacto

Cada entrada dentro de `artifacts` debe incluir:

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

## 4.3 Descripción de campos por artefacto

| Campo                       |    Tipo | Descripción                                                                   |
| --------------------------- | ------: | ----------------------------------------------------------------------------- |
| `path`                      |  string | Ruta o patrón de ruta dentro del repositorio.                                 |
| `category`                  |  string | Categoría aprobada del artefacto.                                             |
| `copy_policy`               |  string | Acción permitida al crear o extraer una base.                                 |
| `allowed_in_framework`      | boolean | Indica si la ruta puede existir en el repositorio madre.                      |
| `contains_real_data`        | boolean | Indica si puede contener datos reales de un proyecto.                         |
| `can_update_from_framework` | boolean | Indica si puede recibir actualizaciones desde el framework madre.             |
| `requires_audit`            | boolean | Indica si requiere revisión antes de copiar, extraer, actualizar o regenerar. |
| `can_regenerate`            | boolean | Indica si el sistema puede regenerarlo.                                       |
| `owner`                     |  string | Responsable lógico del artefacto.                                             |
| `notes`                     |  string | Restricciones, aclaraciones o motivo de la clasificación.                     |

---

# 5. Valores permitidos

## 5.1 `manifest_status`

Valores permitidos:

```text
draft
approved
deprecated
```

Reglas:

* `draft`: puede usarse para auditoría, pero no habilita automatización destructiva.
* `approved`: permite que scripts futuros lo usen como contrato.
* `deprecated`: indica que el manifiesto ya no debe usarse como contrato activo.

## 5.2 `repo_role`

Valores permitidos:

```text
framework_mother
live_project
extracted_candidate
archive_only
```

Definiciones:

* `framework_mother`: repositorio madre limpio.
* `live_project`: repositorio de proyecto vivo independiente.
* `extracted_candidate`: repositorio existente desde el cual se intenta extraer base limpia por Plan B.
* `archive_only`: paquete, snapshot o backup inmutable de retención externa, de carácter no operativo e histórico. Este rol se asigna únicamente a archivos comprimidos o repositorios de respaldo que sirven como evidencia fría, distinguiéndose de proyectos reales terminados, pausados o vivos, que permanecen editables en su respectivo espacio de trabajo activo.

## 5.3 `copy_policy`

Valores permitidos:

```text
copy
skip
generate_empty
regenerate
ask_before_copy
```

Definiciones:

* `copy`: se copia tal como está.
* `skip`: no se copia.
* `generate_empty`: se crea una estructura o archivo vacío equivalente.
* `regenerate`: se vuelve a generar mediante proceso controlado.
* `ask_before_copy`: requiere confirmación humana antes de copiar.

## 5.4 `owner`

Valores recomendados:

```text
equipo_tecnico
equipo_gobernanza
equipo_negocio
equipo_documentacion
proyecto_vivo
usuario
sistema
```

---

# 6. Categorías válidas

Las categorías válidas en v1 son:

```text
FRAMEWORK_BASE
FRAMEWORK_CONFIG
TEMPLATE_CASE
PROJECT_IDENTITY
USER_INPUT
PROJECT_MEMORY
AGENT_GENERATED_OUTPUT
PROJECT_REPORTS
PROJECT_CHANGES
PROJECT_VERSIONS
TEMP_RUNTIME
LOCAL_SECRETS
LEGACY_OR_CONTAMINATED
SYNTHETIC_EXAMPLES
```

## 6.1 Definición resumida

| Categoría                | Descripción                                            |
| ------------------------ | ------------------------------------------------------ |
| `FRAMEWORK_BASE`         | Código, core, scripts, tests, dependencias base.       |
| `FRAMEWORK_CONFIG`       | Reglas, skills, workflows y configuración general.     |
| `TEMPLATE_CASE`          | Plantillas vacías para crear nuevos casos.             |
| `PROJECT_IDENTITY`       | Identidad del nuevo proyecto.                          |
| `USER_INPUT`             | Información aportada por el usuario.                   |
| `PROJECT_MEMORY`         | DMV, decisiones, conocimiento vivo del proyecto.       |
| `AGENT_GENERATED_OUTPUT` | Documentos, dossiers, entregables finales de negocio y salidas generadas por el sistema para el usuario o proyecto vivo. |
| `PROJECT_REPORTS`        | Reportes técnicos de control de calidad, auditoría de fases, validaciones internas, gates y reportes del validador. |
| `PROJECT_CHANGES`        | Feedback, solicitudes de cambio y pivotes.             |
| `PROJECT_VERSIONS`       | Hitos y versiones internas del proyecto vivo.          |
| `TEMP_RUNTIME`           | Cachés, temporales y archivos técnicos descartables.   |
| `LOCAL_SECRETS`          | `.env`, claves, tokens y configuración local sensible. |
| `LEGACY_OR_CONTAMINATED` | Material heredado, dudoso o no clasificado.            |
| `SYNTHETIC_EXAMPLES`     | Ejemplos falsos, mínimos y seguros.                    |

---

# 7. Reglas por categoría

## 7.1 `FRAMEWORK_BASE`

Uso:

```text
Código y estructura técnica reutilizable del framework.
```

Reglas:

* puede vivir en el repositorio madre;
* se copia a nuevos proyectos;
* no puede contener datos reales;
* puede actualizarse desde framework;
* no debe depender de un caso específico.

Valores esperados:

```yaml
copy_policy: "copy"
allowed_in_framework: true
contains_real_data: false
can_update_from_framework: true
requires_audit: false
can_regenerate: false
```

Ejemplos de rutas:

```text
src/
scripts/
pyproject.toml
uv.lock
```

## 7.2 `FRAMEWORK_CONFIG`

Uso:

```text
Configuración general, reglas, skills, workflows y gates reutilizables.
```

Reglas:

* puede vivir en el repositorio madre;
* se copia a nuevos proyectos;
* no puede contener datos reales;
* puede actualizarse desde framework;
* requiere auditoría si contiene prompts, reglas o workflows con riesgo de contaminación.

Valores esperados:

```yaml
copy_policy: "copy"
allowed_in_framework: true
contains_real_data: false
can_update_from_framework: true
requires_audit: true
can_regenerate: false
```

Ejemplos de rutas:

```text
.agent/
docs/gobernanza/
```

## 7.3 `TEMPLATE_CASE`

Uso:

```text
Plantillas vacías para crear casos nuevos.
```

Reglas:

* puede vivir en el repositorio madre;
* se copia o se usa como base para generar un caso;
* no puede contener datos reales;
* puede actualizarse desde framework.

Valores esperados:

```yaml
copy_policy: "copy"
allowed_in_framework: true
contains_real_data: false
can_update_from_framework: true
requires_audit: false
can_regenerate: false
```

Ejemplo:

```text
core/templates/case_template/
```

## 7.4 `PROJECT_IDENTITY`

Uso:

```text
Datos mínimos de identidad del proyecto nuevo.
```

Reglas:

* no se copia desde otro proyecto;
* se genera nuevo en cada proyecto;
* puede contener datos reales;
* no se actualiza desde framework.

Valores esperados:

```yaml
copy_policy: "generate_empty"
allowed_in_framework: false
contains_real_data: true
can_update_from_framework: false
requires_audit: true
can_regenerate: false
```

Ejemplos:

```text
case_config.yml
project_config.yml
origin_manifest.yml
```

## 7.5 `USER_INPUT`

Uso:

```text
Información aportada por el usuario o cliente.
```

Reglas:

* no se copia desde framework;
* no puede vivir en el repositorio madre;
* puede contener datos reales;
* no puede actualizarse desde framework;
* requiere auditoría antes de retención externa.

Valores esperados:

```yaml
copy_policy: "skip"
allowed_in_framework: false
contains_real_data: true
can_update_from_framework: false
requires_audit: true
can_regenerate: false
```

Ejemplos:

```text
inputs/
sources/
```

## 7.6 `PROJECT_MEMORY`

Uso:

```text
Memoria viva del proyecto: DMV, decisiones, hipótesis y estado.
```

Reglas:

* no se copia desde otro proyecto;
* no puede vivir en el repositorio madre;
* puede contener datos reales;
* no se actualiza desde framework;
* no se regenera sin proceso formal del proyecto vivo.

Valores esperados:

```yaml
copy_policy: "generate_empty"
allowed_in_framework: false
contains_real_data: true
can_update_from_framework: false
requires_audit: true
can_regenerate: false
```

Ejemplos:

```text
dmv/
decision_log/
```

## 7.7 `AGENT_GENERATED_OUTPUT`

Uso:

```text
Documentos, dossiers, entregables finales de negocio y salidas generadas por el sistema para el usuario o proyecto vivo.
```

Reglas:

* no se copia al crear un proyecto nuevo;
* no puede vivir en el repositorio madre si corresponde a un proyecto real;
* puede contener datos reales;
* no se actualiza desde framework;
* puede regenerarse si existe contrato de regeneración.

Valores esperados:

```yaml
copy_policy: "skip"
allowed_in_framework: false
contains_real_data: true
can_update_from_framework: false
requires_audit: true
can_regenerate: true
```

Ejemplos:

```text
output/
entregables/
```

## 7.8 `PROJECT_REPORTS`

Uso:

```text
Reportes técnicos de control de calidad, auditoría de fases, validaciones internas, gates y reportes del validador.
```

Reglas:

* no se copian a nuevos proyectos;
* no pueden vivir en repositorio madre si pertenecen a un caso real;
* pueden contener datos reales;
* algunos reportes pueden retenerse externamente;
* los reportes temporales deben ignorarse.

Valores esperados:

```yaml
copy_policy: "skip"
allowed_in_framework: false
contains_real_data: true
can_update_from_framework: false
requires_audit: true
can_regenerate: true
```

Ejemplos:

```text
reports/
cases/*/reports/tmp/
cases/*/reports/official/
```

## 7.9 `PROJECT_CHANGES`

Uso:

```text
Feedback, cambios, pivotes, reaperturas y solicitudes de modificación.
```

Reglas:

* no se copia desde framework;
* no vive en repositorio madre;
* puede contener datos reales;
* pertenece al proyecto vivo;
* no se actualiza desde framework.

Valores esperados:

```yaml
copy_policy: "skip"
allowed_in_framework: false
contains_real_data: true
can_update_from_framework: false
requires_audit: true
can_regenerate: false
```

## 7.10 `PROJECT_VERSIONS`

Uso:

```text
Hitos, versiones internas, releases o cortes del proyecto vivo.
```

Reglas:

* no se copia desde framework;
* puede vivir en el repo del proyecto vivo;
* no vive en repo madre;
* puede ir a retención externa;
* requiere manifiesto o reporte de cierre.

Valores esperados:

```yaml
copy_policy: "skip"
allowed_in_framework: false
contains_real_data: true
can_update_from_framework: false
requires_audit: true
can_regenerate: false
```

## 7.11 `TEMP_RUNTIME`

Uso:

```text
Cachés, temporales y archivos descartables.
```

Reglas:

* no se copia;
* no se versiona;
* no vive en repositorio madre salvo como patrón ignorado;
* puede eliminarse con limpieza segura;
* no requiere retención.

Valores esperados:

```yaml
copy_policy: "skip"
allowed_in_framework: false
contains_real_data: false
can_update_from_framework: false
requires_audit: false
can_regenerate: true
```

Ejemplos:

```text
__pycache__/
.pytest_cache/
cases/tmp_*/
*.tmp
*.local.json
```

## 7.12 `LOCAL_SECRETS`

Uso:

```text
Credenciales, claves, tokens, `.env` y configuración local sensible.
```

Reglas:

* nunca se copia;
* nunca se versiona;
* nunca se retiene en paquetes compartibles;
* si aparece en candidato de extracción, bloquea el proceso.

Valores esperados:

```yaml
copy_policy: "skip"
allowed_in_framework: false
contains_real_data: true
can_update_from_framework: false
requires_audit: true
can_regenerate: false
```

Ejemplos:

```text
.env
*.pem
*.key
secrets/
```

## 7.13 `LEGACY_OR_CONTAMINATED`

Uso:

```text
Material heredado, dudoso, sectorial o no clasificado.
```

Reglas:

* no se copia;
* no se actualiza desde framework;
* no se usa para crear base limpia;
* requiere decisión humana;
* bloquea Plan B si aparece entre candidatos de extracción.

Valores esperados:

```yaml
copy_policy: "ask_before_copy"
allowed_in_framework: false
contains_real_data: true
can_update_from_framework: false
requires_audit: true
can_regenerate: false
```

Ejemplos:

```text
docs_base/
output/
material histórico no clasificado
```

## 7.14 `SYNTHETIC_EXAMPLES`

Uso:

```text
Ejemplos falsos, mínimos y seguros para pruebas o documentación.
```

Reglas:

* pueden vivir en el repositorio madre;
* pueden copiarse opcionalmente;
* no pueden contener datos reales;
* no deben simular ser un proyecto real completo;
* deben ser pequeños y claros.

Valores esperados:

```yaml
copy_policy: "ask_before_copy"
allowed_in_framework: true
contains_real_data: false
can_update_from_framework: false
requires_audit: true
can_regenerate: false
```

Ejemplos:

```text
examples/
cases/demo_*/
```

---

# 8. Reglas de `copy_policy`

## 8.1 `copy`

Se usa cuando el artefacto debe copiarse tal como está al crear un nuevo proyecto o extraer una base.

Permitido principalmente para:

```text
FRAMEWORK_BASE
FRAMEWORK_CONFIG
TEMPLATE_CASE
```

Bloqueado para:

```text
USER_INPUT
PROJECT_MEMORY
AGENT_GENERATED_OUTPUT
PROJECT_REPORTS
PROJECT_CHANGES
PROJECT_VERSIONS
TEMP_RUNTIME
LOCAL_SECRETS
LEGACY_OR_CONTAMINATED
```

## 8.2 `skip`

Se usa cuando el artefacto no debe copiarse.

Debe usarse para:

```text
USER_INPUT
AGENT_GENERATED_OUTPUT
PROJECT_REPORTS
PROJECT_CHANGES
PROJECT_VERSIONS
TEMP_RUNTIME
LOCAL_SECRETS
```

## 8.3 `generate_empty`

Se usa cuando el nuevo proyecto necesita una estructura o archivo equivalente, pero vacío o inicializado desde cero.

Debe usarse para:

```text
PROJECT_IDENTITY
PROJECT_MEMORY
```

Ejemplo:

```text
No copiar el DMV de otro proyecto.
Crear un DMV inicial vacío.
```

## 8.4 `regenerate`

Se usa cuando el artefacto puede volver a generarse por un proceso controlado.

Permitido solo si:

* `can_regenerate: true`;
* no contiene secretos;
* no sobrescribe memoria viva;
* existe contrato de regeneración.

## 8.5 `ask_before_copy`

Se usa cuando el artefacto puede copiarse solo después de decisión humana documentada.

Debe usarse para:

```text
SYNTHETIC_EXAMPLES
LEGACY_OR_CONTAMINATED
```

---

# 9. Validaciones obligatorias

Un validador futuro del manifiesto debe comprobar como mínimo:

## 9.1 Validaciones de estructura

* existe `artifact_manifest.yml`;
* contiene `manifest_version`;
* contiene `manifest_status`;
* contiene `repo_role`;
* contiene lista `artifacts`;
* cada artefacto contiene todos los campos obligatorios;
* no hay campos obligatorios vacíos;
* cada `path` definido en el manifiesto existe físicamente en el repositorio o coincide con un patrón de rutas reales, para prevenir erratas tipográficas.

## 9.2 Validaciones de valores

* `manifest_status` usa un valor permitido;
* `repo_role` usa un valor permitido;
* `category` usa una categoría válida;
* `copy_policy` usa un valor permitido;
* campos booleanos son booleanos reales;
* `owner` no está vacío;
* `notes` no está vacío en ningún artefacto, porque es un campo obligatorio por esquema. Si `requires_audit: true`, el campo `notes` debe detallar obligatoriamente las razones de la auditoría y el protocolo de revisión humana aplicable.

## 9.3 Validaciones de coherencia

Debe bloquearse si:

* `contains_real_data: true` y `allowed_in_framework: true`;
* `LOCAL_SECRETS` tiene cualquier `copy_policy` distinto de `skip`;
* `copy_policy: regenerate` solo se permite si `can_regenerate: true`;
* `TEMP_RUNTIME` tiene `copy_policy` distinto de `skip`;
* `PROJECT_MEMORY` tiene `copy_policy: copy`;
* `USER_INPUT` tiene `copy_policy: copy`;
* `AGENT_GENERATED_OUTPUT` tiene `copy_policy: copy`;
* `PROJECT_REPORTS` tiene `copy_policy: copy`;
* `can_update_from_framework: true` en categorías de proyecto vivo;
* `LEGACY_OR_CONTAMINATED` tiene `copy_policy: copy`;
* `requires_audit: true` y `notes` está vacío.

## 9.4 Validaciones de cobertura

El manifiesto debe cubrir al menos las rutas relevantes de nivel superior:

```text
.agent/
core/
src/
scripts/
examples/
docs/
output/
reports/
cases/
_workspace_cases/
docs_base/
pyproject.toml
uv.lock
README.md
INDEX_MAESTRO.md
.env
.venv/
__pycache__/
```

Si alguna ruta relevante no está clasificada, el gate debe devolver `FAIL`.

---

# 10. Errores bloqueantes

Los siguientes errores deben bloquear cualquier script de creación, extracción, limpieza, actualización o regeneración:

```text
MANIFEST_NOT_FOUND
MANIFEST_STATUS_NOT_APPROVED
UNKNOWN_CATEGORY
UNKNOWN_COPY_POLICY
MISSING_REQUIRED_FIELD
INVALID_BOOLEAN_FIELD
REAL_DATA_ALLOWED_IN_FRAMEWORK
SECRET_MARKED_FOR_COPY
TEMP_MARKED_FOR_COPY
PROJECT_MEMORY_MARKED_FOR_COPY
USER_INPUT_MARKED_FOR_COPY
OUTPUT_MARKED_FOR_COPY
REPORT_MARKED_FOR_COPY
LEGACY_MARKED_FOR_COPY
FRAMEWORK_UPDATE_ON_PROJECT_DATA
AUDIT_REQUIRED_WITHOUT_NOTES
UNCOVERED_TOP_LEVEL_PATH
PLAN_B_GATE_FAILED
PATH_DOES_NOT_EXIST
REDUNDANT_REGENERATION_POLICY
DUPLICATE_PATH_PATTERN
```

---

# 11. Ejemplos válidos

## 11.1 Framework base

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
  notes: "Runtime genérico reutilizable."
```

## 11.2 Plantilla de caso

```yaml
- path: "core/templates/case_template/"
  category: "TEMPLATE_CASE"
  copy_policy: "copy"
  allowed_in_framework: true
  contains_real_data: false
  can_update_from_framework: true
  requires_audit: false
  can_regenerate: false
  owner: "equipo_tecnico"
  notes: "Plantilla vacía para inicializar proyectos vivos."
```

## 11.3 DMV de proyecto vivo

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
  notes: "Memoria viva del proyecto. Nunca se copia desde otro proyecto."
```

## 11.4 Output generado de proyecto

```yaml
- path: "output/"
  category: "AGENT_GENERATED_OUTPUT"
  copy_policy: "skip"
  allowed_in_framework: false
  contains_real_data: true
  can_update_from_framework: false
  requires_audit: true
  can_regenerate: true
  owner: "proyecto_vivo"
  notes: "Entregables generados para un proyecto real. No pertenecen al repositorio madre."
```

## 11.5 Ejemplo sintético

```yaml
- path: "examples/"
  category: "SYNTHETIC_EXAMPLES"
  copy_policy: "ask_before_copy"
  allowed_in_framework: true
  contains_real_data: false
  can_update_from_framework: false
  requires_audit: true
  can_regenerate: false
  owner: "equipo_tecnico"
  notes: "Ejemplos mínimos, falsos y seguros para documentación o pruebas."
```

---

# 12. Ejemplos inválidos

## 12.1 DMV copiado desde proyecto anterior

```yaml
- path: "dmv/"
  category: "PROJECT_MEMORY"
  copy_policy: "copy"
  allowed_in_framework: false
  contains_real_data: true
  can_update_from_framework: false
  requires_audit: true
  can_regenerate: false
  owner: "proyecto_vivo"
  notes: "Inválido: la memoria viva no se copia."
```

Error esperado:

```text
PROJECT_MEMORY_MARKED_FOR_COPY
```

## 12.2 Secretos marcados para copia

```yaml
- path: ".env"
  category: "LOCAL_SECRETS"
  copy_policy: "copy"
  allowed_in_framework: false
  contains_real_data: true
  can_update_from_framework: false
  requires_audit: true
  can_regenerate: false
  owner: "usuario"
  notes: "Inválido: los secretos nunca se copian."
```

Error esperado:

```text
SECRET_MARKED_FOR_COPY
```

## 12.3 Output real permitido en framework

```yaml
- path: "output/"
  category: "AGENT_GENERATED_OUTPUT"
  copy_policy: "skip"
  allowed_in_framework: true
  contains_real_data: true
  can_update_from_framework: false
  requires_audit: true
  can_regenerate: true
  owner: "proyecto_vivo"
  notes: "Inválido: outputs reales no pueden vivir en el repositorio madre."
```

Errores esperados:

```text
REAL_DATA_ALLOWED_IN_FRAMEWORK
```

## 12.4 Legacy marcado para copia automática

```yaml
- path: "docs_base/"
  category: "LEGACY_OR_CONTAMINATED"
  copy_policy: "copy"
  allowed_in_framework: false
  contains_real_data: true
  can_update_from_framework: false
  requires_audit: true
  can_regenerate: false
  owner: "equipo_gobernanza"
  notes: "Inválido: material legacy no puede copiarse automáticamente."
```

Error esperado:

```text
LEGACY_MARKED_FOR_COPY
```

---

# 13. Relación con Plan A

Plan A crea un proyecto nuevo desde el repositorio madre limpio.

El `artifact_manifest.yml` define qué se copia, qué se genera vacío y qué se omite.

En Plan A:

* `FRAMEWORK_BASE` se copia;
* `FRAMEWORK_CONFIG` se copia;
* `TEMPLATE_CASE` se copia o se usa para inicializar;
* `PROJECT_IDENTITY` se genera nuevo;
* `PROJECT_MEMORY` se genera vacío;
* `USER_INPUT` no se copia;
* `AGENT_GENERATED_OUTPUT` no se copia;
* `PROJECT_REPORTS` no se copia;
* `PROJECT_CHANGES` no se copia;
* `PROJECT_VERSIONS` no se copia;
* `TEMP_RUNTIME` no se copia;
* `LOCAL_SECRETS` no se copia;
* `LEGACY_OR_CONTAMINATED` no se copia;
* `SYNTHETIC_EXAMPLES` solo se copia si se confirma.

Regla:

```text
Plan A no puede ejecutar creación de proyecto si artifact_manifest.yml no existe o no está aprobado.
```

---

# 14. Relación con Plan B

Plan B extrae una base limpia desde un repositorio existente.

El `artifact_manifest.yml` es obligatorio para que Plan B no copie por intuición.

Plan B solo puede extraer automáticamente:

```text
FRAMEWORK_BASE
FRAMEWORK_CONFIG
TEMPLATE_CASE
```

Puede considerar con confirmación humana:

```text
SYNTHETIC_EXAMPLES
```

Debe excluir:

```text
PROJECT_IDENTITY
USER_INPUT
PROJECT_MEMORY
AGENT_GENERATED_OUTPUT
PROJECT_REPORTS
PROJECT_CHANGES
PROJECT_VERSIONS
TEMP_RUNTIME
LOCAL_SECRETS
LEGACY_OR_CONTAMINATED
```

Plan B queda bloqueado si:

* no existe manifiesto aprobado;
* hay rutas sin clasificar;
* el candidato contiene datos reales dentro de rutas de framework;
* hay secretos;
* hay memoria de proyecto viva entre los candidatos;
* hay outputs reales entre los candidatos;
* hay material legacy marcado para copia.

Regla:

```text
El Plan B no copia todo y limpia después.
El Plan B solo copia lo aprobado de antemano.
```

---

# 15. Relación con actualización desde framework

La actualización desde framework madre solo puede afectar artefactos:

```text
FRAMEWORK_BASE
FRAMEWORK_CONFIG
TEMPLATE_CASE
```

Queda prohibido actualizar desde framework:

```text
PROJECT_IDENTITY
USER_INPUT
PROJECT_MEMORY
AGENT_GENERATED_OUTPUT
PROJECT_REPORTS
PROJECT_CHANGES
PROJECT_VERSIONS
TEMP_RUNTIME
LOCAL_SECRETS
LEGACY_OR_CONTAMINATED
SYNTHETIC_EXAMPLES
```

La actualización debe respetar:

* `can_update_from_framework: true`;
* `requires_audit`;
* `copy_policy`;
* notas del artefacto.

Si un artefacto tiene:

```yaml
can_update_from_framework: false
```

ningún actualizador puede modificarlo, aunque la ruta exista en el framework.

---

# 16. Relación con retención externa

La retención externa conserva snapshots, backups, entregas publicadas o paquetes de evidencia fuera del repositorio activo.

El `artifact_manifest.yml` no define directamente cómo se almacena la retención externa, pero sí define qué artefactos pueden entrar en paquetes de retención.

Pueden entrar en retención externa, con auditoría:

```text
PROJECT_MEMORY
AGENT_GENERATED_OUTPUT
PROJECT_REPORTS
PROJECT_CHANGES
PROJECT_VERSIONS
```

No deben entrar en retención externa:

```text
LOCAL_SECRETS
TEMP_RUNTIME
.venv/
__pycache__/
cachés
archivos no clasificados
```

Regla:

```text
Ningún paquete de retención externa puede incluir artefactos no clasificados por el manifiesto.
```

---

# 17. Criterios de aceptación

SPEC-001 se considera aceptada cuando cumple todo lo siguiente:

1. Define claramente el propósito del `artifact_manifest.yml`.
2. Define ubicación recomendada.
3. Define esquema mínimo v1.
4. Define campos obligatorios de raíz.
5. Define campos obligatorios por artefacto.
6. Define valores permitidos.
7. Define categorías válidas.
8. Define reglas operativas por categoría.
9. Define reglas de `copy_policy`.
10. Define validaciones obligatorias.
11. Define errores bloqueantes.
12. Incluye ejemplos válidos.
13. Incluye ejemplos inválidos.
14. Explica relación con Plan A.
15. Explica relación con Plan B.
16. Explica relación con actualización desde framework.
17. Explica relación con retención externa.
18. No implementa scripts.
19. No crea el `artifact_manifest.yml` definitivo.
20. No modifica ADR-001.
21. No abre ADR-002.
22. Sirve como contrato previo para futuras tareas técnicas.

---

# 18. Fuera de alcance

SPEC-001 no define todavía:

* implementación del validador del manifiesto;
* creación del `artifact_manifest.yml` real;
* scripts de Plan A;
* scripts de Plan B;
* `clean-case`;
* `reset-workspace`;
* `archive-case`;
* `export-case`;
* integración con Copier;
* integración con GitHub Template;
* migración física de `output/`, `docs_base/` o material logístico;
* apertura de ADR-002.

---

# 19. Nota de control

Hasta que SPEC-001 sea aprobada y exista un `artifact_manifest.yml` válido, queda prohibido implementar automatizaciones de:

```text
creación de proyectos nuevos
extracción de base limpia
limpieza automática
actualización desde framework
regeneración de artefactos
retención externa automatizada
```

Cualquier acción previa solo podrá ser manual, auditada y explícitamente autorizada.
