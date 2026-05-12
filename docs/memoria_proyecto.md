# Memoria Académica del Proyecto: NovaMarket Retail – Power BI Dashboard

**Asignatura:** Proyecto: Análisis de Datos  
**Grado:** Grado en Ingeniería  
**Equipo:** Equipo 9  
**Periodo académico:** 2025-2026  

---

## 1. Resumen Ejecutivo

El presente proyecto tiene como propósito la construcción de un dashboard ejecutivo en Microsoft Power BI para la empresa ficticia NovaMarket Retail, una cadena omnicanal especializada en productos de Tecnología y Estilo de Vida con operaciones en cinco países hispanohablantes durante el año 2025.

El problema central que aborda el proyecto es la necesidad de la dirección de NovaMarket Retail de disponer de una visión integrada y accesible de su rendimiento comercial, operativo y de experiencia de cliente. Sin una herramienta de visualización estructurada, el comité directivo carece de los medios necesarios para evaluar si el crecimiento de la empresa es equilibrado entre países y canales, si la operación logística es eficiente y si la satisfacción del cliente es homogénea en todos los contextos de venta.

La entrega principal del proyecto es un dashboard interactivo de cuatro páginas diseñado para lectura ejecutiva, acompañado de un repositorio documentado con el dataset sintético, los scripts de preparación de datos, las medidas DAX, el tema visual corporativo y la documentación académica completa. El conjunto de entregables permite no solo la evaluación académica sino también la reproducibilidad y la trazabilidad del proceso analítico seguido por el Equipo 9.

---

## 2. Contexto Académico

Este proyecto es el trabajo final de la asignatura **Proyecto: Análisis de Datos**, perteneciente al **Grado en Ingeniería**. La asignatura tiene por objetivo aplicar de forma integrada las competencias adquiridas a lo largo del grado en el campo del análisis de datos y la visualización empresarial. El Equipo 9 ha sido el responsable de la definición del caso de negocio, la preparación del dataset, el diseño del modelo semántico, la construcción del dashboard y la redacción de la documentación académica que se presenta en este documento.

El proyecto ha pasado por distintas fases formales: una validación inicial con presentación ante el profesorado, una fase de desarrollo iterativo y una defensa final. La memoria que aquí se presenta constituye el documento académico principal que acompaña a los entregables técnicos y visuales del proyecto.

El enfoque adoptado es **descriptivo-exploratorio**: no se pretende construir modelos predictivos ni aplicar técnicas de aprendizaje automático, sino transformar datos transaccionales en indicadores significativos que permitan apoyar la toma de decisiones directivas con claridad y rigor analítico.

---

## 3. Contexto Empresarial

**NovaMarket Retail** es una empresa ficticia creada para el desarrollo de este caso académico. Se trata de una cadena omnicanal especializada en dos grandes categorías de producto: **Tecnología** (dispositivos, accesorios y electrónica de consumo) y **Estilo de Vida** (artículos de bienestar, hogar y ocio).

La empresa tiene presencia en cinco mercados hispanohablantes: **España, México, Argentina, Chile y Colombia**, lo que le otorga una dimensión internacional con particularidades en cada mercado en cuanto a volumen de ventas, comportamiento del cliente y coste logístico.

La distribución comercial de NovaMarket Retail se realiza a través de tres canales de venta diferenciados:

- **Canal Web:** tienda en línea de acceso directo desde navegador.
- **Canal App:** aplicación móvil propia para clientes registrados.
- **Canal Tienda Física:** red de establecimientos presenciales en cada país.

Este modelo omnicanal permite a la empresa llegar a distintos perfiles de cliente y adaptarse a las preferencias de compra de cada mercado, pero también introduce complejidad operativa y logística que el dashboard debe ayudar a gestionar.

Es importante destacar que NovaMarket Retail es una empresa completamente ficticia, concebida para que el caso académico tuviese una narrativa coherente y un contexto empresarial realista. Todos los datos manejados en el proyecto son sintéticos y no corresponden a ninguna entidad real.

---

## 4. Problema de Negocio

Durante el año 2025, NovaMarket Retail ha experimentado un periodo de crecimiento sostenido en términos de pedidos e ingresos. Sin embargo, el comité directivo enfrenta una serie de preguntas estratégicas que no pueden responderse con los sistemas transaccionales operativos, ya que estos no ofrecen una visión integrada ni orientada a la toma de decisiones:

- ¿El crecimiento es **equilibrado** entre los diferentes países y canales, o está concentrado en pocos mercados?
- ¿La operación logística es **eficiente**? ¿El coste de envío está bajo control en relación con los ingresos generados?
- ¿El modelo de negocio es **rentable en sentido operativo**, considerando la estructura de ingresos y costes visibles?
- ¿El crecimiento es **sostenible**? ¿La satisfacción del cliente se mantiene en niveles adecuados o existen señales de deterioro que puedan afectar a la fidelización futura?

La ausencia de una herramienta de visualización ejecutiva impide que el comité directivo tenga respuestas rápidas, coherentes y comparables a estas preguntas. El proyecto NovaMarket Retail – Power BI Dashboard da respuesta a esta necesidad mediante la construcción de un cuadro de mando que integra indicadores comerciales, operativos y de experiencia de cliente en un formato accesible y navegable.

