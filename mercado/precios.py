from mercado.errores import TarifaIvaInvalidaError

TARIFAS_IVA = (0, 5, 19)


def calcular_iva(valor, tarifa):
    if tarifa not in TARIFAS_IVA:
        raise TarifaIvaInvalidaError(f"Tarifa de IVA no permitida: {tarifa}.")
    return valor * tarifa // 100