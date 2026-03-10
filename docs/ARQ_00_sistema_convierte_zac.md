

# Manual Operativo Definitivo

## Sistema CONVIERTE ZAC — Repo + Antigravity + NotebookLM + Entregables

**Propósito:** Este repositorio existe para **desarrollar el proyecto CONVIERTE (ZAC)** de forma ordenada, trazable y repetible, permitiendo **explorar varias opciones (nichos/pivotes)** y, una vez elegida una opción, ejecutar **linealmente** el cronograma de entregables del programa.

---

## 1) Qué estamos construyendo realmente

Estamos construyendo **dos cosas al mismo tiempo**:

1. **El proyecto de negocio ZAC** (la idea y su validación: mercado, dolor, propuesta, viabilidad).
2. **Un sistema de trabajo reutilizable** para cualquier proyecto futuro (logística, panadería, peluquería, carpintería, software, etc.), basado en:

   * evidencia (NotebookLM),
   * decisiones registradas,
   * entregables por cronograma,
   * control de calidad (gates),
   * y presentación final legible.

---

## 2) Principio rector: dos carriles (dos modos de trabajo)

### Carril A — Exploración (multi-opción / pivotes)

Aquí se trabaja para **comparar opciones** y decidir:

* nicho vs otro nicho,
* subnicho,
* dolor específico,
* enfoque de solución.

**Regla:** En exploración se permiten hipótesis, comparativos y decisiones.
**Meta:** elegir la **opción activa** con la que se ejecutará el cronograma.

### Carril B — Ejecución (cronograma lineal / entregables)

Aquí se trabaja una sola opción (la elegida) y se produce:

* Mapa de empatía,
* Canvas de propuesta de valor,
* PESTEL, DAFO,
* ODS,
* Resúmenes para tutor,
* y cualquier entregable del cronograma.

**Regla:** En ejecución, todo debe estar trazado y auditado.
**Meta:** entregar documentos sólidos y coherentes por bloque.

---

## 3) Regla clave de orden: una opción activa en `output/`

* En `output/` **solo existe una opción activa a la vez**.
* Todo lo que sea “otra opción”, “comparativo para elegir”, o “posible pivot”, vive en `exploracion/`.

Esto evita que el repo se llene de documentos contradictorios o duplicados.

### 3.1) Declaración oficial de la Opción Activa (obligatoria)
La opción activa se declara **siempre** en: `docs/OPCION_ACTIVA.md`.

Todo documento en `output/` debe alinearse con esa opción activa.  
Si hay un pivote, primero se actualiza `docs/DECISION_LOG.md` y luego `docs/OPCION_ACTIVA.md`.

---

## 4) Estructura estándar del repositorio

### `docs_base/` — Fuentes y materiales base (no entregables)

Aquí van:

* Documento A y Documento B
* Cronograma oficial
* PDFs / informes / documentos externos
* manuales y bibliografía

**Prohibido:** colocar entregables finales aquí.

### `exploracion/` — Árbol de opciones (Carril A)

Aquí modelamos el árbol:

* `transporte/`
* `transitarios/`
* `almacenamiento/`
* `otros/`

Dentro de cada nodo (nicho/subnicho/dolor), siempre debe existir:

* `README_nodo.md` (qué es, hipótesis, a quién sirve)
* `research/` (resumen + trazabilidad NotebookLM)
* `decision/` (por qué seguimos / por qué descartamos)
* `artefactos/` (canvas preliminares, mapas preliminares, comparativos)

### `output/` — Entregables por bloque (Carril B)

Aquí viven los entregables lineales del programa:

* `output/bloque_1/`
* `output/bloque_2/`
* …

**Regla:** lo que está aquí es lo que se considera “entregable oficial del programa” (internamente).

### `docs/` — Manuales, arquitectura, políticas internas

Aquí van las reglas del sistema:

* manual operativo,
* contrato editorial,
* política de aprobaciones,
* taxonomía,
* registro de decisiones,
* glosario.

---

## 5) Entregables del programa: qué son y cómo se gestionan

### Qué es un entregable

Un entregable es un documento en `output/` que:

* responde a un requisito del cronograma,
* se puede leer y entender sin contexto del repo,
* y está respaldado por evidencia o hipótesis validables.

### 5.1) Regla de ubicación (para evitar duplicidades)
- Si un documento sirve para **decidir entre opciones**, vive en `exploracion/`.
- Si un documento sirve para **cumplir el cronograma**, vive en `output/`.
- Nunca se mezclan ambos propósitos en el mismo archivo.

### Reglas de contenido

* Si hay números “duros” como hechos → deben tener **Fuente sólida** (y estar importada en NotebookLM).
* Si no hay fuente sólida → deben ser **HIPÓTESIS** (y decir cómo se validará).
* Debe estar anclado a la opción activa (no logística genérica).

### Jerarquía de documentos cuando hay varios “similares”

Ejemplo mapas de empatía:

