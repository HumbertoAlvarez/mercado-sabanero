from mercado.errores import CantidadInvalidaError, StockInsuficienteError
from mercado.modelos import ItemCarrito

MIN_UNIDADES = 1
MAX_UNIDADES = 50


class Carrito:
    def __init__(self, inventario):
        self._inventario = inventario
        self.items = []

    def agregar(self, producto, cantidad):
        if not MIN_UNIDADES <= cantidad <= MAX_UNIDADES:
            raise CantidadInvalidaError(
                f"Cantidad inválida: {cantidad}. "
                f"Debe estar entre {MIN_UNIDADES} y {MAX_UNIDADES}."
            )
        stock = self._inventario.stock_disponible(producto.id)
        if cantidad > stock:
            raise StockInsuficienteError(
                f"Stock insuficiente: se pidieron {cantidad} y hay {stock}."
            )
        self.items.append(ItemCarrito(producto, cantidad))