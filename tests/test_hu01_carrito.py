"""HU-01: agregar productos al carrito."""
import pytest


@pytest.mark.parametrize("cantidad", [1, 2, 49, 50])
def test_agregar_cantidad_valida_deja_producto_en_carrito(carrito, arroz, cantidad):
    # Arrange: carrito vacío y producto con stock suficiente (fixtures)
    # Act
    carrito.agregar(arroz, cantidad)
    # Assert
    assert carrito.items[0].producto == arroz
    assert carrito.items[0].cantidad == cantidad