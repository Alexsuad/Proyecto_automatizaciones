# Guía de Tono y Voz Institucional (Proyecto_automatizaciones)

Esta guía define el estándar de redacción obligatorio para todos los entregables, auditorías y documentos del repositorio Sistema_ProyectoAuto. El objetivo es mantener un perfil profesional, pragmático, objetivo y medible.

## 1. Voz Institucional Obligatoria
- **Se usa SIEMPRE la voz de equipo o forma impersonal:** “nosotros”, “nuestro”, “el equipo”, “la iniciativa”, “se define”, “se propone”, “se valida”, “se observa”.
- **PROHIBIDO:** El uso de la primera persona singular (“yo”, “mi”, “me”, “mío”, “conmigo”), salvo que sea una cita literal o un testimonio explícitamente marcado como tal (ej. `> "Cita del transporte"`).

## 2. Tono Antihumo y Pragmatismo (CONVIERTE)
El tono debe ser de **negocios, profesional y claro**. Las decisiones se explican como hipótesis sujetas a validación comercial o técnica.

- **Prohibidas las promesas absolutas** sin validación o fuente: 
  - Evitar: “garantiza”, “100%”, “seguro”, “mínimo X días”, “>95%”, “erradica”.
  - Reemplazar por formulaciones basadas en hipótesis: “[HIPÓTESIS] buscamos reducir...”, “se validará en piloto midiendo X”, “nuestro objetivo empírico es...”.

## 3. Identidad Corporativa y Regla Anti-Deriva (Crucial)
El sistema debe mantener inquebrantable nuestra identidad como **Empresa de Servicios B2B a medida e integración operativa**, evitando derivas hacia producto de masas.
- **La Regla Anti-ZAC:** PROHIBIDO usar la palabra "ZAC" como nombre de la empresa, marca o sistema. Referirse a la entidad como `Proyecto_automatizaciones`, `la empresa consultora`, `el modelo de servicio propuesto`.
- **La Regla Anti-SaaS:** PROHIBIDO autodefinir la solución como "SaaS", "App", "Nuestra exitosa plataforma", "Software enlatado" o "Suscripción genérica masiva". *(Excepción: estas palabras sí se usan para describir a la competencia o alternativas del mercado).*
- **La Regla Financiera:** El lenguaje financiero no debe orientarse a la "venta de licencias". Debe comunicar "setup de arquitectura + soporte continuo B2B".

## 4. Glosario de Invalidez (Palabras a evitar)
Queda estrictamente prohibida la **jerga bélica, emocional o grandilocuente**.
Lista de términos bloqueados en los validadores:
- modo militar
- misión cumplida
- letal
- quirúrgico
- mutilada
- infierno
- elefantes
- brutal
- salvando semanas
- erradicación
- erradica

## 5. Tratamiento de la Competencia
- **Prohibido ridiculizar o adjetivar negativamente** a la competencia (ej. "dinosaurios", "elefantes", "infierno de uso").
- Describir a los competidores con un **tono neutro, descriptivo y analítico**: “suite integral”, “plataforma generalista”, “herramienta de gran calado”, “status quo manual”.
- Todo atributo asignado a la competencia debe respaldarse en una fuente de NotebookLM o plantearse como una hipótesis verificable.
- (Recordatorio: Las palabras como *SaaS* o *plataformas estandarizadas* son el vocabulario descriptivo correcto para definir a los competidores tecnológicos de producto escalable).

## 6. Excepciones Controladas
Cualquier desviación intencionada de esta guía debe acogerse al sistema de excepciones documentado en `docs/EXCEPCIONES_ESTILO_Y_CONTENIDO.md`. El documento anómalo deberá incluir explícitamente el marcador `**Excepción aplicada:** EXC-YYYY-MM-DD-XX` para que el validador lo permita.

## 7. Regla de Claridad y Familiaridad Técnica
Cuando el sistema genere o reescriba contenido que incluya términos técnicos, debe seguir este criterio:
- **Formato obligatorio:** `término técnico (explicación sencilla en lenguaje de negocio)`.
- **Uso:** Aplicar en la primera aparición del término o en puntos de decisión clave.
- **Objetivo:** Evitar que el sistema hable un "idioma técnico" que el equipo no pueda trasladar al cliente de forma natural.
- **Lista de referencia:**
  - retainer (mantenimiento mensual)
  - rollout (despliegue / puesta en marcha extendida)
  - wedge (cuña de entrada)
  - MVP (versión inicial útil)
  - kernel técnico (núcleo reutilizable)
- **Criterio de poda:** Si la aclaración sobrecarga el texto o el término no aporta valor real, priorizar la versión sencilla en español.
