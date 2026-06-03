# Skill: audit_repo_baseline

## Propósito
Auditar de forma no destructiva si el repositorio actual puede operar como `framework_mother` antes de proceder con el diseño y creación del manifiesto de artefactos (`artifact_manifest.yml`).

## Cuándo usar este skill
Este skill debe invocarse obligatoriamente antes de:
*   Crear o modificar el archivo `artifact_manifest.yml` real.
*   Clasificar el baseline de archivos y carpetas del repositorio madre.
*   Ejecutar cualquier proceso de limpieza física de directorios.
*   Iniciar una extracción de base limpia (Plan B).
*   Preparar auditorías de conformidad sobre la estructura del framework.

## Entradas esperadas
*   El archivo de identidad `repo_identity.yml` en la raíz del repositorio.
*   Los documentos normativos en `docs/specs/` (`SPEC-001`, `SPEC-002`, `SPEC-003`).
*   La estructura física actual de directorios del working tree.

## Procedimiento operativo
1.  **Ejecutar el script determinista:**
    Ejecutar el script de diagnóstico desde la raíz del workspace:
    ```bash
    python scripts/audit_repo_baseline.py
    ```
2.  **Capturar la salida estándar:**
    Recuperar toda la salida de consola producida por la ejecución del script.
3.  **Localizar y extraer el bloque JSON:**
    Identificar las marcas delimitadoras `=== JSON_START ===` y `=== JSON_END ===` e indexar únicamente el JSON intermedio.
4.  **Generar el reporte de interpretación:**
    El agente de IA interpreta el contenido del JSON y el reporte de texto sin modificar el estado físico del repositorio.
5.  **Validación del Gatekeeper:**
    Un agente en rol de Gatekeeper evalúa si la interpretación y el paso sugerido son correctos basándose en las reglas de transición y la presencia de bloqueos.
6.  **Revisión Humana Final:**
    El usuario final audita el reporte conjunto para validar el avance.

## Interpretación de exit codes
*   **Exit code 0 = PASS:** Aprobado sin observaciones. El repositorio cumple estrictamente con el baseline.
*   **Exit code 1 = PASS_WITH_WARNINGS:** Aprobado con advertencias. No es un fallo del script. Indica presencia de elementos temporales o zonas legacy permitidas en la fase actual del baseline de la gobernanza. El agente debe revisar y validar cada advertencia individualmente.
*   **Exit code 2 = FAIL:** Bloqueo de conformidad. Indica presencia de archivos versionados prohibidos (`.env`, `.venv/`, `__pycache__/`), especificaciones desaprobadas o campos incompatibles de identidad.

## Contrato del JSON
El bloque delimitado por `JSON_START` y `JSON_END` es el contrato de datos estructurados de la auditoría. Toda la lógica interpretativa del agente y el veredicto del Gatekeeper debe apoyarse y citar exclusivamente este bloque, cuya clave `checks` detalla la conformidad del sistema.

## Rol del agente intérprete
*   **Apego estricto a los hechos:** Debe citar únicamente datos contenidos en el JSON. Está estrictamente prohibido asumir, inventar, complementar o maquillar hechos.
*   **No intervención:** No debe intentar modificar ni proponer la corrección de archivos durante este paso de lectura.
*   **Respeto funcional de la severidad:** Está prohibido reinterpretar un resultado de `FAIL` como aceptable o simular que una advertencia crítica es información general.

## Rol del gatekeeper
El rol del Gatekeeper es actuar como auditor de la interpretación agéntica:
*   Verifica que el script Python se ejecutó y produjo salida.
*   Comprueba la presencia e integridad del bloque JSON.
*   Valida que la traducción del agente no agregue alucinaciones ni asuma supuestos no declarados por el script.
*   Asegura que el veredicto de transición seleccionado por el agente cumpla estrictamente con las reglas de decisiones del Gatekeeper.

## Decisiones del gatekeeper
El Gatekeeper debe dictaminar uno de estos cuatro estados exactamente:
*   `APPROVED_TO_CONTINUE`: Si el script da `PASS` (exit 0) o `PASS_WITH_WARNINGS` (exit 1) con todas las advertencias identificadas como aceptables bajo la gobernanza documental actual (ej. zonas legacy esperables).
*   `HUMAN_DECISION_REQUIRED`: Si el script da `PASS_WITH_WARNINGS` (exit 1) pero se detecta alguna anomalía local no contemplada en las reglas estándar del baseline.
*   `BLOCKED`: Si el script da `FAIL` (exit 2). Cualquier acción automatizada posterior queda estrictamente bloqueada.
*   `RE_RUN_REQUIRED`: Si el JSON está ausente, incompleto o si se requiere ejecutar nuevamente la verificación tras corregir una desviación de conformidad.

## Formato obligatorio del reporte
El reporte final presentado al Gatekeeper y al humano debe estructurarse obligatoriamente de la siguiente manera:
1.  **Resultado de la auditoría:** (`PASS`, `PASS_WITH_WARNINGS` o `FAIL`).
2.  **Exit code obtenido:** (`0`, `1` o `2`).
3.  **Errores bloqueantes detectados:** (Lista explícita del JSON. Si no hay, poner "Ninguno").
4.  **Advertencias (Warnings) detectadas:** (Lista explícita del JSON. Si no hay, poner "Ninguna").
5.  **Información general (Info) detectada:** (Lista explícita del JSON. Si no hay, poner "Ninguna").
6.  **Interpretación del Agente:** Análisis del contexto de los hallazgos sin alucinaciones.
7.  **Decisión del Gatekeeper:** (Estrictamente uno de los cuatro estados del Gatekeeper).
8.  **Justificación de la decisión:** Explicación técnica de por qué se asignó ese estado.
9.  **Siguiente paso recomendado:** Acción inmediata a tomar.
10. **Confirmación de no modificación:** Declaración formal de que no se ha modificado ningún archivo del repositorio.

## Prohibiciones
*   No borrar archivos ni carpetas.
*   No mover archivos.
*   No limpiar ni vaciar directorios legacy (`docs_base/`, `output/`).
*   No crear ni modificar `artifact_manifest.yml`.
*   No crear, sobrescribir ni modificar `repo_identity.yml`.
*   No modificar especificaciones (`SPEC-001`, `SPEC-002`, `SPEC-003`).
*   No realizar `git add`.
*   No realizar commits ni push.

## Criterios de éxito
El skill se ha ejecutado con éxito si el reporte final representa con exactitud la salida del validador determinista y provee al humano un diagnóstico claro, estructurado y auditable sobre el estado de conformidad del baseline del framework.
