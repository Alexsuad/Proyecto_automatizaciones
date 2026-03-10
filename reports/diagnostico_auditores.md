# Auditoría del Sistema de Auditores (ZAC)
> Fecha de evaluación: 2026-03-09

## 1. Resumen Ejecutivo
El repositorio cuenta con un sistema robusto, con una fuerte tendencia hacia verificaciones deterministas (Python) que previenen eficazmente errores básicos de formato, trazabilidad y estilo. Se ejecutan e impactan el flujo real. Sin embargo, la capa semántica (IA) está desconectada y desactualizada respecto al código Python. Existen **contradicciones importantes** entre lo que exigen las Skills y lo que exigen los scripts, y se detectó que el mecanismo de integración de reportes semánticos (Gate 7) usa actualmente datos anidados en código (*hardcodeados*) en lugar de un flujo automatizado real. **No se requieren auditores nuevos, sino sincronizar y despurgar los existentes.**

---

## 2. Inventario de Auditores Actuales

| Nombre del auditor / gate | Tipo | Ruta | Función declarada | ¿Existe? | ¿Se ejecuta? |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **Estilo Institucional** | Script Python | `scripts/validar_estilo_equipo.py` | Evita palabras baneadas, grandilocuencia y 1ra persona. | Sí | Sí |
| **Integridad y Métricas** | Script Python | `scripts/validar_entregables.py` | Exige formato NLM, 3 métricas, fuentes sólidas en números. | Sí | Sí |
| **Anti-Deriva Editorial** | Script Python | `scripts/auditar_deriva_editorial.py` | Evita menciones a temas fuera de la `OPCION_ACTIVA.md`. | Sí | Sí |
| **Coherencia Cruzada** | Script Python | `scripts/gate_coherencia_cruzada.py` | Detecta si un HECHO en un doc es HIPÓTESIS en otro. | Sí | Sí (Alerta) |
| **Reporte Semántico G7** | Script Python / Parche | `scripts/generar_reportes_gate7.py` | Transfiere la auditoría semántica al repositorio como .md | Sí | Sí (Falso)* |
| **Gate 7 (Plantilla)** | Documento Markdown | `docs/PLANTILLA_AUDITORIA_SEMANTICA.md`| Guía humana/IA para el análisis de sentido del modelo de negocio. | Sí | Sí |
| **Auditor de Entregable** | Skill | `.agent/skills/skill_auditar_entregable.md` | Consolida todos los gates (0,1,2,3,4) en una instrucción IA. | Sí | No explícito |

*(Falso): El script se ejecuta, pero la información de auditoría está pre-escrita a mano (hardcodeada) dentro del archivo Python y no se genera en tiempo real.*

---

## 3. Matriz de Alcance y Riesgos (Fase 2 y 3)

| Auditor | Qué revisa | Qué NO revisa | Qué evidencia deja | Bloquea | Riesgo / Impacto |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **Estilo (Py)** | Vocabulario prohibido, promesas absolutas, "yo/mi". | Sentido o coherencia de las frases. | `reports/reporte_estilo_bloque_X.md` | SÍ | **Bajo**. Efectivo y seguro. |
| **Entregables (Py)** | Estructura de bloques NLM, UUIDs válidos, cifras con "Fuente sólida", base de métricas > 3. | Calidad analítica real o fuentes verdaderas. | `reports/reporte_validacion_bloque_X.md` | SÍ | **Bajo**. Pipeline determinista muy exigente. |
| **Deriva (Py)** | Ocurrencia de anclas (CMR) vs. términos desviados (DUA) (con filtro legal). | Sentimiento o conclusiones del archivo. | `reports/reporte_deriva_bloque_X.md` | SÍ | **Moderado**. Puede errar en métricas límite. |
| **Cruzada (Py)** | Entidades (SAP, Fenadismer) rotuladas múltiplemente (HECHO vs HIPÓTESIS). | Impacto de negocio de la entidad. | `reports/reporte_coherencia_cruzada_bloque_X.md` | NO | **Bajo**. Útil y pasivo. |
| **Auditor (Skill)** | Reglas idénticas al Python, pidiendo a IA hacerlas. | --- | Salida LLM o interrupción. | SÍ | **Alto**. Repite el trabajo de Python y exige formatos de NLM viejos. |

---

## 4. Redundancias, Huecos y Contradicciones

### 4.1 Contradicciones (Grave)
1. **Conflicto de Formatos NLM:** El script `validar_entregables.py` exige el formato estricto con `hito_note_id` y `auditoria_note_id`. Sin embargo, el `.agent/skills/skill_auditar_entregable.md` (Gate 4) exige el formato obsoleto (solo `note_id`). Esto hace que la IA reciba instrucciones contradictorias y pueda romper el pipeline determinista.
2. **Duplicidad de Esfuerzos (IA vs Determinismo):** La `skill_auditar_entregable.md` contiene *instrucciones completas* para contar palabras baneadas, verificar métricas numéricas y fuentes sólidas. Estas acciones **ya las hace el Python de forma determinista y perfecta**. Pedir a la IA que cuente "3 métricas" falla frecuentemente debido a la arquitectura LLM, mientras que la heurística en Python lo cuenta exacto de forma determinista.

