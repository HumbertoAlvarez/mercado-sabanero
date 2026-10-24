from mercado.errores import TarifaIvaInvalidaError

TARIFAS_IVA = (0, 5, 19)


def calcular_iva(valor, tarifa, descuento_porcentaje=0):
    if tarifa not in TARIFAS_IVA:
        raise TarifaIvaInvalidaError(f"Tarifa de IVA no permitida: {tarifa}.")
    valor_con_descuento = valor * (100 - descuento_porcentaje) // 100
    return valor_con_descuento * tarifa // 100