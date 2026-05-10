# NovaMarket Retail – Power BI Dashboard

Proyecto final del **Equipo 9** para la asignatura **Proyecto: Análisis de Datos** del **Grado en Ingeniería**. El repositorio documenta y organiza el desarrollo de un dashboard ejecutivo en **Microsoft Power BI** para el caso empresarial ficticio **NovaMarket Retail**, con enfoque académico, trazabilidad técnica y orientación a entrega final.

El proyecto aborda un escenario de análisis de datos aplicado a una empresa omnicanal especializada en **Tecnología** y **Estilo de Vida**, con actividad en **España, México, Argentina, Chile y Colombia** durante **2025**. A partir de un dataset transaccional, se construye una solución analítica que integra validación, limpieza, modelado semántico, medidas DAX y visualización ejecutiva.

El problema de negocio planteado consiste en ayudar al comité directivo a determinar si el crecimiento de 2025 ha sido **equilibrado, eficiente y sostenible**, identificando diferencias por país, canal, categoría, producto, satisfacción del cliente y comportamiento logístico, con el fin de apoyar decisiones de mejora para 2026.

- **Herramienta principal:** Power BI
- **Lenguaje de soporte:** Python
- **Estado:** Dashboard v0.9 disponible para revisión del profesor

## Índice

