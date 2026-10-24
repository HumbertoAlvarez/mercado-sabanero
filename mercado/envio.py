"""HU-05: costo de envío."""


UMBRAL_ENVIO_GRATIS = 150_000
TARIFA_SINCELEJO = 8_000
TARIFA_OTROS_MUNICIPIOS = 15_000
MUNICIPIO_LOCAL = "sincelejo"


def calcular_envio(municipio, base_productos_con_iva):
    if base_productos_con_iva >= UMBRAL_ENVIO_GRATIS:
        return 0
    if municipio.strip().lower() == MUNICIPIO_LOCAL:
        return TARIFA_SINCELEJO
    return TARIFA_OTROS_MUNICIPIOS


def base_para_envio_gratis(items):
    return sum(
        item.subtotal for item in items if item.producto.tarifa_iva > 0
    )
