"""HU-04: cupones de descuento."""
from dataclasses import dataclass
from datetime import date
from typing import Optional

from mercado.errores import CuponInvalidoError
from mercado.precios import descuento_volumen_pct


@dataclass(frozen=True)
class Cupon:
    codigo: str
    porcentaje: int = 0
    vence: Optional[date] = None  # None = sin vencimiento
    subtotal_minimo: int = 0
    envio_gratis: bool = False


class CatalogoCupones:
    def __init__(self, cupones=None):
        if cupones is None:
            cupones = [Cupon(CODIGO_SABANERO10, porcentaje=10, subtotal_minimo=SUBTOTAL_MINIMO_SABANERO10)]
        self._cupones = {c.codigo: c for c in cupones}

    def obtener(self, codigo, hoy=None, subtotal=None):
        cupon = self._cupones.get(codigo.strip().upper())
        if cupon is None:
            raise CuponInvalidoError(f"El cupón {codigo!r} no existe")
        hoy = hoy or date.today()
        if cupon.vence is not None and hoy > cupon.vence:
            raise CuponInvalidoError(f"El cupón {cupon.codigo} está vencido")
        if subtotal is not None and subtotal < cupon.subtotal_minimo:
            raise CuponInvalidoError(
                f"El cupon {cupon.codigo} exige un subtotal minimo de {cupon.subtotal_minimo}"
            )
        return cupon


def aplicar_envio(cupon, envio):
    if cupon.envio_gratis:
        return 0
    return envio


def mejor_descuento_pct(subtotal, cupon):
    return max(descuento_volumen_pct(subtotal), cupon.porcentaje)
