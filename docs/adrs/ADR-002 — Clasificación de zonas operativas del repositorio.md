# ADR-002 — Clasificación de zonas operativas del repositorio

## 1. Estado propuesto
*   **Estado:** Aprobado.
*   **Responsable:** Antigravity (Agente operativo de lectura y propuesta) / Equipo Técnico de Saneamiento (Auditor).

## 2. Contexto
El repositorio madre limpio (`framework_mother`) cuenta actualmente con una estructura normativa aprobada compuesta por `docs/adrs/ADR-001 — Repositorio madre limpio y creación de proyectos vivos independientes.md`, `docs/specs/SPEC-001_artifact_manifest.md`, `docs/specs/SPEC-002_estructura_repositorios_carpetas.md` y `docs/specs/SPEC-003_repo_identity.md`. 

Estos documentos definen las bases de la segregación de proyectos y la estructura básica de archivos. Sin embargo, todavía falta una decisión formal que defina la semántica de las **zonas operativas internas** del repositorio madre y las reglas de precedencia e interacciones entre estas zonas cuando se ejecutan procesos automatizados de creación de proyectos, saneamientos o ejecuciones en tiempo de ejecución.

## 3. Problema
El repositorio madre limpio presenta actualmente tres inconsistencias críticas:
1.  **Mezcla de alcances y contaminación sectorial:** Coexisten componentes del framework genérico con datos reales/históricos, código heredado (legacy) y flujos acoplados al caso logístico B2B (Doc-to-Cash).
2.  **Ambigüedad en la granularidad del manifiesto:** El `artifact_manifest.yml` clasifica directorios en general, pero no establece de manera inequívoca las prioridades ni la precedencia de exclusión entre rutas padre e hijas (por ejemplo, si el directorio padre `core/` se permite y copia, pero la subruta `core/templates/` está marcada como excluida/legacy).
3.  **Contradicciones de tiempo de ejecución (Runtime vs Manifiesto):** Scripts de ejecución del framework y componentes del runtime técnico activo (como `init_case.py` y `mock_adapter.py`) consumen recursos alojados en carpetas declaradas como excluidas en el manifiesto actual (como `core/templates/` o `cases/logistica/`).

## 4. Decisión
Definir formalmente estas 9 zonas operativas dentro del repositorio madre limpio (`framework_mother`) para categorizar y aislar conceptualmente la funcionalidad y el flujo de información del sistema:
*   `INPUT`
*   `PROCESS`
*   `OUTPUT`
*   `GOVERNANCE`
*   `RUNTIME`
*   `CASE`
*   `LEGACY`
*   `EVIDENCE`
*   `TEMP`

## 4.1. No consecuencias operativas del ADR-002
*   El ADR-002 no introduce categorías nuevas en `artifact_manifest.yml`.
*   El ADR-002 no modifica la directiva `copy_policy`.
*   El ADR-002 no modifica la directiva `allowed_in_framework`.
*   El ADR-002 no autoriza procesos físicos de copiado, exclusión, migración, eliminación ni promoción de artefactos.
*   El ADR-002 no autoriza refactoring de código, cambios de runtime, cambios en scripts, cambios en tests ni reorganización de la carpeta `.agent/`.
*   El ADR-002 solo aporta una vista conceptual para auditar la coherencia interna, detectar ambigüedades estructurales y preparar el desarrollo técnico de la futura especificación `docs/specs/SPEC-004_artifact_classification.md`.
*   Toda consecuencia operativa, impacto físico o modificación de variables del manifiesto de artefactos deberá formalizarse obligatoriamente en la especificación `docs/specs/SPEC-004_artifact_classification.md` o en una especificación posterior debidamente aprobada.

## 5. Clasificación de Zonas Operativas

