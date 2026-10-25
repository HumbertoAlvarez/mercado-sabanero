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
    iva = sum(
        calcular_iva(item.subtotal, item.producto.tarifa_iva)
        for item in carrito.items
    )
    subtotal = carrito.subtotal
    descuento = redondear_division(subtotal * descuento_volumen_pct(subtotal), 100)
    return Liquidacion(subtotal=subtotal, iva=iva, descuento=descuento)