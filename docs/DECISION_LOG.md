# Decision Log (ZAC)

**Regla:** Toda decisión de nicho/pivote debe registrarse aquí **antes** de tocar `output/`.

---

## Plantilla de entrada
- **Fecha:** YYYY-MM-DD
- **Decisión:** (ej. Activar opción TRANSPORTE / Descartar TRANSITARIOS por ahora)
- **Contexto:** (qué cambió o qué se aprendió)
- **Evidencia NotebookLM:** (notebook_title + note_title + note_id)
- **Impacto en repo:** (qué se mueve a exploración, qué queda en output)
- **Siguiente paso:** (qué entregable del cronograma se ejecuta)

---

## Entradas

### 2026-03-04 — Activación de opción TRANSPORTE (Doc-to-Cash por evidencia)
- **Decisión:** Activar opción TRANSPORTE como única opción activa para `output/`.
- **Contexto:** En exploración se evaluaron rutas (transporte vs transitarios). Se decide ejecutar el cronograma en el camino con dolor más universal y validable: evidencia → cobro.
- **Evidencia NotebookLM:** ZAC_Bloque_1 / Auditoría Semántica Bloque 1 / d27db875-c0ac-458b-94e9-983166a53320
- **Impacto en repo:** `output/` se alinea solo a Transporte. Comparativos y alternativas van a `exploracion/`.
- **Siguiente paso:** Blindar Bloque 1 con validadores deterministas (scripts) y mantener entregables bajo gates.

### 2026-03-04 — Mover comparativo y transitario a exploración
- **Decisión:** Mover comparativo y transitario a exploración para mantener output alineado a TRANSPORTE
- **Contexto:** Se ha ejecutado una auditoría semántica simulada usando NotebookLM (o IA equivalente) determinando que estos documentos rompen la integridad de nicho.
- **Evidencia NotebookLM:** (note_id: d27db875-c0ac-458b-94e9-983166a53320 y de9be0b3-1378-474d-9ff2-3a040dea5d83)
- **Impacto en repo:** `01_mapa_empatia.md` y `01_mapa_empatia_transitario.md` extraídos de `output/bloque_1/` y reubicados en `exploracion/`.
- **Siguiente paso:** Limpieza del resto de entregables y corrida de validador determinista.