---

## 5. Objetivos del Proyecto

### 5.1 Objetivo General

Construir un dashboard ejecutivo en Microsoft Power BI que permita al comité directivo de NovaMarket Retail analizar de forma integrada el rendimiento comercial, operativo y de satisfacción del cliente durante el año 2025, facilitando la toma de decisiones estratégicas y la identificación de oportunidades para el ejercicio 2026.

### 5.2 Objetivos Específicos

1. **Analizar el rendimiento comercial global** de la operación, midiendo ingresos brutos, número de pedidos, clientes únicos, unidades vendidas y ticket medio de manera agregada y con capacidad de desagregación temporal.

2. **Estudiar el comportamiento de productos y categorías**, diferenciando el peso de Tecnología frente a Estilo de Vida, identificando los productos de mayor contribución a los ingresos y evaluando la distribución de unidades y precio unitario.

3. **Comparar el desempeño por país y canal de venta**, evaluando qué mercados y qué canales concentran mayor volumen de negocio, y detectando desequilibrios o dependencias que puedan suponer un riesgo estratégico.

4. **Evaluar la satisfacción del cliente y la eficiencia logística**, monitorizando la puntuación media de satisfacción, la proporción de valoraciones altas y bajas, el coste medio y relativo de envío, y detectando combinaciones de país, canal o producto con mayor presión operativa.

5. **Detectar oportunidades de mejora y crecimiento para 2026**, a partir de los patrones observados en los datos de 2025, formulando recomendaciones analíticamente fundamentadas y estratégicamente coherentes.

---

## 6. Público Objetivo del Dashboard

El dashboard ha sido diseñado para dar respuesta a las necesidades analíticas de diferentes perfiles directivos dentro de NovaMarket Retail. Cada página del cuadro de mando se orienta a uno o varios de estos perfiles:

**Dirección General**

Necesita una visión global del estado del negocio: ingresos totales, evolución mensual, número de pedidos y ticket medio. La página de Resumen Ejecutivo está diseñada específicamente para este perfil.

**Dirección Comercial**

Requiere información sobre qué productos y categorías lideran los ingresos, cuál es la distribución de ventas por línea de producto y cómo se comportan los rankings de producto en términos de contribución. La página de Productos y Categorías es la más relevante para este perfil.

**Expansión Regional**

Necesita entender el peso relativo de cada país, los desequilibrios de crecimiento entre mercados y el comportamiento diferencial por canal en cada región. La página de Países y Canales responde a estas necesidades.

**Operaciones y Logística**

Requiere monitorizar el coste de envío total, el coste medio por pedido y el coste envío relativo sobre los ingresos, identificando qué combinaciones de país, canal o producto generan mayor presión logística. La página de Satisfacción y Logística aborda específicamente estos indicadores.

**Customer Experience**

Necesita valorar la satisfacción media del cliente, la proporción de valoraciones altas y bajas y la relación entre experiencia percibida y variables operativas como el canal o el producto. Esta dimensión también se cubre en la página de Satisfacción y Logística.

---

## 7. Relación con los Objetivos de Desarrollo Sostenible (ODS)

El proyecto NovaMarket Retail – Power BI Dashboard guarda relación directa con dos Objetivos de Desarrollo Sostenible de la Agenda 2030 de Naciones Unidas:

**ODS 8: Trabajo decente y crecimiento económico**

El dashboard permite a la dirección evaluar si el crecimiento de la empresa es equilibrado y sostenible. Al monitorizar la eficiencia logística, la concentración de ingresos por mercado y la satisfacción del cliente, la herramienta facilita la toma de decisiones que pueden conducir a un crecimiento económico más inclusivo y distribuido entre los cinco países donde opera NovaMarket Retail, contribuyendo también a la mejora de las condiciones operativas de los trabajadores de la empresa.

**ODS 12: Producción y consumo responsables**

El seguimiento del coste de envío relativo y la eficiencia operativa logística guarda relación con la producción responsable, en tanto que una logística más eficiente implica un menor desperdicio de recursos. Asimismo, la monitorización de la satisfacción del cliente invita a reflexionar sobre la calidad y la pertinencia de los productos ofrecidos, alineándose con los principios de consumo responsable.

Es importante señalar que esta relación con los ODS se plantea desde la perspectiva del análisis de negocio en el marco del caso académico. No se trata de un compromiso corporativo formal, sino de una reflexión sobre la dimensión social y ambiental del tipo de decisiones que el dashboard puede informar.

---

## 8. Justificación del Dataset Sintético

El dataset utilizado en este proyecto ha sido generado de forma sintética con apoyo de inteligencia artificial. Esta decisión metodológica se justifica por las siguientes razones:

**Coherencia narrativa:** Un dataset sintético permite diseñar los datos de forma que sean internamente consistentes con el caso de negocio definido: mismos países, mismos canales, mismas categorías, rangos de precios plausibles y una distribución temporal que simula un año completo de actividad. No existe riesgo de contradicción entre el contexto del caso y los datos observados.

