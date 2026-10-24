"""HU-02: calcular el IVA."""
import pytest

from mercado.errores import TarifaIvaInvalidaError
from mercado.precios import calcular_iva


@pytest.mark.parametrize("tarifa, iva_esperado", [(0, 0), (5, 5_000), (19, 19_000)])
def test_iva_corresponde_a_la_tarifa_del_producto(tarifa, iva_esperado):
    # Arrange
    valor = 100_000
    # Act
    iva = calcular_iva(valor, tarifa)
    # Assert
    assert iva == iva_esperado


def test_tarifa_de_iva_no_permitida_lanza_error():
    # Arrange
    valor = 100_000
    # Act + Assert
    with pytest.raises(TarifaIvaInvalidaError):
        calcular_iva(valor, 16)