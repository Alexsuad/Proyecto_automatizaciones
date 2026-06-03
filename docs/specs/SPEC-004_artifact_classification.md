# SPEC-004 — Clasificación fina de artefactos y políticas operativas por zonas

## 1. Estado
*   **Estado:** Propuesto / Pendiente de aprobación humana.
*   **Responsable:** Antigravity (Agente operativo de lectura y propuesta) / Equipo Técnico de Saneamiento (Auditor).

## 2. Propósito
Definir la correspondencia técnica y las reglas de mapeo entre la clasificación conceptual de zonas operativas de `ADR-002` y el contrato operativo del manifiesto de artefactos `artifact_manifest.yml`. Este documento establece las restricciones de gobernanza necesarias para preparar el saneamiento de forma documental y la re-auditoría automatizada del repositorio, sin autorizar ni ejecutar cambios de runtime o modificaciones físicas de manera inmediata.

## 2.1. Alcance Normativo y No Alteración
Esta especificación se limita a actuar como un puente de interpretación conceptual y ordenamiento normativo. La `SPEC-004` **no altera** los contratos ni esquemas definidos en la `SPEC-001` ni las directrices operativas vigentes en `artifact_manifest.yml`. Cualquier cambio técnico sobre la estructura del manifiesto o políticas reales deberá implementarse mediante una actualización directa del manifiesto tras su aprobación formal por gatekeeper.

## 3. Relación con documentos existentes
La `SPEC-004` depende y se coordina de manera directa con los siguientes documentos rectores del repositorio:
*   `docs/adrs/ADR-002 — Clasificación de zonas operativas del repositorio.md` (Define el marco conceptual de las 9 zonas operativas).
*   `docs/specs/SPEC-001_artifact_manifest.md` (Especificación del esquema del manifiesto y reglas de categorías).
*   `docs/specs/SPEC-002_estructura_repositorios_carpetas.md` (Define la estructura física canónica de carpetas).
*   `docs/specs/SPEC-003_repo_identity.md` (Define la especificación de identidad y gatekeeper del repositorio).
*   `docs/specs/SPEC-005_agent_skills_workflows_contract.md` (Establece la cuarentena y contrato provisional de skills y workflows).
*   `artifact_manifest.yml` (Contrato de artefactos activo en la raíz).
*   `repo_identity.yml` (Manifiesto de identidad activo).

## 4. Regla central
Las zonas operativas conceptuales definidas en `ADR-002` **no reemplazan** las categorías técnicas de clasificación de archivos del manifiesto `artifact_manifest.yml`. 

La `SPEC-004` actúa como el puente formal entre ambas capas, traduciendo la semántica de la zona al comportamiento determinista esperado por los scripts de automatización:
```text
Zona Operativa (ADR-002) → Categoría (artifact_manifest.yml) → copy_policy → allowed_in_framework → requires_audit → can_update_from_framework
```

## 5. Tabla de correspondencia mínima

