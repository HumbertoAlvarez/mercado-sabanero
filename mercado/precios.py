from mercado.errores import TarifaIvaInvalidaError


def calcular_iva(valor, tarifa):
    if tarifa not in (0, 5, 19):
        raise TarifaIvaInvalidaError(f"Tarifa de IVA no permitida: {tarifa}.")
    return valor * tarifa // 100