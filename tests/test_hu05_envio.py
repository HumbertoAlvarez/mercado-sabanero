"""HU-05: costo de envío."""
from mercado.envio import calcular_envio


def test_envio_a_sincelejo_cuesta_8000():
    # Arrange
    municipio = "Sincelejo"
    # Act
    envio = calcular_envio(municipio, 0)
    # Assert
    assert envio == 8_000

def test_envio_a_otro_municipio_cuesta_15000():
    # Arrange
    municipio = "Corozal"
    # Act
    envio = calcular_envio(municipio, 0)
    # Assert
    assert envio == 15_000


def test_el_municipio_no_distingue_mayusculas_ni_espacios():
    # Arrange
    municipio = "  sincelejo "
    # Act
    envio = calcular_envio(municipio, 0)
    # Assert
    assert envio == 8_000


def test_envio_gratis_desde_150000():
    # Arrange
    municipio = "Sincelejo"
    # Act
    envio = calcular_envio(municipio, 150_000)
    # Assert
    assert envio == 0


def test_envio_se_cobra_con_149999():
    # Arrange
    municipio = "Sincelejo"
    # Act
    envio = calcular_envio(municipio, 149_999)
    # Assert
    assert envio == 8_000