| Zona operativa (ADR-002) | Categorías permitidas (`artifact_manifest.yml`) | `copy_policy` permitido | `allowed_in_framework` esperado | `can_update_from_framework` esperado | `requires_audit` esperado | Observaciones | Riesgo si se clasifica mal |
|---|---|---|---|---|---|---|---|
| **INPUT** | `USER_INPUT` | `skip` | `false` | `false` | `true` | Los datos `USER_INPUT` se omiten con `skip`. La estructura vacía de inputs se genera mediante `generate_empty` cuando esté definida en el manifest como scaffolding aprobado. | Fuga de datos de clientes en el framework base o clonación de variables estáticas. |
| **PROCESS** | `FRAMEWORK_BASE`, `FRAMEWORK_CONFIG`, `TEMPLATE_CASE` | `copy`, `generate_empty` | `true` | `true` | `true` (en config) / `false` (en base) | Base metodológica, reglas, plantillas neutras y prompts globales. | Copia de prompts corruptos o workflows inestables sin pasar por gatekeeper. |
| **OUTPUT** | `AGENT_GENERATED_OUTPUT` | `skip` | `false` | `false` | `true` | Salidas históricas resultantes de ejecuciones. | Contaminación del repositorio madre con ficheros de salida locales. |
| **GOVERNANCE** | `FRAMEWORK_CONFIG`, `PROJECT_IDENTITY` | `copy`, `generate_empty` | `true` (en config) / `false` (en identity) | `true` (en config) / `false` (en identity) | `true` | Documentos rectores, ADRs, SPECs e identidades. | Pérdida de control de versión de políticas operativas o bypass del gatekeeper. |
| **RUNTIME** | `FRAMEWORK_BASE` | `copy` | `true` | `true` | `true` (ante cambios) / `false` (en ejecuciones estándar) | Código ejecutable versionado (`src/`, scripts activos). | Ejecución de utilidades legacy o adapters sectoriales contaminados. |
| **CASE** | `LEGACY_OR_CONTAMINATED` | `exclude` | `false` | `false` | `true` | Caso sectorial acoplado y workflows específicos. | Contaminación sectorial de un caso sobre proyectos de otra naturaleza. |
| **LEGACY** | `LEGACY_OR_CONTAMINATED` | `exclude` | `false` | `false` | `true` | Carpetas heredadas en cuarentena sin saneamiento. | Copiado de dependencias u plantillas obsoletas a proyectos vivos. |
| **EVIDENCE** | `PROJECT_REPORTS`, `PROJECT_CHANGES` | `skip` | `false` | `false` | `true` | Reportes de QA, auditoría de fases e historial de decisiones. | Pérdida de trazabilidad de cambios estructurales o copia de reportes históricos. |
| **TEMP** | `TEMP_RUNTIME`, `LOCAL_SECRETS` | `skip` | `false` | `false` | `true` (en secrets) / `false` (en temp) | Ficheros temporales, entornos `.venv` y variables `.env`. | Fuga de secretos locales (API keys, claves) o cachés residuales subidos a Git. |

### 5.1. Aclaración técnica sobre directivas de `copy_policy` por Perfiles Operativos:
Las directivas de copiado y exclusión se formalizan bajo dos perfiles diferenciados:
*   **Perfil A (Scaffolding de `live_project`):** Regula la creación e inicialización de un nuevo proyecto vivo a partir del repositorio madre `framework_mother`. La `SPEC-004` regula **por defecto** este perfil, aplicando:
    *   `skip`: El recurso no se copia al nuevo proyecto por no formar parte de la base neutra (ej. inputs/outputs/reportes históricos), pero su existencia es válida en la ejecución del entorno.
    *   `exclude`: El recurso no se copia y además representa una zona prohibida, contaminada, local, secreta, temporal o legacy que requiere bloqueo o revisión.
*   **Perfil B (Retención externa / Freeze / Backup / Archivo histórico de evidencias):** Regula los escenarios de congelamiento de estado, exportación de reportes de calidad y archivo histórico en frío de evidencias de ejecución. Este perfil **no queda gobernado** por las directivas de scaffolding de la `SPEC-004` y requiere una especificación posterior o perfil operativo separado.

*Aclaración de evidencias en Scaffolding:* Para el Perfil A, `PROJECT_REPORTS` y `PROJECT_CHANGES` se definen en `skip` porque el nuevo proyecto no debe heredar reportes de calidad previos. Esto no supone una pérdida de trazabilidad documental, sino que restringe la copia automática al scaffolding de destino. Toda exportación o freeze (Perfil B) se regirá por políticas externas exclusivas.

*Aclaración de inputs en Scaffolding:* Para el Perfil A, no se copian datos reales del usuario (`USER_INPUT` queda en `skip`). Si en el manifiesto se define la generación de carpetas vacías como scaffolding aprobado, esta acción se ejecuta mediante `generate_empty` y se trata como una regla estructural y no como copiado de datos. Las plantillas de inputs vacíos neutros se obtienen exclusivamente del directorio `templates/`.