- [Contexto académico](#contexto-académico)
- [Contexto empresarial](#contexto-empresarial)
- [Problema de negocio](#problema-de-negocio)
- [Objetivos del dashboard](#objetivos-del-dashboard)
- [Dataset](#dataset)
- [Estructura del repositorio](#estructura-del-repositorio)
- [Herramientas utilizadas](#herramientas-utilizadas)
- [Scripts Python](#scripts-python)
- [Dashboard Power BI](#dashboard-power-bi)
- [Medidas DAX](#medidas-dax)
- [Metodología](#metodología)
- [Cómo reproducir el proyecto](#cómo-reproducir-el-proyecto)
- [Entregables](#entregables)
- [Limitaciones](#limitaciones)
- [Uso de IA](#uso-de-ia)
- [Autores](#autores)
- [Nota de uso académico](#nota-de-uso-académico)

## Contexto académico

Este repositorio corresponde al proyecto final de la asignatura **Proyecto: Análisis de Datos** del **Grado en Ingeniería**, desarrollado por el **Equipo 9** como entrega académica formal. Su finalidad es demostrar competencias en análisis de datos, preparación reproducible de información, modelado analítico y comunicación ejecutiva mediante herramientas profesionales.

La documentación del repositorio está organizada para respaldar una evaluación universitaria completa: memoria, metodología, diccionario de datos, prompts utilizados, checklist de entrega, guion de defensa y artefactos técnicos asociados al dashboard.

## Contexto empresarial

**NovaMarket Retail** es una empresa ficticia omnicanal especializada en productos de **Tecnología** y **Estilo de Vida**. El caso reproduce una operación comercial con presencia en cinco mercados hispanohablantes:

- España
- México
- Argentina
- Chile
- Colombia

La compañía comercializa sus productos a través de **tres canales de venta** y el análisis se centra en el ejercicio completo de **2025**, con una perspectiva de seguimiento ejecutivo del desempeño comercial y operativo.

## Problema de negocio

El comité directivo de NovaMarket Retail necesita determinar si el crecimiento observado en 2025 ha sido **equilibrado, eficiente y sostenible**. No basta con conocer el volumen de ingresos: también es necesario comprender si dicho crecimiento se distribuye de forma saludable entre países, canales y categorías, y si está acompañado por niveles razonables de satisfacción del cliente y presión logística.

En este contexto, el dashboard se plantea como una herramienta ejecutiva para sintetizar la situación del negocio y facilitar la identificación de áreas de mejora con impacto estratégico en 2026.

## Objetivos del dashboard

- Analizar ingresos, pedidos, clientes y unidades.
- Comparar el desempeño entre países y canales.
- Estudiar el comportamiento de productos y categorías.
- Evaluar satisfacción del cliente y logística.
- Detectar oportunidades de mejora para 2026.

## Dataset

El proyecto utiliza un dataset en formato **CSV** con registros transaccionales del año 2025. El conjunto de datos original se conserva en `data/raw/` y la versión limpia para análisis se genera y almacena en `data/processed/`.

| Variable | Valor |
|---|---|
| Periodo | 2025 |
| Pedidos | 1.500 |
| Clientes únicos | 389 |
| Países | 5 |
| Canales | 3 |
| Categorías | 2 |
| Formato | CSV |

La definición de campos y criterios de interpretación se documenta en `docs/diccionario_datos.md`.

## Estructura del repositorio

```text
novamarket-retail-powerbi/
├── README.md
├── .gitignore
├── data/
│   ├── raw/
│   └── processed/
├── powerbi/
│   ├── NovaMarket_Retail_Dashboard_v0.9_revision_profesor.pbix
│   ├── dax/
│   │   └── medidas_dax.md
│   └── theme/
│       └── novamarket_theme.json
├── scripts/
│   ├── 01_validacion_dataset.py
│   ├── 02_limpieza_dataset.py
│   └── 03_export_resumen_kpis.py
├── docs/
│   ├── memoria_proyecto.md
│   ├── diccionario_datos.md
│   ├── metodologia.md
│   ├── prompts_utilizados.md
│   └── checklist_entrega.md
├── presentation/
│   └── guion_defensa_final.md
└── assets/
    └── capturas_dashboard/
```

**Estado del archivo PBIX:** la versión candidata `powerbi/NovaMarket_Retail_Dashboard_v0.9_revision_profesor.pbix` está disponible en el repositorio para revisión del profesor y sujeta a posibles correcciones académicas posteriores.

## Herramientas utilizadas

| Herramienta | Uso en el proyecto |
|---|---|
| Microsoft Power BI Desktop | Modelado semántico, medidas DAX y visualización ejecutiva |
| Python | Validación, limpieza y exportación de KPIs |
| GitHub | Control de versiones y entrega académica |
| Markdown | Documentación técnica y académica |

## Scripts Python

La carpeta `scripts/` contiene utilidades reproducibles para preparar y verificar los datos antes de su consumo en Power BI:

- `01_validacion_dataset.py`: valida estructura, valores nulos, duplicados, dominios esperados y KPIs base de control.
- `02_limpieza_dataset.py`: genera `data/processed/novamarket_retail_limpio.csv`.
- `03_export_resumen_kpis.py`: genera `data/processed/resumen_kpis_powerbi.md`.

Ejecución desde la raíz del repositorio:

```bash
python scripts/01_validacion_dataset.py
python scripts/02_limpieza_dataset.py
python scripts/03_export_resumen_kpis.py
```

## Dashboard Power BI

El dashboard ejecutivo se estructura en cuatro páginas principales, alineadas con la narrativa analítica del proyecto:

| Página | Objetivo principal |
|---|---|
| Resumen Ejecutivo | Presentar una visión global del desempeño mediante KPIs de ingresos, pedidos, clientes, unidades y lectura general del negocio |
| Productos y Categorías | Analizar la contribución de categorías y productos para identificar concentraciones, líderes y oportunidades comerciales |
| Países y Canales | Comparar el rendimiento por mercado y canal para evaluar equilibrio geográfico y madurez omnicanal |
| Satisfacción y Logística | Evaluar la experiencia del cliente y la presión logística a través de satisfacción, costes de envío e indicadores operativos |

La versión candidata del dashboard está disponible en `powerbi/NovaMarket_Retail_Dashboard_v0.9_revision_profesor.pbix` y se encuentra pendiente de revisión académica por parte del profesor Ortega.

## Medidas DAX

Las medidas oficiales del modelo se documentan en `powerbi/dax/medidas_dax.md`. Este archivo centraliza la definición de KPIs y facilita la trazabilidad entre el dataset limpio, los cálculos del modelo y la validación final en Power BI.

Ejemplos de indicadores incluidos:

- Ingresos Brutos
- Pedidos
- Clientes Únicos
- Ticket Medio
- Satisfacción Media
- Coste Envío Relativo

## Metodología

El flujo metodológico del proyecto se resume en las siguientes etapas:

1. Validación del dataset original.
2. Limpieza y estandarización de datos.
3. Modelado semántico en Power BI.
4. Creación de medidas DAX.
5. Diseño del dashboard ejecutivo.
6. Validación final contra KPIs de control.

La metodología ampliada se encuentra en `docs/metodologia.md`.

## Cómo reproducir el proyecto

1. Clonar el repositorio.
2. Instalar dependencias Python.
3. Ejecutar los scripts de validación, limpieza y exportación.
4. Abrir Power BI Desktop.
5. Cargar `data/processed/novamarket_retail_limpio.csv`.
6. Crear o aplicar las medidas DAX documentadas.
7. Validar los KPIs con `data/processed/resumen_kpis_powerbi.md`.

Comandos de referencia:

```bash
git clone https://github.com/markusx5622/novamarket-retail-powerbi.git
cd novamarket-retail-powerbi
pip install pandas
python scripts/01_validacion_dataset.py
python scripts/02_limpieza_dataset.py
python scripts/03_export_resumen_kpis.py
```

## Entregables

- Dataset original (`data/raw/`).
- Dataset limpio (`data/processed/novamarket_retail_limpio.csv`).
- Scripts Python de validación, limpieza y exportación.
- Dashboard PBIX versión candidata disponible en `powerbi/NovaMarket_Retail_Dashboard_v0.9_revision_profesor.pbix`.
- Tema visual (`powerbi/theme/novamarket_theme.json`).
- Medidas DAX (`powerbi/dax/medidas_dax.md`).
- Memoria (`docs/memoria_proyecto.md`).
- Diccionario de datos (`docs/diccionario_datos.md`).
- Guion de defensa (`presentation/guion_defensa_final.md`).
- Capturas de las 4 hojas disponibles en `assets/capturas_dashboard/`.

## Presentación de validación inicial

`presentation/pitch_validacion_inicial/Presentacion_de_avances_NOVAMARKET_Retail.pdf`

## Limitaciones

- El dataset es sintético y responde a un caso académico ficticio.
- No se dispone de coste real de producto, por lo que ciertos análisis de rentabilidad son necesariamente parciales.
- El margen neto aproximado no representa beneficio contable real, sino un indicador operativo basado en ingresos y coste de envío.
- Los indicadores de satisfacción no implican causalidad directa sobre ventas, fidelización o eficiencia logística.
- El análisis está centrado exclusivamente en 2025 y no incorpora comparativa histórica multianual.

## Uso de IA

El proyecto ha utilizado herramientas de **IA generativa y asistencia tipo Copilot** como apoyo en tareas de **generación**, **validación**, **documentación** y **planificación**, siempre bajo criterio humano, revisión del equipo y responsabilidad académica directa de sus integrantes.

La trazabilidad de este apoyo se documenta en `docs/prompts_utilizados.md`, donde se recoge el alcance del uso de IA, sus límites y los criterios de verificación aplicados para evitar invención de datos o conclusiones no contrastadas.

## Autores

Equipo 9: Camila, Jen, Pablo y Marc  
Asignatura: Proyecto: Análisis de Datos  
Grado: Grado en Ingeniería

## Nota de uso académico

Este repositorio tiene fines **exclusivamente académicos** y **no comerciales**. Su contenido se presenta como parte de una entrega universitaria y no debe interpretarse como un producto empresarial real ni como documentación de una compañía existente.
