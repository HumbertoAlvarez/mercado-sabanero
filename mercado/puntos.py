"""HU-06: puntos de fidelidad."""

PESOS_POR_PUNTO = 1_000
CATEGORIA_ORO = "ORO"
MULTIPLICADOR_ORO = 2


def calcular_puntos(total_sin_envio, categoria=None):
    puntos = total_sin_envio // PESOS_POR_PUNTO
    if categoria and categoria.strip().upper() == CATEGORIA_ORO:
        return puntos * MULTIPLICADOR_ORO
    return puntos