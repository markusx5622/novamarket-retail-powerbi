# Plantilla de medidas DAX – NovaMarket Retail

> Nota: Ajustar los nombres de tabla/columnas al modelo final en Power BI.

## Medidas principales

### 1) Ingresos Brutos
```DAX
Ingresos Brutos =
SUMX(
    'Ventas',
    'Ventas'[Precio_Unitario] * 'Ventas'[Cantidad]
)
```

### 2) Pedidos
```DAX
Pedidos =
DISTINCTCOUNT('Ventas'[ID_Pedido])
```

### 3) Clientes Únicos
```DAX
Clientes Únicos =
DISTINCTCOUNT('Ventas'[ID_Cliente])
```

### 4) Unidades Vendidas
```DAX
Unidades Vendidas =
SUM('Ventas'[Cantidad])
```

### 5) Coste Total Envío
```DAX
Coste Total Envío =
SUM('Ventas'[Costo_Envio])
```

### 6) Ticket Medio
```DAX
Ticket Medio =
DIVIDE([Ingresos Brutos], [Pedidos])
```

### 7) Margen Neto Aproximado
```DAX
Margen Neto Aproximado =
[Ingresos Brutos] - [Coste Total Envío]
```

### 8) Coste Envío Relativo
```DAX
Coste Envío Relativo =
DIVIDE([Coste Total Envío], [Ingresos Brutos])
```

### 9) Satisfacción Media
```DAX
Satisfacción Media =
AVERAGE('Ventas'[Puntuacion_Satisfaccion])
```

### 10) Pedidos Satisfacción Alta
```DAX
Pedidos Satisfacción Alta =
CALCULATE(
    DISTINCTCOUNT('Ventas'[ID_Pedido]),
    'Ventas'[Puntuacion_Satisfaccion] >= 4
)
```

### 11) % Satisfacción Alta
```DAX
% Satisfacción Alta =
DIVIDE([Pedidos Satisfacción Alta], [Pedidos])
```

### 12) Ingresos Tecnología
```DAX
Ingresos Tecnología =
CALCULATE(
    [Ingresos Brutos],
    'Ventas'[Categoria] = "Tecnología"
)
```

### 13) Ingresos Estilo de Vida
```DAX
Ingresos Estilo de Vida =
CALCULATE(
    [Ingresos Brutos],
    'Ventas'[Categoria] = "Estilo de Vida"
)
```

### 14) % Ingresos
```DAX
% Ingresos =
DIVIDE(
    [Ingresos Brutos],
    CALCULATE([Ingresos Brutos], ALL('Ventas'[Categoria]))
)
```
