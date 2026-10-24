"""Liquidación de una compra."""
import pytest

from mercado.errores import CarritoVacioError
from mercado.liquidacion import liquidar


def test_liquidar_un_carrito_vacio_lanza_error(carrito):
    # Arrange: carrito sin productos (fixture)
    # Act + Assert
    with pytest.raises(CarritoVacioError):
        liquidar(carrito, "Sincelejo")