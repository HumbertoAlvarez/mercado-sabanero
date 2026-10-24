"""HU-04: cupones de descuento."""
from datetime import date

import pytest

from mercado.cupones import CatalogoCupones, Cupon
from mercado.errores import CuponInvalidoError


def test_sabanero10_existe_y_da_10_por_ciento():
    # Arrange
    catalogo = CatalogoCupones()
    # Act
    cupon = catalogo.obtener("SABANERO10")
    # Assert
    assert cupon.porcentaje == 10


def test_cupon_inexistente_lanza_error_de_cupon_invalido():
    # Arrange
    catalogo = CatalogoCupones()
    # Act + Assert
    with pytest.raises(CuponInvalidoError):
        catalogo.obtener("NOEXISTE")


def test_codigo_de_cupon_no_distingue_mayusculas_ni_espacios():
    # Arrange
    catalogo = CatalogoCupones()
    # Act
    cupon = catalogo.obtener("  sabanero10 ")
    # Assert
    assert cupon.codigo == "SABANERO10"


def test_cupon_vencido_lanza_error_de_cupon_invalido():
    # Arrange: cupón que venció el 1 de enero
    catalogo = CatalogoCupones([Cupon("VIEJO5", porcentaje=5, vence=date(2026, 1, 1))])
    # Act + Assert: hoy es 2 de enero
    with pytest.raises(CuponInvalidoError):
        catalogo.obtener("VIEJO5", hoy=date(2026, 1, 2))


