# File: docs/governance/DRY_RUN_ACCIONES_SANEAMIENTO_FISICO_v0.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Reporte de simulación de acciones propuestas (dry-run v0).
# Rol: Documento de gobernanza y control operativo de simulación.
# ──────────────────────────────────────────────────────────────────────

# DRY_RUN_ACCIONES_SANEAMIENTO_FISICO_v0

## 1. Estado
Propuesto / Pendiente de aprobación humana.

## 2. Propósito
Simular documentalmente acciones futuras de saneamiento físico a partir del plan aprobado, sin ejecutar cambios reales sobre el repositorio.

## 3. Fuentes usadas
### Fuentes principales:
- `docs/governance/PLAN_SANEAMIENTO_FISICO_v0.md`
- `docs/governance/AUDITORIA_PLAN_SANEAMIENTO_FISICO_v0.md`
- `reports/saneamiento/AUDITORIA_DRY_RUN_SANEAMIENTO_FISICO.md`

### Fuentes de contexto:
- `docs/specs/HARD_SPEC_DRY_RUN_ACCIONES_SANEAMIENTO_FISICO.md`
- `docs/specs/SCENARIOS_DRY_RUN_ACCIONES_SANEAMIENTO_FISICO.feature`
- `artifact_manifest.yml`
- `repo_identity.yml`
- `docs/specs/SPEC-004_artifact_classification.md`
- `docs/specs/SPEC-005_agent_skills_workflows_contract.md`

## 4. No objetivos
Este documento es estrictamente analítico y simulado. No autoriza, programa ni ejecuta en absoluto ninguna de las siguientes acciones en el repositorio físico:
- mover archivos o carpetas;
- borrar archivos o carpetas;
- renombrar archivos o carpetas;
- ejecutar comandos Git de desindexación o movimiento;
- limpiar carpetas físicas de output o base (`output/`, `docs_base/`);
- alterar el caso de uso sectorial `cases/logistica/`;
- modificar runtime en `src/` o `core/`;
- modificar y sobreescribir los archivos de manifiesto.

## 5. Resumen ejecutivo
- **Fase de simulación:** `DRY_RUN_ACCIONES_SANEAMIENTO_FISICO_v0`
- **Elementos simulados:** 10 hallazgos estructurales clasificados según su naturaleza y nivel de riesgo.
- **Razón de no ejecución:** El repositorio madre prohíbe limpiezas automáticas. Todo comando de limpieza en este documento consta exclusivamente a nivel explicativo textual (pseudosimulado) y su estado físico es inalterado.
- **Veredicto documental:** `PASS` (No se ejecuta ningún comando físico y toda acción permanece bloqueada hasta aprobación formal).

## 6. Matriz de acciones simuladas

| ID | Grupo | Ruta / patrón | Hallazgo origen | Acción simulada | Riesgo | Evidencia | Comando simulado / textual | Acción ejecutada | Requiere aprobación humana | Estado |
| -- | ----- | ------------- | --------------- | --------------- | ------ | --------- | -------------------------- | ---------------- | -------------------------- | ------ |
| M-001 | Legacy trackeado | `docs_base/` | Contiene archivos trackeados en Git. | archivar fuera del framework madre | Alto | reports/saneamiento/AUDITORIA_DRY_RUN_SANEAMIENTO_FISICO.md | `# Acción simulada: archivar docs_base` | Ninguna | Sí | Propuesto |
| M-002 | Output histórico | `output/` | Contiene reportes históricos generados. | excluir del baseline | Alto | reports/saneamiento/AUDITORIA_DRY_RUN_SANEAMIENTO_FISICO.md | `# Acción simulada: excluir output/` | Ninguna | Sí | Propuesto |
| M-003 | Caso logístico | `cases/logistica/` | Caso de uso sectorial real. | conservar como histórico | Alto | reports/saneamiento/AUDITORIA_DRY_RUN_SANEAMIENTO_FISICO.md | `# Acción simulada: conservar cases/logistica` | Ninguna | Sí | Propuesto |
| M-004 | Templates transic. | `core/templates/` | Ubicación no recomendada en SPEC-002. | promover parcialmente | Alto | reports/saneamiento/AUDITORIA_DRY_RUN_SANEAMIENTO_FISICO.md | `# Acción simulada: promover templates` | Ninguna | Sí | Propuesto |
| M-005 | Markdown no normat. | `docs_base/*.md` | Documentos de diseño fuera de docs/. | clasificar destino antes de cualquier acción | Medio | reports/saneamiento/AUDITORIA_DRY_RUN_SANEAMIENTO_FISICO.md | `# Acción simulada: clasificar md` | Ninguna | Sí | Propuesto |
| M-006 | Markdown no normat. | `output/**/*.md` | Evidencias y reportes generados. | clasificar destino antes de cualquier acción | Medio | reports/saneamiento/AUDITORIA_DRY_RUN_SANEAMIENTO_FISICO.md | `# Acción simulada: clasificar output md` | Ninguna | Sí | Propuesto |
| M-007 | Ref. operativas reales | `scripts/audit_repo_baseline.py` | Referencias en código activo a cases/logistica. | documentar como deuda técnica | Alto | reports/saneamiento/AUDITORIA_DRY_RUN_SANEAMIENTO_FISICO.md | `# Acción simulada: documentar deuda audit_repo` | Ninguna | Sí | Propuesto |
| M-008 | Ref. operativas reales | `scripts/test_dmv_manager.py` | Depende de dmv_test.json en caso logístico. | documentar como deuda técnica | Alto | reports/saneamiento/AUDITORIA_DRY_RUN_SANEAMIENTO_FISICO.md | `# Acción simulada: documentar deuda test_dmv` | Ninguna | Sí | Propuesto |
| M-009 | Ref. informativas | `scripts/auditar_deriva_editorial.py` | Referencia informativa de argparse. | conservar como histórico | Bajo | reports/saneamiento/AUDITORIA_DRY_RUN_SANEAMIENTO_FISICO.md | `# Acción simulada: mantener comentario` | Ninguna | Sí | Propuesto |
| M-010 | Temporales y cachés | `cases/tmp_*/` | Carpetas de desarrollo local temporales. | excluir del baseline | Bajo | reports/saneamiento/AUDITORIA_DRY_RUN_SANEAMIENTO_FISICO.md | `# Acción simulada: excluir tmp` | Ninguna | Sí | Propuesto |

