# Estructura Oficial de Fases del Proyecto

## Propósito del documento

Este documento define la estructura oficial que debe seguir cada fase del proyecto de validación y estructuración empresarial.

Su función es servir como plantilla maestra para documentar de manera coherente todas las fases del proceso, tanto desde la perspectiva de negocio como desde la futura traducción al sistema agéntico de la app.

Este documento debe utilizarse como marco base para redactar todos los documentos individuales de fase.

---

# Estructura oficial de cada fase

## 1. Nombre de la fase

Nombre claro, corto y coherente con el mapa maestro de fases.

---

## 2. Propósito de la fase

Qué resuelve esta fase dentro del proceso completo.

---

## 3. Nivel 1 — Definición de la fase desde negocio

### 3.1 Función de la fase

Qué papel cumple en el avance del emprendimiento.

### 3.2 Objetivo

Qué debe lograr al terminar.

### 3.3 Qué debe conseguir

Resultados concretos que esta fase debe dejar.

### 3.4 Entradas principales

Qué información, documentos, plantillas, archivos subidos por el emprendedor o decisiones previas necesita.

Cuando una fase dependa de un documento estructurado del emprendedor, esa fase debe usar ese documento como base de trabajo para revisar, completar, corregir, validar e integrar, en lugar de reconstruir toda la información desde cero mediante preguntas abiertas.

### 3.5 Preguntas madre

Las grandes preguntas que esta fase debe responder.

### 3.6 Trabajo del asesor

Qué hace el equipo experto en esta fase.

### 3.7 Investigación necesaria

Qué debe investigarse, validarse o contrastarse.

### 3.8 Resultados esperados

Qué documentos, definiciones o decisiones deja la fase.

### 3.9 Condición de cierre

Cuándo se considera suficientemente cerrada.

---

## 4. Nivel 2 — Traducción de la fase al sistema desde lógica de negocio

### 4.1 Función real dentro del proceso

Qué representa esta fase dentro de la lógica completa de la app.

### 4.2 Rol de NotebookLM en la fase

Qué función cumple NotebookLM dentro de esta fase.

### 4.3 Tipo de trabajo experto

Qué tipo de razonamiento o trabajo técnico ocurre aquí.

### 4.4 Arquitectura de roles de la fase

#### 4.4.1 Rol conductor de la fase

Quién lidera la fase y mantiene el foco.

#### 4.4.2 Roles especialistas de apoyo

Qué expertos intervienen dentro de la fase según el tema.

#### 4.4.3 Rol de interacción con el emprendedor

Quién conversa, explica, guía y traduce al usuario cuando hay contacto directo.

#### 4.4.4 Regla de coordinación entre roles

Cómo se organizan:
- quién conduce,
- quién profundiza,
- quién conversa,
- y quién valida.

### 4.5 Entradas funcionales

Qué entradas necesita el sistema para trabajar la fase.

Estas entradas pueden incluir:
- respuestas guiadas del emprendedor,
- documentos o archivos subidos por el emprendedor,
- plantillas parcialmente diligenciadas,
- documentos base obligatorios de fase,
- y salidas estructuradas de fases anteriores.

Si la fase depende de un documento estructurado, el sistema debe priorizar su lectura, análisis, validación y completado antes de volver a preguntar información que ya debería estar contenida allí.

### 4.6 Mecanismo de interacción

Cómo debería interactuar la fase con el emprendedor o con los documentos.

### 4.7 Salidas funcionales mínimas

Qué resultados mínimos debe producir el sistema en esta fase.

### 4.8 Criterio funcional de avance

Qué debe cumplirse para que el sistema permita pasar a la siguiente fase.

### 4.9 Errores que debe evitar

Qué fallos de lógica, negocio o interacción no deben ocurrir.

### 4.10 Relación con el Documento Maestro Vivo

Qué actualiza, crea o modifica esta fase dentro del documento maestro.

---

## 5. Preguntas específicas finales

Banco de preguntas reales de la fase, con formato guiado:

- pregunta,
- para qué se hace,
- ejemplo,
- apoyo si no lo tiene claro,
- repregunta.

---

## 6. Checklist final del auditor

Checklist para decidir si:

- puede avanzar,
- puede avanzar con observaciones,
- o no puede avanzar todavía.

---

## 7. Secciones del Documento Maestro Vivo que se actualizan o nacen

Qué partes del documento maestro:

- se actualizan,
- nacen,
- o se formalizan mejor.

---

## 8. Resumen ejecutivo de la fase

Versión corta y limpia para dejar la fase cerrada.

---

# Lineamientos fijos para usar esta plantilla

## 1. Cada fase tiene una arquitectura de roles, no un solo rol

Esto queda definido como regla oficial.

## 2. Siempre debe existir un rol conductor

Aunque haya varios especialistas.

## 3. Si la fase tiene contacto con el emprendedor, debe existir rol de interacción

No se deja implícito.

## 4. Los roles especialistas no reemplazan al rol conductor

Lo apoyan.

## 5. El auditor no sustituye la fase

La valida al cierre.

## 6. NotebookLM no decide por sí solo

Apoya investigación, memoria, contraste y respaldo.

## 7. El Documento Maestro Vivo se actualiza en todas las fases

No es opcional.

## 8. Toda fase debe distinguir y registrar

- hechos,
- hipótesis,
- vacíos,
- alertas,
- cambios,
- y pivotajes.

## 9. Cuando una fase dependa de un documento estructurado del emprendedor

La fase debe trabajar sobre ese documento como base principal.

Esto implica:
- leerlo,
- revisarlo,
- detectar vacíos,
- pedir solo la información faltante o dudosa,
- corregir incoherencias,
- y consolidarlo como parte del proceso.

No se debe rehacer desde cero mediante preguntas abiertas lo que ya existe en un documento útil aportado por el emprendedor.

---

# Qué permite esta plantilla

## Capa 1 — Negocio

Sirve como guía real para acompañar al emprendedor.

## Capa 2 — Sistema

Sirve como base para luego definir:

- agentes,
- skills,
- auditorías,
- orquestación,
- y flujos de trabajo.

---

# Decisión metodológica

Con esta estructura ya no se improvisan fases.

Desde ahora, cada fase que se redacte será:

- un documento base,
- una guía metodológica,
- y una pieza de diseño del sistema.

---

# Regla de uso

Toda fase del proyecto debe seguir esta estructura oficial.

Se permite ampliar el contenido de una fase cuando sea necesario, pero no eliminar bloques obligatorios sin una justificación metodológica explícita.