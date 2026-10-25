"""Liquidacion de una compra."""
from dataclasses import dataclass

from mercado.errores import CarritoVacioError
from mercado.precios import calcular_iva


@dataclass(frozen=True)
class Liquidacion:
    subtotal: int
    iva: int


def liquidar(carrito, municipio):
    if not carrito.items:
        raise CarritoVacioError("El carrito esta vacio")
    iva = sum(
        calcular_iva(item.subtotal, item.producto.tarifa_iva)
        for item in carrito.items
    )
    return Liquidacion(subtotal=carrito.subtotal, iva=iva)