### 5.1. INPUT
*   **Qué contiene:** Información aportada directamente por el usuario, fuentes originales del caso práctico, documentos base, hipótesis operativas, datos puros de negocio, respuestas iniciales, evidencia primaria de los procesos y contexto sectorial autorizado a través de la configuración explícita en `case_config`.
*   **Qué no debe contener:** Lógica técnica ejecutable de orquestación, código del framework, secretos locales ni outputs procesados.
*   **¿Puede copiarse a un proyecto vivo?** No (salvo estructuras y ejemplos base de entrada configurados en la plantilla del framework).
*   **¿Puede alimentar el runtime?** Sí, representa la materia prima de información sobre la cual se ejecutan las capacidades de procesamiento.
*   **¿Puede ser fuente normativa?** No.
*   **¿Requiere promoción formal?** Sí, si un documento base de entrada se promueve a plantilla de entrada global o especificación técnica.
*   **Ejemplos de rutas actuales:** Ficheros en `cases/` que contengan datos de entrada iniciales o configuraciones sectoriales autorizadas.

### 5.2. PROCESS
*   **Qué contiene:** La base metodológica del framework, contratos, especificaciones de reglas operativas, prompts de nivel general, especificaciones de workflows lógicos, gates (puertas de decisión), plantillas neutrales (templates) en sedes canónicas, políticas documentales, procedimientos estructurados y capacidades agénticas abstractas no necesariamente ejecutables.
*   **Qué no debe contener:** Código de ejecución técnica activa, orquestadores de runtime, controladores físicos, configuraciones de entorno virtuales, secretos ni datos de negocio de un caso específico.
*   **¿Puede copiarse a un proyecto vivo?** Sí, representa la lógica y el marco metodológico del framework que heredará el proyecto vivo.
*   **¿Puede alimentar el runtime?** Sí, proporcionando la lógica, reglas y prompts que dirigen la ejecución del código.
*   **¿Puede ser fuente normativa?** PROCESS puede contener reglas operativas aplicables por el sistema para su funcionamiento técnico, pero GOVERNANCE sigue siendo la fuente normativa superior para la gobernanza y cumplimiento del repositorio.
*   **¿Requiere promoción formal?** Sí, para la consolidación de nuevos templates neutros o cambios en el flujo de orquestación lógica general. Las plantillas neutrales solo pertenecen a PROCESS cuando estén en una sede canónica aprobada. Esta definición no se debe utilizar para validar `core/templates/`, ya que este directorio sigue estando clasificado como LEGACY hasta que se realice su promoción formal documentada.
*   **Ejemplos de rutas actuales:** [core/](core/), `.agent/skills/` (especificaciones y metadata de skills), `.agent/workflows/` (workflows de orquestación abstractos).

### 5.3. OUTPUT
*   **Qué contiene:** Entregables intermedios y finales generados automáticamente, reportes de salida y artefactos de negocio resultantes del procesamiento de un caso concreto.
*   **Qué no debe contener:** Código base del framework, orquestadores ni documentación normativa de diseño.
*   **¿Puede copiarse a un proyecto vivo?** No.
*   **¿Puede alimentar el runtime?** No.
*   **¿Puede ser fuente normativa?** No, salvo promoción formal.
*   **¿Requiere promoción formal?** Sí, en caso de querer fijar un entregable histórico como plantilla maestra.
*   **Ejemplos de rutas actuales:** `output/bloque_1/`, `output/implementacion/`.

### 5.4. GOVERNANCE
*   **Qué contiene:** La documentación técnica rectora, decisiones de arquitectura (ADRs), especificaciones de diseño (SPECs), el manifiesto de identidad (`repo_identity.yml`) y el manifiesto de artefactos (`artifact_manifest.yml`).
*   **Qué no debe contener:** Lógica ejecutable en tiempo de ejecución, cachés de compilación ni datos de negocio reales del usuario.
*   **¿Puede copiarse a un proyecto vivo?** Sí, en su formato normativo base para regular las operaciones en el repositorio destino.
*   **¿Puede alimentar el runtime?** Sí (el auditor baseline consulta el manifiesto e identidad para aplicar validaciones automáticas).
*   **¿Puede ser fuente normativa?** Sí, es la máxima fuente de gobernanza técnica.
*   **¿Requiere promoción formal?** Sí, a través de gatekeeper técnico y aprobación humana obligatoria.
*   **Ejemplos de rutas actuales:** `docs/adrs/`, `docs/specs/`.