## 6. Reglas de precedencia
1.  **Regla de la subruta específica:** Si una ruta padre y una subruta tienen clasificaciones en zonas o categorías distintas en el manifiesto, prevalecerá siempre la subruta más específica por encima de la regla general de la ruta padre.
2.  **Precedencia absoluta de Identidad:** La declaración de identidad en `repo_identity.yml` prevalece sobre cualquier clasificación de zona en caso de conflicto operativo. *(Ejemplo: Si una zona permite datos de caso, pero `repo_identity.yml` declara `allows_case_data: false`, prevalece la prohibición absoluta de la identidad).*
3.  **Contrato operativo vigente:** El archivo `artifact_manifest.yml` sigue siendo el contrato técnico único y vigente del repositorio. La `SPEC-004` no lo modifica de forma directa hasta que esta especificación sea aprobada por decisión humana y se implemente el cambio en el manifiesto.
4.  **No operatividad física del ADR-002:** El `ADR-002` es una declaración conceptual de zonas y no autoriza de forma autónoma limpiezas físicas, refactors ni modificaciones sobre el sistema.
5.  **Aislamiento físico de la SPEC-004:** La `SPEC-004` tampoco autoriza saneamientos, movimientos ni borrados físicos en el working tree del repositorio hasta que se formalice un plan de saneamiento posterior acompañado de un dry-run documentado.

## 7. Políticas por categoría

### 7.1. `FRAMEWORK_BASE`
*   **Finalidad:** Código fuente común, scripts de control general, dependencias base y utilidades transversales.
*   **Zonas compatibles:** `RUNTIME`, `PROCESS`.
*   **Políticas permitidas:** `copy_policy: "copy"`.
*   **¿Puede copiarse a proyecto vivo?** Sí.
*   **¿Puede actualizarse desde framework?** Sí.
*   **¿Requiere auditoría?** Sí, el auditor baseline lo verifica de manera automatizada siempre que existan cambios en el código.
*   **Ejemplos de rutas:** `src/`, `scripts/` (excluyendo legacy).
*   **Errores comunes:** Introducir variables de negocio o rutas locales hardcodeadas en los scripts.

### 7.2. `FRAMEWORK_CONFIG`
*   **Finalidad:** Configuración y reglas operativas metodológicas generales.
*   **Zonas compatibles:** `GOVERNANCE`, `PROCESS`.
*   **Políticas permitidas:** `copy_policy: "copy"`.
*   **¿Puede copiarse a proyecto vivo?** Sí.
*   **¿Puede actualizarse desde framework?** Sí.
*   **¿Requiere auditoría?** Sí, obligatoria ante cualquier modificación.
*   **Ejemplos de rutas:** `.agent/`, `docs/adrs/`.
*   **Errores comunes:** Incluir workflows específicos de un caso (como logística) como si fueran workflows genéricos del framework.

### 7.3. `LEGACY_OR_CONTAMINATED`
*   **Finalidad:** Recursos y carpetas históricas pendientes de análisis de saneamiento o que contienen datos contaminados.
*   **Zonas compatibles:** `LEGACY`, `CASE`.
*   **Políticas permitidas:** `copy_policy: "exclude"` (durante el proceso transitorio) / `ask_before_copy` (en frío).
*   **¿Puede copiarse a proyecto vivo?** No.
*   **¿Puede actualizarse desde framework?** No.
*   **¿Requiere auditoría?** Sí, con carácter de bloqueo.
*   **Ejemplos de rutas:** `docs_base/`, `output/`, `cases/logistica/`.
*   **Errores comunes:** Leer recursos legacy directamente desde el runtime activo.

### 7.4. `TEMP_RUNTIME`
*   **Finalidad:** Entornos locales, cachés de compilación e intérprete y reportes efímeros.
*   **Zonas compatibles:** `TEMP`.
*   **Políticas permitidas:** `copy_policy: "exclude"` / `skip`.
*   **¿Puede copiarse a proyecto vivo?** No.
*   **¿Puede actualizarse desde framework?** No.
*   **¿Requiere auditoría?** No.
*   **Ejemplos de rutas:** `.venv/`, `__pycache__/`, `cases/tmp_*/`.
*   **Errores comunes:** Versionar las carpetas temporales de compilación o de entornos locales.

## 8. Tratamiento de `LEGACY_OR_CONTAMINATED`
Existe una tensión conceptual entre el manifiesto actual (que aplica `copy_policy: "exclude"` para rutas legacy) y la especificación `SPEC-001` (que define `copy_policy: "ask_before_copy"` para la categoría `LEGACY_OR_CONTAMINATED`). 

