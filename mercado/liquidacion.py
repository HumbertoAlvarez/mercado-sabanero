"""Liquidacion de una compra."""
from dataclasses import dataclass

from mercado.envio import calcular_envio
from mercado.errores import CarritoVacioError
from mercado.precios import calcular_iva, descuento_volumen_pct, redondear_division
from mercado.envio import calcular_envio, base_para_envio_gratis
from mercado.puntos import calcular_puntos


@dataclass(frozen=True)
class Liquidacion:
    subtotal: int
    iva: int
    descuento: int
    envio: int
    total: int
    puntos: int


def liquidar(carrito, municipio, categoria=None, cupon=None):
    if not carrito.items:
        raise CarritoVacioError("El carrito esta vacio")
    subtotal = carrito.subtotal
    porcentaje_descuento = descuento_volumen_pct(subtotal)
    descuento = redondear_division(subtotal * porcentaje_descuento, 100)
    iva = sum(
        calcular_iva(item.subtotal, item.producto.tarifa_iva, porcentaje_descuento)
        for item in carrito.items
    )
    base_envio_gratis = base_para_envio_gratis(carrito.items)
    envio = calcular_envio(municipio, base_envio_gratis)
    if cupon == "ENVIOGRATIS":
        envio = 0
    total = subtotal - descuento + iva + envio
    puntos = calcular_puntos(total - envio, categoria)
    return Liquidacion(subtotal=subtotal, iva=iva, descuento=descuento, envio=envio, total=total, puntos=puntos)