## 7. Acciones simuladas por grupo

### 1. Legacy trackeado en Git
Se registra como posible línea de decisión futura la exclusión y desindexación del directorio `docs_base/`. Podría evaluarse en una fase posterior, previa aprobación humana, su traslado a un archivo documental comprimido externo para conservar el historial sin cargar la base limpia.

### 2. Documentos Markdown en zonas no normativas
Deberá clasificarse antes de decidir destino el contenido de archivos Markdown en `docs_base/` y `output/`. Podría evaluarse como promoción parcial, archivo, histórico, cuarentena o exclusión, previa aprobación humana, para los de valor normativo de arquitectura.

### 3. Output histórico
Se registra como posible línea de decisión futura declarar el directorio `output/` como zona temporal/ignore en Git. Podría evaluarse en una fase posterior, sin modificar `.gitignore` en esta microfase.

### 4. Caso logístico histórico
Se registra como posible línea de decisión futura el aislamiento conceptual de `cases/logistica/` en una rama o repositorio histórico dedicado a ejemplos de aplicación sectorial.

### 5. Templates transicionales
Deberá clasificarse antes de decidir destino la ubicación de las plantillas de `core/templates/` para una posible migración futura hacia el directorio de plantillas estándar.

### 6. Referencias operativas reales a rutas legacy
Se registra como posible línea de decisión futura la sustitución de las referencias en código de `scripts/` y `tests/` a través de mockups o fixtures independientes del caso logístico.

### 7. Referencias informativas o de auditoría
Podrían evaluarse como "conservar como histórico", permitiendo que los comentarios descriptivos o textos informativos no operativos permanezcan inalterados.

### 8. Temporales y cachés
Se registra como posible línea de decisión futura la inclusión de patrones como `cases/tmp_prueba_case_lifecycle` en el archivo `.gitignore` local de desarrollo, sin modificar `.gitignore` en esta microfase.

### 9. Posibles falsos positivos
Se registran como elementos bloqueados para revisión humana las cadenas y patrones de test que no representen acoplamiento real.

### 10. Elementos bloqueados por requerir decisión humana
Se registra como posible línea de decisión futura el bloqueo de toda acción física sobre archivos de configuración compartidos.

## 8. Acciones explícitamente bloqueadas
Queda estrictamente bloqueada toda acción física o de control sobre el repositorio. Las siguientes pseudoacciones no se aplican:
- Pseudoacción bloqueada: desindexar docs_base/ solo en una fase futura con aprobación humana.
- Pseudoacción bloqueada: excluir output/ del baseline solo mediante plan aprobado.
- Pseudoacción bloqueada: aislar cases/logistica/ como histórico sin borrar en esta fase.
- Pseudoacción bloqueada: revisar core/templates/ para posible migración futura sin remoción ni movimiento.
- Pseudoacción bloqueada: refactorizar scripts/audit_repo_baseline.py para desacoplar dependencias rígidas en fase técnica posterior.

## 9. Decisiones humanas requeridas
Antes de proceder a cualquier fase técnica futura de ejecución, se exige:
1. Aprobación formal escrita del plan y dry-run de acciones por parte del arquitecto (Alex).
2. Definición del repositorio o almacenamiento externo para albergar el contenido extraído de `cases/logistica/`.
3. Verificación de que las pruebas automatizadas del core no rompen al simular la ausencia de fixtures legacy.

## 10. Riesgos de ejecución prematura
- **Ruptura de baseline:** La eliminación física prematura de `cases/logistica/` causaría fallos automáticos en el suite de pruebas actual.
- **Pérdida de evidencia:** El borrado de reportes históricos en `output/` eliminaría el registro físico de auditorías pasadas.
- **Pérdida de trazabilidad:** No contar con un respaldo externo antes de archivar violaría la política de integridad de la gobernanza documental.

## 11. Resultado del dry-run de acciones
El veredicto final sobre la coherencia y apego del dry-run a las normas operativas es:
- **PASS**

*Justificación:* El documento cumple plenamente al simular de forma exclusivamente conceptual y de texto descriptivo las acciones de saneamiento, declarando inalterada toda estructura física real y bloqueando la ejecución autónoma de comandos.

## 12. Cierre
Este documento simula. No ejecuta. No limpia. No mueve. No borra. No autoriza saneamiento físico.
