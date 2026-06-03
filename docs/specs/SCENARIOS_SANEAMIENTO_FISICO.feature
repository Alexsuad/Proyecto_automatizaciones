# File: docs/specs/SCENARIOS_SANEAMIENTO_FISICO.feature
# ──────────────────────────────────────────────────────────────────────
# Propósito: Escenarios Gherkin para la verificación previa al saneamiento físico.
# Rol: Especificación ejecutable de comportamiento esperado.
# ──────────────────────────────────────────────────────────────────────

Característica: Verificación previa al saneamiento físico del repositorio (Dry-run)

  Como Agente de Integridad Técnica
  Quiero ejecutar un análisis de solo lectura del repositorio
  Para detectar de manera determinista discrepancias con la gobernanza aprobada sin alterar ningún archivo

  Escenario: Error técnico por ausencia de repositorio Git válido
    Dado que el directorio de trabajo no es un repositorio Git activo
    Cuando se ejecuta el script de dry-run de saneamiento
    Entonces el script debe abortar inmediatamente
    Y debe devolver un código de salida igual a 3 (ERROR_TECNICO)
    Y no debe generar ningún reporte Markdown

  Escenario: Error técnico por ausencia de documentos normativos obligatorios (Bloqueo)
    Dado que el archivo de identidad "repo_identity.yml" no existe en la raíz
    Cuando se ejecuta el script de dry-run de saneamiento
    Entonces el script debe abortar inmediatamente
    Y debe devolver un código de salida igual a 3 (ERROR_TECNICO)
    Y no debe generar ningún reporte Markdown

  Escenario: Detección de discrepancia de rol entre identidad y manifiesto
    Dado que "repo_identity.yml" define el rol de repositorio como "framework_mother"
    Pero "artifact_manifest.yml" define el rol como "case_study"
    Cuando se ejecuta el script de dry-run de saneamiento
    Entonces el script debe registrar una contradicción grave
    Y debe devolver un código de salida igual a 2 (FAIL)
    Y debe reflejar esta discrepancia de rol en el reporte Markdown generado

  Escenario: Zona legacy física detectada sin estar en Git (Hallazgo con advertencia)
    Dado que la carpeta legacy "docs_base/" existe físicamente en el repositorio
    Y no contiene ningún archivo registrado (tracked) en Git
    Cuando se ejecuta el script de dry-run de saneamiento
    Entonces el script debe registrar un hallazgo de nivel bajo
    Y debe proponer mantener en cuarentena física local
    Y debe devolver un código de salida igual a 1 (WARN)
    Y debe generar el reporte Markdown documentando la presencia física pero sin contradicción de Git

  Escenario: Zona legacy física con archivos registrados en Git (Contradicción grave)
    Dado que la carpeta legacy "cases/logistica/" existe físicamente
    Y contiene archivos registrados (tracked) en el control de versiones de Git
    Cuando se ejecuta el script de dry-run de saneamiento
    Entonces el script debe registrar una contradicción grave de gobernanza
    Y debe devolver un código de salida igual a 2 (FAIL)
    Y debe incluir la contradicción en el reporte de auditoría proponiendo conservar como histórico en rama de transición

  Escenario: Script del framework madre que depende de ruta legacy (dependencia operativa real)
    Dado que existe un script general en "scripts/validar_entregables.py"
    Y ese script contiene una referencia de código activa a la ruta legacy "cases/logistica/"
    Cuando se ejecuta el script de dry-run de saneamiento
    Entonces el script debe detectar la dependencia operativa real hacia la ruta legacy
    Y debe clasificarla como FAIL en el reporte
    Y debe devolver un código de salida igual a 2 (FAIL)

  Escenario: Script del framework madre con referencia informativa/comentario a ruta legacy
    Dado que existe un script general en "scripts/validar_entregables.py"
    Y ese script contiene un comentario de código "# esto es un caso como cases/logistica/" o texto de ayuda (help)
    Cuando se ejecuta el script de dry-run de saneamiento
    Entonces el script debe clasificar esta referencia como WARN en el reporte
    Y el código de salida debe ser 1 (WARN) si no hay contradicciones de tipo FAIL

  Escenario: Documento arquitectónico en zona no normativa
    Dado que existe un archivo Markdown "docs_base/ARQ_OLD_diseno.md" en una zona legacy
    Y contiene secciones de diseño o decisiones técnicas
    Cuando se ejecuta el script de dry-run de saneamiento
    Entonces el script debe proponer clasificar destino y promover parcialmente
    Y registrarlo como hallazgo para revisión humana en el reporte
    Y el código de salida debe ser 1 (WARN) si no hay contradicciones de Git

  Escenario: El script no modifica nada en el sistema (Solo Lectura)
    Dado que se ejecuta el script de dry-run de saneamiento en cualquier entorno
    Cuando finaliza su ejecución
    Entonces el estado de Git del repositorio debe permanecer intacto
    Y ningún archivo existente debe haber sido modificado, borrado, renombrado o creado (excepto el reporte)
    Y la matriz de hallazgos debe indicar explícitamente "Requiere aprobación humana: Sí" para cualquier acción propuesta
    Y declarar que ninguna acción física queda autorizada automáticamente