**Control de la narrativa analítica:** Al generar el dataset, el equipo puede asegurarse de que los datos contienen patrones analíticamente interesantes (diferencias entre países, variación por canal, distribución de satisfacción) sin que estos estén dominados por ruido o anomalías difíciles de interpretar en un contexto académico.

**Adecuación al objetivo pedagógico:** El objetivo del proyecto no es aplicar técnicas avanzadas de aprendizaje automático sobre datos reales, sino construir un dashboard ejecutivo de calidad que demuestre competencias en preparación de datos, modelado semántico, diseño visual y comunicación analítica. Para este objetivo, un dataset sintético bien construido es tan válido como uno real.

**Ausencia de restricciones de privacidad y propiedad intelectual:** El uso de datos reales de empresa requeriría acuerdos de confidencialidad, anonimización y posiblemente autorizaciones que están fuera del alcance de un proyecto académico. El dataset sintético elimina estas barreras.

**Limitaciones reconocidas:** Es obligatorio señalar que el dataset sintético tiene limitaciones inherentes. Los patrones observados no reflejan la complejidad y la variabilidad de datos empresariales reales. Las correlaciones pueden ser artificialmente regulares. La distribución de valores puede no capturar fenómenos reales como estacionalidad extrema, fraude, devoluciones o campañas promocionales. Cualquier conclusión extraída de este dataset debe interpretarse exclusivamente en el marco del caso académico y nunca generalizarse como reflejo del comportamiento real de ninguna empresa.

---

## 9. Descripción del Dataset

El dataset del proyecto cubre el **ejercicio completo 2025** y constituye el conjunto de datos transaccionales de NovaMarket Retail sobre el que se construye todo el análisis. A continuación se describen sus principales características:

**Dimensión del dataset:**
- 1.500 pedidos registrados
- 389 clientes únicos identificados
- 2.440 unidades vendidas en total

**Cobertura geográfica:**
- 5 países: España, México, Argentina, Chile y Colombia

**Canales de venta:**
- 3 canales: Web, App y Tienda Física

**Categorías de producto:**
- 2 categorías: Tecnología y Estilo de Vida

**Columnas principales del dataset:**

- `ID_Pedido`: identificador único de cada transacción (tipo texto).
- `Fecha`: fecha de registro de la transacción (tipo fecha, formato AAAA-MM-DD).
- `ID_Cliente`: identificador único del cliente (tipo texto).
- `Pais`: país de la operación (tipo texto, valores: España, México, Argentina, Chile, Colombia).
- `Categoria`: categoría del producto (tipo texto, valores: Tecnología, Estilo de Vida).
- `Producto`: nombre del producto comercializado (tipo texto).
- `Precio_Unitario`: precio unitario del producto en euros (tipo decimal).
- `Cantidad`: número de unidades vendidas en la transacción (tipo entero).
- `Costo_Envio`: coste logístico asociado al pedido en euros (tipo decimal).
- `Canal_Venta`: canal de venta utilizado (tipo texto, valores: Web, App, Tienda Física).
- `Puntuacion_Satisfaccion`: valoración de satisfacción del cliente (escala 1 a 5).

El dataset se encuentra en dos versiones dentro del repositorio:

- `data/raw/`: versión original sin modificaciones, tal como fue generada y entregada.
- `data/processed/novamarket_retail_limpio.csv`: versión procesada y limpia, lista para su importación directa en Power BI.

---

## 10. Preparación y Limpieza de Datos

El flujo de preparación de datos es reproducible y está implementado mediante tres scripts Python ubicados en la carpeta `scripts/`. Cada script tiene una responsabilidad única y bien delimitada, siguiendo el principio de separación de responsabilidades.

### 10.1 `01_validacion_dataset.py`

Este script realiza una primera inspección del dataset original almacenado en `data/raw/`. Su función es detectar problemas de calidad de datos antes de proceder a ninguna transformación. Concretamente, verifica:

- La estructura general del archivo (número de filas, número de columnas, nombres de columnas).
- La presencia de valores nulos o vacíos en cualquier campo.
- La existencia de registros duplicados que puedan distorsionar los cálculos agregados.
- La coherencia de los tipos de datos (por ejemplo, que `Fecha` sea interpretable como fecha y que `Precio_Unitario` sea numérico).
- La consistencia de los dominios esperados: que los valores de `Pais`, `Canal_Venta` y `Categoria` se limiten a los valores válidos definidos para el caso.

La salida de este script es un informe en consola que permite al equipo confirmar que el dataset original cumple los requisitos mínimos de calidad o, en su defecto, identificar los problemas a resolver en el paso siguiente.

### 10.2 `02_limpieza_dataset.py`

Este script toma como entrada el dataset original de `data/raw/` y aplica las transformaciones necesarias para producir el dataset limpio en `data/processed/novamarket_retail_limpio.csv`. Las operaciones de limpieza incluyen:

- Estandarización de nombres de columnas (eliminación de espacios, normalización de mayúsculas).
- Normalización de valores de texto en campos categóricos (eliminación de espacios extra, unificación de variantes ortográficas).
- Conversión y verificación de tipos de datos para garantizar que las columnas numéricas y de fecha sean interpretadas correctamente.
- Generación de columnas derivadas necesarias para el análisis (por ejemplo, año y mes a partir de la fecha).
- Detección de errores críticos de integridad: si se identifican anomalías que comprometan la coherencia del dataset, el script detiene el proceso e informa al equipo, sin eliminar registros salvo que sea estrictamente necesario. La limpieza es conservadora y orientada a preservar la integridad del dato original.
- Validación final de que el dataset resultante cumple con los dominios esperados y la integridad referencial mínima.

El dataset limpio generado es el único fichero que se importa en Power BI, garantizando que el modelo semántico trabaja siempre sobre datos de calidad verificada.

### 10.3 `03_export_resumen_kpis.py`

Este script toma el dataset limpio y calcula los KPIs de control que sirven como referencia para validar que las medidas DAX implementadas en Power BI producen resultados coherentes. El script genera el archivo `data/processed/resumen_kpis_powerbi.md`, que contiene los valores esperados para:

- Total de pedidos, clientes únicos y unidades vendidas.
- Ingresos brutos totales y por país, canal y categoría.
- Coste total de envío y coste envío relativo.
- Ticket medio.
- Satisfacción media y porcentaje de satisfacción alta.

Este resumen actúa como tabla de verdad para la fase de validación del dashboard, permitiendo detectar errores de modelado o de implementación DAX antes de la presentación final.

---

## 11. Validación del Dataset

La validación del dataset es una fase metodológica esencial que precede a cualquier análisis. En este proyecto, la validación se aborda en dos niveles complementarios:

**Validación estructural:** se comprueba que el dataset tiene el número esperado de filas y columnas, que los nombres de campo son los definidos en el diccionario de datos y que no existen columnas adicionales no previstas.

**Validación de nulos y duplicados:** se verifica que no existen valores nulos en campos obligatorios como `ID_Pedido`, `Fecha`, `ID_Cliente` o `Precio_Unitario`, y que no existen filas duplicadas que puedan inflar artificialmente los totales.

**Validación de tipos de datos:** se comprueba que `Fecha` es interpretable como tipo fecha, que `Precio_Unitario`, `Cantidad` y `Costo_Envio` son numéricos positivos, y que `Puntuacion_Satisfaccion` toma valores enteros en el rango 1 a 5.

**Validación de dominios esperados:** se verifica que los valores de `Pais` se limitan a los cinco países del caso, que `Canal_Venta` solo contiene los tres canales definidos, y que `Categoria` solo presenta los valores Tecnología y Estilo de Vida.

**Validación de fechas:** se comprueba que todas las fechas pertenecen al año 2025 y que no existen fechas futuras o claramente erróneas.

**Validación de KPIs de control:** una vez obtenido el dataset limpio, se calculan los KPIs de referencia mediante Python y se comparan con los valores esperados. Esta validación cruzada garantiza que el proceso de limpieza no ha alterado accidentalmente los datos y que las medidas DAX del dashboard producirán resultados coherentes.

---

## 12. Modelo Semántico en Power BI

El modelo semántico del dashboard se construye sobre una única tabla principal denominada `Ventas`, que corresponde directamente al dataset limpio `novamarket_retail_limpio.csv`. En el contexto del caso académico, no se han definido tablas de dimensiones adicionales, ya que toda la información necesaria está contenida en la tabla de hechos y el volumen de datos no requiere un modelo estrella complejo.

**Tabla principal `Ventas`:** contiene las 1.500 filas del dataset limpio con todas las columnas definidas en el diccionario de datos. Es la fuente única de todos los indicadores calculados mediante medidas DAX.

**Configuración de tipos de datos:** al importar el dataset en Power BI Desktop, se verifica que cada columna tenga asignado el tipo de dato correcto. En particular, `Fecha` debe configurarse como tipo Fecha, `Precio_Unitario` y `Costo_Envio` como tipo Decimal, y `Cantidad` y `Puntuacion_Satisfaccion` como tipo Número entero. Esta configuración es imprescindible para que las medidas temporales y los cálculos agregados funcionen correctamente.

**Medidas DAX:** todas las métricas del dashboard se implementan como medidas explícitas en Power BI, siguiendo el principio de no utilizar columnas calculadas donde una medida es suficiente. Las medidas se organizan en una tabla auxiliar denominada **Medidas**, lo que facilita su localización, mantenimiento y comprensión dentro del modelo.

**Tema visual corporativo:** el dashboard aplica el tema visual definido en `powerbi/theme/novamarket_theme.json`, que establece la paleta de colores corporativos de NovaMarket Retail, los estilos tipográficos, los colores de fondo de las páginas y los formatos de los elementos visuales. El uso de un tema centralizado garantiza la coherencia visual entre las cuatro páginas y evita la configuración manual elemento a elemento.

**Uso de DAX:** el lenguaje DAX (Data Analysis Expressions) se utiliza para definir todas las medidas del modelo. Se priorizan funciones básicas de agregación (`SUM`, `AVERAGE`, `DISTINCTCOUNT`), funciones de ratio (`DIVIDE`), funciones de filtrado contextual (`CALCULATE`, `ALL`) y funciones de ranking (`RANKX`). Las medidas temporales se implementan con `DATEADD` sobre la columna `Fecha`.

