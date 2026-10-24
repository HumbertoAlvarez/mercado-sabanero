# Mercado Sabanero · Módulo de liquidación de compras

Lógica de negocio (sin interfaz ni base de datos) que liquida un pedido: carrito, IVA, descuento por
volumen, cupones, envío y puntos. Desarrollado con **TDD** (rojo → verde → refactor).

- Lenguaje: Python 3.10+ · Pruebas: **pytest** · Dobles de prueba: **unittest.mock** · Cobertura: **pytest-cov (coverage.py)**

## Cómo ejecutar las pruebas

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -v                        # todas las pruebas
pytest --cov=mercado --cov-report=term-missing --cov-report=html   # cobertura (abre htmlcov/index.html)
```

## Estructura

| Carpeta / archivo | Contenido |
|---|---|
| `mercado/carrito.py` | HU-01 carrito (rango 1–50, stock, suma de cantidades) |
| `mercado/precios.py` | Redondeo, IVA (HU-02) y descuento por volumen (HU-03) |
| `mercado/cupones.py` | HU-04 cupones SABANERO10 y ENVIOGRATIS |
| `mercado/envio.py` | HU-05 costo de envío |
| `mercado/puntos.py` | HU-06 puntos (ORO = doble) |
| `mercado/liquidacion.py` | Orquesta todo y calcula el total |
| `tests/test_hu0X_*.py` | Una suite por historia de usuario |
| `docs/` | Plan de pruebas, matriz de casos, registro de defectos |

## Supuestos de diseño (el enunciado es ambiguo en estos puntos)

1. **Cantidad acumulada:** al agregar de nuevo un producto, la cantidad *acumulada* también debe ser ≤ 50 y ≤ stock.
2. **Envío gratis:** "productos con IVA" = suma del valor (antes de descuento) de los productos con tarifa de IVA > 0 %.
3. **SABANERO10 bajo el mínimo:** si el subtotal es menor a $50.000, se rechaza con `CuponInvalidoError`.
4. **Redondeo:** al peso más cercano, el 0,5 sube. El IVA se calcula por línea sobre el valor con descuento.
5. **Un solo cupón** por compra; ENVIOGRATIS no excluye el descuento por volumen.
6. **Puntos:** sobre el total pagado sin envío, 1 por cada $1.000 completos.
