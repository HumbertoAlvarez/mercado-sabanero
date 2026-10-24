"""HU-01: agregar productos al carrito."""
import pytest

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
        item = self._buscar_item(producto)
        nueva_cantidad = (item.cantidad if item else 0) + cantidad
        self._validar_rango(nueva_cantidad)
        self._validar_stock(producto, nueva_cantidad)
        if item:
            item.cantidad = nueva_cantidad
        else:
            self.items.append(ItemCarrito(producto, nueva_cantidad))


        @property
        def subtotal(self):
            return sum(item.producto.precio * item.cantidad for item in self.items)        


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

    def _buscar_item(self, producto):
        for item in self.items:
            if item.producto == producto:
                return item
        return None
    
    def test_agregar_de_nuevo_valida_el_stock_sobre_la_cantidad_acumulada(carrito, inventario, arroz):
    # Arrange: el inventario (mock) dice que hay 4 unidades y ya hay 3 en el carrito
        inventario.stock_disponible.return_value = 4
        carrito.agregar(arroz, 3)
    # Act + Assert
        with pytest.raises(StockInsuficienteError):
            carrito.agregar(arroz, 2)