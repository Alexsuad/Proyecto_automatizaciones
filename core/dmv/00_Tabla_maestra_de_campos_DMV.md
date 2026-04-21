# Tabla maestra inicial de campos del Documento Maestro Vivo (DMV)

| Campo | Bloque | Nace en fase | Se actualiza en | Tipo sugerido | Obligatorio | Nota de uso |
|---|---|---:|---|---|---|---|
| proyecto_id | Identidad general | 01 | Todas | string | Sí | Identificador único del proyecto |
| nombre_provisional | Identidad general | 01 | 09, 10 | string | No | Nombre inicial o provisional del proyecto |
| estado_proyecto | Identidad general | 01 | Todas | string enum | Sí | Ej. inicial, en definición, en validación, en cierre |
| fecha_inicio_proceso | Identidad general | 01 | — | date | Sí | Fecha de apertura del proceso |
| ultima_actualizacion | Identidad general | 01 | Todas | datetime | Sí | Última modificación del DMV |

| formulacion_inicial_proyecto | Definición del proyecto | 01 | 02 | string | Sí | Cómo se entiende inicialmente la idea |
| narrativa_emprendedor | Perfil del emprendedor | 01 | 02 | string | Sí | Explicación libre del emprendedor |
| motivacion_principal | Perfil del emprendedor | 01 | — | string | Sí | Qué mueve al emprendedor a iniciar |
| problema_necesidad_percibida | Perfil del emprendedor | 01 | 03 | string | Sí | Problema o necesidad percibida al inicio |
| intensidad_preliminar_problema | Perfil del emprendedor | 01 | 03, 04 | string enum | No | Bajo, medio, alto; o equivalente |
| relato_externo | Perfil del emprendedor | 01 | 02 | string | No | Cómo lo cuenta hacia afuera |
| duda_interna | Perfil del emprendedor | 01 | 02, 04 | string | No | Miedos, dudas y fragilidades iniciales |
| tiempo_disponible | Perfil del emprendedor | 01 | 05, 11 | string | No | Tiempo real disponible |
| recursos_iniciales | Perfil del emprendedor | 01 | 05, 11 | list[string] | No | Recursos con los que cuenta |
| limitaciones_iniciales | Perfil del emprendedor | 01 | 05, 11 | list[string] | No | Límites reales de arranque |
| apoyos_red_cercana | Perfil del emprendedor | 01 | 09 | list[string] | No | Red de apoyo o acompañamiento |
| diagnostico_inicial_claridad | Perfil del emprendedor | 01 | 02 | string enum | Sí | Bajo, medio, alto o equivalente |
| diagnostico_inicial_madurez | Perfil del emprendedor | 01 | 04, 08, 12 | string enum | Sí | Nivel de madurez del proyecto |
| alertas_tempranas | Perfil del emprendedor | 01 | Todas | list[string] | No | Alertas relevantes tempranas |

| definicion_inicial_proyecto | Definición del proyecto | 02 | 08, 12 | string | Sí | Definición ya más ordenada |
| descripcion_general_proyecto | Definición del proyecto | 02 | 12 | string | Sí | Descripción comprensible del proyecto |
| alcance_inicial | Definición del proyecto | 02 | 05, 08 | string | Sí | Qué incluye esta etapa |
| foco_inicial | Definición del proyecto | 02 | 05, 08 | string | Sí | Prioridad de arranque |
| tipo_general_negocio | Definición del proyecto | 02 | 05 | string enum | Sí | Producto, servicio o mixto |
| que_entra | Definición del proyecto | 02 | 05 | list[string] | No | Lo que sí forma parte del proyecto |
| que_no_entra | Definición del proyecto | 02 | 05 | list[string] | No | Lo que queda fuera por ahora |
| chequeo_viabilidad_inicial | Definición del proyecto | 02 | 04 | string | No | Lectura temprana de realismo |
| devolucion_fase_02 | Definición del proyecto | 02 | — | string | No | Texto o resumen devuelto al emprendedor |
| validacion_emprendedor_fase_02 | Definición del proyecto | 02 | — | string | Sí | Confirmación, ajuste o corrección |
| direccion_inicial_validada | Definición del proyecto | 02 | 08 | string | Sí | Dirección inicial ya confirmada |

| cliente_inicial | Cliente y valor | 03 | 04, 07, 10 | string | Sí | Primer cliente o usuario razonable |
| necesidad_relevante | Cliente y valor | 03 | 04, 08 | string | Sí | Necesidad, problema o deseo relevante |
| situacion_actual_cliente | Cliente y valor | 03 | 04 | string | No | Cómo vive hoy esa necesidad |
| propuesta_valor_inicial | Cliente y valor | 03 | 04, 08, 10 | string | Sí | Qué valor ofrece inicialmente |
| diferenciacion_inicial | Cliente y valor | 03 | 07, 08 | string | No | Diferencia inicial realista |
| hechos_observados | Cliente y valor | 03 | 04 | list[string] | No | Hechos o señales observadas |
| hipotesis_pendientes | Cliente y valor | 03 | 04, 05, 11 | list[string] | No | Supuestos aún no validados |
| vacios_validacion | Cliente y valor | 03 | 04 | list[string] | No | Lo que falta contrastar |
| encaje_inicial_cliente_necesidad_valor | Cliente y valor | 03 | 04, 08 | string | Sí | Síntesis del encaje inicial |