### Decisión normativa: Recomendación de la Opción C (Subtipificación de Legacy)
Se determina que la mejor solución es implementar la **Opción C**, la cual distingue de manera conceptual los siguientes subtipos dentro de la categoría legacy para facilitar la toma de decisiones:
1.  **`legacy_excluido`:** Rutas con código contaminado o datos del caso B2B de logística que no deben copiarse nunca (`copy_policy: "exclude"`).
2.  **`legacy_promovible`:** Documentos de arquitectura o plantillas obsoletas que contienen valor de ingeniería y que deben migrar a `GOVERNANCE` o `PROCESS` mediante un plan documentado.
3.  **`legacy_retenible`:** Actas e informes de decisiones históricas de negocio que no deben copiarse pero sí retenerse en el histórico local de evidencias (`copy_policy: "ask_before_copy"`).

*Aclaración de Gobernanza:* Estos subtipos son una clasificación conceptual propuesta para la fase de inventario y saneamiento futuro, no categorías activas actuales en `artifact_manifest.yml`. Se podrán registrar temporalmente en el campo de `notes` de cada entrada, pero no como nombres de categorías del manifiesto. Cualquier incorporación futura de estos subtipos como campos reales, categorías o políticas operativas requerirá una actualización explícita y formal de la `SPEC-001`, de `artifact_manifest.yml` o de una SPEC posterior aprobada.

*Justificación:* Esta opción evita que el framework copie componentes legacy por error al automatizar la creación de proyectos vivos, a la vez que proporciona a los humanos un mapa preciso de cuáles deben excluirse, conservarse como histórico, promoverse o someterse a una decisión humana posterior.

## 9. Reglas para promoción formal
Para realizar cualquier cambio de estado o ubicación física de un artefacto, se debe registrar obligatoriamente una bitácora de promoción que contenga:
*   **Ruta origen:** Ruta relativa del artefacto.
*   **Ruta destino propuesta:** Nueva ubicación física canónica.
*   **Zona anterior:** Clasificación conceptual previa.
*   **Zona nueva:** Nueva clasificación propuesta.
*   **Categoría anterior:** Categoría en el manifiesto.
*   **Categoría nueva:** Categoría de destino en el manifiesto.
*   **Motivo:** Justificación técnica de la promoción.
*   **Impacto:** Análisis de implicaciones de dependencias.
*   **Evidencia:** Pruebas técnicas (dry-run, tests de compilación).
*   **Aprobación humana:** Firma y autorización explícita del responsable.
*   **Validación posterior:** Ejecución del auditor baseline para asegurar que el cambio mantiene el estado en `PASS`.

## 10. Reglas para proyectos vivos (Scaffolding)
Al instanciar un nuevo `live_project` desde el repositorio madre limpio (`framework_mother`), el script de clonación y aprovisionamiento debe cumplir las siguientes reglas:
*   **Exclusión absoluta de datos reales:** Queda prohibido copiar cualquier fichero con datos reales del usuario. La categoría `USER_INPUT` (datos del usuario o fuentes del caso real) siempre debe ignorarse en la copia (`copy_policy: skip`).
*   **Estructura de entrada vacía:** Sí se permite y se recomienda la generación de carpetas vacías de entrada para el scaffolding de destino de forma automatizada mediante la regla `generate_empty` en el manifiesto. Esta generación se considera una regla de scaffolding autorizada y de higiene, nunca un copiado de datos `USER_INPUT`.
*   **Uso de plantillas neutras:** Se permite el copiado de plantillas de caso neutras aprobadas alojadas en la sede canónica `templates/`.
*   **Exclusión de outputs históricos:** La carpeta `output/` no debe copiarse.
*   **Exclusión de casos sectoriales:** Ficheros específicos de casos (como `cases/logistica/`) no deben formar parte del scaffolding base.
*   **Respeto al manifiesto:** Toda operación de copiado o exclusión física debe ser dictada exclusivamente por las directivas declaradas en `artifact_manifest.yml`.

