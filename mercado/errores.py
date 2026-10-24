class CantidadInvalidaError(ValueError):
    """La cantidad a agregar está fuera del rango permitido (1 a 50)."""


class StockInsuficienteError(Exception):
    """El inventario tiene menos unidades de las solicitadas."""



class TarifaIvaInvalidaError(ValueError):
    """La tarifa de IVA no es 0, 5 ni 19 por ciento."""
class CuponInvalidoError(Exception):
    """El cupón no existe, está vencido o no cumple sus condiciones."""