---

## 13. Medidas DAX Principales

A continuación se describen brevemente las medidas DAX más relevantes del modelo semántico, explicando su lógica de cálculo y su interpretación analítica.

**Ingresos Brutos**

Se calcula como la suma del producto entre `Precio_Unitario` y `Cantidad` para cada fila de la tabla `Ventas`. Representa el valor total de las ventas antes de cualquier deducción. Es la medida central del análisis comercial. Su valor de referencia para 2025 es 1.154.961,21 €.

**Pedidos**

Se calcula como el recuento distinto de `ID_Pedido`. Mide el número de transacciones únicas registradas en el periodo. No debe confundirse con el número de líneas de venta. Su valor de referencia para 2025 es 1.500 pedidos.

**Clientes Únicos**

Se calcula como el recuento distinto de `ID_Cliente`. Mide el número de clientes que han realizado al menos un pedido en el periodo analizado. Su valor de referencia para 2025 es 389 clientes únicos.

**Ticket Medio**

Se calcula dividiendo los Ingresos Brutos entre el número de Pedidos. Representa el valor medio por transacción y es un indicador clave de la capacidad de monetización por pedido. Su valor de referencia para 2025 es 769,97 €.

**Satisfacción Media**

Se calcula como la media aritmética de `Puntuacion_Satisfaccion`. Mide el nivel promedio de satisfacción del cliente en una escala de 1 a 5. Su valor de referencia para 2025 es 3,91 sobre 5. Esta medida se complementa con alertas operativas que señalan si la satisfacción media cae por debajo del umbral de 3,8.

**Coste Envío Relativo**

Se calcula dividiendo el Coste Total de Envío entre los Ingresos Brutos. Expresa qué porcentaje de los ingresos se destina a cubrir los costes logísticos. Su valor de referencia para 2025 es 3,76%. Una alerta operativa se activa cuando este indicador supera el 5%, señalando una presión logística elevada.

**Margen Neto Aproximado**

Se calcula restando el Coste Total de Envío a los Ingresos Brutos. Es importante aclarar explícitamente que **esta medida no representa el beneficio contable real de la empresa**, ya que el dataset no contiene el coste de adquisición o producción de los productos. El Margen Neto Aproximado debe interpretarse exclusivamente como un indicador operativo que mide la presión del coste logístico sobre los ingresos, no como una medida de rentabilidad empresarial en sentido estricto. Su valor de referencia para 2025 es 1.111.478,14 €.

---

## 14. Diseño del Dashboard

El dashboard de NovaMarket Retail ha sido diseñado siguiendo criterios de claridad ejecutiva, comparabilidad analítica y consistencia visual. A continuación se describen los principios de diseño aplicados:

**Estructura de cuatro páginas:** el dashboard se organiza en cuatro hojas temáticas, cada una con un foco analítico diferenciado. Esta estructura facilita la navegación dirigida según el perfil del usuario y evita la sobrecarga de información en una sola página.

**Lectura ejecutiva:** cada página está diseñada para que el mensaje principal sea comprensible en una primera lectura rápida, sin necesidad de explorar todos los elementos. Los KPIs más importantes se presentan en tarjetas de gran visibilidad en la parte superior de cada página.

**Filtros globales:** se definen segmentaciones (slicers) que permiten al usuario filtrar la información por país, canal de venta, categoría y periodo temporal. Estos filtros actúan de forma cruzada sobre todos los visuales de la página, garantizando la coherencia del análisis comparativo.

**Colores corporativos:** el tema visual `novamarket_theme.json` establece una paleta de colores coherente con la identidad ficticia de NovaMarket Retail. Se usa de forma sistemática para diferenciar categorías (Tecnología vs. Estilo de Vida), países y canales, facilitando la lectura de los gráficos comparativos.

**Tarjetas KPI:** los indicadores más críticos (Ingresos Brutos, Pedidos, Clientes Únicos, Ticket Medio, Satisfacción Media, Coste Envío Relativo) se muestran como tarjetas de un único valor en la parte superior de las páginas relevantes, proporcionando una referencia rápida antes de explorar los detalles.

**Visuales nativos de Power BI:** el dashboard utiliza exclusivamente visualizaciones nativas de Power BI (gráficos de barras, gráficos de columnas, gráficos de anillo, gráficos de dispersión, tablas y matrices). No se emplean visuales de terceros, garantizando la compatibilidad y la estabilidad del archivo.

**Tablas finales de detalle:** cada página incluye una tabla o matriz en la parte inferior que permite acceder al detalle de los datos filtrados, complementando la lectura visual con la precisión numérica.

---

## 15. Descripción Página por Página

### 15.1 Página 1: Resumen Ejecutivo

**Objetivo:** proporcionar una visión global del rendimiento comercial de NovaMarket Retail durante 2025, con foco en los indicadores de mayor relevancia para la Dirección General.

**Visuales principales:**
- Tarjetas KPI con Ingresos Brutos, Pedidos, Clientes Únicos, Unidades Vendidas, Coste Total de Envío y Satisfacción Media.
- Gráfico de evolución mensual de los ingresos brutos durante 2025.
- Gráfico de ingresos por país.
- Gráfico de ingresos por canal de venta.
- Gráfico del peso de categoría en el total de ingresos.
- Tabla top productos por ingresos.

