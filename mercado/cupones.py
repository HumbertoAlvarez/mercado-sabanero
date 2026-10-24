"""HU-04: cupones de descuento."""
from dataclasses import dataclass

from mercado.errores import CuponInvalidoError


@dataclass(frozen=True)
class Cupon:
    codigo: str
    porcentaje: int = 0


class CatalogoCupones:
    def __init__(self):
        self._cupones = {"SABANERO10": Cupon("SABANERO10", porcentaje=10)}

    def obtener(self, codigo):
        cupon = self._cupones.get(codigo)
        if cupon is None:
            raise CuponInvalidoError(f"El cupón {codigo!r} no existe")
        return cupon