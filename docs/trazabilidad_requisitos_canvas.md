# Trazabilidad de requisitos de Canvas

## Objetivo

Este documento relaciona los elementos solicitados en Canvas con los artefactos efectivamente almacenados en el repositorio de **NovaMarket Retail**. Su finalidad es facilitar la revisión académica y reforzar la trazabilidad entre requisitos de entrega y evidencias documentales.

## Matriz de correspondencia

| Requisito indicado en Canvas | Evidencia en el repositorio | Observación académica |
|---|---|---|
| ZIP con memoria | `docs/memoria_proyecto.md` y el contenido versionado del repositorio | El repositorio concentra la documentación y materiales necesarios para su empaquetado final en formato ZIP. |
| Datos limpios | `data/processed/novamarket_retail_limpio.csv` | Dataset limpio y preparado para su uso analítico en Power BI. |
| Prompts | `docs/prompts_utilizados.md` | Documento de trazabilidad del apoyo de IA y criterios de uso responsable. |
| Scripts de limpieza | `scripts/01_validacion_dataset.py`, `scripts/02_limpieza_dataset.py`, `scripts/03_export_resumen_kpis.py` | Flujo reproducible de validación, limpieza y exportación de KPIs de control. |
| Link/dashboard o PBIX | `powerbi/NovaMarket_Retail_Dashboard_v0.9_revision_profesor.pbix` y `docs/landing_page.md` | El archivo PBIX es el entregable analítico principal; la landing page actúa como apoyo complementario de comunicación. |
| Repositorio GitHub | `README.md` y estructura completa del repositorio | Repositorio usado como fuente de verdad para datos, scripts, documentación y evidencias. |
| Capturas | `assets/capturas_dashboard/` y `assets/landing_page/` | Evidencias visuales del dashboard y del material complementario web. |
| Presentación inicial | `presentation/pitch_validacion_inicial/Presentacion_de_avances_NOVAMARKET_Retail.pdf` | Presentación de avance conservada como antecedente del proyecto. |
| Landing page | `docs/landing_page.md` y capturas en `assets/landing_page/` | Material complementario de comunicación pública del proyecto. |

## Observaciones de control

- La memoria académica, los datos procesados, los scripts y el archivo PBIX permanecen separados para mejorar claridad, mantenimiento y revisión.
- La trazabilidad entre datos, scripts y dashboard se refuerza además con `data/processed/resumen_kpis_powerbi.md`, que actúa como referencia de validación.
- La documentación almacenada en `docs/` permite justificar tanto el proceso técnico como el uso responsable de apoyo con IA.

## Conclusión

La entrega dispone de correspondencia explícita entre los requisitos de Canvas y los artefactos versionados en GitHub. Esto permite una revisión más ordenada, verificable y alineada con el carácter académico del proyecto.