## 11. Reglas para `.agent/`
En estricta conformidad con `SPEC-005` y `SPEC-003`:
*   Los contenidos de `.agent/skills/` y `.agent/workflows/` se mantienen clasificados en la zona `PROCESS` como **operativo provisional**.
*   Cualquier cambio en el estatus operacional o la habilitación de ejecución de runtime de estas habilidades dependerá exclusivamente de las condiciones definidas en `SPEC-005` y del cumplimiento del gatekeeper de `SPEC-003`.
*   Se prohíbe cualquier reorganización de estas carpetas en esta fase.
*   Ninguno de estos archivos o prompts puede ejecutarse como contrato runtime formal.
*   Queda prohibido copiar de forma indiscriminada a proyectos vivos los flujos provisionales.
*   Cualquier workflow acoplado sectorialmente (como `WORKFLOW_VALIDACION_NEGOCIO.md`) requiere su correspondiente plan de migración y reclasificación antes de ser considerado parte oficial del framework.

## 11.1. Reglas para `PROJECT_IDENTITY`
*   **Uso de `copy`:** Se utilizará la directiva de copiado únicamente para esquemas de identidad vacíos, manuales de perfiles e instrucciones generales del framework que deban replicarse en el destino para regular el nuevo repositorio.
*   **Uso de `generate_empty`:** Se utilizará para la identidad particular y parametrización específica de cada caso de negocio, asegurando que el nuevo repositorio sea inicializado con un manifiesto e identidad limpios y exclusivos de su instancia de ejecución.

## 12. Validaciones futuras del auditor baseline
Se propone que en versiones posteriores del validador determinista (utilizando como ejemplo de referencia el script `scripts/audit_repo_baseline.py`) se implementen los siguientes controles automáticos:
*   **Validación de campos obligatorios:** Comprobar que ninguna entrada del manifiesto carezca de los campos definidos en `SPEC-001`.
*   **Validación de coherencia interna:** Comprobar que `category` coincida con las directrices de `copy_policy`.
*   **Validación de precedencia de subrutas:** Asegurar que las exclusiones específicas de subrutas prevalezcan sobre los permisos de carpetas padres.
*   **Detección de contaminación legacy:** Lanzar advertencias o fallos si existen referencias directas a rutas legacy en los scripts del runtime.
*   **Detección de workflows sectoriales:** Auditar los archivos de prompts en `.agent/` para advertir sobre la presencia de palabras clave acopladas a logística o casos históricos.
*   **Auditoría de Owners y Metadatos:** Comprobar que todas las entradas de `artifacts` contengan los campos `owner` y `can_update_from_framework`.

## 13. Bloqueos
Hasta que la `SPEC-004` sea aprobada formalmente por decisión humana, quedan bloqueadas las siguientes acciones operativas:
*   La limpieza física de archivos en `docs_base/` o en `output/`.
*   La modificación del runtime técnico (scripts y adapters activos).
*   El movimiento de carpetas en el working tree del repositorio.
*   La reorganización de la carpeta `.agent/`.
*   La modificación de la directiva `copy_policy` en el manifiesto de artefactos.
*   Cambiar el `manifest_status` a `approved` en `artifact_manifest.yml`.
*   Aprobar el `ADR-002` como documento definitivo.

## 14. Criterio de cierre de SPEC-004
La `SPEC-004` se considera completada y lista para su revisión final si:
1.  Define de forma clara la matriz de correspondencia zona → categoría.
2.  Establece las reglas de precedencia y promoción formal de artefactos.
3.  Resuelve normativamente el tratamiento de la categoría `LEGACY_OR_CONTAMINATED` mediante subtipos conceptuales.
4.  No contradice las especificaciones técnicas `SPEC-001`, `SPEC-002` ni `SPEC-003`.
5.  No contradice los permisos y restricciones de `repo_identity.yml`.
6.  No autoriza ninguna modificación física o de runtime de manera autónoma.
7.  Precisa que toda acción física debe supeditarse a un plan de saneamiento posterior con ejecución de dry-run y auditoría de evidencias.
8.  La aprobación de la `SPEC-004` no ejecuta ni autoriza por sí sola cambios físicos. Solo habilita la redacción posterior de un plan de saneamiento formal con dry-run, evidencias y aprobación humana explícita.
