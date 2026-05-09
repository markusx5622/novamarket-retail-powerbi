#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
01_validacion_dataset.py
Proyecto: NovaMarket Retail – Power BI Dashboard

Objetivo:
Validar de forma reproducible el dataset original antes de construir el dashboard.
El script comprueba estructura, tipos, valores nulos, duplicados, dominios esperados,
rangos numéricos y KPIs base de control.

Uso recomendado desde la raíz del repositorio:
    python scripts/01_validacion_dataset.py

Entradas esperadas:
    data/raw/Base_Datos_Proyecto_Final_NovaMarket_Retail.csv

Salidas generadas:
    data/processed/resumen_validacion_dataset.txt

Nota académica:
Este script no modifica el dataset original. Solo valida y documenta su estado.
"""

from pathlib import Path
import sys
import pandas as pd

RAW_PATH = Path("data/raw/Base_Datos_Proyecto_Final_NovaMarket_Retail.csv")
OUTPUT_DIR = Path("data/processed")
REPORT_PATH = OUTPUT_DIR / "resumen_validacion_dataset.txt"

EXPECTED_COLUMNS = [
    "ID_Pedido",
    "Fecha",
    "ID_Cliente",
    "Pais",
    "Categoria",
    "Producto",
    "Precio_Unitario",
    "Cantidad",
    "Costo_Envio",
    "Canal_Venta",
    "Puntuacion_Satisfaccion",
]

EXPECTED_COUNTRIES = {"España", "México", "Argentina", "Chile", "Colombia"}
EXPECTED_CATEGORIES = {"Tecnología", "Estilo de Vida"}
EXPECTED_CHANNELS = {"Web", "App", "Tienda Física"}
EXPECTED_SATISFACTION_VALUES = {1, 2, 3, 4, 5}
EXPECTED_PRODUCTS = {
    "Auriculares Noise-Cancelling",
    "Botella Térmica Inteligente",
    "Laptop Pro 15",
    "Lámpara LED Escritorio",
    "Mochila Ergonómica",
    "Monitor 4K Curved",
    "Set de Teclado Mecánico",
    "Silla Gaming X",
    "Smartphone Alpha",
    "Smartwatch Series Z",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def format_currency(value: float) -> str:
    return f"{value:,.2f} €".replace(",", "X").replace(".", ",").replace("X", ".")


def validate_file_exists() -> None:
    if not RAW_PATH.exists():
        fail(
            "No se encuentra el CSV original. "
            f"Ruta esperada: {RAW_PATH.as_posix()}"
        )


def load_dataset() -> pd.DataFrame:
    try:
        return pd.read_csv(RAW_PATH, encoding="utf-8")
    except UnicodeDecodeError:
        return pd.read_csv(RAW_PATH, encoding="latin-1")
    except Exception as exc:
        fail(f"No se pudo leer el CSV: {exc}")


def validate_structure(df: pd.DataFrame, report: list[str]) -> None:
    report.append("## 1. Validación de estructura")
    report.append(f"Columnas detectadas: {list(df.columns)}")

    missing = [col for col in EXPECTED_COLUMNS if col not in df.columns]
    extra = [col for col in df.columns if col not in EXPECTED_COLUMNS]

    if missing:
        fail(f"Faltan columnas obligatorias: {missing}")
    if extra:
        report.append(f"Advertencia: columnas adicionales detectadas: {extra}")
    else:
        report.append("Estructura de columnas correcta.")

    if list(df.columns) != EXPECTED_COLUMNS:
        report.append(
            "Advertencia: las columnas existen, pero el orden no coincide exactamente "
            "con el diccionario de datos."
        )


def validate_types_and_ranges(df: pd.DataFrame, report: list[str]) -> pd.DataFrame:
    report.append("\n## 2. Validación de tipos y rangos")

    df = df.copy()
    df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce")
    numeric_columns = ["Precio_Unitario", "Cantidad", "Costo_Envio", "Puntuacion_Satisfaccion"]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    if df["Fecha"].isna().any():
        fail("Hay fechas no válidas en la columna Fecha.")

    for column in numeric_columns:
        if df[column].isna().any():
            fail(f"Hay valores no numéricos o nulos en la columna {column}.")

    if df["Fecha"].min().year != 2025 or df["Fecha"].max().year != 2025:
        report.append(
            "Advertencia: el dataset contiene fechas fuera de 2025 o el rango no cubre solo 2025."
        )
    else:
        report.append("Rango temporal correcto: todas las fechas pertenecen a 2025.")

    if (df["Precio_Unitario"] <= 0).any():
        fail("Existen precios unitarios menores o iguales a cero.")

    if (df["Cantidad"] <= 0).any():
        fail("Existen cantidades menores o iguales a cero.")

    if (df["Costo_Envio"] < 0).any():
        fail("Existen costes de envío negativos.")

    invalid_satisfaction = set(df["Puntuacion_Satisfaccion"].dropna().astype(int)) - EXPECTED_SATISFACTION_VALUES
    if invalid_satisfaction:
        fail(f"Existen puntuaciones de satisfacción fuera del rango 1–5: {invalid_satisfaction}")

    report.append("Tipos numéricos, fechas y rangos principales validados correctamente.")
    return df


def validate_nulls_duplicates_domains(df: pd.DataFrame, report: list[str]) -> None:
    report.append("\n## 3. Nulos, duplicados y dominios")

    nulls = df.isna().sum()
    total_nulls = int(nulls.sum())
    report.append(f"Valores nulos totales: {total_nulls}")
    if total_nulls > 0:
        report.append(nulls[nulls > 0].to_string())
        fail("El dataset contiene valores nulos. Revisar antes de continuar.")

    duplicated_rows = int(df.duplicated().sum())
    duplicated_orders = int(df["ID_Pedido"].duplicated().sum())
    report.append(f"Filas duplicadas: {duplicated_rows}")
    report.append(f"ID_Pedido duplicados: {duplicated_orders}")

    if duplicated_rows > 0:
        fail("Existen filas duplicadas completas.")
    if duplicated_orders > 0:
        fail("Existen IDs de pedido duplicados.")

    domain_checks = {
        "Pais": EXPECTED_COUNTRIES,
        "Categoria": EXPECTED_CATEGORIES,
        "Canal_Venta": EXPECTED_CHANNELS,
        "Producto": EXPECTED_PRODUCTS,
    }

    for column, expected_values in domain_checks.items():
        detected_values = set(df[column].dropna().unique())
        unexpected = detected_values - expected_values
        missing_expected = expected_values - detected_values
        report.append(f"{column} detectados: {sorted(detected_values)}")
        if unexpected:
            fail(f"Valores no esperados en {column}: {sorted(unexpected)}")
        if missing_expected:
            report.append(f"Advertencia: valores esperados no presentes en {column}: {sorted(missing_expected)}")


def calculate_control_kpis(df: pd.DataFrame, report: list[str]) -> None:
    report.append("\n## 4. KPIs de control")

    ingresos = (df["Precio_Unitario"] * df["Cantidad"]).sum()
    pedidos = df["ID_Pedido"].nunique()
    clientes = df["ID_Cliente"].nunique()
    unidades = df["Cantidad"].sum()
    coste_envio = df["Costo_Envio"].sum()
    satisfaccion_media = df["Puntuacion_Satisfaccion"].mean()
    ticket_medio = ingresos / pedidos if pedidos else 0
    ratio_envio = coste_envio / ingresos if ingresos else 0

    report.append(f"Pedidos: {pedidos:,}".replace(",", "."))
    report.append(f"Clientes únicos: {clientes:,}".replace(",", "."))
    report.append(f"Unidades vendidas: {int(unidades):,}".replace(",", "."))
    report.append(f"Ingresos brutos: {format_currency(ingresos)}")
    report.append(f"Coste total de envío: {format_currency(coste_envio)}")
    report.append(f"Ticket medio: {format_currency(ticket_medio)}")
    report.append(f"Ratio logístico sobre ingresos: {ratio_envio:.2%}".replace(".", ","))
    report.append(f"Satisfacción media: {satisfaccion_media:.2f} / 5".replace(".", ","))


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    validate_file_exists()
    df = load_dataset()

    report = [
        "# Resumen de validación del dataset – NovaMarket Retail",
        "",
        "Este informe ha sido generado automáticamente por scripts/01_validacion_dataset.py.",
        "",
    ]

    validate_structure(df, report)
    df = validate_types_and_ranges(df, report)
    validate_nulls_duplicates_domains(df, report)
    calculate_control_kpis(df, report)

    report.append("\n## 5. Resultado final")
    report.append("Validación completada correctamente. El dataset es apto para Power BI.")

    REPORT_PATH.write_text("\n".join(report), encoding="utf-8")
    print(f"Validación completada correctamente. Informe generado en: {REPORT_PATH}")


if __name__ == "__main__":
    main()
