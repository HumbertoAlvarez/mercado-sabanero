"""HU-04: cupones de descuento."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Cupon:
    codigo: str
    porcentaje: int = 0


class CatalogoCupones:
    def obtener(self, codigo):
        return Cupon("SABANERO10", porcentaje=10)