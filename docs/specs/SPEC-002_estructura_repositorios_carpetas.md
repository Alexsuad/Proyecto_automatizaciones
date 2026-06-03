# SPEC-002 — Estructura estándar de repositorios y carpetas

## Estado

Aprobado.

---

# 1. Relación con ADR-001 y SPEC-001

## 1.1 Relación con ADR-001

ADR-001 define el modelo arquitectónico base:

* repositorio madre limpio;
* proyectos vivos independientes;
* actualización controlada desde framework;
* retención externa;
* reutilización sin contaminación;
* separación entre framework, proyectos vivos y artefactos históricos.

SPEC-002 no modifica ADR-001.
SPEC-002 convierte esa decisión en una estructura estándar de carpetas y archivos.

## 1.2 Relación con SPEC-001

SPEC-001 define el contrato del `artifact_manifest.yml`.

SPEC-001 responde:

```text
Qué es cada artefacto.
Qué categoría tiene.
Qué se copia.
Qué se omite.
Qué se genera vacío.
Qué se puede actualizar desde framework.
Qué debe bloquearse.
```

SPEC-002 responde:

```text
Dónde debe vivir cada cosa.
Qué carpetas puede tener el repositorio madre.
Qué carpetas puede tener un proyecto vivo.
Qué carpetas pertenecen a retención externa.
Qué carpetas son temporales, legacy, privadas o prohibidas.
```

Regla principal:

```text
SPEC-001 clasifica artefactos.
SPEC-002 organiza físicamente el repositorio.
```

---

# 2. Propósito

El propósito de SPEC-002 es definir una estructura estándar para que los repositorios del sistema sean:

* reutilizables;
* auditables;
* limpios;
* fáciles de copiar;
* fáciles de actualizar desde framework;
* fáciles de congelar;
* fáciles de archivar;
* difíciles de contaminar.

SPEC-002 debe evitar que cada proyecto invente sus propias carpetas, porque eso dificultaría:

* validar el `artifact_manifest.yml`;
* extraer una base limpia;
* crear proyectos nuevos;
* diferenciar framework de proyecto vivo;
* limpiar temporales;
* auditar cambios;
* preparar retención externa.

---

# 3. Principios de estructura

## 3.1 Separación entre framework y proyecto vivo

El repositorio madre no debe almacenar proyectos reales completos.

El repositorio madre contiene:

```text
framework
plantillas
contratos y herramientas técnicas aprobadas
scripts técnicos
documentación normativa
ejemplos sintéticos mínimos
```

El proyecto vivo contiene:

```text
identidad del proyecto
inputs del usuario
fuentes
DMV
outputs
reportes
cambios
versiones
evidencias
```

## 3.2 Un proyecto real por repositorio

Cada proyecto real debe vivir en un repositorio independiente o en un espacio de trabajo independiente.

Ejemplos:

```text
proyauto_framework/
proyecto_logistica/
proyecto_carpinteria/
proyecto_turismo/
```

El repositorio madre no debe convertirse en un monorepo de proyectos reales.

## 3.3 El repositorio madre debe poder clonarse limpio

Un clon nuevo del repositorio madre debe contener solo infraestructura reutilizable.

No debe contener:

* outputs de proyectos reales;
* documentos de negocio reales;
* inputs reales;
* memoria viva de un caso;
* reportes de un análisis específico;
* secretos;
* históricos contaminados.

## 3.4 Los outputs no definen estructura normativa

La carpeta `output/` no debe ser sede normativa del framework.

Si un documento es estable y normativo, debe vivir en `docs/`.

Si un documento es una salida generada por un proyecto vivo, debe vivir dentro del proyecto vivo.

## 3.5 La retención externa no es proyecto vivo

La retención externa sirve para conservar evidencia fría, snapshots, backups o paquetes cerrados.

No debe confundirse con un proyecto vivo editable.

## 3.6 No se limpia borrando sin contrato

La limpieza futura debe basarse en:

* `artifact_manifest.yml`;
* categorías de SPEC-001;
* estructura de SPEC-002;
* dry-run obligatorio;
* confirmación explícita para acciones destructivas.

---

# 4. Estructura estándar del repositorio madre

## 4.1 Objetivo del repositorio madre

El repositorio madre es la base limpia desde la cual se crean proyectos vivos independientes.

Debe contener el framework reutilizable, no los resultados de proyectos reales.

## 4.2 Estructura recomendada

```text
/
├── .agent/
├── core/
├── src/
├── scripts/
├── tests/
├── templates/
├── examples/
├── docs/
│   ├── adrs/
│   ├── specs/
│   ├── governance/
│   └── guides/
├── artifact_manifest.yml
├── repo_identity.yml
├── pyproject.toml
├── uv.lock
├── README.md
├── INDEX_MAESTRO.md
└── .gitignore
```

## 4.2.1 Estado de archivos raíz normativos

SPEC-002 distingue entre estructura objetivo y baseline actual.

Los archivos raíz normativos pueden tener uno de estos estados:

| Estado | Significado |
|---|---|
| `baseline_actual` | Ya forma parte del estado aprobado del repositorio. |
| `objetivo_v1` | Debe existir antes de implementar los flujos derivados de ADR-001. |
| `placeholder_permitido` | Puede existir como marcador sin habilitar automatización. |
| `pendiente_de_especificacion` | No debe crearse hasta que su especificación sea aprobada. |
| `prohibido_en_repo_madre` | No debe existir en el repositorio madre. |

Para SPEC-002, los archivos quedan así:

| Archivo | Estado | Regla |
|---|---|---|
| `artifact_manifest.yml` | `objetivo_v1` | Debe existir antes de implementar creación, extracción, limpieza, actualización o regeneración. Se permite un placeholder vacío o documental solo si está marcado explícitamente como `placeholder_permitido`. No se permite usarlo como contrato activo hasta que SPEC-001 esté aprobada y exista autorización explícita para su creación operativa. |
| `repo_identity.yml` | `objetivo_v1` | Debe existir antes de activar protecciones operativas del repositorio madre o proyectos vivos. No debe crearse hasta que su especificación o tarea documental sea autorizada. |
| `case_config.yml` | `prohibido_en_repo_madre` | Solo pertenece a proyectos vivos. |
| `origin_manifest.yml` | `prohibido_en_repo_madre` | Solo pertenece a proyectos vivos creados desde framework. |
| `.env` | `prohibido_en_repo_madre` | Nunca debe versionarse. |

Regla:
La estructura recomendada muestra el modelo objetivo, no autoriza por sí sola la creación inmediata de todos los archivos.

## 4.3 Carpetas obligatorias del repositorio madre

| Carpeta / archivo       | Estado                                             | Propósito                                                        |
| ----------------------- | -------------------------------------------------- | ---------------------------------------------------------------- |
| `.agent/`               | Obligatoria si se usan agentes                     | Reglas, skills, workflows y configuración agéntica reutilizable. |
| `core/`                 | Obligatoria                                        | Contratos, componentes metodológicos y base reutilizable. No debe ser sede canónica de plantillas de caso. |
| `src/`                  | Obligatoria si hay runtime                         | Código fuente reutilizable del framework.                        |
| `scripts/`              | Obligatoria si hay automatización                  | Utilidades técnicas no destructivas y herramientas del sistema.  |
| `docs/`                 | Obligatoria                                        | Documentación normativa, ADRs, SPECs y guías.                    |
| `docs/adrs/`            | Obligatoria                                        | Decisiones arquitectónicas aprobadas.                            |
| `docs/specs/`           | Obligatoria                                        | Especificaciones técnicas derivadas de ADRs.                     |
| `artifact_manifest.yml` | Obligatorio cuando se implemente SPEC-001          | Contrato de clasificación de artefactos.                         |
| `repo_identity.yml`     | Obligatorio cuando se implemente identidad de repo | Identidad del repositorio y rol del repo.                        |
| `README.md`             | Obligatorio                                        | Entrada principal del repositorio.                               |
| `.gitignore`            | Obligatorio                                        | Reglas de exclusión para temporales, privados y generados.       |

