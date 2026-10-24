"""HU-04: cupones de descuento."""
import pytest

from mercado.cupones import CatalogoCupones
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


