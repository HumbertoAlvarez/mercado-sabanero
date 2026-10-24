class Inventario:
    """Contrato del servicio externo de inventario."""

    def stock_disponible(self, producto_id):
        raise NotImplementedError