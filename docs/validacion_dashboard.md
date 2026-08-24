# Validación del dashboard

## Propósito

Este documento recoge los criterios de validación del dashboard Power BI frente al archivo de control `data/processed/resumen_kpis_powerbi.md`. El objetivo es asegurar que las tarjetas KPI, los filtros y las visualizaciones mantienen coherencia con los valores de control exportados desde el dataset limpio.

## Fuente de referencia

La validación se apoya en el documento:

- `data/processed/resumen_kpis_powerbi.md`

Este archivo resume los valores de control exportados desde el dataset limpio y constituye la referencia principal para verificar el comportamiento del dashboard final.

## KPIs generales que deben coincidir

Las tarjetas y cálculos globales del dashboard deben reproducir los siguientes valores de control:

| Indicador | Valor de referencia |
|---|---|
| Pedidos | 1.500 |
| Clientes únicos | 389 |
| Unidades vendidas | 2.440 |
| Ingresos brutos | 1.154.961,21 € |
| Coste total de envío | 43.483,07 € |
| Margen neto aproximado | 1.111.478,14 € |
| Ticket medio | 769,97 € |
| Coste envío relativo | 3,76% |
| Satisfacción media | 3,91 / 5 |
| % satisfacción alta | 69,33% |

## Validación por dimensión analítica

### 1. País

La página **Países y Canales** debe ser consistente con los ingresos por país reflejados en el resumen de control:

| País | Valor de referencia |
|---|---|
| España | 447.272,26 € (38,73%) |
| México | 240.072,58 € (20,79%) |
| Argentina | 170.683,80 € (14,78%) |
| Colombia | 164.527,69 € (14,25%) |
| Chile | 132.404,88 € (11,46%) |

### 2. Canal

La página **Países y Canales** debe ser consistente con los ingresos por canal:

| Canal | Valor de referencia |
|---|---|
| Web | 607.231,51 € (52,58%) |
| App | 316.265,09 € (27,38%) |
| Tienda Física | 231.464,61 € (20,04%) |

### 3. Categoría

La página **Productos y Categorías** debe respetar la distribución de ingresos por categoría:

| Categoría | Valor de referencia |
|---|---|
| Tecnología | 993.136,25 € (85,99%) |
| Estilo de Vida | 161.824,96 € (14,01%) |

### 4. Satisfacción y logística

La página **Satisfacción y Logística** debe mantener coherencia con los indicadores generales ya documentados:

- Satisfacción media: `3,91 / 5`
- % satisfacción alta: `69,33%`
- Coste total de envío: `43.483,07 €`
- Coste envío relativo: `3,76%`

## Validación de filtros

Los filtros globales del dashboard deben comprobarse con los siguientes criterios:

1. **Consistencia global:** un filtro aplicado en una página debe conservar la misma lógica de cálculo en todas las visualizaciones afectadas.
2. **Trazabilidad numérica:** al filtrar por país, canal o categoría, los importes mostrados deben ser coherentes con la distribución del resumen de control y con el dataset limpio.
3. **No duplicidad de conteos:** el número de pedidos y clientes no debe inflarse al interactuar con segmentadores o visuales cruzados.
4. **Lectura ejecutiva estable:** los KPIs principales deben responder a la selección activa sin romper la narrativa de cada página.

## Validación por página

| Página del dashboard | Alcance de validación | Referencia principal |
|---|---|---|
| Resumen Ejecutivo | Comprobación de KPIs globales y coherencia general del negocio | Sección "KPIs generales" del resumen de control |
| Productos y Categorías | Verificación de reparto por categoría y lectura de productos destacados | Sección "Ingresos por categoría" |
| Países y Canales | Contraste de ingresos por país y por canal | Secciones "Ingresos por país" e "Ingresos por canal" |
| Satisfacción y Logística | Revisión de satisfacción, costes de envío y métricas operativas asociadas | KPIs generales del resumen de control |

## Criterio de aceptación

Se considera que el dashboard queda validado cuando:

- las tarjetas principales coinciden con los valores del documento de control;
- las visualizaciones por país, canal y categoría conservan la misma jerarquía y magnitud relativa;
- los filtros no generan incoherencias entre páginas;
- la lectura ejecutiva de las cuatro hojas se mantiene alineada con el dataset limpio.

## Alcance de esta validación

Esta validación documenta la correspondencia entre el dashboard y el resumen de control disponible en el repositorio. No sustituye la revisión visual final del archivo PBIX en Power BI Desktop, pero proporciona criterios objetivos de verificación para una evaluación académica rigurosa.
