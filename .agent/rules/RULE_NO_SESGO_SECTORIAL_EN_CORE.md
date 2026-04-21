# File: .agent/rules/RULE_NO_SESGO_SECTORIAL_EN_CORE.md
# ──────────────────────────────────────────────────────────────────────
# Propósito: Evitar que el núcleo de la app quede contaminado por lógica
# específica de un solo sector de prueba.
# Rol: Regla transversal de arquitectura y revisión de contenido.
# ──────────────────────────────────────────────────────────────────────

# REGLA — NO SESGO SECTORIAL EN EL CORE

## Propósito

La app está diseñada como un sistema general de acompañamiento al emprendedor para analizar proyectos, construir documentación útil por fases y llegar a un Plan de Empresa.

Por tanto:

- el `core/` define lógica general y reutilizable;
- la carpeta `cases/` contiene casos de prueba o validación sectorial;
- ningún caso concreto define el producto.

## Regla madre

**El caso logístico no define la app.**  
`cases/logistica/` es solo un caso de prueba, igual que podrían existir `cases/carpinteria/`, `cases/peluqueria/`, `cases/restaurante/` o cualquier otro.

## Regla operativa obligatoria

Si un contenido, skill, regla, workflow, plantilla, prompt, contrato o campo del DMV:

- solo tiene sentido para logística,
- nombra procesos exclusivos de logística,
- depende de documentos exclusivos del transporte,
- o no podría reutilizarse en otro negocio de emprendimiento,

entonces **NO debe vivir en `core/`**.

Debe vivir en una de estas capas:

- `cases/<sector>/`
- documentación de ejemplo
- anexos sectoriales
- prompts o assets específicos del caso

## Qué sí puede vivir en `core/`

Sí pueden vivir en `core/` elementos generales como:

- cliente
- necesidad
- propuesta de valor
- validación
- modelo de negocio
- mercado
- competencia
- síntesis estratégica
- estructura legal
- marca y comunicación
- viabilidad económica
- integración final y Plan de Empresa

También pueden vivir en `core/` preguntas generales como:

- ¿qué problema resuelves?
- ¿qué evidencia necesitas para cobrar o cerrar una operación?
- ¿qué documentos, hitos o validaciones necesitas para avanzar?
- ¿qué errores te cuestan tiempo, dinero o control?

## Qué NO debe vivir en `core/`

No deben aparecer como lógica base del sistema, salvo en ejemplos o casos:

- CMR / eCMR
- POD
- DUA
- albarán como supuesto universal
- peajes
- subcontrata de transporte
- tacógrafo
- conciliación viaje → evidencia → factura → cobro como si fuera válida para todos los negocios
- referencias a transitarios, navieras o flotas como si fueran parte del modelo general

## Regla de traducción correcta

Cuando un caso sectorial se use para probar la app:

- primero se formula la lógica en lenguaje general;
- después se aterriza al caso sectorial.

### Ejemplo correcto
General:
- “documento o evidencia necesaria para poder facturar o cerrar una operación”

Caso logístico:
- CMR, POD, albarán, evidencia de entrega

Caso carpintería:
- orden de trabajo, diseño aprobado, entrega firmada, anticipo/saldo

Caso peluquería:
- reserva, servicio realizado, productos usados, pago y recurrencia

## Gate de revisión

Antes de aprobar cualquier cambio en `core/`, el sistema debe preguntarse:

1. ¿Esto sirve solo para logística o sirve para cualquier emprendimiento?
2. ¿Este contenido podría entenderse y reutilizarse en carpintería, peluquería, restaurante o servicios profesionales?
3. ¿Estoy metiendo un ejemplo sectorial donde debería haber una formulación general?

Si la respuesta indica dependencia sectorial fuerte, el cambio debe bloquearse o moverse a `cases/`.

## Regla de redacción

En el `core/`:

- usar lenguaje general;
- evitar ejemplos logísticos como redacción principal;
- si se usa un ejemplo sectorial, marcarlo explícitamente como ejemplo y no como regla universal.

## Criterio de arquitectura

- `core/` = producto general
- `cases/` = pruebas por sector
- `programa_convierte/` = entregables del programa
- `research/` = evidencia e investigación
- `runtime/` = ejecución en Antigravity

## Cierre

Toda mejora hecha a partir del caso logístico debe fortalecer la app general, no convertirla en una herramienta exclusiva para logística.
