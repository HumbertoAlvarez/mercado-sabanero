"""Fixtures compartidas: producto de ejemplo y doble de prueba del inventario."""
from unittest.mock import MagicMock

import pytest

from mercado.carrito import Carrito
from mercado.inventario import Inventario
from mercado.modelos import Producto


@pytest.fixture
def inventario():
    """Doble de prueba del servicio externo: por defecto hay 100 unidades de todo."""
    mock = MagicMock(spec=Inventario)
    mock.stock_disponible.return_value = 100
    return mock


@pytest.fixture
def carrito(inventario):
    return Carrito(inventario)


@pytest.fixture
def arroz():
    return Producto("P3", "Arroz", 4_500, 0)




@pytest.fixture
def cafe():
    return Producto("P2", "Café", 15_000, 5)