### 5.5. RUNTIME
*   **Qué contiene:** El código ejecutable versionado del sistema, incluyendo el directorio `src/`, scripts ejecutables activos de control, adaptadores (adapters), orquestadores, manejadores de eventos (handlers), cargadores (loaders), la interfaz de línea de comandos (CLI), validadores lógicos y los tests ejecutables del sistema.
*   **Qué no debe contener:** Metodología documental abstracta, carpetas locales de entorno virtual (`.venv/`), cachés del intérprete (`__pycache__/`) ni cachés de pruebas locales.
*   **¿Puede copiarse a un proyecto vivo?** Sí, es el motor ejecutable necesario para el funcionamiento del framework en destino.
*   **¿Puede alimentar el runtime?** Sí, es el propio código que se ejecuta.
*   **¿Puede ser fuente normativa?** No.
*   **¿Requiere promoción formal?** Sí, cualquier modificación en la base ejecutable requiere aprobación y paso por el auditor baseline.
*   **Ejemplos de rutas actuales:** `src/` (excluyendo subrutas legacy), `scripts/` (excluyendo scripts legacy).

### 5.6. CASE
*   **Qué contiene:** Flujos de trabajo específicos (workflows sectoriales), prompts especializados por industria y configuraciones concretas asociadas a un caso de uso particular activo.
*   **Qué no debe contener:** Orquestadores genéricos del framework, código de infraestructura base común.
*   **¿Puede copiarse a un proyecto vivo?** No, a menos que el proyecto vivo tenga exactamente la misma naturaleza y sector del caso, debidamente parametrizado.
*   **¿Puede alimentar el runtime?** Sí, pero **únicamente** cuando el caso está explícitamente activo, declarado mediante `case_config`, no opera como default del framework, no contamina las zonas `PROCESS` ni `RUNTIME`, y no se copia a proyectos vivos de otra naturaleza.
*   **¿Puede ser fuente normativa?** No.
*   **¿Requiere promoción formal?** Sí.
*   **Ejemplos de rutas actuales:** `cases/logistica/`, `.agent/workflows/WORKFLOW_VALIDACION_NEGOCIO.md` (por su acoplamiento sectorial).

### 5.7. LEGACY
*   **Qué contiene:** Archivos históricos, especificaciones previas a la estructuración de la arquitectura limpia de `framework_mother`, plantillas obsoletas o código no saneado.
*   **Qué no debe contener:** Documentos normativos del framework actual ni código activo de runtime en producción.
*   **¿Puede copiarse a un proyecto vivo?** No.
*   **¿Puede alimentar el runtime?** No.
*   **¿Puede ser fuente normativa?** No.
*   **¿Requiere promoción formal?** Sí, obligatoriamente antes de poder ser reutilizado o interactuar con el runtime.
*   **Ejemplos de rutas actuales:** `docs_base/`, `core/templates/`.

### 5.8. EVIDENCE
*   **Qué contiene:** Logs históricos de ejecuciones validadas, reportes del auditor baseline, capturas de verificación de tests de integración, actas de decisiones humanas e históricos de decisiones de saneamiento.
*   **Qué no debe contener:** Lógica funcional activa del software.
*   **¿Puede copiarse a un proyecto vivo?** No.
*   **¿Puede alimentar el runtime?** No.
*   **¿Puede ser fuente normativa?** No.
*   **¿Requiere promoción formal?** Sí.
*   **Ejemplos de rutas actuales:** `docs/evidencias/`, `docs/DECISION_LOG.md`.