## 4.4 Carpetas opcionales del repositorio madre

| Carpeta            | Condición de uso                          | Propósito                                         |
| ------------------ | ----------------------------------------- | ------------------------------------------------- |
| `tests/`           | Si se adopta estructura formal de pruebas | Pruebas del framework.                            |
| `templates/`       | Obligatoria si se crearán proyectos desde plantilla | Sede canónica de plantillas reutilizables de proyecto, caso o documento. |
| `examples/`        | Solo con ejemplos sintéticos              | Fixtures mínimos, falsos y seguros.               |
| `docs/governance/` | Si hay reglas de gobierno adicionales     | Políticas, controles y protocolos.                |
| `docs/guides/`     | Si hay guías de uso                       | Instructivos de operación del framework.          |

## 4.5 Carpetas no recomendadas en el repositorio madre

| Carpeta                                      | Motivo                                                                  |
| -------------------------------------------- | ----------------------------------------------------------------------- |
| `output/` con documentos de proyectos reales | Puede contener outputs generados y contaminar el framework.             |
| `docs_base/`                                 | Puede mezclar documentos históricos, legacy o de caso.                  |
| `cases/` con proyectos reales completos      | Convierte el framework en monorepo contaminado.                         |
| `_workspace_cases/` versionado               | Debe ser privado/local e ignorado.                                      |
| `reports/` global con reportes de casos      | Puede mezclar auditorías del framework con reportes de proyectos vivos. |

## 4.6 Carpetas prohibidas en el repositorio madre

Estas carpetas no deben versionarse dentro del repositorio madre:

```text
.venv/
__pycache__/
.pytest_cache/
.env
secrets/
_workspace_cases/
cases/tmp_*/
node_modules/
dist/
build/
```

---

# 5. Estructura estándar del proyecto vivo

## 5.1 Objetivo del proyecto vivo

El proyecto vivo es una instancia independiente creada desde el framework.

Contiene información específica de un proyecto real o sintético.

Puede evolucionar, pivotar, cerrarse, congelarse o exportarse.

## 5.2 Estructura recomendada

```text
/
├── .agent/
├── core/
├── src/
├── scripts/
├── docs/
├── inputs/
├── sources/
├── dmv/
├── changes/
├── impact_assessments/
├── output/
├── reports/
│   └── official/
├── versions/
├── artifact_manifest.yml
├── repo_identity.yml
├── case_config.yml
├── origin_manifest.yml
├── pyproject.toml
├── uv.lock
├── README.md
└── .gitignore
```


`reports/tmp/` puede existir durante ejecución local, pero debe tratarse como `TEMP_RUNTIME`, estar cubierto por `.gitignore` y no formar parte de la estructura versionada obligatoria.

## 5.3 Carpetas obligatorias del proyecto vivo

| Carpeta / archivo       | Categoría SPEC-001                          | Propósito                                                   |
| ----------------------- | ------------------------------------------- | ----------------------------------------------------------- |
| `inputs/`               | `USER_INPUT`                                | Datos aportados por el usuario o cliente.                   |
| `sources/`              | `USER_INPUT`                                | `sources/` contiene fuentes del proyecto vivo. Puede incluir documentos aportados por el usuario, referencias externas o material curado del caso. Debe clasificarse como `USER_INPUT` mientras contenga fuentes específicas del proyecto y nunca debe copiarse a otros proyectos. |
| `dmv/`                  | `PROJECT_MEMORY`                            | Documento Maestro Vivo y memoria estructurada del proyecto. |
| `output/`               | `AGENT_GENERATED_OUTPUT`                    | Entregables y salidas generadas para el proyecto.           |
| `reports/`              | `PROJECT_REPORTS`                           | Reportes de auditoría, validación y control.                |

