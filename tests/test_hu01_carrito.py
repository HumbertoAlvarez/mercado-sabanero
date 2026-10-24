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


def test_agregar_de_nuevo_valida_el_stock_sobre_la_cantidad_acumulada(carrito, inventario, arroz):
    # Arrange: el inventario (mock) dice que hay 4 unidades y ya hay 3 en el carrito
    inventario.stock_disponible.return_value = 4
    carrito.agregar(arroz, 3)
    # Act + Assert
    with pytest.raises(StockInsuficienteError):
        carrito.agregar(arroz, 2)     


def test_agregar_consulta_al_inventario_el_stock_del_producto(carrito, inventario, arroz):
    # Arrange: inventario es un doble de prueba
    # Act
    carrito.agregar(arroz, 2)
    # Assert
    inventario.stock_disponible.assert_called_once_with(arroz.id)


def test_cantidad_invalida_no_consulta_al_inventario(carrito, inventario, arroz):
    # Arrange: inventario es un doble de prueba
    # Act
    with pytest.raises(CantidadInvalidaError):
        carrito.agregar(arroz, 0)
    # Assert
    inventario.stock_disponible.assert_not_called()


def test_subtotal_del_carrito_suma_precio_por_cantidad(carrito, arroz, cafe):
    # Arrange
    carrito.agregar(arroz, 4)   # 18.000
    carrito.agregar(cafe, 2)    # 30.000
    # Act
    subtotal = carrito.subtotal
    # Assert
    assert subtotal == 48_000