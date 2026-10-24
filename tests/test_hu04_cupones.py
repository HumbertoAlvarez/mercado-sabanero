"""HU-04: cupones de descuento."""
from mercado.cupones import CatalogoCupones


def test_sabanero10_existe_y_da_10_por_ciento():
    # Arrange
    catalogo = CatalogoCupones()
    # Act
    cupon = catalogo.obtener("SABANERO10")
    # Assert
    assert cupon.porcentaje == 10