### 4.2 Huecos (Grave)
1. **Auditoría Semántica Desconectada:** El script `scripts/generar_reportes_gate7.py` contiene un diccionario de Python pre-cargado con texto escrito a mano con las auditorías del bloque 1. **No está automatizado para escalar (Bloque 2 no tiene soporte sin editar el script).** Ningún bot ni script va a NotebookLM a traerse la evaluación y hacer el archivo .md; es una simulación.

---

## 5. Evaluación de Suficiencia

- **¿Son suficientes para el estado actual?** Sí, en términos de cantidad de "chequeos", el sistema está incluso sobre-parametrizado. El código determinista es sorprendentemente minucioso.
- **¿Son suficientes para escalar a más bloques?** **NO.** Si empezamos el bloque 2, el `generar_reportes_gate7.py` se va a romper o dejar de emitir archivos porque requiere intervención manual (modificar el dict en código de Python). 
- **¿Faltan o sobran?** **Sobran instrucciones duplicadas en las skills**. Faltan integraciones reales. El punto de quiebre actual está en la fricción que causa tener la misma regla en la skill y en Python.

---

## 6. Veredicto por Auditor

| Auditor / Gate | Veredicto | Motivo (Prioridad) |
| :--- | :--- | :--- |
| `validar_estilo_equipo.py` | **MANTENER** | Funciona perfecto. Determinismo ideal para reglas léxicas. (Prioridad Baja) |
| `validar_entregables.py` | **MANTENER** | Clave para obligar trazabilidad real NLM y sintaxis de fuente sólida. (Prioridad Baja) |
| `auditar_deriva_editorial.py` | **MANTENER** | Funciona como safety-net antes de aprobar entregables. Buen regex legal. (Prioridad Baja) |
| `gate_coherencia_cruzada.py`| **MANTENER** | Pasivo, da info valiosa. (Prioridad Baja) |
| `PLANTILLA_AUDITORIA.md` | **MANTENER** | Gran base para hacerle el QA puro de negocio. (Prioridad Baja) |
| `generar_reportes_gate7.py` | **RECREAR / ELIMINAR** | **URGENTE**. Es un parche hardcodeado de diccionario en Python. La generación de este reporte la debiera hacer Antigravity por instrucción en lugar de falsear un script que "crea" los archivos. (Prioridad Alta) |
| `skill_auditar_entregable.md`| **AJUSTAR (Poda)** | **URGENTE**. Tiene Gates 0 al 4 que YA HACE PYTHON. La IA no debe auditar ni formato NLM ni conteo de métricas exactas; debe auditar **la calidad y el negocio** usando la Plantilla Semántica. (Prioridad Alta) |

---

## 7. Diagnóstico Global

Hoy en día, el repositorio posee un sistema de validación **parcialmente sólido, pero descompensado**.
La capa "sintáctica" (Python) está resuelta con excelencia, mitigando riesgos de lenguaje genérico y forzando estándares de código de forma determinista (siguiendo las Reglas de Intake / Híbridas del usuario).
Sin embargo, la capa "semántica" (IA) sufre de **confusión de roles**: las instrucciones a la IA (Skills) intentan hacer el trabajo aburrido que ya hace Python, y al mismo tiempo el trabajo clave de la IA (Gate 7 semántico) fue reemplazado por un documento hardcodeado en un script de Python que aparenta un proceso automático. El salto real no es crear nuevos auditores visuales, sino limpiar el flujo de modo que Python haga lo estructurado e IA haga puramente validación lógica sin solaparse.

---

## 8. Recomendación Final

> **¿Conviene crear nuevos auditores/agentes ahora?**
> **NO, EN ABSOLUTO.**

Primero se debe **depurar, organizar y fortalecer** lo existente. 

**Hoja de Ruta Inmediata (Antes de arrancar el Bloque 2):**

1. **Podar la `skill_auditar_entregable.md`:** Eliminar toda exigencia de formato NLM (Formatos 0, 1, 3, 4) para evitar la doble validación cruzada contradictoria. Dejarla exclusivamente como un asistente de auditoría cualitativa enganchada a la `PLANTILLA_AUDITORIA_SEMANTICA.md`.
2. **Sustituir la simulación del Gate 7:** Destruir o limitar `generar_reportes_gate7.py`. Implantar una instrucción en el workflow para que sea **Antigravity** (vía tool `write_to_file`) quien genere el archivo `auditoria_semantica_X.md` localmente tras hablar con NotebookLM, en vez de mantener un inventario de textos gigante y rígido pre-cargado en un script de Python.

**Con estas dos acciones, el sistema estará balanceado, mantendrá la protección absoluta actual, pero estará 100% libre de parches para empezar el Bloque 2.**
