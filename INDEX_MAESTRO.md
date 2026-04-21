# INDEX MAESTRO: Proyecto_automatizaciones

Este documento es el eje central de navegación del repositorio, separando el núcleo metodológico del sistema de los casos de prueba sectoriales.

## 0) Identidad del Sistema (Core App)
- **Nombre:** Proyecto_automatizaciones
- **Propósito:** Sistema general de acompañamiento al emprendedor para la validación y estructuración de modelos de negocio.
- **Marco Rector de Redacción:** [ARQ_01_MARCO_RECTOR_REDACCION.md](docs/ARQ_01_MARCO_RECTOR_REDACCION.md)
- **Regla de Oro:** [RULE_NO_SESGO_SECTORIAL_EN_CORE.md](.agent/rules/RULE_NO_SESGO_SECTORIAL_EN_CORE.md)

---

## 🧠 BLOQUE I: NÚCLEO METODOLÓGICO (Agnóstico)

Define la lógica, fases y contratos de datos que aplica a cualquier proyecto de emprendimiento.

### A. Metodología de Fases
- [Mapa Maestro de Fases](core/fases/00_Mapa_Maestro_Fases.md)
- [Estructura Oficial de Fases (Plantilla)](core/fases/00_Estructura_Oficial_Fases.md)
- [Repositorio de las 12 Fases](core/fases/)

### B. Contrato de Datos (DMV)
- [Tabla Maestra de Campos (DMV)](core/dmv/00_Tabla_maestra_de_campos_DMV.md)

---

## 🚚 BLOQUE II: CASOS DE PRUEBA Y VALIDACIÓN (Sectores)

Implementaciones específicas utilizadas para testear la robustez del sistema.

### 1. Caso: Logística FTL (Activo)
*Aislamiento del historial operativo y entregables del sector transporte.*

- **Índice del Caso:** [cases/logistica/README.md](cases/logistica/README.md)
- **Entregables:** [cases/logistica/output/bloque_1/](cases/logistica/output/bloque_1/)
- **Evidencias de Ejecución:** [cases/logistica/evidencias/DRY_RUN_2_LOGISTICA_LIMPIA.md](cases/logistica/evidencias/DRY_RUN_2_LOGISTICA_LIMPIA.md)
- **Documentos de Contexto:** [cases/logistica/docs/](cases/logistica/docs/)

---

## 🛠️ BLOQUE III: GOBERNANZA Y RUNTIME (Mantenimiento)

Control de la arquitectura, migración y herramientas del repositorio.

### A. Estado de la Migración (Fase 1)
- [Plan Maestro de Migración](output/arquitectura/ARQ_04_plan_de_migracion_del_repositorio.md)
- [Registro de Aislamiento Caso Logístico (Copia)](output/migracion/05_aislamiento_caso_logistico_fase_copia.md)
- [Consolidación Final Core Metodológico](output/migracion/07_consolidacion_final_core_metodologico.md)

### B. Inventario y Componentes
- [Inventario Actual del Repositorio](output/arquitectura/00_inventario_actual_del_repositorio.md)
- [Mapa de Componentes de la App](output/arquitectura/ARQ_01_mapa_de_componentes_de_la_app.md)

---

## 📁 Zona de Control Reciente
- [x] Consolidación del Core Metodológico en `core/fases/`
- [x] Aislamiento del Caso Logístico en `cases/logistica/`
- [x] Redefinición Agnóstica del Índice Maestro
- [ ] Ajuste de Scripts de Validación (Siguiente Paso)