### 5.9. TEMP
*   **Qué contiene:** Archivos temporales de pruebas locales, bases de datos SQLite temporales creadas para validaciones en caliente, reportes efímeros, entornos virtuales locales (`.venv/`), cachés del intérprete (`__pycache__/`) y otros metadatos volátiles.
*   **Qué no debe contener:** Código de framework versionado, especificaciones normativas ni datos persistentes de producción.
*   **¿Puede copiarse a un proyecto vivo?** No.
*   **¿Puede alimentar el runtime?** Sí, durante la ejecución dinámica local.
*   **¿Puede ser fuente normativa?** No.
*   **¿Requiere promoción formal?** No (deben quedar como temporales, entorno local o fuera de Git).
*   **Ejemplos de rutas actuales:** `cases/tmp_prueba_case_lifecycle/`, `reports/tmp/`, `.venv/`, `__pycache__/`.

## 6. Reglas de precedencia y promoción
Para evitar conflictos de límites en el repositorio, se aplican de forma estricta las siguientes reglas:
1.  **Prioridad de la ruta específica (subruta):** En caso de conflicto de clasificación entre una carpeta padre y una subruta, prevalecerá siempre la subruta más específica. *(Ejemplo: Si `core/` está categorizado como PROCESS, pero la subruta `core/templates/` está catalogada como LEGACY, la subruta mantendrá de forma estricta el aislamiento de la zona LEGACY).*
2.  **Cuarentena absoluta de LEGACY:** Ningún archivo ubicado físicamente en una zona `LEGACY` podrá ser leído para alimentar prompts agénticos, ejecuciones de runtime o scripts de inicialización sin haber pasado por una promoción formal documentada.
3.  **Promoción formal de OUTPUT y CASE:** Ningún artefacto ubicado en `OUTPUT`, `LEGACY` o un `CASE` histórico puede convertirse en fuente normativa, prompt, workflow, fixture o test base sin una promoción formal documentada.
4.  **Aislamiento sectorial de CASE:** Ninguna configuración, workflow o fichero de datos sectoriales que resida en la zona `CASE` podrá acoplarse ni contaminar los componentes base ubicados en `PROCESS` o en `RUNTIME`.
5.  **Exclusión de TEMP y Entornos Locales:** Ningún recurso ubicado en una zona `TEMP` podrá formar parte del empaquetado de copia para proyectos vivos, ni ser subido al control de versiones (Git).
6.  **Estructura Obligatoria de Promoción Formal:** Toda promoción formal de un archivo o carpeta entre zonas del repositorio debe registrar obligatoriamente los siguientes 9 campos:
    *   **Ruta origen:** Ruta relativa del archivo o directorio de origen.
    *   **Ruta destino propuesta:** Ruta relativa propuesta para el destino final.
    *   **Motivo:** Explicación justificada del cambio de estado.
    *   **Tipo de artefacto:** Definición técnica de su tipología.
    *   **Zona anterior:** Clasificación operativa previa del recurso.
    *   **Zona nueva:** Clasificación operativa asignada tras la promoción.
    *   **Impacto:** Análisis de implicaciones en el runtime, dependencias o prompts.
    *   **Evidencia:** Pruebas técnicas o de dry-run que validen la integridad tras el cambio.
    *   **Aprobación humana:** Aprobación explícitamente firmada del responsable.
7.  **Restricción Normativa Absoluta de Artefactos Históricos:** Ningún artefacto ubicado en la zona `OUTPUT`, `LEGACY` o un `CASE` histórico puede convertirse en fuente normativa, prompt, workflow, fixture o test base sin pasar previamente por el proceso formal de promoción documentado.

## 7. Consecuencias

### 7.1. Qué queda bloqueado hasta aprobar el ADR-002
*   Cualquier saneamiento físico de archivos (limpieza de `docs_base/`, migración de `output/` y eliminación de código).
*   La modificación del runtime técnico (scripts de automatización como `init_case.py` y `mock_adapter.py`) para evitar la propagación de rutas contaminadas.
*   La reorganización de la estructura de skills en `.agent/`.

