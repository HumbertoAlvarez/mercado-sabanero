"""HU-03: descuento por volumen."""
from mercado.precios import descuento_volumen_pct


def test_subtotal_menor_a_200000_no_tiene_descuento():
    # Arrange
    subtotal = 199_999
    # Act
    porcentaje = descuento_volumen_pct(subtotal)
    # Assert
    assert porcentaje == 0