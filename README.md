# ZAC — Proyecto: Control Operativo Instalado (Logística)

## 0) Qué es (en 1 frase)
Diseñamos e implementamos sistemas a medida para que pymes logísticas pasen de procesos manuales (Excel/correos/validaciones dispersas) a control operativo real: trazabilidad, alertas y evidencia.

## 1) Cómo se organiza la documentación (regla A/B)
- **Documento A (externo):** narrativa sin buzzwords, centrada en resultados (dossier ampliado).
- **Documento B (interno):** verdad completa para viabilidad/mercado (stack, riesgos, sustitutos, criterios, anti-humo).

Regla de uso:
- Si el objetivo es **comunicar/vender/explicar**, usar A.
- Si el objetivo es **decidir/analizar/validar**, usar B.

## 2) Fuente de verdad del plan
El orden de trabajo lo manda el **Cronograma Convierte ZAC**. Cada bloque del cronograma se resuelve con “agentes/chats” (skills) y deja entregables versionados en /output.

## 3) Estructura del repo (dinámico y escalable)
- `/docs_base/` → Documento A, Documento B, cronograma y PDFs de investigación
- `/output/` → entregables por bloque (Bloque_1, Bloque_2, etc.)
- `ZAC_INDEX_00.md` → índice maestro (qué se hizo, qué falta, links internos)
- `ODS_00.md` → mapeo ODS (2–3 ODS máximo, con acciones e indicadores)
- `/.agent/` → reglas, skills y workflows para Antigravity

## 4) Principio interno (anti-humo)
No nos posicionamos como “empresa de IA de moda”. Priorizamos soluciones realistas, medibles y mantenibles. La IA se usa solo si aporta valor comprobable y bajo criterios de confiabilidad, trazabilidad y costo total.

## 5) Estado y próximas entregas
Ver `ZAC_INDEX_00.md` para estado actualizado por fechas del cronograma.

Perfecto. Y sí: esto calza **muy bien** con lo que ya hiciste en tu sistema de YouTube (Vault como fuente de verdad + “biblioteca” aparte + gates + outputs versionados).

Aquí te dejo una **Política de Documentación ZAC** lista para pegar en el `README.md`, basada en ese mismo enfoque.

---

## Política de Documentación ZAC (Repo + NotebookLM)

### 1) Regla A/B (igual que en YouTube)

* **Documento A (Dossier):** narrativa externa, sin buzzwords, centrada en resultados.
* **Documento B (Realidad interna):** verdad completa para análisis (stack, riesgos, sustitutos, criterios).

**No se contradicen.** A omite detalles; B los incluye.

---

### 2) Repo = Fuente de verdad operativa (Vault)

El repositorio es el lugar donde vive lo que **cuenta** y lo que se **entrega**:

* `docs_base/` → **solo** base estable (A, B, cronograma, PDFs marco).
* `output/` → entregables finales por bloque (lo que se presenta a tutores).
* `ZAC_INDEX_00.md` → tablero maestro: estado, links, fechas, próximos pasos.
* (Opcional) `decisions/` → decisiones importantes tipo “ADR” (1 página).

**Regla:** si no está en repo, no está oficialmente validado.

---

### 3) NotebookLM = Biblioteca y memoria de investigación (organizada por cronograma)

NotebookLM se usa para manejar volumen y fuentes:

* Cuadernos por bloque: `ZAC_Bloque_1`, `ZAC_Bloque_2`, `ZAC_Bloque_3`, `ZAC_Bloque_4`
* Cuaderno adicional: `ZAC_Tutorias` (notas por fecha, feedback, cambios)

Aquí va:

* investigación web, PDFs, artículos, notas largas
* borradores, comparativas, entrevistas/resúmenes
* evidencia que respalda entregables

---

### 4) Regla de sincronización (obligatoria)

Cada “agente/chat/skill” debe producir siempre:

1. **Entregable final** en `output/bloque_X/…`
2. **Resumen ejecutivo (10–15 líneas)** dentro del entregable o en `ZAC_INDEX_00.md`
3. **Referencia a NotebookLM** (cuaderno + sección + fecha) donde vive la investigación completa

Esto evita doble verdad y mantiene trazabilidad.

---

### 5) Gates (no se avanza sin salida)

No se avanza al siguiente paso del cronograma si:

* no existe entregable final en `output/`
* no hay fuentes registradas (repo o NotebookLM)
* no hay “insights” accionables para el siguiente documento (Canvas/DAFO/PESTEL/etc.)

---

## 6) Ejecución con uv (Estándar del Repositorio)

Este repositorio utiliza `uv` como gestor de dependencias y entornos virtuales para asegurar reproducibilidad y velocidad.

### Instalación de dependencias:
Para sincronizar el entorno y crear el `.venv` local con todas las dependencias exactas del `uv.lock`:
```bash
uv sync
```

### Ejecutar Streamlit:
```bash
uv run streamlit run apps/bmc_streamlit/streamlit_app.py
```

### Ejecutar QA scripts:
```bash
uv run python -m py_compile scripts/*.py
uv run python scripts/validar_entregables.py --bloque output/bloque_1 --salida reports/reporte_validacion_bloque_1.md
uv run python scripts/validar_estilo_equipo.py --bloque output/bloque_1 --salida reports/reporte_estilo_bloque_1.md
```
