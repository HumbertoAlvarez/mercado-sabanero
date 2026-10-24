"""Liquidación de una compra."""
import pytest

from mercado.errores import CarritoVacioError
from mercado.liquidacion import liquidar


def test_liquidar_un_carrito_vacio_lanza_error(carrito):
    # Arrange: carrito sin productos (fixture)
    # Act + Assert
    with pytest.raises(CarritoVacioError):
        liquidar(carrito, "Sincelejo")

def test_liquidar_cuatro_arroces_a_sincelejo_da_subtotal_18000(carrito, arroz):
    # Arrange
    carrito.agregar(arroz, 4)
    # Act
    resultado = liquidar(carrito, "Sincelejo")
    # Assert
    assert resultado.subtotal == 18_000