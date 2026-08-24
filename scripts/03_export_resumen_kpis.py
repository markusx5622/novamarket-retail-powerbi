#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
03_export_resumen_kpis.py
Proyecto: NovaMarket Retail – Power BI Dashboard

Objetivo:
Exportar un resumen de KPIs de control para validar que Power BI coincide con el dataset limpio.

Uso recomendado desde la raíz del repositorio:
    python scripts/03_export_resumen_kpis.py

Entrada prioritaria:
    data/processed/novamarket_retail_limpio.csv

Salida:
    data/processed/resumen_kpis_powerbi.md
"""

from pathlib import Path
import sys
import pandas as pd

CLEAN_PATH = Path("data/processed/novamarket_retail_limpio.csv")
OUTPUT_PATH = Path("data/processed/resumen_kpis_powerbi.md")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    sys.exit(1)


def format_currency(value: float) -> str:
    return f"{value:,.2f} €".replace(",", "X").replace(".", ",").replace("X", ".")


def format_percent(value: float) -> str:
    return f"{value:.2%}".replace(".", ",")


def load_clean_dataset() -> pd.DataFrame:
    if not CLEAN_PATH.exists():
        fail(
            "No se encuentra el dataset limpio. Ejecuta primero: "
            "python scripts/02_limpieza_dataset.py"
        )
    return pd.read_csv(CLEAN_PATH, encoding="utf-8")


def ensure_required_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "Ingresos_Brutos" not in df.columns:
        df["Ingresos_Brutos"] = df["Precio_Unitario"] * df["Cantidad"]

    if "Ingreso_Neto_Logistico" not in df.columns:
        df["Ingreso_Neto_Logistico"] = df["Ingresos_Brutos"] - df["Costo_Envio"]

    return df


def build_summary(df: pd.DataFrame) -> str:
    ingresos = df["Ingresos_Brutos"].sum()
    pedidos = df["ID_Pedido"].nunique()
    clientes = df["ID_Cliente"].nunique()
    unidades = df["Cantidad"].sum()
    coste_envio = df["Costo_Envio"].sum()
    margen_aprox = df["Ingreso_Neto_Logistico"].sum()
    ticket_medio = ingresos / pedidos if pedidos else 0
    coste_relativo = coste_envio / ingresos if ingresos else 0
    satisfaccion_media = df["Puntuacion_Satisfaccion"].mean()
    satisfaccion_alta = (df["Puntuacion_Satisfaccion"] >= 4).mean()

    lines = [
        "# Resumen de KPIs de control – Power BI",
        "",
        "Este documento sirve para validar que las medidas DAX del dashboard coinciden con el dataset limpio.",
        "",
        "## KPIs generales",
        "",
        f"- Pedidos: {pedidos:,}".replace(",", "."),
        f"- Clientes únicos: {clientes:,}".replace(",", "."),
        f"- Unidades vendidas: {int(unidades):,}".replace(",", "."),
        f"- Ingresos brutos: {format_currency(ingresos)}",
        f"- Coste total de envío: {format_currency(coste_envio)}",
        f"- Margen neto aproximado: {format_currency(margen_aprox)}",
        f"- Ticket medio: {format_currency(ticket_medio)}",
        f"- Coste envío relativo: {format_percent(coste_relativo)}",
        f"- Satisfacción media: {satisfaccion_media:.2f} / 5".replace(".", ","),
        f"- % satisfacción alta: {format_percent(satisfaccion_alta)}",
        "",
        "## Ingresos por país",
        "",
    ]

    country = (
        df.groupby("Pais", as_index=False)["Ingresos_Brutos"]
        .sum()
        .sort_values("Ingresos_Brutos", ascending=False)
    )
    for _, row in country.iterrows():
        share = row["Ingresos_Brutos"] / ingresos if ingresos else 0
        lines.append(f"- {row['Pais']}: {format_currency(row['Ingresos_Brutos'])} ({format_percent(share)})")

    lines.extend(["", "## Ingresos por canal", ""])
    channel = (
        df.groupby("Canal_Venta", as_index=False)["Ingresos_Brutos"]
        .sum()
        .sort_values("Ingresos_Brutos", ascending=False)
    )
    for _, row in channel.iterrows():
        share = row["Ingresos_Brutos"] / ingresos if ingresos else 0
        lines.append(f"- {row['Canal_Venta']}: {format_currency(row['Ingresos_Brutos'])} ({format_percent(share)})")

    lines.extend(["", "## Ingresos por categoría", ""])
    category = (
        df.groupby("Categoria", as_index=False)["Ingresos_Brutos"]
        .sum()
        .sort_values("Ingresos_Brutos", ascending=False)
    )
    for _, row in category.iterrows():
        share = row["Ingresos_Brutos"] / ingresos if ingresos else 0
        lines.append(f"- {row['Categoria']}: {format_currency(row['Ingresos_Brutos'])} ({format_percent(share)})")

    lines.extend([
        "",
        "## Nota de uso",
        "",
        "Estos valores deben utilizarse como referencia para validar las tarjetas KPI y visuales principales en Power BI.",
    ])

    return "\n".join(lines)


def main() -> None:
    df = load_clean_dataset()
    df = ensure_required_columns(df)
    summary = build_summary(df)
    OUTPUT_PATH.write_text(summary, encoding="utf-8")
    print(f"Resumen de KPIs exportado correctamente en: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