| `reports/official/`     | `PROJECT_REPORTS`                           | Reportes oficiales aprobados.                               |
| `case_config.yml`       | `PROJECT_IDENTITY`                          | Identidad y configuración del caso/proyecto.                |
| `origin_manifest.yml`   | `PROJECT_IDENTITY`                          | Trazabilidad de origen desde framework.                     |
| `artifact_manifest.yml` | Contrato transversal                        | Clasificación real de artefactos del proyecto.              |
| `repo_identity.yml`     | `PROJECT_IDENTITY`                          | Identidad del repositorio vivo.                             |
| `README.md`             | Documentación del proyecto                  | Entrada principal del proyecto vivo.                        |

## 5.4 Carpetas opcionales del proyecto vivo

| Carpeta               | Categoría SPEC-001                   | Uso                                                     |
| --------------------- | ------------------------------------ | ------------------------------------------------------- |
| `changes/`            | `PROJECT_CHANGES`                    | Cambios, pivotes, feedback y solicitudes.               |
| `impact_assessments/` | `PROJECT_CHANGES`                    | Evaluaciones de impacto antes de modificar entregables. |
| `versions/`           | `PROJECT_VERSIONS`                   | Cortes, hitos y versiones internas.                     |
| `docs/`               | Según contenido                      | `docs/` en un proyecto vivo solo debe contener documentación estable del caso. No debe usarse para modificar documentación normativa del framework salvo mediante actualización controlada desde framework. |
| `evidence/`           | `PROJECT_REPORTS` o `PROJECT_MEMORY` | Evidencias de validación o soporte.                     |
| `exports/`            | `PROJECT_VERSIONS`                   | Exportaciones temporales antes de retención externa.    |
| `reports/tmp/`        | `TEMP_RUNTIME`                      | Reportes temporales de ejecución. Puede existir localmente, pero no debe versionarse. |

## 5.5 Carpetas prohibidas o no recomendadas en proyecto vivo

| Carpeta                                                    | Motivo                                                                 |
| ---------------------------------------------------------- | ---------------------------------------------------------------------- |
| `docs_base/`                                               | Ambigua. Puede mezclar documentos base, legacy y caso real.            |
| `output/` usado como documentación normativa del framework | En proyecto vivo sí puede existir, pero solo como salida del proyecto. |
| `.agent/` con reglas modificadas sin trazabilidad          | Puede romper actualización desde framework.                            |
| `core/` modificado sin registro                            | Puede dificultar actualización desde framework.                        |
| `src/` modificado sin control                              | Puede crear divergencia técnica respecto al framework.                 |

## 5.6 Proyecto vivo y actualización desde framework

En un proyecto vivo, las carpetas copiadas desde el framework pueden actualizarse solo si SPEC-001 lo permite.

Normalmente actualizables:

```text
.agent/
core/
src/
scripts/
templates/
docs/ de framework
```

No actualizables desde framework:

```text
inputs/
sources/
dmv/
output/
reports/
changes/
versions/
case_config.yml
repo_identity.yml
origin_manifest.yml
```

---

# 6. Estructura de retención externa

## 6.1 Propósito

La retención externa conserva evidencia fría fuera del repositorio activo.

No reemplaza al proyecto vivo.

No debe usarse como espacio de trabajo.

## 6.2 Tipos de retención externa

| Tipo                 | Descripción                                         | Editable |
| -------------------- | --------------------------------------------------- | -------- |
| Snapshot             | Corte completo o parcial de un estado del proyecto. | No       |
| Backup               | Copia de seguridad técnica.                         | No       |
| Entrega publicada    | Paquete final entregado al usuario o cliente.       | No       |
| Paquete de evidencia | Conjunto de reportes, manifiestos y hashes.         | No       |

## 6.3 Estructura recomendada de paquete de retención