| validacion_cliente_inicial | Validación inicial | 04 | 08 | string | No | Lectura de validación del cliente |
| validacion_necesidad_inicial | Validación inicial | 04 | 08 | string | No | Lectura de validación de la necesidad |
| validacion_propuesta_inicial | Validación inicial | 04 | 08 | string | No | Lectura de validación de la propuesta |
| senales_a_favor | Validación inicial | 04 | 08 | list[string] | No | Señales positivas |
| senales_en_contra | Validación inicial | 04 | 08 | list[string] | No | Señales negativas |
| senales_dudosas | Validación inicial | 04 | 08 | list[string] | No | Señales ambiguas |
| mapa_senales | Validación inicial | 04 | 08 | object | Sí | Estructura agrupada de señales |
| diagnostico_madurez_validacion | Validación inicial | 04 | 08, 12 | string | Sí | Lectura de madurez tras contraste |
| hipotesis_vivas_post_validacion | Validación inicial | 04 | 05, 08 | list[string] | No | Hipótesis que siguen abiertas |
| recomendacion_continuidad_ajuste | Validación inicial | 04 | 08 | string | Sí | Seguir, ajustar o frenar |

| que_vende_realmente | Modelo de negocio | 05 | 08, 11 | string | Sí | Qué compra o contrata el cliente |
| captura_valor_inicial | Modelo de negocio | 05 | 11 | string | Sí | Cómo captura valor el negocio |
| logica_ingreso | Modelo de negocio | 05 | 11 | string | Sí | Cómo entra el dinero |
| logica_entrega_valor | Modelo de negocio | 05 | 11 | string | Sí | Cómo se cumple la promesa |
| canal_basico_inicial | Modelo de negocio | 05 | 10 | string | Sí | Canal principal inicial |
| relacion_basica_cliente | Modelo de negocio | 05 | 10 | string | Sí | Relación básica con cliente |
| actividades_clave_iniciales | Modelo de negocio | 05 | 11 | list[string] | Sí | Actividades mínimas clave |
| recursos_clave_iniciales | Modelo de negocio | 05 | 11 | list[string] | Sí | Recursos mínimos clave |
| dependencias_relevantes | Modelo de negocio | 05 | 11 | list[string] | No | Dependencias críticas |
| supuestos_criticos_modelo | Modelo de negocio | 05 | 08, 11 | list[string] | No | Supuestos no cerrados |
| alerta_realismo_economico_basico | Modelo de negocio | 05 | 11 | string | No | Señal de fragilidad inicial |

| mercado_general | Mercado y entorno | 06 | 08, 12 | string | Sí | Mercado o sector general |
| entorno_relevante | Mercado y entorno | 06 | 08 | string | Sí | Descripción del entorno |
| factores_externos_relevantes | Mercado y entorno | 06 | 08 | list[string] | No | Económicos, sociales, regulatorios, etc. |
| tendencias_detectadas | Mercado y entorno | 06 | 08 | list[string] | No | Tendencias relevantes |
| oportunidades_externas | Mercado y entorno | 06 | 08 | list[string] | No | Oportunidades del contexto |
| barreras_externas | Mercado y entorno | 06 | 08 | list[string] | No | Barreras o condiciones externas |
| riesgos_externos | Mercado y entorno | 06 | 08 | list[string] | No | Riesgos del entorno |
| lectura_oportunidad | Mercado y entorno | 06 | 08 | string | No | Lectura general de oportunidad |
| atractivo_externo_preliminar | Mercado y entorno | 06 | 08 | string enum | No | Favorable, desafiante, incierto, mixto |
| vacios_contexto | Mercado y entorno | 06 | 08 | list[string] | No | Lo que falta entender del contexto |

| competidores_directos | Competencia | 07 | 08 | list[string] | Sí | Competidores más directos |
| competidores_indirectos | Competencia | 07 | 08 | list[string] | No | Competidores indirectos |
| alternativas_reales_cliente | Competencia | 07 | 08 | list[string] | Sí | Alternativas sustitutas |
| comparacion_competitiva | Competencia | 07 | 08 | object | No | Comparación resumida |
| fortalezas_entorno_competitivo | Competencia | 07 | 08 | list[string] | No | Lo que otros hacen bien |
| debilidades_entorno_competitivo | Competencia | 07 | 08 | list[string] | No | Lo que hacen mal o dejan descubierto |
| huecos_detectados | Competencia | 07 | 08 | list[string] | No | Huecos competitivos |
| diferenciacion_competitiva_inicial | Competencia | 07 | 08, 10 | string | Sí | Diferenciación inicial |
| postura_competitiva_inicial | Competencia | 07 | 08, 10 | string | Sí | Lugar desde donde entra |
| riesgos_competitivos_principales | Competencia | 07 | 08 | list[string] | No | Amenazas competitivas visibles |

