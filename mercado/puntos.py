"""HU-06: puntos de fidelidad."""

PESOS_POR_PUNTO = 1_000


def calcular_puntos(total_sin_envio, categoria=None):
    puntos = total_sin_envio // PESOS_POR_PUNTO
    if categoria == "ORO":
        return puntos * 2
    return puntos