from mercado.modelos import ItemCarrito


class Carrito:
    def __init__(self, inventario):
        self._inventario = inventario
        self.items = []

    def agregar(self, producto, cantidad):
        self.items.append(ItemCarrito(producto, cantidad))