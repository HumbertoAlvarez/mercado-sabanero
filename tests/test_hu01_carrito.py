"""HU-01: agregar productos al carrito."""
import pytest

from mercado.errores import CantidadInvalidaError


@pytest.mark.parametrize("cantidad", [1, 2, 49, 50])
def test_agregar_cantidad_valida_deja_producto_en_carrito(carrito, arroz, cantidad):
    # Arrange: carrito vacío y producto con stock suficiente (fixtures)
    # Act
    carrito.agregar(arroz, cantidad)
    # Assert
    assert carrito.items[0].producto == arroz
    assert carrito.items[0].cantidad == cantidad


@pytest.mark.parametrize("cantidad", [-1, 0, 51, 100])
def test_agregar_cantidad_fuera_de_rango_lanza_error(carrito, arroz, cantidad):
    # Arrange: carrito vacío
    # Act + Assert
    with pytest.raises(CantidadInvalidaError):
        carrito.agregar(arroz, cantidad)