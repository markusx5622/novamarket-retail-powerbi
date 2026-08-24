# LEEME de entrega

> Documento de revisión rápida para localizar el dashboard, los datos, la documentación y las evidencias principales del proyecto **NovaMarket Retail**.

## Propósito

Este documento resume los entregables principales del proyecto **NovaMarket Retail** y facilita una revisión rápida de la entrega académica.

## Estado general

- **Estado del dashboard:** versión final.
- **Archivo principal Power BI:** [`powerbi/NovaMarket_Retail_Dashboard.pbix`](powerbi/NovaMarket_Retail_Dashboard.pbix)
- **Repositorio de trabajo:** este repositorio GitHub concentra datos, scripts, documentación y evidencias visuales.

## Acceso rápido

| Elemento | Ruta directa |
|---|---|
| Dashboard Power BI | [`powerbi/NovaMarket_Retail_Dashboard.pbix`](powerbi/NovaMarket_Retail_Dashboard.pbix) |
| Dataset original | [`data/raw/Base_Datos_Proyecto_Final_NovaMarket_Retail.csv`](data/raw/Base_Datos_Proyecto_Final_NovaMarket_Retail.csv) |
| Dataset limpio | [`data/processed/novamarket_retail_limpio.csv`](data/processed/novamarket_retail_limpio.csv) |
| KPIs de control | [`data/processed/resumen_kpis_powerbi.md`](data/processed/resumen_kpis_powerbi.md) |
| Memoria | [`docs/memoria_proyecto.md`](docs/memoria_proyecto.md) |
| Guion de defensa | [`presentation/guion_defensa_final.md`](presentation/guion_defensa_final.md) |
| Capturas del dashboard | [`assets/capturas_dashboard/`](assets/capturas_dashboard/) |

## Entregables principales

### 1. Dashboard Power BI

- Archivo: [`powerbi/NovaMarket_Retail_Dashboard.pbix`](powerbi/NovaMarket_Retail_Dashboard.pbix)
- Estado: versión final entregada.

### 2. Datos

- Dataset original: [`data/raw/Base_Datos_Proyecto_Final_NovaMarket_Retail.csv`](data/raw/Base_Datos_Proyecto_Final_NovaMarket_Retail.csv)
- Dataset limpio: [`data/processed/novamarket_retail_limpio.csv`](data/processed/novamarket_retail_limpio.csv)
- Resumen de KPIs de control: [`data/processed/resumen_kpis_powerbi.md`](data/processed/resumen_kpis_powerbi.md)

### 3. Scripts reproducibles

- Validación del dataset: [`scripts/01_validacion_dataset.py`](scripts/01_validacion_dataset.py)
- Limpieza del dataset: [`scripts/02_limpieza_dataset.py`](scripts/02_limpieza_dataset.py)
- Exportación de KPIs de control: [`scripts/03_export_resumen_kpis.py`](scripts/03_export_resumen_kpis.py)

Ejecución desde la raíz del repositorio:

```bash
python scripts/01_validacion_dataset.py
python scripts/02_limpieza_dataset.py
python scripts/03_export_resumen_kpis.py
```

### 4. Memoria y documentación

- Memoria del proyecto: [`docs/memoria_proyecto.md`](docs/memoria_proyecto.md)
- Metodología: [`docs/metodologia.md`](docs/metodologia.md)
- Diccionario de datos: [`docs/diccionario_datos.md`](docs/diccionario_datos.md)
- Prompts utilizados: [`docs/prompts_utilizados.md`](docs/prompts_utilizados.md)
- Documentación complementaria de entrega y validación: [`docs/`](docs/)

### 5. Capturas

- Capturas del dashboard: [`assets/capturas_dashboard/`](assets/capturas_dashboard/)
- Capturas de la landing page: [`assets/landing_page/`](assets/landing_page/)

### 6. Presentación y guion

- Presentación inicial: [`presentation/pitch_validacion_inicial/README.md`](presentation/pitch_validacion_inicial/README.md)
- Guion de defensa final: [`presentation/guion_defensa_final.md`](presentation/guion_defensa_final.md)

## Material complementario

- Landing page documentada en [`docs/landing_page.md`](docs/landing_page.md)
- Archivo de requisitos Python: [`requirements.txt`](requirements.txt)

## Nota de revisión

La entrega está organizada para que el profesor pueda localizar de forma rápida el archivo PBIX, los datos de soporte, la memoria, las capturas y el guion de defensa. La documentación complementaria proporciona trazabilidad de requisitos, validación de comportamiento y guías de uso para una evaluación completa y ordenada.
