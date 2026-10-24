from mercado.errores import CantidadInvalidaError
from mercado.modelos import ItemCarrito


class Carrito:
    def __init__(self, inventario):
        self._inventario = inventario
        self.items = []

    def agregar(self, producto, cantidad):
        if cantidad < 1 or cantidad > 50:
            raise CantidadInvalidaError(f"Cantidad inválida: {cantidad}. Debe estar entre 1 y 50.")
        self.items.append(ItemCarrito(producto, cantidad))