# File: output/bloque_1/02_canvas_valor.md

**Opción activa:** TRANSPORTE  
**Subnicho:** Pyme transportista 10–50 camiones (Zaragoza/Aragón)  
**Dolor:** Viaje → Evidencia (POD/CMR/albarán) → Factura → Cobro (Doc-to-Cash)

# ──────────────────────────────────────────────────────────────────────
# Propósito: Canvas de Propuesta de Valor enfocado en Pymes Transportistas Terrestres.
# Rol: Definir el producto/servicio que ZAC construye en base a las frustraciones documentadas.
# ──────────────────────────────────────────────────────────────────────

## 1. Perfil del Cliente (Client Profile)
**Segmento Objetivo:** Pyme de transporte logístico terrestre (flotas medias de 10 a 50 camiones articulados o rígidos), enfocada en carga general y grupaje a nivel nacional/ibérico.

### 1.1 Tareas del Cliente (Customer Jobs)
- Gestionar y asignar cargas a chóferes evitando viajes en vacío (retornos).
- Recolectar Cartas de Porte (CMR) y albaranes sellados para probar la ejecución impecable del servicio.
- Facturar la carga, conciliar peajes y surtidores de gasóleo para medir rentabilidad por ruta.
- Cumplir con la normativa del MITMA sobre control de tiempos de conducción y trazabilidad de facturación.

### 1.2 Dolores (Pains)
- **Asfixia financiera por retrasos [HIPÓTESIS]:** En pymes de transporte, el cobro se retrasa cuando faltan conformidades (POD/CMR/albarán) o cuando hay incidencias documentales que bloquean la validación interna. **Esta hipótesis se validará midiendo el ciclo real “fin de viaje → factura emitida” y “factura emitida → cobro” en el cliente piloto (baseline).** *(Fuente contexto: reportes sectoriales y entrevistas; cifra exacta pendiente de validación en piloto y/o fuente oficial importada en NotebookLM).*
- **Tensión de márgenes operativos [HECHO]:** El gasóleo y el personal superan por amplio margen la estructura de costes directos, reduciendo la flexibilidad frente a la guerra de precios *(Fuente sólida: Observatorio de Costes del Transporte de Mercancías por Carretera, MITMA, Julio 2024)*.
- **Congestión manual administrativa [HIPÓTESIS]:** El departamento de tráfico pierde gran parte de su jornada reclamando albaranes por WhatsApp y punteando hojas de cálculo contra facturas, generando un coste hundido administrativo no medido formalmente, pero muy perjudicial para la liquidez.

#### 1.2.1 Fuentes Sólidas del Análisis (Top 2)
1. **MITMA (Oficial):** Observatorio de Costes del Transporte de Mercancías por Carretera (Julio 2024).
2. **DBK (Consultora con metodología):** Mercado Ibérico - Transporte de Mercancías por Carretera (Nota de prensa 2026).


*Nota de integridad: Fenadismer se eliminó de esta sección porque el dato de plazo de cobro que sustentaba fue degradado a hipótesis en una revisión anterior. No puede aparecer como fuente sólida si ya no respalda ningún dato validado.*


### 1.3 Ganancias (Gains)
- Poder emitir la factura en menos de 24h tras la descarga en el muelle de llegada.
- Lograr una auditoría automática de rentabilidad por vehículo: saber si un viaje ganó o perdió dinero al instante de cruzar la tarifa cobrada con el coste real de peaje y combustible incurrido.
- Disponer de trazabilidad documental sin intervención humana ("zero data-entry").

---

## 2. Mapa de Valor

**Propuesta de Valor (1 frase):** 
"El sistema se integra y automatiza la auditoría documental y operativa de tu flota, permitiendo facturar en tiempo real y blindar tu margen de maniobra sin necesidad de migrar tu histórico ERP o contratar más personal."

### 2.1 Productos y Servicios (Módulos de Solución)
- **Módulo de Trazabilidad Documental (Visión IA/OCR):** Extracción automatizada de datos desde fotografías de CMRs y albaranes de entrega para su validación automática frente a la orden de carga original.
- **Módulo de Auditoría de Rentabilidad Operativa:** Cruce determinista y automático de datos de facturación (ingresos) contra gastos extraídos de archivos estructurados (tarjetas de combustible, telepeajes) para emitir alertas directas de desviación de márgenes.
- **Dashboard Activo de Cuello de Botella Pyme:** Visualización accionable del estado real de los cobros en base operativa (expedientes bloqueados por falta de firma vs. cargas listas para enviar a facturación al segundo).

### 2.2 Evidencia / KPIs (Métricas)
Las soluciones impactarán (y se evaluarán) directamente sobre estas métricas:
1. **[HIPÓTESIS] Reducción del ciclo Doc-to-Cash:** Se busca reducir el número de días transcurridos desde que el camión finaliza el porte hasta la emisión de la factura. **Cómo se validará:** estableciendo y reduciendo el baseline real del cliente piloto (medido antes/después).
2. **% de Reducción de Costes Administrativos Ocultos [HIPÓTESIS]:** Se medirá la reducción de al menos un 40% de las horas/semana empleadas en el punteado puramente manual de albaranes de tránsito.
3. **[HIPÓTESIS] Control Desviación del Margen Bruto / Kilómetro:** Se busca medir la precisión en el coste kilométrico real frente a la referencia teórica del mercado (base MITMA). **Cómo se validará:** comparando el coste kilométrico declarado por el cliente piloto contra los datos del Observatorio MITMA para su categoría de vehículo, durante al menos 30 operaciones consecutivas.

---

## 3. Diferenciación y Alcance del Sistema

### Diferenciación Competitiva (Por qué esta solución y no otras)
- **Frente a las "Suites Integrales" (SAP, Dynamics, grandes TMS):** No obliga a la pequeña Pyme de transportes a detener la operativa de oficina durante 6 meses para integrarse dolorosamente. Se implementa de manera focalizada y pragmática (automatización sobre herramientas que ya dominan, conectores ligeros, flujos preexistentes).
- **Frente a la Consultoría Convencional:** No entregamos un "PDF bonito de 100 páginas con recomendaciones de reingeniería corporativa". Entregamos un sistema de código logístico ejecutable y funcional desde la primera iteración ("hands-on deployment").

### Alcance (Boundary Rules - Qué es y qué NO es)
- **Qué SÍ asume el proyecto:** La implementación técnica real, la automatización del puente de datos, la orquestación documental (integraciones APIs, OCR de albaranes), sistemas de alertas, e ingeniería de sistemas acoplable de alta disponibilidad.
- **Qué NO asume el proyecto:** No es una gestoría laboral o de nóminas, no somos fabricantes de un sistema monolítico (TMS "todo en uno") y no hacemos consultoría de management corporativo puramente teórica (cualquier hora facturada acaba en código o sistema operativo).

---

## Nota de Registro NotebookLM
_Documento auditado y respaldado por el sistema inteligente de fuentes e hitos_
- **notebook_title:** ZAC_Bloque_1
- **notebook_id:** a9776342-15b0-4d0d-9280-86fb060e7027

**Registro (HITO)**
- **hito_note_title:** HITO: Canvas Propuesta de Valor
- **hito_note_id:** ff2aa51a-0ab0-46c0-b313-bc64ee7d5589

**Auditoría semántica (Gate 7)**
- **auditoria_note_title:** AUDITORÍA SEMÁNTICA — 02_canvas_valor.md
- **auditoria_note_id:** c7d8a63e-4e6b-4e0c-a798-45b74d99a693
- **fecha:** 2026-03-03
