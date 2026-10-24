import pytest

from mercado.puntos import calcular_puntos


@pytest.mark.parametrize("total, esperado", [
    (999, 0),
    (1_000, 1),
    (1_999, 1),
])
def test_puntos_sin_categoria_en_los_limites(total, esperado):
    # Arrange
    # (total y esperado llegan por parametro)
    # Act
    puntos = calcular_puntos(total)
    # Assert
    assert puntos == esperado


def test_cliente_oro_recibe_el_doble_con_1000_pesos():
    # Arrange
    total = 1_000
    # Act
    puntos = calcular_puntos(total, categoria="ORO")
    # Assert
    assert puntos == 2


def test_cliente_oro_recibe_500_puntos_con_el_ejemplo_oficial():
    # Arrange
    total = 250_515
    # Act
    puntos = calcular_puntos(total, categoria="ORO")
    # Assert
    assert puntos == 500


def test_250515_pesos_sin_categoria_dan_250_puntos():
    # Arrange
    total = 250_515
    # Act
    puntos = calcular_puntos(total)
    # Assert
    assert puntos == 250