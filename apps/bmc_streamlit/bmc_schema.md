# Business Model Canvas (BMC) - Contrato de Datos

Este documento define la estructura oficial para el almacenamiento de datos del BMC en `data/bmc_state.json`.

## Bloques del BMC (9 Pilares)
Las claves principales del JSON siempre deben ser:
1. `key_partners`: Asociaciones clave.
2. `key_activities`: Actividades clave.
3. `key_resources`: Recursos clave.
4. `value_propositions`: Propuestas de valor.
5. `customer_relationships`: Relaciones con los clientes.
6. `channels`: Canales.
7. `customer_segments`: Segmentos de mercado.
8. `cost_structure`: Estructura de costes.
9. `revenue_streams`: Fuentes de ingresos.

## Estructura de un Post-it (Nota)
Cada nota dentro de un bloque es un objeto JSON con los siguientes campos estrictos:

```json
{
  "id": "uuid a-b-c-d",
  "block": "customer_segments",
  "text": "Contenido del post-it",
  "tag": "hipotesis",
  "order": 1,
  "created_at": "YYYY-MM-DD",
  "updated_at": "YYYY-MM-DD"
}
```

## Contrato de Etiquetas (`tag`)
Las notas solo pueden tener una de las siguientes tres etiquetas (enums):

- **`hipotesis`**: Suposiciones fundamentales que la iniciativa asume, pero que aún no están validadas empíricamente en el contexto del cliente piloto. En el export, requieren un bloque `[HIPÓTESIS] + [CÓMO SE VALIDA]`.
- **`hecho`**: Afirmaciones respaldadas por investigación, entrevistas, o base empírica documentada. No deben contener promesas absolutas ni números inventados. Al exportar, se incluyen bajo viñetas estándar.
- **`accion`**: Siguientes pasos operativos o decisiones directas tomadas por el equipo.