* Mapa Empatía Transporte = específico
* Mapa Empatía Transitario = específico
* Comparativo = **solo para decidir** (por eso suele vivir en exploración)

---

## 6) Canvas: contenido y presentación (Streamlit u otro)

### Canvas como entregable

El **Canvas de Propuesta de Valor** es un entregable oficial de Bloque 1 (cuando aplique).

Debe estar en:

* `output/bloque_1/02_canvas_valor.md`

### Canvas presentable (formato “bonito”)

Además del Markdown, el sistema puede generar una versión presentable en:

* **Streamlit** (recomendado),
* u otro sistema similar (por ejemplo: una vista HTML, un PDF formateado, etc.).

**Importante:**

* El Markdown en `output/` siempre es la **fuente de verdad**.
* La versión en Streamlit es **solo presentación** (no reemplaza el contenido).

### Qué debe mostrar el Canvas presentable

* secciones claras del canvas,
* KPIs y criterios de medición,
* “opción activa” y “dolor” en cabecera,
* y si aplica, “fuentes/hipótesis” con notas cortas.
- Estado del entregable (READY_FOR_REVIEW / DONE).
- Opción activa y dolor (tomados de `docs/OPCION_ACTIVA.md`).
- Trazabilidad NotebookLM (visible o colapsable): notebook_id y note_id.
- Versión/fecha del entregable (para control de cambios).

---

## 7) NotebookLM: para qué se usa y cómo se usa

### NotebookLM es biblioteca de evidencia

NotebookLM se usa para:

* importar fuentes reales (documentos oficiales, informes, etc.)
* mantener el registro de investigaciones
* evitar inventar datos

### Regla de oro de evidencia

* Todo “HECHO” numérico debe tener fuente sólida importada en NotebookLM.
* Todo entregable debe cerrar con su nota de registro (ver siguiente sección).

---

## 8) Trazabilidad obligatoria (bloque final en cada entregable)

Todo documento en `output/` debe terminar con:

**Regla:** 1 entregable en `output/` = 1 nota dedicada en NotebookLM (no se reutilizan notas entre entregables).

**Nota de Registro NotebookLM**

* notebook_title
* notebook_id (UUID)
* note_title
* note_id (UUID)
* fecha (YYYY-MM-DD)

Esto permite auditar después sin confusiones.

---

## 9) Antigravity: qué hace y cómo trabaja

Antigravity es el ejecutor del repo:

* edita y crea archivos,
* ejecuta skills,
* aplica gates,
* registra notas en NotebookLM,
* y mantiene el índice.

**Regla operativa:** tú decides el cierre.
Antigravity no puede mover documentos a DONE final sin tu aprobación literal.

---

## 10) Gates de calidad (auditoría interna)

### Gate 1 — Fuentes y veracidad

* HECHOS numéricos solo con fuente sólida.
* Si no hay fuente sólida → HIPÓTESIS.

### Gate 2 — Dominio y no generalidad

* Debe hablar del dolor real y operativo.
* Evitar macro texto vacío.

### Gate 2.1 — Enfoque (anti-deriva)
- El texto debe conectar con la **Opción Activa** y el **Dolor principal** declarados en `docs/OPCION_ACTIVA.md`.
- Temas secundarios (ej. aduanas/DUA) solo si la opción activa lo requiere.
- Si no se cumple, el entregable queda **BLOCKED** aunque los otros gates pasen.

### Gate 3 — Métricas mínimas

* Mínimo 3 métricas por entregable (si aplica).
* Si son métricas inventadas → deben ser HIPÓTESIS y decir cómo se validarán.

### Gate 4 — Trazabilidad NotebookLM

* Bloque final completo con 5 campos.

---

## 11) Política de aprobación (la regla que mantiene el sistema limpio)

Un documento solo se considera cerrado cuando tú escribes:

**Aprobado: <nombre del entregable> (ruta del archivo)**

Estados internos recomendados:

* TODO
* IN_PROGRESS
* READY_FOR_REVIEW
* DONE
* BLOCKED

---

## 12) Flujo de trabajo estándar (paso a paso)

Para cualquier entregable oficial (output):

1. Confirmar la **opción activa** (nicho/subnicho/dolor)
2. Ejecutar gate “¿requiere investigación?”
3. Si requiere: research_start → importar fuentes → research_status
4. Redactar / editar el entregable en Markdown
5. Ejecutar auditoría determinista (Python gates)
6. Corregir hasta PASS
7. Auditoría semántica (NotebookLM / IA) usando `docs/PLANTILLA_AUDITORIA_SEMANTICA.md` para verificar sentido, enfoque y coherencia CONVIERTE.
8. Registrar en NotebookLM (nota con IDs)
9. Dejar en READY_FOR_REVIEW
10. Tú apruebas (“Aprobado: …”)
11. Se mueve a DONE en índice


## 13) Uso de Python en este sistema (cuándo SÍ vale la pena)

