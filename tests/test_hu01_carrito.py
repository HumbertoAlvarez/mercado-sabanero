"""HU-01: agregar productos al carrito."""
import pytest

from mercado.errores import CantidadInvalidaError, StockInsuficienteError


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
def test_agregar_con_stock_menor_a_lo_pedido_lanza_stock_insuficiente(carrito, inventario, arroz):
    # Arrange: el inventario externo (mock) dice que solo hay 3 unidades
    inventario.stock_disponible.return_value = 3
    # Act + Assert
    with pytest.raises(StockInsuficienteError):
        carrito.agregar(arroz, 4)

def test_agregar_el_mismo_producto_dos_veces_suma_las_cantidades(carrito, arroz):
    # Arrange
    carrito.agregar(arroz, 3)
    # Act
    carrito.agregar(arroz, 2)
    # Assert
    assert len(carrito.items) == 1
    assert carrito.items[0].cantidad == 5

def test_agregar_de_nuevo_que_supera_50_acumuladas_lanza_error(carrito, arroz):
    # Arrange
    carrito.agregar(arroz, 30)
    # Act + Assert
    with pytest.raises(CantidadInvalidaError):
        carrito.agregar(arroz, 21) 