```text
<project_id>_<fecha>_<tipo>/
├── MANIFEST_FREEZE.md
├── artifact_manifest.yml
├── repo_identity.yml
├── case_config.yml
├── output/
├── reports/official/
├── versions/
├── checksums/
└── README_ARCHIVE.md
```

## 6.4 Qué puede entrar en retención externa

Puede entrar, con auditoría:

```text
PROJECT_MEMORY
AGENT_GENERATED_OUTPUT
PROJECT_REPORTS
PROJECT_CHANGES
PROJECT_VERSIONS
PROJECT_IDENTITY
```

## 6.5 Qué no debe entrar en retención externa

No debe entrar:

```text
LOCAL_SECRETS
TEMP_RUNTIME
.venv/
__pycache__/
.pytest_cache/
.env
secrets/
tokens
cachés
archivos no clasificados
```

---

# 7. Carpetas prohibidas o no recomendadas

## 7.1 Prohibidas para versionado

```text
.venv/
.env
secrets/
__pycache__/
.pytest_cache/
node_modules/
dist/
build/
cases/tmp_*/
_workspace_cases/
reports/tmp/
```

## 7.2 No recomendadas en el repositorio madre

```text
output/
docs_base/
reports/
cases/ con proyectos reales
```

Estas carpetas pueden existir localmente durante transición o pruebas, pero no deben incorporarse al repositorio madre sin decisión explícita.

## 7.3 No recomendadas en proyectos vivos sin manifiesto

```text
legacy/
archivo_viejo/
final_final/
backup_manual/
nuevo/
pruebas/
```

Si existen, deben clasificarse en `artifact_manifest.yml` como:

```text
LEGACY_OR_CONTAMINATED
TEMP_RUNTIME
PROJECT_VERSIONS
```

según corresponda.

---

# 8. Mapa carpeta → categoría

| Ruta                  | Categoría SPEC-001                 | Vive en repo madre | Vive en proyecto vivo |            Se copia | Observación                                |
| --------------------- | ---------------------------------- | -----------------: | --------------------: | ------------------: | ------------------------------------------ |
| `.agent/`             | `FRAMEWORK_CONFIG`                 |                 Sí |                    Sí |                  Sí | Reglas, skills y workflows.                |
| `core/`               | `FRAMEWORK_BASE`                   |                 Sí |                    Sí |                  Sí | Contratos, componentes metodológicos y base reutilizable del framework. Las plantillas de caso deben vivir en `templates/`. |
| `core/templates/`     | `LEGACY_OR_CONTAMINATED` o no recomendado | No recomendado | No recomendado |                  No | No debe usarse como sede canónica de plantillas de caso; migrar conceptualmente a `templates/` si aplica. |
| `src/`                | `FRAMEWORK_BASE`                   |                 Sí |                    Sí |                  Sí | Runtime reutilizable.                      |
| `scripts/`            | `FRAMEWORK_BASE`                   |                 Sí |                    Sí |                  Sí | Herramientas técnicas controladas.         |
| `tests/`              | `FRAMEWORK_BASE`                   |                 Sí |              Opcional |                  Sí | Pruebas del framework.                     |
| `templates/`          | `TEMPLATE_CASE`                    |                 Sí |              Opcional |                  Sí | Plantillas reutilizables.                  |
| `examples/`           | `SYNTHETIC_EXAMPLES`               |                 Sí |              Opcional |            Opcional | Solo ejemplos falsos y mínimos.            |
| `docs/adrs/`          | `FRAMEWORK_CONFIG`                 |                 Sí |                    Sí |                  Sí | Decisiones arquitectónicas.                |
| `docs/specs/`         | `FRAMEWORK_CONFIG`                 |                 Sí |                    Sí |                  Sí | Especificaciones técnicas.                 |
| `inputs/`             | `USER_INPUT`                       |                 No |                    Sí |                  No | Datos del usuario.                         |
| `sources/`            | `USER_INPUT`                       |                 No |                    Sí |                  No | Fuentes del proyecto.                      |
| `dmv/`                | `PROJECT_MEMORY`                   |                 No |                    Sí | No, se genera vacío | Memoria viva.                              |
| `changes/`            | `PROJECT_CHANGES`                  |                 No |                    Sí |                  No | Cambios y pivotes.                         |
| `impact_assessments/` | `PROJECT_CHANGES`                  |                 No |                    Sí |                  No | Evaluaciones de impacto.                   |
| `output/`             | `AGENT_GENERATED_OUTPUT`           |                 No |                    Sí |                  No | Salidas del proyecto.                      |
| `reports/tmp/`        | `TEMP_RUNTIME`                     |                 No |            Opcional |                  No | Reportes temporales de ejecución. Puede existir localmente, pero no debe versionarse. |
| `reports/official/`   | `PROJECT_REPORTS`                  |                 No |                    Sí |                  No | Reportes oficiales.                        |
| `versions/`           | `PROJECT_VERSIONS`                 |                 No |                    Sí |                  No | Hitos y versiones.                         |
| `_workspace_cases/`   | `TEMP_RUNTIME` o workspace local   |                 No |                    No |                  No | Trabajo privado local.                     |
| `docs_base/`          | `LEGACY_OR_CONTAMINATED`           |     No recomendado |        No recomendado |                  No | Carpeta ambigua; requiere decisión humana. |
| `.env`                | `LOCAL_SECRETS`                    |                 No |                    No |                  No | Nunca versionar.                           |
| `.venv/`              | `TEMP_RUNTIME`                     |                 No |                    No |                  No | Nunca versionar.                           |

