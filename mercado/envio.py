"""HU-05: costo de envío."""


def calcular_envio(municipio, base_productos_con_iva):
    if base_productos_con_iva >= 150_000:
        return 0
    if municipio.strip().lower() == "sincelejo":
        return 8_000
    return 15_000