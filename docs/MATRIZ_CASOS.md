# Matriz de casos de prueba (30 casos)

Estado tras ejecutar `pytest`: **todas Aprobadas**. Las "pruebas" referenciadas están en `tests/`.

| ID | Historia | Descripción | Datos de entrada | Resultado esperado | Prueba automatizada | Estado |
|---|---|---|---|---|---|---|
| T01 | HU-01 CA1 | Cantidad mínima válida | 1 unidad, stock 100 | Queda en el carrito con 1 | `test_agregar_cantidad_valida_...[1]` | Aprobada |
| T02 | HU-01 CA1 | Cantidad máxima válida | 50 unidades | Queda con 50 | `...[50]` | Aprobada |
| T03 | HU-01 CA1 | Cantidades intermedias | 2 y 49 unidades | Quedan con esa cantidad | `...[2]`, `...[49]` | Aprobada |
| T04 | HU-01 CA2 | Cero unidades | 0 | `CantidadInvalidaError` | `test_agregar_cantidad_fuera_de_rango_...[0]` | Aprobada |
| T05 | HU-01 CA2 | Cincuenta y una unidades | 51 | `CantidadInvalidaError` | `...[51]` | Aprobada |
| T06 | HU-01 CA2 | Negativo y muy grande | -1 y 100 | `CantidadInvalidaError` | `...[-1]`, `...[100]` | Aprobada |
| T07 | HU-01 CA3 | Stock menor a lo pedido | stock 3, pide 4 | `StockInsuficienteError` | `test_agregar_con_stock_menor_...` | Aprobada |
| T08 | HU-01 CA3 | Stock igual a lo pedido | stock 4, pide 4 | Se agrega | `test_agregar_con_stock_exactamente_...` | Aprobada |
| T09 | HU-01 CA4 | Mismo producto dos veces | 3 + 2 | 1 línea con 5 | `test_agregar_el_mismo_producto_...` | Aprobada |
| T10 | HU-01 CA4 | Acumulado supera 50 | 30 + 21 | `CantidadInvalidaError` | `test_agregar_de_nuevo_que_supera_50_...` | Aprobada |
| T11 | HU-01 (mock) | Se consulta el stock correcto | Agregar 2 | `stock_disponible(id)` llamado 1 vez | `test_agregar_consulta_al_inventario_...` | Aprobada |
| T12 | HU-01 (mock) | Cantidad inválida no consulta | 0 | Inventario no se llama | `test_cantidad_invalida_no_consulta_...` | Aprobada |
| T13 | HU-02 CA1 | IVA 0 % | $100.000, tarifa 0 | IVA $0 | `test_iva_corresponde_...[0-0]` | Aprobada |
| T14 | HU-02 CA1 | IVA 5 % | $100.000, tarifa 5 | IVA $5.000 | `...[5-5000]` | Aprobada |
| T15 | HU-02 CA1 | IVA 19 % | $100.000, tarifa 19 | IVA $19.000 | `...[19-19000]` | Aprobada |
| T16 | HU-02 CA2 | IVA sobre valor con descuento | $250.000, IVA 19 %, desc. 5 % | IVA $45.125 | `test_iva_se_calcula_sobre_el_valor_...` | Aprobada |
| T17 | HU-02 | Tarifa de IVA inválida | tarifa 16 | `TarifaIvaInvalidaError` | `test_producto_con_tarifa_...` | Aprobada |
| T18 | HU-03 CA1 | Justo debajo de $200.000 | $199.999 | Descuento 0 % ($0) | `test_porcentaje_...[199999-0]` y `test_liquidacion_aplica_...[199999-0]` | Aprobada |
| T19 | HU-03 CA2 | Límite inferior 5 % | $200.000 | 5 % ($10.000) | `...[200000-5]` | Aprobada |
| T20 | HU-03 CA2 | Límite superior 5 % | $499.999 | 5 % ($25.000) | `...[499999-5]` | Aprobada |
| T21 | HU-03 CA3 | Límite inferior 10 % | $500.000 | 10 % ($50.000) | `...[500000-10]` | Aprobada |
| T22 | HU-04 CA1 | SABANERO10 en el mínimo | $50.000 | Descuento $5.000 | `test_sabanero10_con_subtotal_minimo_...` | Aprobada |
| T23 | HU-04 CA1 | SABANERO10 bajo el mínimo | $49.999 | `CuponInvalidoError` | `test_sabanero10_con_subtotal_por_debajo_...` | Aprobada |
| T24 | HU-04 CA2 | ENVIOGRATIS | Corozal, $100.000 | Envío $0 | `test_enviogratis_deja_el_envio_en_cero` | Aprobada |
| T25 | HU-04 CA3 | Cupón inexistente | NOEXISTE | `CuponInvalidoError` | `test_cupon_inexistente_...` | Aprobada |
| T26 | HU-04 CA3 | Cupón vencido | Venció 01/01, hoy 02/01 | `CuponInvalidoError` | `test_cupon_vencido_...` | Aprobada |
| T27 | HU-04 CA4 | Cupón 10 % + volumen 10 % | $600.000 + SABANERO10 | 10 %, no 20 % | `test_cupon_y_descuento_...[600000-10]` | Aprobada |
| T28 | HU-04 CA4 | Cupón 10 % + volumen 5 % | $250.000 + SABANERO10 | 10 % (el mayor) | `...[250000-10]` | Aprobada |
| T29 | HU-05 CA1 | Envío Sincelejo / otro municipio | Sincelejo; Corozal | $8.000; $15.000 | `test_envio_cuesta_8000_...` | Aprobada |
| T30 | HU-05 CA2 | Envío gratis en el límite | Con IVA $149.999 y $150.000 | $8.000; $0 | `test_envio_es_gratis_...` | Aprobada |
| T31 | HU-05 | Productos sin IVA no cuentan | $300.000 con IVA 0 % | Envío $8.000 | `test_productos_sin_iva_...` | Aprobada |
| T32 | HU-05 CA3 | Fórmula del total | $100.000, IVA 19 %, Sincelejo | Total $127.000 | `test_total_es_subtotal_menos_...` | Aprobada |
| T33 | HU-06 CA1 | Puntos en el límite | $999 / $1.000 / $1.999 | 0 / 1 / 1 | `test_un_punto_por_cada_mil_...` | Aprobada |
| T34 | HU-06 CA2 | Cliente ORO | $1.000 y $250.515 | 2 y 500 puntos | `...[1000-ORO]`, `...[250515-ORO]` | Aprobada |
| T35 | HU-06 | Puntos sin contar envío | $500 + envío $8.000 | 0 puntos | `test_los_puntos_se_calculan_sin_...` | Aprobada |
| T36 | Transversal | Carrito vacío | — | `CarritoVacioError` | `test_liquidar_un_carrito_vacio_...` | Aprobada |
| T37 | Transversal | Redondeo al peso | 49/100, 50/100, 1.010 × 5 % | 0, 1, 51 | `test_precios.py` | Aprobada |
| T38 | **Ejemplo oficial** | Licuadora + 2 cafés + 4 arroces, ESTÁNDAR, Sincelejo | Subtotal $228.000 | Desc. $11.400 · IVA $33.915 · Envío $0 · **Total $250.515** · 250 pts | `test_ejemplo_oficial_...` | Aprobada |