**Valor analítico:** esta página permite detectar a primera vista la estacionalidad del negocio, el peso relativo de cada mercado y la distribución omnicanal de los ingresos. El comité directivo puede identificar en segundos si los resultados globales son coherentes con las expectativas estratégicas para 2025.

---

### 15.2 Página 2: Productos y Categorías

**Objetivo:** analizar en profundidad el rendimiento de las dos categorías de producto (Tecnología y Estilo de Vida) y de los productos individuales, permitiendo a la Dirección Comercial tomar decisiones de priorización y gestión de catálogo.

**Visuales principales:**
- Gráfico de barras con los top productos por ingresos.
- Gráfico de dispersión (scatter) de ingresos frente a satisfacción por producto.
- Gráfico de ingresos por categoría.
- Gráfico de top productos por unidades vendidas.
- Tabla de detalle de productos con ingresos, unidades, precio y satisfacción.

**Valor analítico:** esta página evidencia la concentración de los ingresos en la categoría Tecnología (que representa el 85,99% del total en el caso de referencia) y permite identificar qué productos individuales son los principales motores del negocio. También facilita comparar el precio medio y la satisfacción entre categorías.

---

### 15.3 Página 3: Países y Canales

**Objetivo:** comparar el desempeño de los cinco países y los tres canales de venta, ayudando a la Dirección de Expansión Regional a evaluar el equilibrio de la cartera geográfica y omnicanal.

**Visuales principales:**
- Gráfico de ingresos por país.
- Gráfico de ingresos por país y canal de venta.
- Gráfico de pedidos por país.
- Gráfico de satisfacción media por país.
- Matriz cruzada de país × canal con ingresos.

**Valor analítico:** esta página permite identificar la dependencia del negocio respecto a España (que concentra el 38,73% de los ingresos en el caso de referencia) y el peso dominante del canal Web (52,58%). También facilita detectar asimetrías: qué países utilizan más cada canal y qué combinaciones país-canal son más rentables en términos de ticket medio.

---

### 15.4 Página 4: Satisfacción y Logística

**Objetivo:** integrar la dimensión de experiencia de cliente con la eficiencia operativa logística, permitiendo a las áreas de Operaciones y Customer Experience identificar situaciones de riesgo y oportunidades de mejora.

**Visuales principales:**
- Gráfico de satisfacción media por canal de venta.
- Gráfico de coste medio de envío por canal.
- Gráfico de distribución de valoraciones de satisfacción.
- Gráfico de dispersión (scatter) de coste logístico frente a satisfacción por país.
- Tabla de combinaciones producto-canal con menor satisfacción.

**Valor analítico:** esta página traduce la experiencia del cliente en una métrica monitorizable y la cruza con el coste logístico para identificar combinaciones de bajo rendimiento en ambas dimensiones. Las medidas de alerta automática permiten al equipo operativo priorizar las acciones de mejora sin necesidad de leer los datos en detalle.

---

## 16. Principales Insights Esperados

A continuación se describen los hallazgos analíticos que, de forma general y con la prudencia que exige trabajar con un dataset sintético, cabe esperar del análisis de los datos de NovaMarket Retail en 2025. Estos insights deben interpretarse como hipótesis analíticamente fundamentadas, no como conclusiones definitivas sobre el comportamiento real de ninguna empresa:

**Concentración de ingresos en Tecnología:** la categoría Tecnología representa aproximadamente el 86% de los ingresos brutos totales. Esta concentración puede interpretarse como una fortaleza (especialización en productos de alto valor) pero también como una dependencia estratégica que conviene monitorizar. La categoría Estilo de Vida, con un 14% de participación, tiene margen de crecimiento.

**España como mercado principal:** España concentra cerca del 39% de los ingresos totales, siendo el mercado más desarrollado. México (21%) y Argentina (15%) ocupan las siguientes posiciones. Chile y Colombia presentan una participación más reducida, lo que podría indicar oportunidades de desarrollo en estos mercados.

**Dominio del canal Web:** el canal Web genera más de la mitad de los ingresos (52,58%), seguido por el canal App (27,38%) y la Tienda Física (20,04%). Este patrón es coherente con el perfil tecnológico de los productos y sugiere que la estrategia digital es el eje central del modelo omnicanal.

**Satisfacción elevada pero con posibles diferencias:** la satisfacción media global se sitúa en torno a 3,91 sobre 5, un nivel positivo. Sin embargo, es probable que existan diferencias entre canales (la Tienda Física puede tener una dinámica diferente a los canales digitales), entre categorías (los productos tecnológicos pueden tener valoraciones distintas a los de Estilo de Vida) y entre países. Estas diferencias merecen un seguimiento específico.

**Logística bajo control con vigilancia necesaria:** el coste de envío relativo global se sitúa alrededor del 3,76%, por debajo del umbral de alerta del 5%. Sin embargo, el coste medio de envío y el coste relativo pueden variar significativamente entre países (el coste logístico a Colombia o Chile puede ser superior al de España) y entre canales (la Tienda Física puede tener una estructura de costes diferente). Esta variabilidad justifica el seguimiento específico en la página de Satisfacción y Logística.

