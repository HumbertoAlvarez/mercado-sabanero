"""Liquidacion de una compra."""
from dataclasses import dataclass

from mercado.errores import CarritoVacioError


@dataclass(frozen=True)
class Liquidacion:
    subtotal: int


def liquidar(carrito, municipio):
    if not carrito.items:
        raise CarritoVacioError("El carrito esta vacio")
    return Liquidacion(subtotal=carrito.subtotal)