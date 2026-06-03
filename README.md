# Proyecto_automatizaciones

Repositorio maestro y base normativa para el diseño, validación y control de un framework estructurado de automatización, gobernanza y creación controlada de proyectos vivos independientes.

---

## 1. Qué es este repositorio

Este repositorio es un **repositorio madre limpio** (`framework_mother`). Funciona como la sede de gobernanza técnica y metodológica. El baseline versionado del framework no debe contener datos reales activos. Las zonas legacy detectadas en el working tree o clasificadas en el manifiesto no forman parte del framework limpio y están excluidas de copia/reutilización. Su propósito es definir:
*   Las decisiones de arquitectura y la gobernanza documental (ADRs y SPECs).
*   La estructura de directorios y reglas físicas del ecosistema.
*   El runtime y los scripts técnicos base para la auditoría de conformidad.
*   Los contratos para la creación de proyectos vivos independientes (`live_project`).

---

## 2. Qué NO es este repositorio

Este repositorio:
*   **No contiene datos reales ni memoria de proyectos vivos activos en su baseline limpio.**
*   **No es un espacio de almacenamiento para el runtime de ejecución de casos de negocio.**
*   **No es un producto cerrado para producción.**
*   **No está diseñado para recibir datos operativos sin control.**
*   Las carpetas legacy (`docs_base/`, `output/`) y el caso histórico (`cases/logistica/`) son zonas transicionales en cuarentena, no representativas del framework limpio.

---

## 3. Rol del Repositorio (repo_identity.yml)

La identidad operativa global de este repositorio está declarada formalmente en `repo_identity.yml` con el perfil:
*   `repo_role: framework_mother`
*   `repo_status: active`
*   `contains_real_data: false`
*   `allows_project_creation: true`
*   `allows_case_data: false`

Cualquier operación automática que viole esta identidad (ej. intentar guardar datos reales o ejecutar limpiezas de proyectos vivos aquí) será bloqueada de inmediato por la automatización.

---

## 4. Gobernanza Documental Aprobada

El diseño y ciclo de vida del repositorio se rigen por los siguientes contratos oficiales:
*   **[ADR-001](docs/adrs/ADR-001%20%E2%80%94%20Repositorio%20madre%20limpio%20y%20creaci%C3%B3n%20de%20proyectos%20vivos%20independientes.md):** Define la separación física del repositorio madre y la creación de proyectos vivos independientes de forma no contaminada.
*   **[SPEC-001](docs/specs/SPEC-001_artifact_manifest.md):** Especifica el contrato de `artifact_manifest.yml` para clasificar y excluir artefactos en procesos de migración y copia.
*   **[SPEC-002](docs/specs/SPEC-002_estructura_repositorios_carpetas.md):** Establece la estructura física obligatoria de carpetas del repositorio madre.
*   **[SPEC-003](docs/specs/SPEC-003_repo_identity.md):** Establece el contrato de identidad de `repo_identity.yml`.

---

## 5. Archivos Operativos y de Auditoría

El baseline del repositorio cuenta con herramientas para validar la conformidad:
*   **`repo_identity.yml`:** Declaración formal de la identidad del repositorio.
*   **`artifact_manifest.yml`:** Manifiesto defensivo de clasificación de artefactos y políticas de copia/exclusión.
*   **`scripts/audit_repo_baseline.py`:** Script determinista que valida hechos de identidad y estructura del baseline.
*   **`.agent/skills/audit_repo_baseline/SKILL.md`:** Protocolo agéntico para la interpretación de diagnósticos y decisiones de Gatekeeper.

---

## 6. Cómo Auditar el Baseline

Para auditar la conformidad de la estructura y del working tree, ejecute:
```bash
python scripts/audit_repo_baseline.py
```

### Interpretación de Resultados:
*   **Exit code 0 (PASS):** El repositorio cumple estrictamente con el baseline del framework limpio.
*   **Exit code 1 (PASS_WITH_WARNINGS):** Aprobado con advertencias. Es el comportamiento normal actual debido a la existencia autorizada de carpetas legacy o temporales locales. No bloquea el avance al diseño del manifiesto.
*   **Exit code 2 (FAIL):** Bloqueo de conformidad. Se detectó presencia de archivos prohibidos versionados (`.env`, `.venv/`, `__pycache__/`) o inconsistencias de identidad.

---

## 7. Estructura Relevante

*   `docs/adrs/` & `docs/specs/`: Sede del marco normativo y decisiones técnicas.
*   `src/`: Runtime técnico reutilizable del framework.
*   `scripts/`: Utilidades y herramientas del sistema (ej. auditor del baseline).
*   `.agent/`: Configuración, workflows y skills de orquestación agéntica.
*   `examples/`: ejemplos o fixtures sintéticos, libres de datos reales.
*   `docs_base/` & `output/`: **Zonas legacy transicionales en cuarentena.** Pendientes de decisión final de migración/limpieza física.
*   `cases/logistica/`: Caso histórico transicional (legacy). No debe tratarse como framework limpio ni copiarse a nuevos proyectos.
*   `core/templates/`: Ruta transicional heredada. La sede canónica aprobada por SPEC-002 para plantillas es `templates/`.

---

## 8. Reglas de Trabajo Críticas

1.  **Staging selectivo:** Nunca ejecute `git add .` ni `git add -A`. Añada únicamente archivos de forma manual e individual.
2.  **Exclusión de datos legacy:** No modifique ni stages archivos dentro de `docs_base/` ni `output/` sin aprobación o instrucción explícita.
3.  **Inmutabilidad de contratos:** No edite especificaciones ni decisiones arquitectónicas (ADRs/SPECs) aprobadas sin previa aprobación.
4.  **Ejecución del auditor:** Corra siempre `python scripts/audit_repo_baseline.py` antes de realizar cambios estructurales y verifique que no haya fallos.
5.  **Historial limpio:** Realice commits pequeños y selectivos con mensajes profesionales descriptivos en español.
6.  **Sin datos reales:** Este repositorio nunca debe albergar secretos (`.env`) o datos reales en áreas de código o especificaciones activas.