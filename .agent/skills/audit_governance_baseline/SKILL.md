# Skill: audit_governance_baseline

## Propósito
Auditar de forma no destructiva la coherencia cruzada del baseline de gobernanza v1 del repositorio `framework_mother`.

Este skill no reemplaza `audit_repo_baseline`. Lo complementa:
- `audit_repo_baseline`: valida el baseline técnico apoyado en script determinista.
- `audit_governance_baseline`: valida coherencia documental entre identidad, manifiesto, ADRs, SPECs y matriz de coherencia.

## Cuándo usar este skill
Antes de:
- aprobar ADR-002;
- declarar cerrado el baseline de gobernanza v1;
- preparar un commit normativo;
- diseñar un plan de saneamiento físico;
- cambiar `manifest_status`;
- promover documentos de `Propuesto` a `Aprobado`.

## Entradas requeridas
- repo_identity.yml
- artifact_manifest.yml
- docs/adrs/ADR-001 — Repositorio madre limpio y creación de proyectos vivos independientes.md
- docs/adrs/ADR-002 — Clasificación de zonas operativas del repositorio.md
- docs/governance/COHERENCIA_CROSSCHECK_ADR-002.md
- docs/specs/SPEC-001_artifact_manifest.md
- docs/specs/SPEC-002_estructura_repositorios_carpetas.md
- docs/specs/SPEC-003_repo_identity.md
- docs/specs/SPEC-004_artifact_classification.md
- docs/specs/SPEC-005_agent_skills_workflows_contract.md

## Procedimiento
1. Verificar que todos los documentos requeridos existen.
2. Ejecutar `python scripts/audit_repo_baseline.py` como apoyo técnico, si está disponible.
3. Revisar coherencia cruzada entre `repo_identity.yml`, `artifact_manifest.yml`, ADRs y SPECs.
4. Emitir una matriz `PASS` / `FAIL` / `NO_VERIFICADO`.
5. Confirmar explícitamente que no se modificó ningún archivo.

## Checks obligatorios
1. `repo_identity.yml` no contradice ADR-001.
2. `repo_identity.yml` no contradice SPEC-003.
3. `artifact_manifest.yml` cumple SPEC-001.
4. `artifact_manifest.yml` respeta `repo_identity.yml`.
5. SPEC-004 no contradice SPEC-001.
6. SPEC-004 no contradice `artifact_manifest.yml`.
7. SPEC-004 no autoriza saneamiento físico.
8. SPEC-005 no autoriza reorganización de `.agent`.
9. ADR-002 no reemplaza `artifact_manifest.yml`.
10. ADR-002 no autoriza cambios físicos.
11. `COHERENCIA_CROSSCHECK_ADR-002.md` contiene evidencia cruzada suficiente.
12. El paquete completo permite aprobar ADR-002 sin aprobar todavía `manifest_status`.
13. El paquete completo mantiene bloqueado el saneamiento físico hasta plan con dry-run.
14. `docs/PRODUCTO_DECLARACION_MAESTRA.md` queda fuera del paquete normativo.
15. `docs_base/PROYAUTO_DOC_A_DOSSIER.md` queda fuera del paquete normativo.

## Salida esperada
Reporte estructurado con:
- resultado general;
- matriz `PASS` / `FAIL` / `NO_VERIFICADO`;
- errores bloqueantes;
- observaciones no bloqueantes;
- archivos que pertenecen al paquete normativo;
- archivos que quedan fuera del paquete normativo;
- recomendación final;
- confirmación de no modificación.

## Prohibiciones
- No modificar archivos.
- No mover carpetas.
- No borrar archivos.
- No cambiar estados documentales.
- No cambiar `manifest_status`.
- No modificar `artifact_manifest.yml`.
- No modificar `repo_identity.yml`.
- No modificar ADRs ni SPECs durante la auditoría.
- No hacer `git add`.
- No hacer commit.
- No hacer push.
- No iniciar saneamiento físico.

## Criterio de éxito
El skill es válido si permite decidir, con evidencia, si el baseline de gobernanza v1 está listo para aprobación humana sin ejecutar ningún cambio operativo.
