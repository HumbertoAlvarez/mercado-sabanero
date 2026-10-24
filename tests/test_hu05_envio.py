"""HU-05: costo de envío."""
import pytest

from mercado.envio import base_para_envio_gratis, calcular_envio
from mercado.modelos import ItemCarrito, Producto


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


@pytest.mark.parametrize("base, esperado", [
    (149_999, 8_000),
    (150_000, 0),
])
def test_envio_en_el_limite_del_envio_gratis(base, esperado):
    # Arrange
    municipio = "Sincelejo"
    # Act
    envio = calcular_envio(municipio, base)
    # Assert
    assert envio == esperado


def test_los_productos_sin_iva_no_cuentan_para_el_envio_gratis():
    # Arrange
    sin_iva = ItemCarrito(Producto("P1", "Arroz", 300_000, 0), 1)
    con_iva = ItemCarrito(Producto("P2", "Galletas", 149_999, 19), 1)
    # Act
    base = base_para_envio_gratis([sin_iva, con_iva])
    envio = calcular_envio("Sincelejo", base)
    # Assert
    assert envio == 8_000

def test_la_base_del_envio_gratis_solo_suma_productos_con_iva():
    # Arrange
    arroz = ItemCarrito(Producto("P3", "Arroz", 4_500, 0), 2)
    cafe = ItemCarrito(Producto("P2", "Café", 15_000, 5), 3)
    # Act
    base = base_para_envio_gratis([arroz, cafe])
    # Assert
    assert base == 45_000

def test_la_base_del_envio_gratis_solo_suma_productos_con_iva():
    # Arrange
    arroz = ItemCarrito(Producto("P3", "Arroz", 4_500, 0), 2)
    cafe = ItemCarrito(Producto("P2", "Café", 15_000, 5), 3)
    # Act
    base = base_para_envio_gratis([arroz, cafe])
    # Assert
    assert base == 45_000