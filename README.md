# NovaMarket Retail – Power BI Dashboard

> Proyecto final de la asignatura **Proyecto: Análisis de Datos** | Grado en Ingeniería | Equipo 9

---

## Contexto académico
Este repositorio corresponde al proyecto final del Equipo 9 en la asignatura **Proyecto: Análisis de Datos** del Grado en Ingeniería. El trabajo se desarrolla en el marco de un caso empresarial ficticio y tiene como propósito aplicar técnicas de análisis de datos, modelado semántico y visualización ejecutiva mediante Microsoft Power BI.

El repositorio está diseñado para cumplir con los criterios de una entrega universitaria formal: organización, trazabilidad, documentación completa y reproducibilidad.

---

## Contexto empresarial
**NovaMarket Retail** es una empresa omnicanal ficticia especializada en dos grandes categorías de producto:
- **Tecnología** (dispositivos, accesorios, electrónica)
- **Estilo de Vida** (hogar, bienestar, moda y ocio)

Opera en cinco mercados de habla hispana:

| País | Presencia |
|---|---|
| España | ✓ |
| México | ✓ |
| Argentina | ✓ |
| Chile | ✓ |
| Colombia | ✓ |

La empresa comercializa a través de **tres canales de venta** y el análisis se centra en el periodo completo del año **2025**.

---

## Objetivo del dashboard
Desarrollar un **dashboard ejecutivo en Microsoft Power BI** que permita a los responsables de NovaMarket Retail:
- Supervisar el rendimiento comercial global.
- Comparar desempeño por producto, categoría, país y canal.
- Medir la satisfacción del cliente y los costes logísticos.
- Identificar oportunidades de optimización y toma de decisiones informadas.

---

## Herramientas utilizadas
| Herramienta | Uso |
|---|---|
| Microsoft Power BI Desktop | Modelado semántico, medidas DAX y visualización |
| Python | Validación, limpieza y exportación de KPIs |
| Git / GitHub | Control de versiones y entrega académica |

---

## Estructura del repositorio
```text
novamarket-retail-powerbi/
├── README.md                          ← Este archivo
├── .gitignore
├── data/
│   ├── raw/                           ← Dataset original (CSV sin modificar)
│   │   └── README.md
│   └── processed/                     ← Dataset limpio y validado
│       └── README.md
├── powerbi/
│   ├── README.md                      ← Instrucciones para el archivo PBIX
│   ├── dax/
│   │   └── medidas_dax.md             ← Plantilla de medidas KPI
│   └── theme/
│       └── novamarket_theme.json      ← Tema visual corporativo
├── scripts/
│   └── README.md                      ← Plan de scripts Python
├── docs/
│   ├── memoria_proyecto.md
│   ├── diccionario_datos.md
│   ├── metodologia.md
│   ├── prompts_utilizados.md
│   └── checklist_entrega.md
├── presentation/
│   └── guion_defensa_final.md
└── assets/
    ├── README.md
    └── capturas_dashboard/
        └── README.md
```

---

## Páginas del dashboard
El dashboard está organizado en **cuatro páginas analíticas**:

| # | Página | Contenido principal |
|---|---|---|
| 1 | **Resumen Ejecutivo** | KPIs globales: ingresos, pedidos, clientes únicos, ticket medio |
| 2 | **Productos y Categorías** | Comparativa Tecnología vs. Estilo de Vida, top productos |
| 3 | **Países y Canales** | Desempeño geográfico y por canal de venta |
| 4 | **Satisfacción y Logística** | Satisfacción del cliente, coste de envío y eficiencia operativa |

---

## Dataset
El dataset de NovaMarket Retail recoge transacciones del año 2025 con la siguiente información general del caso académico:

| Indicador | Valor |
|---|---|
| Número de pedidos | 1.500 |
| Clientes únicos | 389 |
| Países | 5 |
| Canales de venta | 3 |
| Categorías | 2 |
| Periodo | 2025 |

Los campos del dataset se documentan en [`docs/diccionario_datos.md`](docs/diccionario_datos.md).

---

## Metodología resumida
1. **Validación** del dataset original (integridad, tipos, nulos, duplicados).
2. **Limpieza** y normalización de campos para consumo analítico.
3. **Modelado semántico** en Power BI con relaciones y tabla de fechas.
4. **Definición de medidas DAX** para cálculo de KPIs ejecutivos.
5. **Diseño visual** orientado a lectura ejecutiva y consistencia gráfica.

La metodología completa se encuentra en [`docs/metodologia.md`](docs/metodologia.md).

---

## Limitaciones
- Este es un caso académico ficticio; los datos no representan ninguna empresa real.
- El archivo `NovaMarket_Retail_Dashboard.pbix` se incorporará al repositorio al finalizar el desarrollo.
- Los scripts de `scripts/` están planificados y se añadirán con lógica real en fases posteriores.
- El análisis está restringido al año 2025.

---

## Autores
**Equipo 9** – Asignatura *Proyecto: Análisis de Datos*  
Grado en Ingeniería

---

## Nota de uso académico
Este repositorio se publica con fines exclusivamente académicos. Todo el contenido es original del Equipo 9, excepto donde se indica explícitamente el uso de herramientas de IA como apoyo (documentado en [`docs/prompts_utilizados.md`](docs/prompts_utilizados.md)). Queda prohibida su reproducción total o parcial con fines comerciales.
