"""Redondeo al peso más cercano."""
import pytest

from mercado.precios import redondear_division


@pytest.mark.parametrize(
    "numerador, denominador, esperado",
    [(49, 100, 0), (50, 100, 1), (5_050, 100, 51)],
)
def test_redondeo_al_peso_mas_cercano(numerador, denominador, esperado):
    # Arrange: fracciones de peso (0,49; 0,5 y 50,5)
    # Act
    resultado = redondear_division(numerador, denominador)
    # Assert
    assert resultado == esperado

