from mercado.errores import CantidadInvalidaError, StockInsuficienteError
from mercado.modelos import ItemCarrito

MIN_UNIDADES = 1
MAX_UNIDADES = 50


class Carrito:
    def __init__(self, inventario):
        self._inventario = inventario
        self.items = []

    def agregar(self, producto, cantidad):
        self._validar_rango(cantidad)
        self._validar_stock(producto, cantidad)
        self.items.append(ItemCarrito(producto, cantidad))

    def _validar_rango(self, cantidad):
        if not MIN_UNIDADES <= cantidad <= MAX_UNIDADES:
            raise CantidadInvalidaError(
                f"Cantidad inválida: {cantidad}. "
                f"Debe estar entre {MIN_UNIDADES} y {MAX_UNIDADES}."
            )

    def _validar_stock(self, producto, cantidad):
        stock = self._inventario.stock_disponible(producto.id)
        if cantidad > stock:
            raise StockInsuficienteError(
                f"Stock insuficiente: se pidieron {cantidad} y hay {stock}."
            )
        
    def agregar(self, producto, cantidad):
        self._validar_rango(cantidad)
        self._validar_stock(producto, cantidad)
        for item in self.items:
            if item.producto == producto:
                item.cantidad += cantidad
                return
        self.items.append(ItemCarrito(producto, cantidad))
        
    def agregar(self, producto, cantidad):
        self._validar_rango(cantidad)
        self._validar_stock(producto, cantidad)
        item = self._buscar_item(producto)
        if item:
            item.cantidad += cantidad
        else:
            self.items.append(ItemCarrito(producto, cantidad))

    def _buscar_item(self, producto):
        for item in self.items:
            if item.producto == producto:
                return item
        return None