| sintesis_estrategica | Síntesis y rumbo | 08 | 12 | string | Sí | Lectura integrada del proyecto |
| fortalezas_principales | Síntesis y rumbo | 08 | 12 | list[string] | Sí | Principales fortalezas |
| debilidades_principales | Síntesis y rumbo | 08 | 12 | list[string] | Sí | Principales debilidades |
| oportunidades_relevantes | Síntesis y rumbo | 08 | 12 | list[string] | Sí | Principales oportunidades |
| riesgos_amenazas_relevantes | Síntesis y rumbo | 08 | 12 | list[string] | Sí | Principales riesgos |
| tensiones_estrategicas | Síntesis y rumbo | 08 | 12 | list[string] | No | Contradicciones relevantes |
| prioridades_enfoque | Síntesis y rumbo | 08 | 12 | list[string] | Sí | Qué priorizar |
| ajustes_recomendados | Síntesis y rumbo | 08 | 10, 11, 12 | list[string] | No | Ajustes sugeridos |
| decision_rumbo_inicial | Síntesis y rumbo | 08 | 12 | string | Sí | Continuar, ajustar, simplificar, etc. |
| recomendacion_estrategica_sintetizada | Síntesis y rumbo | 08 | 12 | string | Sí | Recomendación breve y clara |

| base_legal_inicial | Legal y formal | 09 | 12 | string | Sí | Base formal inicial |
| forma_juridica_preliminar | Legal y formal | 09 | 12 | string | No | Forma más razonable en este punto |
| estructura_individual_o_socios | Legal y formal | 09 | 12 | string | Sí | Solo o acompañado |
| responsabilidades_basicas | Legal y formal | 09 | 12 | list[string] | No | Responsabilidades identificadas |
| pactos_minimos_requeridos | Legal y formal | 09 | 12 | list[string] | No | Pactos o acuerdos necesarios |
| obligaciones_formales_minimas | Legal y formal | 09 | 12 | list[string] | No | Obligaciones legales mínimas |
| alerta_revision_marca | Legal y formal | 09 | 10 | string | No | Revisión futura de naming/marca |
| vacios_legales_pendientes | Legal y formal | 09 | 12 | list[string] | No | Temas legales pendientes de revisión |

| identidad_marca_inicial | Marca y comercial | 10 | 12 | string | No | Identidad de marca inicial |
| arquetipo_marca | Marca y comercial | 10 | 12 | string | No | Arquetipo principal |
| personalidad_marca | Marca y comercial | 10 | 12 | string | No | Rasgos principales |
| mensaje_central | Marca y comercial | 10 | 12 | string | No | Mensaje principal |
| narrativa_comercial | Marca y comercial | 10 | 12 | string | No | Cómo se cuenta el negocio |
| tono_comunicacion | Marca y comercial | 10 | 12 | string | No | Tono principal |
| canales_comunicacion | Marca y comercial | 10 | 12 | list[string] | No | Canales elegidos |
| logica_marketing_inicial | Marca y comercial | 10 | 12 | string | No | Cómo se atraerá interés |
| logica_ventas_inicial | Marca y comercial | 10 | 12 | string | No | Cómo se convierte en venta |
| papel_redes_sociales | Marca y comercial | 10 | 12 | string | No | Función real de redes |
| alertas_comerciales | Marca y comercial | 10 | 12 | list[string] | No | Límites o fragilidades comerciales |

| plan_economico_financiero_base | Finanzas | 11 | 12 | object/file_ref | No | Documento base del emprendedor |
| supuestos_ventas | Finanzas | 11 | 12 | list[string] | No | Supuestos de ventas |
| precios_validados | Finanzas | 11 | 12 | object | No | Precios revisados |
| estructura_costes | Finanzas | 11 | 12 | object | No | Costes fijos y variables |
| lectura_margen | Finanzas | 11 | 12 | string | No | Lectura de margen |
| alertas_tesoreria | Finanzas | 11 | 12 | list[string] | No | Alertas de caja |
| alertas_fiscales_basicas | Finanzas | 11 | 12 | list[string] | No | Fiscalidad básica pendiente |
| necesidades_financiacion | Finanzas | 11 | 12 | list[string] | No | Necesidades de financiación |
| riesgos_financieros_principales | Finanzas | 11 | 12 | list[string] | No | Riesgos financieros |
| lectura_viabilidad_economica_inicial | Finanzas | 11 | 12 | string | No | Lectura de viabilidad |

| resumen_ejecutivo_final | Cierre | 12 | — | string | No | Resumen ejecutivo del proyecto |
| plan_empresa_final | Cierre | 12 | — | object/file_ref | No | Documento final integrado |
| lectura_sostenibilidad_final | Cierre | 12 | — | string | No | Lectura final de sostenibilidad |
| diagnostico_madurez_final | Cierre | 12 | — | string | No | Estado final de madurez |
| recomendaciones_finales | Cierre | 12 | — | list[string] | No | Recomendaciones finales |
| siguientes_pasos | Cierre | 12 | — | list[string] | No | Próximos pasos sugeridos |
| cierre_documental_proceso | Cierre | 12 | — | string | No | Cierre formal del proceso |   