---

## 17. Limitaciones del Proyecto

El equipo reconoce las siguientes limitaciones del proyecto, que deben tenerse en cuenta al valorar los resultados y las conclusiones:

**Dataset sintético:** todos los datos son artificialmente generados y no corresponden a ninguna empresa real. Los patrones observados pueden ser más regulares y predecibles de lo que serían en un entorno empresarial real. Las conclusiones extraídas no son generalizables fuera del caso académico.

**Ausencia de coste real de producto:** el dataset no contiene el coste de adquisición o producción de los artículos vendidos. Por esta razón, no es posible calcular el margen bruto real ni la rentabilidad por producto. La medida "Margen Neto Aproximado" debe interpretarse exclusivamente como un indicador de presión logística, no como un indicador de beneficio.

**Ausencia de campañas, devoluciones y margen contable:** el dataset no incluye información sobre campañas de marketing, promociones, descuentos aplicados, devoluciones o abonos. Estos factores son relevantes para entender el margen real del negocio y la eficacia de las acciones comerciales. Su ausencia limita la profundidad del análisis económico.

**La satisfacción no implica causalidad:** las correlaciones observadas entre satisfacción y otras variables (canal, producto, país) no permiten inferir relaciones causales. Una satisfacción media diferente entre dos países puede responder a multitud de factores no recogidos en el dataset (perfil del cliente, expectativas culturales, calidad del servicio postventa). El análisis es descriptivo, no causal.

**Análisis centrado en 2025:** el dataset cubre exclusivamente el año 2025. No es posible realizar comparaciones interanuales ni analizar tendencias de largo plazo. Los insights identificados corresponden a un único ejercicio y deben complementarse con datos históricos para obtener una perspectiva estratégica más robusta.

---

## 18. Uso de Inteligencia Artificial y Trazabilidad

El Equipo 9 ha utilizado herramientas de inteligencia artificial generativa como apoyo complementario en diversas fases del proyecto. A continuación se detalla el alcance de este uso y los criterios de responsabilidad académica aplicados:

**Generación y validación del dataset:** la IA ha sido utilizada como asistente para definir la estructura del dataset sintético, revisar la coherencia de los campos y validar la distribución de valores. Las decisiones sobre qué variables incluir, qué rangos de valores utilizar y qué patrones simular han sido tomadas por el equipo con criterio analítico propio.

**Documentación:** la IA ha apoyado la redacción de borradores de documentos como la memoria, la metodología, el diccionario de datos y el checklist de entrega. En todos los casos, el equipo ha revisado, corregido y validado el contenido generado, asumiendo la autoría intelectual del resultado final.

**Validación técnica:** la IA ha sido consultada para revisar la sintaxis de medidas DAX, verificar la lógica de los cálculos y sugerir buenas prácticas de diseño en Power BI. Las decisiones de implementación han correspondido siempre al equipo.

**Planificación del proyecto:** la IA ha contribuido a estructurar el plan de trabajo, identificar fases y proponer una organización del repositorio coherente con los estándares académicos y profesionales.

**Landing page complementaria:** la landing page complementaria del proyecto fue creada con el apoyo de **GitHub Copilot** y desplegada mediante **Vercel**. El contenido generado fue revisado y validado por el equipo antes de su publicación, siguiendo los mismos criterios de uso responsable aplicados al resto de entregables.

**Criterios de uso responsable:** el equipo ha seguido en todo momento los siguientes principios: (1) ningún contenido generado por IA se ha aceptado sin revisión humana; (2) la IA no ha inventado datos, resultados ni conclusiones; (3) el uso de IA está explícitamente documentado en el repositorio (`docs/prompts_utilizados.md`); (4) la autoría intelectual del análisis, las decisiones metodológicas y las conclusiones recae íntegramente en el Equipo 9.

---

## 19. Organización del Repositorio

El repositorio del proyecto sigue una estructura de carpetas clara y documentada, diseñada para garantizar la trazabilidad, la reproducibilidad y la facilidad de evaluación:

**`data/`**

Contiene el dataset del proyecto organizado en dos subcarpetas:
- `data/raw/`: versión original del dataset, sin ninguna modificación.
- `data/processed/`: versión limpia y procesada lista para Power BI, junto con el resumen de KPIs de control.

**`scripts/`**

Contiene los tres scripts Python del flujo de preparación de datos: validación (`01_validacion_dataset.py`), limpieza (`02_limpieza_dataset.py`) y exportación de KPIs (`03_export_resumen_kpis.py`).

**`powerbi/`**

Contiene el archivo `.pbix` del dashboard Power BI, el tema visual corporativo (`powerbi/theme/novamarket_theme.json`) y el documento de medidas DAX (`powerbi/dax/medidas_dax.md`).

**`docs/`**

Contiene toda la documentación académica del proyecto: esta memoria (`memoria_proyecto.md`), el diccionario de datos (`diccionario_datos.md`), la metodología (`metodologia.md`), el registro de prompts de IA (`prompts_utilizados.md`) y el checklist de entrega (`checklist_entrega.md`).

**`presentation/`**

