"""Liquidación de una compra."""
import pytest

from mercado.errores import CarritoVacioError
from mercado.liquidacion import liquidar
from mercado.modelos import Producto

def test_liquidar_un_carrito_vacio_lanza_error(carrito):
    # Arrange: carrito sin productos (fixture)
    # Act + Assert
    with pytest.raises(CarritoVacioError):
        liquidar(carrito, "Sincelejo")

def test_liquidar_cuatro_arroces_a_sincelejo_da_subtotal_18000(carrito, arroz):
    # Arrange
    carrito.agregar(arroz, 4)
    # Act
    resultado = liquidar(carrito, "Sincelejo")
    # Assert
    assert resultado.subtotal == 18_000

def test_liquidar_cuatro_arroces_a_sincelejo_da_subtotal_18000(carrito, arroz):
    # Arrange
    carrito.agregar(arroz, 4)
    # Act
    resultado = liquidar(carrito, "Sincelejo")
    # Assert
    assert resultado.subtotal == 18_000


@pytest.mark.parametrize("tarifa, iva_esperado", [(0, 0), (5, 5_000), (19, 19_000)])
def test_liquidar_calcula_el_iva_segun_la_tarifa_del_producto(carrito, tarifa, iva_esperado):
    # Arrange: un producto de 100.000, por debajo del descuento por volumen
    carrito.agregar(Producto("PX", "Producto de prueba", 100_000, tarifa), 1)
    # Act
    resultado = liquidar(carrito, "Sincelejo")
    # Assert
    assert resultado.iva == iva_esperado


@pytest.mark.parametrize("precio, descuento_esperado", [
    (199_999, 0),
    (200_000, 10_000),
    (500_000, 50_000),
])
def test_liquidar_aplica_el_descuento_por_volumen_segun_el_subtotal(carrito, precio, descuento_esperado):
    # Arrange: un producto sin IVA, para aislar el descuento
    carrito.agregar(Producto("PX", "Producto de prueba", precio, 0), 1)
    # Act
    resultado = liquidar(carrito, "Sincelejo")
    # Assert
    assert resultado.descuento == descuento_esperado