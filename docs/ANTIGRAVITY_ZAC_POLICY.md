# File: docs/ANTIGRAVITY_ZAC_POLICY.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Política operativa del proyecto ZAC para trabajar con Antigravity
# Rol: Manual humano (versionado en repo) que complementa las Global Rules del workspace
# ──────────────────────────────────────────────────────────────────────

# Política Antigravity — Proyecto ZAC (ZAC-Lite)

## 0) Contexto (por qué existe este documento)
Este proyecto se ejecuta hasta mayo y tendrá cambios frecuentes por tutorías. Para mantener orden y coherencia:

- **Las Global Rules del workspace Antigravity** gobiernan seguridad, aprobación, trazabilidad, gates, estilo y cierre.
- Este documento define únicamente lo **específico del proyecto ZAC** (estructura, flujo, y forma de documentar).

Este archivo es “manual humano” y se versiona en el repo.  
Las reglas “motor” del agente se configuran además en **Customizations (Project Rules)** con un resumen corto.

---

## 1) Fuente de verdad (A/B + Cronograma)
### 1.1 Cronograma manda el orden
El orden de trabajo y entregables se rigen por:
- `docs_base/CronogramaConvierteZAC.txt`

Si el tutor cambia el orden o pide un nuevo entregable:
- se registra el cambio en `ZAC_INDEX_00.md` (log de tutorías)
- se ajusta el bloque correspondiente en `output/`

### 1.2 Doble documentación (A/B)
- **Documento A (externo):** narrativa para explicar el proyecto sin buzzwords y centrada en resultados.
- **Documento B (interno):** verdad completa para análisis (stack, riesgos, sustitutos, criterios, anti-humo).

**Regla de consistencia:** nada en A debe ser falso frente a B.  
B puede contener detalles que A omite por estrategia de comunicación.

Documentos base:
- Documento A: `docs_base/dossier_ampliado_proyecto_zac_operaciones_inteligentes.md`
- Documento B: `docs_base/documento_b_realidad_interna_y_marco_de_analisis_viabilidad_mercado.md`

---

## 2) Repo vs NotebookLM (modelo “Vault + Biblioteca”)
### 2.1 Repo = entregables y decisiones finales
El repo contiene lo que se entrega y lo que se valida.

- `output/` → entregables finales por bloque (lo que cuenta)
- `ZAC_INDEX_00.md` → tablero maestro y auditoría de cambios
- `docs_base/` → base estable (no crece sin control)
- `docs/` → políticas y documentación operativa del sistema (como esta)

**Regla:** si un entregable no está en `/output/`, no está validado.

### 2.2 NotebookLM = investigación y memoria organizada
NotebookLM se usa para:
- investigación web y fuentes extensas
- notas largas, borradores y comparativas
- documentación de apoyo por bloque

Cuadernos recomendados:
- `ZAC_Bloque_1`
- `ZAC_Bloque_2`
- `ZAC_Bloque_3`
- `ZAC_Bloque_4`
- `ZAC_Tutorias`

---

## 3) Regla de sincronización (obligatoria)
Cada “agente/chat/skill” debe producir siempre:

1) **Entregable final** en `output/bloque_X/...`
2) **Resumen ejecutivo (10–15 líneas)** dentro del entregable o en `output/bloque_X/99_resumen_...`
3) **Referencia a NotebookLM** (Cuaderno / Sección / Fecha) dentro del entregable

Esto evita “doble verdad” y mantiene trazabilidad.

---

## 4) Convención de entregables (output/)
### 4.1 Estructura
- `output/bloque_1/`
- `output/bloque_2/`
- `output/bloque_3/`
- `output/bloque_4/`
- `output/final/`

### 4.2 Regla anti-caos
En cada bloque se trabaja sobre los archivos ya definidos en el índice.  
**No crear nuevos archivos** sin necesidad; si se crean, se registra en `ZAC_INDEX_00.md`.

---

## 5) ZAC_INDEX_00.md (tablero maestro)
`ZAC_INDEX_00.md` es la “torre de control” del repo. Debe reflejar:

- estado por bloque: TODO / IN_PROGRESS / DONE / BLOCKED
- rutas de entregables en `output/`
- referencia a NotebookLM por entregable
- log de tutorías y cambios (qué cambió y qué impacta)

**Regla:** al cerrar un entregable, se actualiza el índice.

---

## 6) Investigación web (cuando aplique)
Cuando una tarea requiera datos de mercado, competencia, leyes, ecosistema, etc.:

- se hace investigación web con fuentes actuales y verificables
- se guardan fuentes en NotebookLM (biblioteca)
- se citan en el entregable final (con fecha y por qué sirven)

---

## 7) Principio interno del proyecto (anti-humo)
El proyecto evita posicionarse como “empresa de IA de moda”. Internamente se prioriza construir soluciones:

- realistas
- medibles
- mantenibles
- basadas en reglas del negocio, control operativo y evidencia

La IA se usa solo si aporta valor comprobable y bajo criterios de confiabilidad, trazabilidad y costo total.

---

## 8) Cómo usar Antigravity de forma eficiente (sin mega-desarrollo)
### 8.1 Dónde viven las instrucciones
- **Global Rules (workspace):** seguridad, aprobación, gates, trazabilidad, estilo, cierre.
- **Project Rules (Customizations):** resumen corto de reglas ZAC (cronograma, A/B, repo vs NotebookLM, rutas).
- **Repo (este documento):** manual humano versionado.

### 8.2 Modo de trabajo recomendado
- Cambios pequeños por archivo (evitar “reescribir todo”).
- Revisar diffs antes de aceptar cambios grandes.
- Respetar las gates por bloque: no avanzar si falta el entregable.

---

## 9) Checklist del Gate 0 (arranque)
Antes de iniciar Bloque 1:
- [ ] `docs_base/` contiene: Documento A, Documento B, cronograma y PDFs base
- [ ] cuadernos de NotebookLM creados (Bloque_1..4 y Tutorías)
- [ ] `output/` contiene carpetas por bloque + archivos base del Bloque 1
- [ ] `ZAC_INDEX_00.md` está actualizado y usable

---

## 10) Cómo se actualiza esta política
Este documento se ajusta cuando:
- el cronograma cambie
- los tutores introduzcan nuevos entregables
- aparezcan nuevas reglas operativas necesarias

Cualquier cambio se registra en `ZAC_INDEX_00.md` (log de cambios).