### 7.2. Qué se podrá hacer tras la aprobación del ADR-002
*   Definir la `docs/specs/SPEC-004_artifact_classification.md` (o similar) para estructurar la clasificación final de artefactos, aplicando las reglas de precedencia y promoción formal.
*   Redactar la especificación para sanear los fixtures sintéticos de prueba neutros y eliminar las referencias del caso logístico B2B del núcleo del framework de forma coordinada.
*   Iniciar la propuesta y diseño de la remoción segura de las carpetas y archivos legacy redundantes basándose en inventarios previos.

### 7.3. Qué riesgos reduce
*   Evita la creación de proyectos vivos que hereden de forma inadvertida datos sectoriales, dependencias legacy o código con secretos locales.
*   Elimina falsos positivos y falsos negativos en el auditor baseline al dotar a los validadores deterministas de un mapa de zonas consistente.
*   Protege la integridad del repositorio frente a operaciones masivas o destructivas.

## 8. Relación con documentos existentes
*   `docs/adrs/ADR-001 — Repositorio madre limpio y creación de proyectos vivos independientes.md`: El ADR-002 complementa la separación funcional entre framework y casos reales mediante el establecimiento de fronteras lógicas internas dentro de `framework_mother`.
*   `docs/specs/SPEC-001_artifact_manifest.md`: Sentará las bases para actualizar la especificación técnica de las categorías del manifiesto conforme a las nuevas 9 zonas.
*   `docs/specs/SPEC-002_estructura_repositorios_carpetas.md`: Alinea la ubicación de las carpetas con la clasificación semántica de las zonas operativas.
*   `docs/specs/SPEC-003_repo_identity.md`: Asegura que las restricciones operativas de la identidad del repositorio se hagan cumplir basándose en el alcance de las zonas.
*   `artifact_manifest.yml` & `repo_identity.yml`: Constituyen la parametrización de datos estructurados de las zonas y permisos declarados en este ADR.

## 9. Decisiones pendientes

### 9.1. Qué hacer con `output/arquitectura/`
Los ficheros de arquitectura `ARQ_05` a `ARQ_10` generados son indispensables para la definición detallada de la arquitectura. Sin embargo, al residir en `output/` (clasificado como `LEGACY_OR_CONTAMINATED` en el manifiesto), están fuera del flujo normativo actual.
*   **Acción requerida:** Requiere inventario previo de todos los archivos de arquitectura generados y una decisión humana para acordar qué elementos conceptuales se integrarán en las especificaciones. Requiere un plan de migración con dry-run antes de moverlos a `docs/specs/` y presentarlos como documentación viva del framework.

### 9.2. Qué hacer con `docs_base/`
Esta zona contiene el dossier histórico legado (`PROYAUTO_DOC_A_DOSSIER.md`).
*   **Acción requerida:** Requiere decisión humana para determinar qué requisitos heredados de negocio B2B se mantienen. Requiere inventario previo detallado de requerimientos, diseño de una especificación en `docs/` y generación de evidencia técnica antes de ejecutar cambios físicos o eliminación de la carpeta original.

### 9.3. Qué hacer con `cases/logistica/`
Representa el caso sectorial con el que se probó el sistema de manera temprana.
*   **Acción requerida:** Requiere un plan de migración con dry-run para aislar formalmente el caso del repositorio madre limpio. Se requiere decisión humana y recopilación de evidencia sobre la desconexión funcional en runtime antes de ejecutar cambios físicos, asegurando que el caso B2B se ubique en un repositorio independiente para pruebas.

