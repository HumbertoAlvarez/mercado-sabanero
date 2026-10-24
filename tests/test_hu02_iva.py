"""HU-02: calcular el IVA."""
import pytest

from mercado.precios import calcular_iva


@pytest.mark.parametrize("tarifa, iva_esperado", [(0, 0), (5, 5_000), (19, 19_000)])
def test_iva_corresponde_a_la_tarifa_del_producto(tarifa, iva_esperado):
    # Arrange
    valor = 100_000
    # Act
    iva = calcular_iva(valor, tarifa)
    # Assert
    assert iva == iva_esperado
    