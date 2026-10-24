"""HU-03: descuento por volumen."""
import pytest

from mercado.precios import descuento_volumen_pct


def test_subtotal_menor_a_200000_no_tiene_descuento():
    # Arrange
    subtotal = 199_999
    # Act
    porcentaje = descuento_volumen_pct(subtotal)
    # Assert
    assert porcentaje == 0


@pytest.mark.parametrize("subtotal", [200_000, 350_000, 499_999])
def test_subtotal_desde_200000_y_menor_a_500000_tiene_5_por_ciento(subtotal):
    # Arrange: límite inferior, valor intermedio y límite superior del tramo
    # Act
    porcentaje = descuento_volumen_pct(subtotal)
    # Assert
    assert porcentaje == 5


@pytest.mark.parametrize("subtotal", [500_000, 750_000])
def test_subtotal_desde_500000_tiene_10_por_ciento(subtotal):
    # Arrange: límite inferior del tramo y un valor mayor
    # Act
    porcentaje = descuento_volumen_pct(subtotal)
    # Assert
    assert porcentaje == 10