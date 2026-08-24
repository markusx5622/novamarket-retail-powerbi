#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
02_limpieza_dataset.py
Proyecto: NovaMarket Retail – Power BI Dashboard

Objetivo:
Generar una versión limpia y normalizada del dataset para Power BI.
La limpieza es conservadora: no elimina registros válidos ni altera el significado de los datos.

Uso recomendado desde la raíz del repositorio:
    python scripts/02_limpieza_dataset.py

Entrada:
    data/raw/Base_Datos_Proyecto_Final_NovaMarket_Retail.csv

Salida:
    data/processed/novamarket_retail_limpio.csv

Nota académica:
El dataset original es sintético y ya presenta alta calidad. Este script garantiza reproducibilidad,
estandarización de tipos y columnas derivadas útiles para Power BI.
"""

from pathlib import Path
import sys
import pandas as pd

RAW_PATH = Path("data/raw/Base_Datos_Proyecto_Final_NovaMarket_Retail.csv")
OUTPUT_DIR = Path("data/processed")
CLEAN_PATH = OUTPUT_DIR / "novamarket_retail_limpio.csv"

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


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def load_dataset() -> pd.DataFrame:
    if not RAW_PATH.exists():
        fail(f"No se encuentra el archivo de entrada: {RAW_PATH.as_posix()}")

    try:
        return pd.read_csv(RAW_PATH, encoding="utf-8")
    except UnicodeDecodeError:
        return pd.read_csv(RAW_PATH, encoding="latin-1")
    except Exception as exc:
        fail(f"No se pudo leer el CSV: {exc}")


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Normalización de nombres de columnas y orden esperado.
    df.columns = [column.strip() for column in df.columns]
    missing = [column for column in EXPECTED_COLUMNS if column not in df.columns]
    if missing:
        fail(f"Faltan columnas obligatorias: {missing}")
    df = df[EXPECTED_COLUMNS]

    # Limpieza básica de texto.
    text_columns = ["ID_Pedido", "ID_Cliente", "Pais", "Categoria", "Producto", "Canal_Venta"]
    for column in text_columns:
        df[column] = df[column].astype(str).str.strip()

    # Conversión de tipos.
    df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce")
    df["Precio_Unitario"] = pd.to_numeric(df["Precio_Unitario"], errors="coerce").round(2)
    df["Cantidad"] = pd.to_numeric(df["Cantidad"], errors="coerce").astype("Int64")
    df["Costo_Envio"] = pd.to_numeric(df["Costo_Envio"], errors="coerce").round(2)
    df["Puntuacion_Satisfaccion"] = pd.to_numeric(
        df["Puntuacion_Satisfaccion"], errors="coerce"
    ).astype("Int64")

    if df.isna().sum().sum() > 0:
        fail(
            "La limpieza detectó valores nulos tras la conversión de tipos. "
            "Ejecuta primero 01_validacion_dataset.py y revisa el CSV original."
        )

    # Columnas derivadas simples y trazables.
    df["Ingresos_Brutos"] = (df["Precio_Unitario"] * df["Cantidad"]).round(2)
    df["Ingreso_Neto_Logistico"] = (df["Ingresos_Brutos"] - df["Costo_Envio"]).round(2)
    df["Coste_Envio_Relativo"] = (df["Costo_Envio"] / df["Ingresos_Brutos"]).round(6)
    df["Anio"] = df["Fecha"].dt.year
    df["Mes_Numero"] = df["Fecha"].dt.month
    df["Mes"] = df["Fecha"].dt.strftime("%Y-%m")
    df["Trimestre"] = "T" + df["Fecha"].dt.quarter.astype(str)

    df["Nivel_Satisfaccion"] = pd.cut(
        df["Puntuacion_Satisfaccion"].astype(int),
        bins=[0, 2, 3, 5],
        labels=["Baja", "Media", "Alta"],
        include_lowest=True,
    ).astype(str)

    df["Indicador_Satisfaccion_Alta"] = (
        df["Puntuacion_Satisfaccion"].astype(int) >= 4
    ).astype(int)

    # Orden estable para facilitar comparaciones en Git y Power BI.
    df = df.sort_values("ID_Pedido").reset_index(drop=True)

    # Formato ISO para evitar ambigüedades regionales en Power BI.
    df["Fecha"] = df["Fecha"].dt.strftime("%Y-%m-%d")

    return df


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    raw_df = load_dataset()
    clean_df = clean_dataset(raw_df)
    clean_df.to_csv(CLEAN_PATH, index=False, encoding="utf-8")
    print(f"Dataset limpio generado correctamente en: {CLEAN_PATH}")
    print(f"Filas exportadas: {len(clean_df)}")
    print(f"Columnas exportadas: {len(clean_df.columns)}")


if __name__ == "__main__":
    main()
