# Reporte Gate 7 — Auditoría Semántica (CONVIERTE / ZAC)

- **Archivo auditado:** `output/bloque_1/10_business_model_canvas.md`
- **Fecha de auditoría:** 2026-03-09
- **Cuaderno NotebookLM:** ZAC_Bloque_1_Investigacion_Sector (`a9776342-15b0-4d0d-9280-86fb060e7027`)
- **auditoria_note_id:** `6b3e9f2a-4d17-4b08-a9e3-2c8f1d0b5e39`

---

## 1. Propósito del entregable

Sintetizar el modelo de negocio de ZAC en los 9 bloques del Business Model Canvas: Segmentos, Propuesta de Valor, Canales, Relaciones, Fuentes de Ingreso, Recursos Clave, Actividades Clave, Socios Clave y Estructura de Costes.

---

## 2. Hallazgos positivos

- **Segmento bien acotado:** "Pymes de transporte, 10–50 camiones, operando FTL/LTL, con gestión manual de albaranes". No es un segmento genérico de "PYMES de logística".
- **Propuesta de valor coherente con el Canvas anterior:** "Reducir el ciclo Doc-to-Cash de semanas a días, sin reemplazar el ERP" conecta directamente con los KPIs y la estrategia competitiva.
- **Estructura de costes ampliada en TANDA 1:** Post-corrección, ahora incluye el coste principal real (tiempo técnico interno de implementación) con su hipótesis de validación. Este cambio mejora significativamente la honestidad del modelo.
- **Canales de venta específicos:** "Llamada consultiva presencial + demo en cliente" — no es "publicidad en redes sociales", es un canal de venta B2B consultivo coherente con el perfil del decisor.

---

## 3. Hallazgos críticos o débiles

- **Fuentes de Ingreso sin anclaje de mercado:** Los rangos (1.500–3.500€ setup + 250–600€/mes) son razonables pero no están respaldados por ninguna fuente (pricing de competidores comparado, entrevistas de disposición a pagar, o benchmarking sectorial). Son hipótesis sin clasificar como tal.
- **Socios Clave no diferencian "clave" de "deseable":** Se listan proveedores de APIs LLM, socios de integración ERP y asociaciones sectoriales. No está claro cuáles son imprescindibles para el MVP y cuáles son para versiones futuras.
- **Recursos Clave no mencionan el equipo humano:** Para un proyecto early-stage de 1–2 personas, el equipo fundador es el recurso más crítico. El BMC lo omite completamente.

---

## 4. Coherencia con `OPCION_ACTIVA`

**ALINEADO.** El modelo de negocio opera en el carril de pyme transportista española, con modelo SaaS/servicio de implementación. Sin referencias a aduanas, DUA ni perfiles de transitario.

---

## 5. Coherencia con el resto del bloque

- Las Fuentes de Ingreso deben cruzarse con la estrategia de diferenciación: si competimos por "menor fricción de adopción", el precio bajo el de Dashdoc debería aparecer explícitamente.
- Las Actividades Clave (implementación, OCR, validación) alinean con la estrategia técnica del proyecto.
- La Propuesta de Valor del BMC es consistente con el Canvas de Valor del bloque 1.

---

## 6. Veredicto

**APTO CON OBSERVACIONES.** El documento tiene buen nivel estructural pero necesita tres correcciones para ser completamente defendible ante un evaluador de programa de emprendimiento.

---

## 7. Correcciones mínimas sugeridas

1. Añadir `[HIPÓTESIS]` a las Fuentes de Ingreso e indicar la fuente de estimación: ej. "estimado por comparación con Dashdoc/Track-POD + validación de willingness-to-pay pendiente en piloto".
2. Clarificar en Socios Clave cuáles son imprescindibles para el MVP (API LLM) vs. deseables (asociación sectorial).
3. Añadir en Recursos Clave: "Equipo técnico fundador" como recurso principal para la fase de validación.
