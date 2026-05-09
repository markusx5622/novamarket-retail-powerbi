# Medidas DAX – NovaMarket Retail Power BI

Este documento contiene las medidas DAX oficiales del modelo semántico de Power BI.

**Tabla esperada:** `Ventas`  
**Uso:** crear las medidas en Power BI Desktop dentro de la tabla `Ventas` o en una tabla auxiliar denominada `Medidas`.

---

## 1. KPIs comerciales base

```DAX
Ingresos Brutos =
SUMX(
    Ventas,
    Ventas[Precio_Unitario] * Ventas[Cantidad]
)
```

```DAX
Pedidos =
DISTINCTCOUNT(Ventas[ID_Pedido])
```

```DAX
Clientes Únicos =
DISTINCTCOUNT(Ventas[ID_Cliente])
```

```DAX
Unidades Vendidas =
SUM(Ventas[Cantidad])
```

```DAX
Ticket Medio =
DIVIDE([Ingresos Brutos], [Pedidos])
```

---

## 2. KPIs logísticos y operativos

```DAX
Coste Total Envío =
SUM(Ventas[Costo_Envio])
```

```DAX
Coste Medio Envío =
AVERAGE(Ventas[Costo_Envio])
```

```DAX
Margen Neto Aproximado =
[Ingresos Brutos] - [Coste Total Envío]
```

```DAX
Coste Envío Relativo =
DIVIDE([Coste Total Envío], [Ingresos Brutos])
```

```DAX
Ingreso Neto Logístico por Pedido =
DIVIDE([Margen Neto Aproximado], [Pedidos])
```

> Nota: `Margen Neto Aproximado` no representa beneficio contable real, ya que el dataset no contiene coste de producto. Se interpreta como indicador operativo de presión logística.

---

## 3. KPIs de satisfacción

```DAX
Satisfacción Media =
AVERAGE(Ventas[Puntuacion_Satisfaccion])
```

```DAX
Pedidos Satisfacción Alta =
CALCULATE(
    [Pedidos],
    Ventas[Puntuacion_Satisfaccion] >= 4
)
```

```DAX
Pedidos Satisfacción Baja =
CALCULATE(
    [Pedidos],
    Ventas[Puntuacion_Satisfaccion] <= 2
)
```

```DAX
% Satisfacción Alta =
DIVIDE([Pedidos Satisfacción Alta], [Pedidos])
```

```DAX
% Satisfacción Baja =
DIVIDE([Pedidos Satisfacción Baja], [Pedidos])
```

---

## 4. Medidas por categoría

```DAX
Ingresos Tecnología =
CALCULATE(
    [Ingresos Brutos],
    Ventas[Categoria] = "Tecnología"
)
```

```DAX
Ingresos Estilo de Vida =
CALCULATE(
    [Ingresos Brutos],
    Ventas[Categoria] = "Estilo de Vida"
)
```

```DAX
% Ingresos Tecnología =
DIVIDE([Ingresos Tecnología], [Ingresos Brutos])
```

```DAX
% Ingresos Estilo de Vida =
DIVIDE([Ingresos Estilo de Vida], [Ingresos Brutos])
```

---

## 5. Participación y ranking

```DAX
% Ingresos =
DIVIDE(
    [Ingresos Brutos],
    CALCULATE([Ingresos Brutos], ALL(Ventas))
)
```

```DAX
% Ingresos por País =
DIVIDE(
    [Ingresos Brutos],
    CALCULATE([Ingresos Brutos], ALL(Ventas[Pais]))
)
```

```DAX
% Ingresos por Canal =
DIVIDE(
    [Ingresos Brutos],
    CALCULATE([Ingresos Brutos], ALL(Ventas[Canal_Venta]))
)
```

```DAX
Ranking Producto por Ingresos =
RANKX(
    ALL(Ventas[Producto]),
    [Ingresos Brutos],
    ,
    DESC,
    DENSE
)
```

```DAX
Ranking País por Ingresos =
RANKX(
    ALL(Ventas[Pais]),
    [Ingresos Brutos],
    ,
    DESC,
    DENSE
)
```

---

## 6. Medidas temporales

```DAX
Ingresos Mes Anterior =
CALCULATE(
    [Ingresos Brutos],
    DATEADD(Ventas[Fecha], -1, MONTH)
)
```

```DAX
Variación Ingresos Mes Anterior =
[Ingresos Brutos] - [Ingresos Mes Anterior]
```

```DAX
% Variación Ingresos Mes Anterior =
DIVIDE([Variación Ingresos Mes Anterior], [Ingresos Mes Anterior])
```

> Nota: las medidas temporales requieren que `Ventas[Fecha]` esté configurada como tipo Fecha. Para un modelo más avanzado, se recomienda crear una tabla calendario.

---

## 7. Medidas para alertas operativas

```DAX
Alerta Satisfacción =
IF(
    [Satisfacción Media] < 3.8,
    "Revisar",
    "Correcto"
)
```

```DAX
Alerta Coste Envío Relativo =
IF(
    [Coste Envío Relativo] > 0.05,
    "Coste elevado",
    "Coste controlado"
)
```

```DAX
Segmento Operativo =
SWITCH(
    TRUE(),
    [Satisfacción Media] < 3.8 && [Coste Envío Relativo] > 0.05, "Prioridad alta",
    [Satisfacción Media] < 3.8, "Mejorar experiencia",
    [Coste Envío Relativo] > 0.05, "Optimizar logística",
    "Situación estable"
)
```
