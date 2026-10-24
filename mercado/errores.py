class CantidadInvalidaError(ValueError):
    """La cantidad a agregar está fuera del rango permitido (1 a 50)."""


class StockInsuficienteError(Exception):
    """El inventario tiene menos unidades de las solicitadas."""

class CuponInvalidoError(Exception):
    """El cupón no existe, está vencido o no cumple sus condiciones."""