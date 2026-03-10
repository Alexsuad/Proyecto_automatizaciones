**Opción activa:** TRANSPORTE  
**Subnicho:** Pyme transportista 10–50 camiones (Zaragoza/Aragón)  
**Dolor:** Viaje → Evidencia (POD/CMR/albarán) → Factura → Cobro (Doc-to-Cash)

# ──────────────────────────────────────────────────────────────────────
# Propósito: Curva de Valor (Océano Azul / CONVIERTE) vs Competencia.
# Rol: Entregable de fase de Competencia y Estrategia (CONVIERTE)
# ──────────────────────────────────────────────────────────────────────

## 1) Ejes Generales de Competencia (Mercado Español)

Se evalúan los siguientes ejes para comparar a los actores vigentes:
1. **Precio / Coste Adopción** (Licencias puras y despliegue)
2. **Capacidad Productiva / Funcionalidades** (Gestión perimetral de la empresa)
3. **Curva de Aprendizaje / Fricción** (Tiempo necesario para enseñar a la plantilla)
4. **Foco en Analítica y Control Financiero** (Dashboard final de márgenes)
5. **Especialización Doc-To-Cash** (Resolución específica del cruce albarán/peaje vs orden de carga)
6. **Agilidad Local Pyme** (Servicio y cercanía pre-configurada sin "hacer un máster")

## 2) Valoración de la Curva Narrada (1: Bajo, 5: Alto)

- **Competidor Alta (Suites Grandes TMS, ej. Dashdoc):** 
  Su precio es ALTO (5), su barrera de aprendizaje es ALTA (5) y su nivel funcional es ALTO (5). Cubren todas las periferias empresariales, pero el despliegue es lento y forzoso.
- **Competidor Media (SaaS última milla, ej. Track-POD):** 
  Foco exhaustivo en GPS y mapa, pero su especialización financiera/doc-to-cash FTL es BAJA (2). Curva de adopción es MEDIA (3).
- **Competidor Baja (Whatsapp / Nada):** 
  Precio BAJO (1), fricción BAJA (1), analítica BAJA (1) y mitigación doc-to-cash NULA (1). 

### Posición de ZAC
- **Precio/Coste Adopción:** MEDIO (3). Competimos por valor demostrado.
- **Curva de Aprendizaje:** BAJO (1). Diferenciador nuclear: sin cambiar el software legacy del cliente, conectando con sus bandejas de correos. "Fricción Cero".
- **Capacidad Productiva Periférica (Funcionalidades):** BAJO (1). Deliberadamente ignoraremos bolsas de carga, tacógrafos o flotas.
- **Especialización Doc-to-Cash:** ALTO (5). Todo el bloque técnico del desarrollo estará al servicio de leer el albarán sellado, conciliar el coste y dictaminar facturación veloz.

## 3) Conclusión de Océano Azul para ZAC

**Dónde ZAC debe sobresalir e innovar (Crear/Aumentar):**
En la eliminación del error de "punteo manual" y la extracción rápida del dato crudo documental que frena la facturación mensual y asfixia a la Pyme.

**A qué no debemos dedicar recursos (Reducir/Eliminar):**
Al desarrollo de plataformas de visualización complejas, controles de tacógrafo o aplicaciones de tracking satelital. Ese espacio está ocupado por empresas fondeadas con millones de euros e ingenieros C++. Nuestro terreno diferencial es el **flujo de caja administrativo** de la pyme.

## 4) Hipótesis + Cómo se valida

- **[HIPÓTESIS]** ZAC puede alcanzar la puntuación máxima (5/5) en Especialización Doc-to-Cash frente a competidores que puntúan 1–2 en ese eje.
  - **[CÓMO SE VALIDA]** Análisis funcional de las 3 plataformas comparadas (Dashdoc, Track-POD, status quo manual): listar funcionalidades de conciliación albarán/factura. Si ninguna ofrece conciliación automática cruzada, la hipótesis se confirma.

- **[HIPÓTESIS]** La curva de aprendizaje de ZAC (puntuación 1 = mínima fricción) es sostenible sin formación presencial al cliente.
  - **[CÓMO SE VALIDA]** En piloto: medir las horas de soporte técnico requeridas en los primeros 30 días. Objetivo: <4 horas de soporte total por cliente en onboarding.

- **[HIPÓTESIS]** La deliberación de NO competir en funcionalidades periféricas (GPS, tacógrafo, bolsas de carga) no reduce la conversión comercial en el segmento objetivo.
  - **[CÓMO SE VALIDA]** Encuesta a 10 gerentes/dueños de pymes FTL: preguntar si la ausencia de funcionalidades de tracking satelital es un factor de descarte. Si <20% lo menciona como bloqueante, la hipótesis se refuerza.

---

**Nota de Registro NotebookLM**
- **notebook_title:** ZAC_Bloque_1_Competencia
- **notebook_id:** 7aee3bc4-233d-4b2d-9941-04b53fa270ca

**Registro (HITO)**
- **hito_note_title:** HITO — 08_curva_valor_vs_competencia.md
- **hito_note_id:** 6b1f1ed2-3455-4f46-b12d-fc3f31ae8ea3

**Auditoría semántica (Gate 7)**
- **auditoria_note_title:** AUDITORÍA SEMÁNTICA — 08_curva_valor_vs_competencia.md
- **auditoria_note_id:** cc0cabb2-492f-41a0-9d9e-0ba0eac26711
- **fecha:** 2026-03-06
