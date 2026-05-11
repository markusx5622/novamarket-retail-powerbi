# Decisiones de diseño del dashboard

## Finalidad del documento

Este documento explica las decisiones de diseño adoptadas en el dashboard de **NovaMarket Retail** para justificar su coherencia analítica, visual y académica.

## Por qué el dashboard tiene 4 páginas

La estructura en cuatro páginas responde a un criterio de claridad narrativa y de separación temática:

1. **Resumen Ejecutivo** concentra la lectura global del negocio y permite una primera interpretación rápida.
2. **Productos y Categorías** profundiza en la composición comercial del negocio.
3. **Países y Canales** analiza el equilibrio geográfico y omnicanal.
4. **Satisfacción y Logística** incorpora la dimensión operativa y de experiencia del cliente.

Esta organización evita la sobrecarga visual en una sola hoja y facilita que cada página responda a una pregunta de negocio concreta, manteniendo una progresión lógica desde la visión general hasta el análisis detallado.

## Por qué se usan KPIs

Los KPIs se utilizan porque sintetizan las magnitudes principales del proyecto en indicadores de lectura inmediata. En un contexto académico y ejecutivo, permiten:

- identificar rápidamente el volumen de actividad;
- comparar resultados entre páginas y filtros;
- verificar coherencia con el resumen de control exportado desde los scripts;
- apoyar una narrativa orientada a decisiones.

El uso de KPIs también refuerza la trazabilidad entre dataset limpio, medidas DAX y dashboard final.

## Por qué se usan filtros globales

Los filtros globales favorecen una lectura consistente del informe completo. Su utilidad principal es que permiten analizar el mismo fenómeno desde varias perspectivas sin perder coherencia entre páginas.

Desde un punto de vista metodológico, los filtros globales:

- reducen la fragmentación del análisis;
- permiten comparar subconjuntos del negocio con una lógica única;
- mejoran la experiencia de revisión del profesor al mantener una navegación uniforme;
- ayudan a comprobar la robustez de los KPIs cuando cambia el contexto de análisis.

## Por qué se utiliza un fondo gris claro

El fondo gris claro se emplea para aportar contraste sin introducir ruido visual excesivo. Esta decisión mejora la legibilidad de tarjetas, tablas y gráficos, y evita la dureza visual de un fondo completamente blanco cuando se combinan varios elementos analíticos en una misma página.

Además, un fondo neutro favorece que la atención se concentre en los datos y en la jerarquía de la información, que es la prioridad del proyecto.

## Por qué se utiliza una paleta corporativa

La paleta corporativa aporta consistencia visual y refuerza la identidad del caso NovaMarket Retail. En una entrega académica, esta decisión transmite mayor madurez en la construcción del dashboard y mejora la percepción de unidad entre páginas, capturas y materiales de apoyo.

También ayuda a:

- distinguir visuales sin recurrir a colores arbitrarios;
- mantener continuidad entre el archivo PBIX, las capturas y la documentación;
- facilitar una presentación más profesional del proyecto.

## Por qué se utilizan tablas finales

Las tablas finales permiten complementar los gráficos con un nivel de detalle verificable. Son especialmente útiles para revisión académica porque muestran valores concretos y facilitan el contraste entre visualización y dato subyacente.

Su inclusión aporta:

- soporte de comprobación numérica;
- mayor transparencia en la lectura de resultados;
- capacidad de cerrar cada página con una evidencia más precisa.

## Por qué se utilizan visuales nativos de Power BI

El uso de visuales nativos de Power BI responde a criterios de estabilidad, compatibilidad y simplicidad de revisión. Al tratarse de una entrega académica, resulta preferible priorizar componentes estándar que:

- funcionen sin dependencias externas adicionales;
- sean fáciles de interpretar por cualquier revisor con Power BI Desktop;
- reduzcan riesgos técnicos de compatibilidad;
- mantengan el foco en el análisis y no en efectos visuales accesorios.

## Conclusión

Las decisiones de diseño del dashboard buscan equilibrar rigor analítico, claridad visual y facilidad de evaluación académica. La estructura elegida no persigue solo una presentación estética, sino una organización del contenido que refuerza la comprensión, la validación y la defensa del proyecto.
