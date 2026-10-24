from mercado.puntos import calcular_puntos


def test_999_pesos_no_dan_puntos():
    # Arrange
    total = 999
    # Act
    puntos = calcular_puntos(total)
    # Assert
    assert puntos == 0


def test_1000_pesos_dan_1_punto():
    # Arrange
    total = 1_000
    # Act
    puntos = calcular_puntos(total)
    # Assert
    assert puntos == 1


def test_1999_pesos_dan_1_punto():
    # Arrange
    total = 1_999
    # Act
    puntos = calcular_puntos(total)
    # Assert
    assert puntos == 1