### Principio clave

En este repo, Python se usa **solo** para tareas **deterministas** (verificables, repetibles y sin interpretación).
Python **NO** se usa para “inventar contenido”, “decidir por ti” o “hacer IA”.

Piensa en Python como un **guardia de calidad** que evita errores humanos.

---

# 13.1 Cuándo SÍ usar Python (3 usos recomendados)

## Uso 1 — Validador automático de entregables (blindaje de gates)

**Cuándo usarlo:** cada vez que se termina un documento en `output/` o antes de cerrar un bloque completo.

**Qué hace el script:**

* Recorre `output/bloque_X/*.md` y verifica:

  1. Existe el bloque **“Nota de Registro NotebookLM”** al final.
  2. Tiene los **5 campos obligatorios**:

     * notebook_title
     * notebook_id (UUID)
     * note_title
     * note_id (UUID)
     * fecha (YYYY-MM-DD)
  3. Detecta `[HECHO]` con números sin “Fuente sólida”.
  4. Verifica mínimo de métricas/KPIs cuando aplique (ej. 3).
  5. Reporta PASS/FAIL por archivo con razón exacta.

**Por qué es útil:**
Evita que se te “escape” un documento sin trazabilidad o con números peligrosos.

**Convención:** Los validadores Python viven en `scripts/` y generan reportes en `reports/` (Markdown o JSON) que se adjuntan al cierre de bloque.

---

## Uso 2 — Auditor anti-deriva (evitar que el contenido se vuelva genérico o se desvíe)

**Cuándo usarlo:** cuando notes que Antigravity “se va” hacia logística genérica, aduanas sin motivo, o macro vacío.

**Qué hace el script:**

* Para la **opción activa** (ej. Transporte):

  * Verifica que los entregables mencionen palabras ancla mínimas:

    * CMR/eCMR, POD, albarán, incidencias, subcontrata, conciliación, doc-to-cash…
  * Detecta términos “fuera de foco”:

    * DUA/aduanas en documentos de Transporte (sin justificación)


---

## Uso 3 — Generador/actualizador del índice (evitar inconsistencias en estados)

**Cuándo usarlo:** cuando ya hay varios entregables y el índice puede desalinearse.

**Qué hace el script:**

* Lee `output/bloque_1/`
* Según el validador:

  * sugiere estado por archivo:

    * BLOCKED (si falta trazabilidad)
    * READY_FOR_REVIEW (si pasa gates)
    * DONE (si existe aprobación explícita registrada)
* Genera un reporte y/o un “diff sugerido” para `ZAC_INDEX_00.md`

**Por qué es útil:**
Evita el error típico: “el índice dice DONE pero el archivo no cumple”.

---

# 13.2 Cuándo NO usar Python (para evitar perder tiempo)

## NO usar Python para:

* crear el contenido de mapas/canvas/PESTEL/DAFO (eso es editorial)
* decidir qué nicho elegir (eso es decisión estratégica)
* “poner números” para que pase Gate 3
* reemplazar NotebookLM (fuentes y evidencia van ahí)

En resumen:

* **NotebookLM = evidencia y auditoría semántica (sentido y enfoque)**
* **Antigravity = ejecución de redacción y corrección de gates**
* **Python = verificador automático determinista (estructura y riesgos)**

---

# 13.3 Momento recomendado para introducir Python (sin adelantarnos)

Para no complicar el sistema demasiado pronto:

### Fase 1 (ahora)

* Solo definir la “política” (este capítulo) y el contrato del validador.

### Fase 2 (cuando Bloque 1 esté estable)

* Implementar el validador #1 (típicamente el más útil).

### Fase 3 (cuando haya varios bloques)

* Implementar auditor deriva + actualizador de índice.

---

# 13.4 Regla operativa final (simple)

**Si la tarea es “verificar / validar / detectar”, Python sí.**
**Si la tarea es “escribir / decidir / argumentar”, Python no.**

---

---

## 14) Qué hacer cuando hay pivote (cambio de opción)

1. Registrar decisión en `docs/DECISION_LOG.md`:

   * qué opción se descarta,
   * por qué,
   * qué evidencia lo motivó.
2. Mover todo lo “no activo” a `exploracion/`.
2.1) Congelar histórico del output anterior:
- Copiar el estado final del bloque a `exploracion/<opcion_anterior>/artefactos/` como histórico (sin seguir editándolo).
- Mantener `output/` limpio para la nueva opción activa.
3. Definir nueva opción activa.
4. Reiniciar Bloque 1 si el pivot cambia el corazón del proyecto (solo si corresponde).

---

# Cierre: qué resuelve este manual

* Evita desorden de documentos duplicados.
* Permite explorar opciones sin contaminar entregables oficiales.
* Obliga trazabilidad y evidencia.
* Da un flujo lineal para ejecutar el cronograma.
* Permite tener Canvas presentables sin perder la fuente de verdad.

---

