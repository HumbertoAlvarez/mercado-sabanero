"""HU-05: costo de envío."""
from mercado.envio import calcular_envio


def test_envio_a_sincelejo_cuesta_8000():
    # Arrange
    municipio = "Sincelejo"
    # Act
    envio = calcular_envio(municipio, 0)
    # Assert
    assert envio == 8_000