---

# 9. Reglas de naming

## 9.1 Nombres de carpetas

Usar preferentemente:

```text
snake_case
```

Ejemplos válidos:

```text
impact_assessments/
case_templates/
project_reports/
```

Evitar:

```text
Mi Carpeta/
final final/
Nuevo(2)/
```

## 9.2 Identificadores de proyectos

Los identificadores deben usar:

```text
minúsculas
números
guion bajo
```

Ejemplos:

```text
proyecto_logistica
taller_carpinteria
demo_restaurante
```

No usar:

```text
Proyecto Logística
taller-carpintería
cliente.final
```

## 9.3 Nombres de documentos normativos

ADRs:

```text
ADR-001 — titulo_descriptivo.md
```

SPECs:

```text
SPEC-001_nombre_descriptivo.md
```

Ejemplos:

```text
ADR-001 — Repositorio madre limpio y creación de proyectos vivos independientes.md
SPEC-001_artifact_manifest.md
SPEC-002_estructura_repositorios_carpetas.md
```

Para documentos normativos nuevos, debe usarse una convención portable basada en ASCII, sin tildes, sin espacios y con `snake_case` después del prefijo.

Formatos obligatorios para documentos nuevos:

```text
ADR-001_titulo_descriptivo.md
SPEC-001_nombre_descriptivo.md
```

Los documentos existentes que ya usan guion largo, espacios o caracteres especiales pueden mantenerse por compatibilidad histórica, pero no deben usarse como patrón para nuevos documentos.

No renombrar documentos existentes durante esta tarea.

## 9.4 Fechas

Cuando un artefacto requiera fecha, usar:

```text
YYYY-MM-DD
```

Para timestamps técnicos:

```text
YYYY-MM-DDTHH-MM-SS
```

---

# 10. Reglas para carpetas legacy

## 10.1 Definición de legacy

Una carpeta se considera legacy si:

* proviene de una fase anterior del proyecto;
* no está clasificada en `artifact_manifest.yml`;
* mezcla outputs, documentos base y decisiones;
* contiene datos de un caso real;
* contiene material sectorial no depurado;
* no tiene dueño claro;
* no tiene política de copia.

## 10.2 Tratamiento de legacy

Las carpetas legacy no deben copiarse automáticamente.

Deben tratarse como:

