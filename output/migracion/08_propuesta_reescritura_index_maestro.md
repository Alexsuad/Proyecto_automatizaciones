# File: output/migracion/08_propuesta_reescritura_index_maestro.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Análisis y propuesta de redefinición del índice principal.
# Rol: Plano de navegación para la nueva arquitectura del repositorio.
# ──────────────────────────────────────────────────────────────────────

# 1. Problemas Detectados en el Índice Actual

- **Sesgo Sectorial Dominante**: El índice actual presenta la "Logística FTL" como el foco del proyecto, en lugar de un caso de prueba.
- **Rutas Obsoletas**: Sigue apuntando a `docs/fases_marketing/` (directorio ahora vacío) y a `output/bloque_1/` en lugar de la nueva estructura `cases/logistica/`.
- **Desconexión con el Core**: No hay una sección clara que defina el núcleo del sistema de acompañamiento (`core/`).
- **Narrativa Mezclada**: Confunde entregables de un programa específico con la arquitectura del software.

# 2. Estructura Propuesta (Secciones Nuevas)

El nuevo `INDEX_MAESTRO.md` se organizará en tres grandes bloques jerárquicos:

### I. NÚCLEO DEL SISTEMA (The Core App)
Sección dedicada a la metodología agnóstica y al contrato de datos.
- **Metodología**: Enlace al Mapa Maestro y Estructura en `core/fases/`.
- **Contrato de Datos**: Enlace al DMV en `core/dmv/`.

### II. CASOS DE PRUEBA Y VALIDACIÓN (The Use Cases)
Sección donde reside el valor específico por sector.
- **Caso Logística (Activo)**: Enlace a `cases/logistica/INDEX_LOGISTICA.md` (o sección interna con el historial de logística).
- **Caso Otros**: Placeholder para nuevas implementaciones.

### III. GOBERNANZA Y RUNTIME (The Engine)
Sección para el mantenimiento del sistema.
- **Marco Rector**: Reglas de redacción en `docs/`.
- **Migración y Arquitectura**: Enlace a la carpeta `output/migracion/` y `output/arquitectura/`.

# 3. Acciones Específicas

- **Eliminar**: La tabla de "Cronograma de Validación B2B" centrada en logística de la página principal. Esa tabla se moverá a un índice específico del caso logístico.
- **Corregir**: Todas las rutas de fases para que apunten a `core/fases/`.
- **Añadir**: Una sección de "Identidad del Sistema" que deje claro que el producto es una App de Acompañamiento General.

# 4. Riesgos de No Actualizar

- **Desorientación del Agente**: El sistema podría seguir intentando escribir o leer de carpetas obsoletas.
- **Incoherencia Documental**: El repositorio cuenta una historia (Logística) mientras que la arquitectura física cuenta otra (Core App).
- **Mantenimiento Imposible**: Dificultad para añadir nuevos casos de prueba si la raíz sigue "secuestrada" por la lógica logística.
