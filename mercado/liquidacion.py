"""Liquidacion de una compra."""
from mercado.errores import CarritoVacioError


def liquidar(carrito, municipio):
    if not carrito.items:
        raise CarritoVacioError("El carrito esta vacio")
