from mercado.errores import TarifaIvaInvalidaError

TARIFAS_IVA = (0, 5, 19)


def calcular_iva(valor, tarifa, descuento_porcentaje=0):
    if tarifa not in TARIFAS_IVA:
        raise TarifaIvaInvalidaError(f"Tarifa de IVA no permitida: {tarifa}.")
    return redondear_division(valor * (100 - descuento_porcentaje) * tarifa, 100 * 100)


def redondear_division(numerador, denominador):
    """Divide con enteros y redondea al entero más cercano (la mitad sube)."""
    return (2 * numerador + denominador) // (2 * denominador)