# Language: es
# File: docs/specs/SCENARIOS_DRY_RUN_ACCIONES_SANEAMIENTO_FISICO.feature
# ──────────────────────────────────────────────────────────────────────
# Propósito: Escenarios Gherkin para la validación lógica del dry-run.
# Rol: Especificación de criterios de comportamiento y no-ejecución.
# ──────────────────────────────────────────────────────────────────────

Característica: Dry-run de acciones propuestas de saneamiento físico

  Escenario: Una acción propuesta no equivale a una acción autorizada
    Dado que existe el documento "PLAN_SANEAMIENTO_FISICO_v0.md"
    Cuando se evalúa el dry-run de acciones propuestas
    Entonces la columna "Acción propuesta" debe permanecer como una intención documental
    Y la columna "Acción autorizada" debe registrar "Ninguna" en todos los casos.

  Escenario: Una ruta legacy trackeada puede recibir acción simulada de exclusión, pero no ejecución real
    Dado que se evalúa la ruta legacy "docs_base/"
    Cuando se simula la acción "excluir del baseline"
    Entonces no se debe invocar a "git rm" sobre el sistema de archivos
    Y el archivo físico original debe permanecer intacto.

  Escenario: Un documento Markdown en zona no normativa debe clasificarse antes de promoverse
    Dado que existe "output/arquitectura/*.md"
    Cuando se detecta como Markdown fuera de la zona normativa
    Entonces la acción propuesta debe ser "clasificar destino antes de cualquier acción"
    Y la acción ejecutada debe ser "Ninguna".

  Escenario: Una referencia operativa real puede generar propuesta de refactor futuro, pero no modificación de código
    Dado que existe una referencia real a "cases/logistica/" en "scripts/audit_repo_baseline.py"
    Cuando se simula la acción "documentar como deuda técnica"
    Entonces no se debe aplicar ningún refactor de código
    Y el archivo fuente de python debe conservar su código intacto.

  Escenario: Un posible falso positivo debe quedar bloqueado para revisión humana
    Dado que se detecta una referencia dudosa en la lógica de pruebas
    Cuando se clasifica como "Posible falso positivo"
    Entonces el estado en la matriz de acciones debe ser "Posible falso positivo"
    Y se debe requerir la aprobación humana obligatoria.

  Escenario: Una acción sobre output/ no puede ejecutarse en esta fase
    Dado que la matriz de acciones lista el directorio "output/"
    Cuando se simula el saneamiento documental
    Entonces no se debe limpiar físicamente la carpeta "output/"
    Y la columna "Acción ejecutada" para este ID debe ser "Ninguna".

  Escenario: Una acción sobre docs_base/ no puede ejecutarse en esta fase
    Dado que la matriz de acciones lista el directorio "docs_base/"
    Cuando se simula el saneamiento documental
    Entonces no se debe eliminar ni mover la carpeta "docs_base/"
    Y el estado de la ruta local debe ser activo y sin cambios.

  Escenario: Una acción sobre cases/logistica/ no puede ejecutarse en esta fase
    Dado que la matriz de acciones lista el directorio "cases/logistica/"
    Cuando se simula el saneamiento documental
    Entonces no se debe reubicar ni eliminar la carpeta "cases/logistica/"
    Y la columna "Acción ejecutada" para este caso debe registrar "Ninguna".

  Escenario: Una acción sobre manifests debe quedar fuera de alcance
    Dado que existen los archivos "artifact_manifest.yml" y "repo_identity.yml"
    Cuando se procesa el dry-run de acciones
    Entonces no se debe autorizar ninguna alteración en la versión o campos de los manifests
    Y cualquier propuesta sobre manifests debe registrar estado "Bloqueado".

  Escenario: Si una acción simulada aparece como ejecutada, el resultado debe ser FAIL
    Dado que se lee la matriz de acciones propuestas
    Cuando alguna fila contiene "Acción ejecutada" distinta a "Ninguna"
    Entonces el resultado del dry-run de acciones debe reportar "FAIL"
    Y la fase completa debe declararse en estado bloqueado de seguridad.
