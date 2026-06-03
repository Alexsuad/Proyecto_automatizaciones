# SPEC-005 — Contrato futuro de `.agent/skills` y `.agent/workflows`

## Estado
Propuesto / Pendiente de desarrollo.

## Propósito
Definir el contrato mínimo futuro para clasificar, validar y gobernar `.agent/skills` y `.agent/workflows` sin tratarlos prematuramente como runtime puro ni como documentación informal.

## Decisión inicial
Mientras esta SPEC no esté aprobada, `.agent/skills` y `.agent/workflows` quedan clasificados como `PROCESS operativo provisional`.

Esto significa:
* No se reorganizan.
* No se ejecutan como contrato runtime formal.
* No se copian indiscriminadamente a proyectos vivos.
* No se consideran fuente normativa superior.
* No se usan para contaminar el framework con workflows de caso histórico.

## Contenido mínimo futuro de una skill oficial
Toda skill oficial deberá declarar:
* propósito;
* cuándo usarla;
* entradas;
* salidas;
* permisos;
* restricciones;
* evidencia requerida;
* errores que detecta;
* criterio de cierre;
* relación con runtime;
* zona operativa;
* estado: oficial / candidata / legacy / caso específico / no ejecutable.

## Contenido mínimo futuro de un workflow oficial
Todo workflow oficial deberá declarar:
* propósito;
* alcance;
* pasos;
* entradas;
* salidas;
* dependencias;
* permisos;
* evidencia requerida;
* criterios de bloqueo;
* criterio de cierre;
* relación con skills;
* relación con runtime;
* zona operativa;
* estado: oficial / candidato / legacy / caso específico / no ejecutable.

## Reglas de protección
* Ninguna skill o workflow heredado se considera oficial sin revisión.
* Ningún workflow de caso histórico puede operar como workflow general del framework.
* Ninguna skill o workflow puede alimentar runtime formal sin contrato aprobado.
* Toda promoción debe registrar evidencia y aprobación humana.

## Relación con ADR-002
Esta SPEC desarrolla el punto pendiente de ADR-002 sobre `.agent/skills` y `.agent/workflows`.
