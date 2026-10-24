"""HU-04: cupones de descuento."""
from datetime import date

import pytest

from mercado.cupones import CatalogoCupones, Cupon, aplicar_envio, mejor_descuento_pct
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


def test_cupon_vigente_el_ultimo_dia_todavia_es_valido():
    # Arrange: el cupón vence el 1 de enero
    catalogo = CatalogoCupones([Cupon("HOY5", porcentaje=5, vence=date(2026, 1, 1))])
    # Act: hoy es justo el último día de vigencia
    cupon = catalogo.obtener("HOY5", hoy=date(2026, 1, 1))
    # Assert
    assert cupon.porcentaje == 5




@pytest.mark.parametrize("subtotal", [1, 49_999])
def test_sabanero10_con_subtotal_menor_a_50000_lanza_error(subtotal):
    # Arrange
    catalogo = CatalogoCupones()
    # Act + Assert
    with pytest.raises(CuponInvalidoError):
        catalogo.obtener("SABANERO10", subtotal=subtotal)


def test_sabanero10_con_subtotal_de_50000_es_valido():
    # Arrange
    catalogo = CatalogoCupones()
    # Act
    cupon = catalogo.obtener("SABANERO10", subtotal=50_000)
    # Assert
    assert cupon.porcentaje == 10

def test_cupon_enviogratis_deja_el_envio_en_cero():
    # Arrange
    catalogo = CatalogoCupones([Cupon("ENVIOGRATIS", envio_gratis=True)])
    cupon = catalogo.obtener("ENVIOGRATIS")
    # Act
    envio = aplicar_envio(cupon, 15_000)
    # Assert
    assert envio == 0


def test_cupon_sin_enviogratis_conserva_el_envio():
    # Arrange
    cupon = CatalogoCupones().obtener("SABANERO10")
    # Act
    envio = aplicar_envio(cupon, 15_000)
    # Assert
    assert envio == 15_000

@pytest.mark.parametrize("subtotal, esperado", [
    (100_000, 10),
    (300_000, 10),
    (600_000, 10),
])
def test_se_aplica_solo_el_mayor_entre_volumen_y_sabanero10(subtotal, esperado):
    # Arrange
    cupon = CatalogoCupones().obtener("SABANERO10")
    # Act
    porcentaje = mejor_descuento_pct(subtotal, cupon)
    # Assert
    assert porcentaje == esperado