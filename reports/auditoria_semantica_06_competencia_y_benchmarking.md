# Reporte Gate 7 — Auditoría Semántica (CONVIERTE / ZAC)

- **Archivo auditado:** `output/bloque_1/06_competencia_y_benchmarking.md`
- **Fecha de auditoría:** 2026-03-09
- **Cuaderno NotebookLM:** ZAC_Bloque_1_Competencia (`b7e21034-3a12-4b89-c0f1-91da040f6309`)
- **auditoria_note_id:** `8e3f4d2a-1c89-4f17-a6b5-7d90c421e9f2`

---

## 1. Propósito del entregable

Mapear el panorama competitivo del nicho Doc-to-Cash en transporte terrestre: quién compite, en qué dimensiones y dónde están las brechas que ZAC puede capitalizar.

---

## 2. Hallazgos positivos

- **Tipología Alta/Media/Baja muy bien estructurada:** La separación entre competidores directos (Alta), soluciones alternativas (Media) y sustitutos imperfectos (Baja, incluyendo el "no hacer nada") da un panorama completo y realista del mercado.
- **Los huecos están específicos y accionables:** "Nadie en el mercado ofrece solo la capa documental de captura y validación sin requerir adopción de ERP completo" es una brecha concreta, no genérica.
- **Hipótesis de validación concretas por competidor:** Para Dashdoc, Track-POD, Igarle: "verificar pricing pages, Capterra reviews, entrevistas a usuarios". Es metodología de investigación competitiva, no análisis de escritorio.
- **Todos los puntajes de benchmarking están clasificados como HIPÓTESIS:** Correcto, ya que no hay datos primarios todavía.

---

## 3. Hallazgos críticos o débiles

- **Falta análisis de la amenaza de Microsoft/Google/SAP entrando al mercado SMB:** En el segmento de herramientas habilitadas por IA, los grandes podrían lanzar soluciones similares a precio cero. Esto no está evaluado como amenaza.
- **El eje de "integración con ERP" en el benchmarking no diferencia entre integración unidireccional y bidireccional:** ZAC propone ser un "satélite que envía datos al ERP del cliente", lo que es una integración unidireccional ligera. Los competidores tipo TMS suelen proponer bidireccional. Esta distinción técnica debería reflejarse en la curva de valor.

---

## 4. Coherencia con `OPCION_ACTIVA`

**ALINEADO.** El análisis se centra en software para transporte terrestre (Dashdoc, Track-POD, Igarle). No hay análisis de herramientas para transitarios, despachos aduaneros ni navieras.

---

## 5. Coherencia con el resto del bloque

- Conecta directamente con la **curva de valor** (que usa como input los mismos ejes de benchmarking).
- Conecta con la **estrategia competitiva** (diferenciación enfocada en Doc-to-Cash se justifica por el hueco identificado aquí).
- El DAFO menciona como amenaza la "comoditización del OCR" — que no está analizada en profundidad en este documento de competencia.

---

## 6. Veredicto

**APTO para READY_FOR_REVIEW.**

---

## 7. Correcciones mínimas sugeridas

1. Añadir una mención a la amenaza de herramientas genéricas de IA (ChatGPT, Gemini) como sustitutos potenciales de bajo coste a largo plazo.
2. Clarificar en el benchmarking la distinción integración unidireccional vs. bidireccional como eje relevante.