```text
LEGACY_OR_CONTAMINATED
```

Hasta decisión humana.

## 10.3 Ejemplos de carpetas legacy o ambiguas

```text
docs_base/
output/
archivo/
old/
legacy/
tmp/
```

## 10.4 Reglas de migración

Antes de mover o eliminar legacy se debe:

1. identificar su contenido;
2. clasificarlo;
3. decidir si pertenece a framework, proyecto vivo o retención externa;
4. registrar la decisión;
5. evitar borrado destructivo sin respaldo o dry-run.

`docs_base/` debe clasificarse como `LEGACY_OR_CONTAMINATED` hasta decisión humana explícita. No puede copiarse, migrarse ni usarse como fuente normativa sin auditoría previa.

---

# 11. Relación con `artifact_manifest.yml`

SPEC-002 no reemplaza el `artifact_manifest.yml`.

SPEC-002 define la estructura esperada.
`artifact_manifest.yml` clasifica la estructura real.

Un validador futuro debe poder comprobar:

```text
1. si las carpetas reales existen donde corresponde;
2. si están clasificadas;
3. si la categoría declarada coincide con la ruta;
4. si una carpeta prohibida aparece versionada;
5. si un proyecto vivo contiene memoria generada desde otro proyecto;
6. si un repositorio madre contiene outputs reales;
7. si hay carpetas no clasificadas.
```

Regla:

```text
Si una carpeta existe pero no está clasificada, el gate debe fallar.
```

---

# 12. Criterios de aceptación

SPEC-002 será aceptable si cumple:

1. No contradice ADR-001.
2. No contradice SPEC-001.
3. Mantiene un proyecto real por repositorio.
4. Mantiene el repositorio madre limpio.
5. No convierte la retención externa en proyecto muerto.
6. No mete proyectos reales dentro del framework.
7. Define claramente qué carpetas pueden existir en el repositorio madre.
8. Define claramente qué carpetas pertenecen solo al proyecto vivo.
9. Define qué carpetas no deben copiarse.
10. Define carpetas temporales y secretas.
11. Ayuda a construir después el `artifact_manifest.yml`.
12. No implementa scripts.
13. No abre ADR-002.
14. No intenta resolver pivotes internos del proyecto vivo.
15. No decide todavía cómo migrar físicamente `output/` ni `docs_base/`.

---

# 13. Fuera de alcance

SPEC-002 no implementa:

* scripts;
* validadores;
* Copier;
* GitHub Template;
* `artifact_manifest.yml`;
* `repo_identity.yml`;
* Plan A;
* Plan B;
* limpieza automática;
* migración física de carpetas;
* eliminación de legacy;
* congelación de proyectos;
* retención externa real;
* ADR-002.

SPEC-002 tampoco decide todavía:

* qué hacer con el `output/` actual;
* qué hacer con `docs_base/`;
* qué hacer con material logístico heredado;
* qué documentos deben moverse a `docs/`;
* qué carpetas actuales deben eliminarse.

---

# 14. Decisiones pendientes

Quedan pendientes para fases posteriores:

1. Auditar y aprobar SPEC-002.
2. Definir si se requiere `repo_identity.yml`.
3. Crear `artifact_manifest.yml` real.
4. Implementar validador del manifiesto.
5. Definir Plan A de creación de proyecto vivo.
6. Definir Plan B de extracción de base limpia.
7. Definir política de migración de `output/`.
8. Definir política de migración de `docs_base/`.
9. Definir retención externa operativa.

## 14.1 Siguientes pasos mínimos sugeridos

1. Auditar SPEC-002 corregida contra ADR-001 y SPEC-001.
2. Aprobar SPEC-002 o devolver ajustes puntuales.
3. Definir SPEC-003 para `repo_identity.yml` o pasar a creación controlada del `artifact_manifest.yml`, según prioridad del Equipo Técnico.
4. Mantener `output/` y `docs_base/` fuera de migración hasta tener manifiesto y política específica.
