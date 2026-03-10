**Opción activa:** TRANSPORTE  
**Subnicho:** Pyme transportista 10–50 camiones (Zaragoza/Aragón)  
**Dolor:** Viaje → Evidencia (POD/CMR/albarán) → Factura → Cobro (Doc-to-Cash)

# ──────────────────────────────────────────────────────────────────────
# Propósito: Business Model Canvas (BMC) Operativo.
# Rol: Entregable de fase de Competencia y Estrategia (CONVIERTE)
# ──────────────────────────────────────────────────────────────────────

## Segmentos de Clientes
- Pymes aragonesas de transporte de cargas completas (FTL).
- Flotas de aproximadamente 10 a 50 vehículos.
- Estructura manual o pseudo-digital, operando sin TMS Enterprise. Su cobro depende del retorno y verificación manual de papeles de evidencia (Albaranes/CMR).

## Propuesta de Valor
- **Backoffice Operativo Invisible:** Eliminación del "punteo" manual y del retraso de caja. Sin forzar migraciones severas de software.
- Se validan en tiempo real las conformidades de los transportes, se calcula el extracoste y se entregan listos los datos finales para facturar, reduciendo drásticamente el ciclo doc-to-cash. El cliente recupera su dinero en una fracción de tiempo.

## Canales
- Contacto personal hiper-local (Red local, asociaciones base Aragon).
- Llamada consultiva presencial ("auditoría de retrasos").
- Demo técnica con datos/casos reales del cliente en corto alcance.

## Relaciones con Clientes
- Transaccional de alto toque técnico inicial (Onboarding).
- Retención vía "as-a-service" y soporte local de extrema confianza. ZAC como socio infraestructural de finanzas operativas.

## Fuentes de Ingreso (Hipótesis por validar)
- Instalación guiada + Setup inicial / piloto: [Hipótesis de rango: 1.500€ - 3.500€].
- Suscripción recurrente SaaS / Mantenimiento y proceso batch documental: [Hipótesis de rango: 250€ - 600€/mes].

## Recursos Clave
- Motor o plataforma inteligente de extracción documental (OCR + LLM semi-estructurado o parser rígido).
- Integrador local (desarrollo web, scripts de conciliación, automatismos lógicos que simulen el trabajo humano - Python, n8n, Make).
- Entendimiento del sector y regulaciones locales del viaje FTL.

## Actividades Clave
- Diseño e implantación técnica del colector de buzones (Email, drive/whatsapp folders) a bases de datos limpias.
- Creación de paneles / reportes simples para validación rápida.
- Aseguramiento contínuo de los SLAs operativos y el 99% de acierto interpretativo en CMRs de mala calidad.

## Asociaciones Clave
- Suministradores Cloud (AWS/GCP o modelos Open-source).
- Agencias digitalizadoras (Eventualmente, para subvenciones tipo Kit Digital).
- Proveedores de APIs aduaneras de soporte (si hubiere derivación lateral marginal en el futuro).

## Estructura de Costes (Hipótesis)
- **Infraestructura técnica:** Coste fijo bajo si se opera con arquitectura serverless o API-based (costes de tokens LLM, almacenamiento cloud, hosting backend/frontend). Variable según volumen de documentos procesados.
- **[COSTE PRINCIPAL — HIPÓTESIS] Tiempo técnico interno de implementación:** El mayor coste estructural no es la infraestructura, sino las horas de diseño, parametrización, desarrollo e integración adaptadas a las singularidades de cada cliente (formatos de albarán, ERP de destino, canales de entrada). **Cómo se validará:** midiendo las horas reales por cliente en el piloto y comparando con el precio de setup. Si el coste de horas supera el precio de setup, el modelo de ingreso inicial no es viable sin ajuste.
- **Soporte de puesta en marcha:** Horas de acompañamiento durante el onboarding del primer mes (formación de administración, ajuste de reglas de validación, corrección de errores de extracción OCR). [HIPÓTESIS: estimado en 4–8 horas por cliente, sin cifra validada todavía.]
- **Coste variable de mantenimiento:** Actualizaciones de reglas cuando el cliente cambia formatos documentales o incorpora nuevas rutas/subcontratas.

---

### Supuestos a desaturar
- ¿El cliente dispone de los PDF en los bandejas de correo que se le asignen como vector de entrada o están estrictamente estancados en WhatsApp personal? (Riesgo conductual).
- ¿Dispuesto a pagar una recurrencia mensual si elimina un dolor administrativo claro y no requiere despido presencial?

### Próximo paso (Bloque 2)
El molde conceptual de viabilidad económica y competidores está ensamblado. El próximo salto orgánico es asentar la estructura Legal (Ley Morosidad, RGPD) y blindar la viabilidad de la forma de actuar antes de definir el embudo técnico final.

## Hipótesis + Cómo se valida

- **[HIPÓTESIS]** El rango de precio de setup inicial (1.500€–3.500€) es aceptable para una pyme de transporte de 10–50 camiones con facturación anual entre 1M€ y 5M€.
  - **[CÓMO SE VALIDA]** Entrevistas de disposición a pagar (willingness to pay) con 5–8 gerentes objetivo. Presentar 3 rangos de precio y medir la reacción. Si >50% acepta el rango medio, la hipótesis se refuerza.

- **[HIPÓTESIS]** La suscripción recurrente de 250€–600€/mes se justifica si el ahorro demostrable en tiempo administrativo supera ese coste (ROI positivo en <6 meses).
  - **[CÓMO SE VALIDA]** En piloto: medir horas/semana del administrativo dedicadas al "punteo" antes y después. Multiplicar el ahorro de horas por coste/hora del administrativo. Si el ahorro mensual >600€, la hipótesis se confirma.

- **[HIPÓTESIS]** El canal de contacto personal hiper-local (Red local, asociaciones de Aragón) es suficiente para conseguir los primeros 3–5 clientes piloto sin inversión en marketing digital.
  - **[CÓMO SE VALIDA]** Registrar el número de leads obtenidos en 2 meses exclusivamente a través de red local y asociaciones. Objetivo: >10 leads cualificados y >3 conversiones a piloto.

- **[HIPÓTESIS]** El cliente dispone de los documentos de evidencia (CMR, albarán, ticket de peaje) en bandeja de correo electrónico o carpeta compartida, no únicamente en WhatsApp personal.
  - **[CÓMO SE VALIDA]** En las entrevistas exploratorias: preguntar dónde almacenan los documentos de cada viaje. Si >60% utiliza correo o drive como canal principal, la hipótesis se confirma. Si no, considerar integración con WhatsApp Business.

---

**Nota de Registro NotebookLM**
- **notebook_title:** ZAC_Bloque_1_Competencia
- **notebook_id:** 7aee3bc4-233d-4b2d-9941-04b53fa270ca

**Registro (HITO)**
- **hito_note_title:** HITO — 10_business_model_canvas.md
- **hito_note_id:** ce981137-971e-4dbf-b62a-1e146c78576d

**Auditoría semántica (Gate 7)**
- **auditoria_note_title:** AUDITORÍA SEMÁNTICA — 10_business_model_canvas.md
- **auditoria_note_id:** 762498a3-9cad-4163-ac83-9e642da7c3af
- **fecha:** 2026-03-06
