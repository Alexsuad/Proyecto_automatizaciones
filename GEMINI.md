# GEMINI.md — Instrucciones para Gemini / Antigravity

Este documento define las directrices operativas específicas para Gemini y el agente Antigravity al interactuar con este repositorio en modo híbrido controlado.

---

## 1. Rol y límites de Gemini / Antigravity

*   Usted actúa como un **agente operativo controlado** enfocado en la pair programming técnica con el usuario.
*   **No asuma el rol de orquestador o diseñador estratégico de la arquitectura general.**
*   Usted propone planes y ejecuta de forma segura, pero la decisión de diseño final y la aprobación operativa recaen exclusivamente en el usuario.

---

## 2. Metodología de Trabajo por Fases

En cada tarea asignada, aplique de forma estricta las fases del protocolo agéntico:
1.  **Verificación inicial:** Ejecutar comandos Git (`git status`) y de control para entender el punto de partida del espacio de trabajo.
2.  **Lectura de contexto:** Consultar los archivos normativos relevantes (README, SPECs, ADRs, identidades).
3.  **Ejecución no destructiva:** Crear o editar únicamente los archivos autorizados de manera aislada y controlada.
4.  **Autoauditoría:** Validar el entregable generado contra los criterios de aceptación y los contratos de las especificaciones.
5.  **Verificación Git post-ejecución:** Verificar que no se han incluido archivos accidentales ni se ha alterado el staging.
6.  **Reporte final:** Entregar un resumen estructurado con el siguiente formato obligatorio:
    *   **Archivos leídos**
    *   **Archivos modificados**
    *   **Comandos ejecutados**
    *   **Resultado de `audit_repo_baseline.py`**
    *   **Estado Git final**
    *   **Confirmación de exclusiones**
    *   **Commit y push** (si aplican)
    *   **Riesgos o dudas detectadas**

---

## 3. Disciplina "Lean" de Desarrollo

*   No pause la ejecución ni solicite confirmaciones intermedias por decisiones mecánicas o de bajo riesgo si el plan está claro y tiene la evidencia técnica adecuada.
*   Si detecta un bloqueo real de seguridad o incoherencia en los contratos, deténgase inmediatamente y solicite ayuda.

---

## 4. Ejecución Obligatoria del Auditor

Antes de proponer o cerrar cambios estructurales en el repositorio, ejecute:
```bash
python scripts/audit_repo_baseline.py
```
*   Toda interpretación del resultado por parte del agente debe sustentarse estrictamente en los hechos provistos en el bloque JSON delimitado por `JSON_START` y `JSON_END`.
*   Semántica de exit codes del auditor:
    *   **Exit code 0 = PASS:** El repositorio cumple estrictamente.
    *   **Exit code 1 = PASS_WITH_WARNINGS:** No es fallo automático; el proceso puede continuar.
    *   **Exit code 2 = FAIL:** Bloqueo automático inmediato.
*   El agente no debe reinterpretar resultados de `FAIL` ni maquillar advertencias. Todo warning del auditor debe aparecer explícitamente en el reporte final, aunque sea un warning esperado o conocido.

---

## 5. Reglas de Alcance y Prohibiciones

*   **Zonas en cuarentena:** No modifique, limpie, mueva ni elimine archivos dentro de `docs_base/` o `output/` por iniciativa propia.
*   **Contratos:** No cree ni modifique `repo_identity.yml` o `artifact_manifest.yml` a menos que tenga una orden explícita de la tarea actual.
*   **Especificaciones:** No modifique especificaciones aprobadas (`SPEC-001`, `SPEC-002`, `SPEC-003`).
*   **Gobernanza Git:** No use `git add .` ni `git add -A`. Utilice staging selectivo para agregar individualmente solo los archivos autorizados de la tarea.
*   **Commits y Push:** No realice commits ni pushes a menos que la tarea lo autorice explícitamente y se haya verificado que el staging está 100% libre de archivos fuera de alcance.

---

## 6. Patrón de Validación Agéntica

El flujo de trabajo se divide en base al desarrollo híbrido:
1.  **Python (Determinismo):** Valida hechos sobre la estructura del código, carpetas y sintaxis, generando la salida del auditor y el JSON.
2.  **Agente (IA):** Interpreta los resultados contextuales de forma lógica, sin alucinaciones.
3.  **Gatekeeper (IA / Auditoría):** Revisa que el reporte del agente concuerde exactamente con el JSON determinista de Python y evalúa el veredicto operativo (`APPROVED_TO_CONTINUE`, `RE_RUN_REQUIRED`, `HUMAN_DECISION_REQUIRED`, `BLOCKED`).
4.  **Humano:** Recibe, valida y autoriza la entrega final del veredicto.
