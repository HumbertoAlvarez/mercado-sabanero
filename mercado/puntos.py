"""HU-06: puntos de fidelidad."""

PESOS_POR_PUNTO = 1_000


def calcular_puntos(total_sin_envio):
    return total_sin_envio // PESOS_POR_PUNTO