Contiene los materiales de presentación del proyecto: la presentación de validación inicial (`pitch_validacion_inicial/`) y el guion de defensa final (`guion_defensa_final.md`).

**`assets/`**

Contiene los recursos visuales del proyecto, incluyendo las capturas de pantalla de las cuatro páginas del dashboard (`assets/capturas_dashboard/`) que sirven de referencia para la evaluación y la documentación.

---

## 20. Materiales Complementarios

### 20.1 Presentación de Validación Inicial

El repositorio incluye la presentación empleada en la fase de validación inicial del proyecto, ubicada en `presentation/pitch_validacion_inicial/`. Este material recoge el planteamiento del caso de negocio, los objetivos del dashboard y la propuesta metodológica que fue expuesta y validada ante el profesorado al inicio del desarrollo. Forma parte del proceso académico formal y está disponible para su consulta como referencia del punto de partida del proyecto.

### 20.2 Landing Page Complementaria

Como material adicional de comunicación, el Equipo 9 ha publicado una landing page complementaria accesible en la siguiente dirección:

**[https://novamarket-retail.vercel.app/](https://novamarket-retail.vercel.app/)**

Esta página tiene un propósito exclusivamente divulgativo: presenta el proyecto de forma visual y accesible para audiencias no técnicas. Es importante aclarar que la landing page **no sustituye al dashboard, a esta memoria ni al repositorio**, que constituyen los entregables académicos principales. Se trata de un recurso complementario de comunicación, elaborado con el apoyo de **GitHub Copilot** y desplegado mediante **Vercel**, revisado por el equipo, que no forma parte de los criterios de evaluación formales del proyecto.

---

## 21. Conclusiones

El proyecto NovaMarket Retail – Power BI Dashboard demuestra cómo el análisis de datos transaccionales puede transformarse en una herramienta ejecutiva de valor real para la toma de decisiones de negocio. A través de un proceso metodológico estructurado —que incluye la definición del caso, la preparación y validación del dataset, el modelado semántico, el diseño del dashboard y la documentación académica— el Equipo 9 ha construido una solución analítica que integra cuatro dimensiones clave del negocio: rendimiento comercial, gestión de producto, expansión geográfica y experiencia de cliente y logística.

El dashboard entregado no es únicamente un conjunto de gráficos. Es una herramienta de comunicación analítica que estructura la información en función de las necesidades de distintos perfiles directivos, que aplica criterios de diseño ejecutivo para facilitar la lectura y la navegación, y que incorpora medidas de alerta para señalar situaciones que requieren atención operativa inmediata.

Desde el punto de vista académico, el proyecto demuestra la integración de competencias técnicas (Python, DAX, Power BI), competencias analíticas (preparación de datos, definición de KPIs, análisis descriptivo) y competencias de comunicación (diseño de dashboard, documentación y presentación). El repositorio documentado garantiza que el proceso es reproducible y trazable, lo que añade valor tanto para la evaluación académica como para cualquier eventual extensión futura del proyecto.

En resumen, el Equipo 9 entrega un proyecto coherente, bien documentado y analíticamente sólido, que transforma datos transaccionales sintéticos de una empresa ficticia en una herramienta ejecutiva real, demostrando la relevancia práctica del análisis de datos para la gestión empresarial moderna.

---

## 22. Líneas Futuras de Mejora

El proyecto actual, diseñado y desarrollado en el marco temporal y académico definido, deja abiertas varias líneas de mejora que permitirían ampliar su alcance y su utilidad en un contexto profesional o en una futura extensión académica:

**Incorporación del margen real por producto:** la limitación más relevante del análisis actual es la ausencia del coste de producto. Incorporar esta información permitiría calcular el margen bruto real por artículo, categoría, canal y país, transformando el dashboard en una herramienta de control de rentabilidad genuino.

**Inclusión de campañas y datos de marketing:** añadir información sobre campañas promocionales, descuentos y canales de captación permitiría analizar el impacto de las acciones de marketing en el volumen de ventas y en el ticket medio, completando la dimensión comercial del análisis.

**Comparativa interanual:** extender el dataset para incluir datos de años anteriores (por ejemplo, 2023 y 2024) permitiría analizar tendencias de crecimiento, comparar el rendimiento por periodos y detectar cambios estructurales en el negocio.

**Incorporación de modelos predictivos:** una extensión natural del proyecto sería añadir modelos de predicción de ventas (por ejemplo, series temporales con Prophet o ARIMA) que permitan anticipar el comportamiento del negocio en los próximos meses, complementando el análisis descriptivo con una perspectiva prescriptiva.

**Segmentación de clientes:** con la información de los 389 clientes únicos, sería posible aplicar técnicas de clustering (por ejemplo, RFM: Recencia, Frecuencia, Monetización) para segmentar la base de clientes y diseñar estrategias de fidelización diferenciadas.

**Automatización del refresco de datos:** en un entorno profesional, el dashboard se conectaría a fuentes de datos en tiempo real o con actualización periódica automatizada a través de Power BI Service, eliminando la necesidad de actualización manual del archivo `.pbix`. Esta mejora requeriría configurar un gateway de datos y programar refresco en la nube.
