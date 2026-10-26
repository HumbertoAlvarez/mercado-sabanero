"""Liquidacion de una compra."""
from dataclasses import dataclass

from mercado.errores import CarritoVacioError
from mercado.precios import calcular_iva, descuento_volumen_pct, redondear_division


@dataclass(frozen=True)
class Liquidacion:
    subtotal: int
    iva: int
    descuento: int


def liquidar(carrito, municipio):
    if not carrito.items:
        raise CarritoVacioError("El carrito esta vacio")
    subtotal = carrito.subtotal
    porcentaje_descuento = descuento_volumen_pct(subtotal)
    descuento = redondear_division(subtotal * porcentaje_descuento, 100)
    iva = sum(
        calcular_iva(item.subtotal, item.producto.tarifa_iva, porcentaje_descuento)
        for item in carrito.items
    )
    return Liquidacion(subtotal=subtotal, iva=iva, descuento=descuento)