### 9.4. Qué hacer con `core/templates/`
Este directorio contradice el manifiesto, ya que es consultado activamente por `init_case.py` a pesar de estar marcado como excluido.
*   **Acción requerida:** Requiere decisión humana para validar la consolidación del directorio de plantillas de primer nivel `templates/` (según define la `docs/specs/SPEC-002_estructura_repositorios_carpetas.md`). Requiere plan de migración con dry-run sobre los scripts de inicialización de runtime y comprobación mediante pruebas unitarias (evidencia física de no afectación) antes de modificar rutas.

### 9.5. Qué hacer con workflows y skills heredadas
*   Las skills requieren un inventario previo y unificación metodológica bajo `docs/specs/` o dentro de `.agent/skills/` con su correspondiente `SKILL.md` estructurado. El contrato ejecutable uniforme de `.agent/skills` y `.agent/workflows` se define en la especificación `docs/specs/SPEC-005_agent_skills_workflows_contract.md`, la cual reserva dicho contrato futuro para evitar ejecuciones o copias prematuras.
*   El fichero `.agent/workflows/WORKFLOW_VALIDACION_NEGOCIO.md`, por su alto acoplamiento sectorial con el caso logístico B2B, requiere decisión humana y plan de migración con dry-run para ser retirado del framework genérico y documentado en el repositorio del caso de uso correspondiente.
*   **Requisitos obligatorios de aprobación:** La matriz de validación `docs/governance/COHERENCIA_CROSSCHECK_ADR-002.md` es un requisito obligatorio para aprobar el ADR-002. Asimismo, la especificación `docs/specs/SPEC-005_agent_skills_workflows_contract.md` establece las directrices de cuarentena para skills y workflows. El ADR-002 no debe pasar al estado de `Aprobado` hasta que ambos artefactos existan, se implementen físicamente y sean debidamente auditados y aprobados por decisión humana. Estos artefactos no autorizan todavía cambios en runtime, `.agent/`, scripts, manifiestos, carpetas legacy ni estructura física del repositorio.

## 10. Checklist de no contradicción
1.  El ADR-002 mantiene el `repo_identity.yml` como la fuente superior y definitiva de identidad del repositorio.
2.  El ADR-002 prohíbe explícitamente el uso de datos reales si el `repo_identity.yml` declara `contains_real_data: false`.
3.  El ADR-002 prohíbe el procesamiento de datos de caso si el `repo_identity.yml` declara `allows_case_data: false`.
4.  El ADR-002 respeta y valida el `artifact_manifest.yml` como el contrato técnico operativo de copiado, exclusión y validaciones automatizadas del baseline.
5.  El ADR-002 no altera la política de copiado (`copy_policy`) desde el propio texto de este ADR.
6.  El ADR-002 respeta en su totalidad el `docs/adrs/ADR-001 — Repositorio madre limpio y creación de proyectos vivos independientes.md` sobre segregación de entornos.
7.  El ADR-002 respeta las directrices de la `docs/specs/SPEC-001_artifact_manifest.md` como especificación rectora del manifiesto.
8.  El ADR-002 se ajusta y respeta la estructura de carpetas definida en la `docs/specs/SPEC-002_estructura_repositorios_carpetas.md`.
9.  El ADR-002 respeta la definición de identidad detallada en la `docs/specs/SPEC-003_repo_identity.md`.
10. El ADR-002 deja cualquier cambio operativo e impacto real sobre el manifiesto de artefactos supeditado al desarrollo y aprobación formal de la futura `docs/specs/SPEC-004_artifact_classification.md` o una especificación posterior debidamente aprobada.

---

## EVIDENCIA CONSULTADA
1.  `README.md`
2.  `AGENTS.md`
3.  `repo_identity.yml`
4.  `artifact_manifest.yml`
5.  `docs/adrs/ADR-001 — Repositorio madre limpio y creación de proyectos vivos independientes.md`
6.  `docs/specs/SPEC-001_artifact_manifest.md`
7.  `docs/specs/SPEC-002_estructura_repositorios_carpetas.md`
8.  `docs/specs/SPEC-003_repo_identity.md`
9.  `scripts/audit_repo_baseline.py`
