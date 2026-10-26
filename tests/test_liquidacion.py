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

@pytest.mark.parametrize("precio, iva_esperado", [
    (250_000, 45_125),
    (600_000, 102_600),
])
def test_liquidar_calcula_el_iva_sobre_el_valor_ya_descontado(carrito, precio, iva_esperado):
    # Arrange: un producto con IVA de 19 %, con descuento por volumen de 5 % y de 10 %
    carrito.agregar(Producto("PX", "Producto de prueba", precio, 19), 1)
    # Act
    resultado = liquidar(carrito, "Sincelejo")
    # Assert
    assert resultado.iva == iva_esperado


@pytest.mark.parametrize("municipio, envio_esperado", [
    ("Sincelejo", 8_000),
    ("Corozal", 15_000),
])


def test_liquidar_cobra_8000_en_sincelejo_y_15000_en_otros_municipios(carrito, municipio, envio_esperado):
    # Arrange: un producto sin IVA y de poco valor, para no activar el envío gratis
    carrito.agregar(Producto("PX", "Producto de prueba", 20_000, 0), 1)
    # Act
    resultado = liquidar(carrito, municipio)
    # Assert
    assert resultado.envio == envio_esperado

@pytest.mark.parametrize("precio, envio_esperado", [
    (149_999, 8_000),
    (150_000, 0),
])
def test_liquidar_da_envio_gratis_desde_150000_en_productos_con_iva(carrito, precio, envio_esperado):
    # Arrange: un producto con IVA 19 % justo debajo y justo en el umbral
    carrito.agregar(Producto("PX", "Producto de prueba", precio, 19), 1)
    # Act
    resultado = liquidar(carrito, "Sincelejo")
    # Assert
    assert resultado.envio == envio_esperado


@pytest.mark.parametrize("precio, total_esperado", [
    (100_000, 127_000),
    (250_000, 282_625),
])
def test_liquidar_calcula_el_total_como_subtotal_menos_descuento_mas_iva_mas_envio(carrito, precio, total_esperado):
    # Arrange: un producto con IVA del 19 % en Sincelejo, sin descuento y con descuento del 5 %
    carrito.agregar(Producto("PX", "Producto de prueba", precio, 19), 1)
    # Act
    resultado = liquidar(carrito, "Sincelejo")
    # Assert
    assert resultado.total == total_esperado

@pytest.mark.parametrize("precio, puntos_esperados", [
    (100_000, 119),
    (250_000, 282),
])
def test_liquidar_da_un_punto_por_cada_1000_pagados_sin_contar_el_envio(carrito, precio, puntos_esperados):
    # Arrange: un producto con IVA del 19 % en Sincelejo, con y sin envío cobrado
    carrito.agregar(Producto("PX", "Producto de prueba", precio, 19), 1)
    # Act
    resultado = liquidar(carrito, "Sincelejo")
    # Assert
    assert resultado.puntos == puntos_esperados
