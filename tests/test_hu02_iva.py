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


def test_iva_se_calcula_sobre_el_valor_con_descuento_aplicado():
    # Arrange
    valor = 250_000
    # Act
    iva = calcular_iva(valor, 19, descuento_porcentaje=5)
    # Assert
    assert iva == 45_125       

    @pytest.mark.parametrize("valor, esperado", [(1_005, 50), (1_010, 51)])
    def test_iva_con_fraccion_de_peso_se_redondea_al_peso_mas_cercano(valor, esperado):
    # Arrange: IVA de 5 % da 50,25 y 50,5 pesos
    # Act
        iva = calcular_iva(valor, 5)
    # Assert
        assert iva == esperado