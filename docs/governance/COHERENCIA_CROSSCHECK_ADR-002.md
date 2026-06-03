# COHERENCIA_CROSSCHECK_ADR-002

## Estado
Pendiente de revisión / Pendiente de aprobación humana.

## Propósito
Verificar de forma explícita que ADR-002 no contradice los documentos rectores ya aprobados del repositorio.

## Documentos contrastados
* `repo_identity.yml`
* `artifact_manifest.yml`
* `docs/adrs/ADR-001 — Repositorio madre limpio y creación de proyectos vivos independientes.md`
* `docs/specs/SPEC-001_artifact_manifest.md`
* `docs/specs/SPEC-002_estructura_repositorios_carpetas.md`
* `docs/specs/SPEC-003_repo_identity.md`
* `docs/adrs/ADR-002 — Clasificación de zonas operativas del repositorio.md`

## Matriz de verificación

| ID | Check | Documento contrastado | Evidencia revisada | Resultado | Observación | Responsable | Fecha |
|---|---|---|---|---|---|---|---|
| 01 | ADR-002 mantiene `repo_identity.yml` como fuente superior de identidad del repositorio. | `repo_identity.yml` | `repo_identity.yml` + ADR-002 sección 10 punto 1. | `PASS` | Mantiene el manifiesto de identidad como rector supremo. | Antigravity / Auditoría | 2026-06-03 |
| 02 | ADR-002 no permite datos reales si `repo_identity.yml` declara `contains_real_data: false`. | `repo_identity.yml` | `repo_identity.yml` campo `contains_real_data` + ADR-002 sección 10 punto 2. | `PASS` | Respeta la exclusión de datos reales del framework_mother. | Antigravity / Auditoría | 2026-06-03 |
| 03 | ADR-002 no permite datos de caso si `repo_identity.yml` declara `allows_case_data: false`. | `repo_identity.yml` | `repo_identity.yml` campo `allows_case_data` + ADR-002 sección 10 punto 3. | `PASS` | Prohíbe el uso de datos de casos reales en el framework base. | Antigravity / Auditoría | 2026-06-03 |
| 04 | ADR-002 respeta `artifact_manifest.yml` como contrato operativo de copiado, exclusión y validación automatizada. | `artifact_manifest.yml` | `artifact_manifest.yml` + ADR-002 sección 4.1 y sección 10 punto 4. | `PASS` | Valida el manifiesto sin alterarlo en runtime. | Antigravity / Auditoría | 2026-06-03 |
| 05 | ADR-002 no modifica `copy_policy`. | `artifact_manifest.yml` | `artifact_manifest.yml` campo `copy_policy` + ADR-002 sección 4.1 y sección 10 punto 5. | `PASS` | No altera directivas desde el texto del ADR. | Antigravity / Auditoría | 2026-06-03 |
| 06 | ADR-002 no modifica `allowed_in_framework`. | `artifact_manifest.yml` | `artifact_manifest.yml` campo `allowed_in_framework` + ADR-002 sección 4.1. | `PASS` | No cambia pertenencias lógicas del framework. | Antigravity / Auditoría | 2026-06-03 |
| 07 | ADR-002 respeta ADR-001 sobre separación entre `framework_mother` y `live_project`. | `docs/adrs/ADR-001 — Repositorio madre limpio y creación de proyectos vivos independientes.md` | ADR-001 + ADR-002 sección 10 punto 6. | `PASS` | Alínea las zonas para garantizar que la copia a live_projects sea segura. | Antigravity / Auditoría | 2026-06-03 |
| 08 | ADR-002 respeta SPEC-001 como especificación del `artifact_manifest.yml`. | `docs/specs/SPEC-001_artifact_manifest.md` | SPEC-001 + ADR-002 sección 10 punto 7. | `PASS` | Respeta y expande la semántica de categorías de artefactos. | Antigravity / Auditoría | 2026-06-03 |
| 09 | ADR-002 respeta SPEC-002 como especificación de estructura de carpetas. | `docs/specs/SPEC-002_estructura_repositorios_carpetas.md` | SPEC-002 + ADR-002 sección 10 punto 8. | `PASS` | Respeta las ubicaciones de carpetas canónicas (ej. templates). | Antigravity / Auditoría | 2026-06-03 |
| 10 | ADR-002 respeta SPEC-003 como especificación de identidad del repositorio. | `docs/specs/SPEC-003_repo_identity.md` | SPEC-003 + ADR-002 sección 10 punto 9, y ADR-002 sección 10 punto 10. | `PASS` | Respeta las reglas de gatekeeper de identidad y aprobaciones. | Antigravity / Auditoría | 2026-06-03 |

## Criterio de cierre
La matriz solo puede considerarse aprobada si todos los checks obligatorios están en `PASS`.
Cualquier `FAIL` bloquea la aprobación final de ADR-002.
Cualquier `NO_VERIFICADO` requiere decisión humana explícita.
