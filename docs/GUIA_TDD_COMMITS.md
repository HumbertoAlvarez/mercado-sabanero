# Guía para reproducir el ciclo TDD con commits (evidencia exigida)

El código y las pruebas finales ya están escritos, pero **la evidencia de TDD son sus commits** y debe ser
genuina: hagan el ciclo ustedes, historia por historia, con commits `test:` → `feat:` → `refactor:`.
Cada integrante debe tener commits propios en al menos dos historias y revisar las pruebas de un compañero.

## Cómo hacerlo con este proyecto
1. Creen el repo, copien `README.md`, `pyproject.toml`, `requirements.txt`, `docs/` y `tests/conftest.py`, y hagan el primer commit (`chore:`).
2. Por cada historia: copien **un solo archivo de prueba** (`tests/test_hu0X_*.py`) o solo las primeras pruebas → corren `pytest` → **rojo** → `git commit -m "test: HU-0X ..."`.
3. Copien/escriban **lo mínimo** del código de `mercado/` para pasar → **verde** → `git commit -m "feat: HU-0X ..."`.
4. Mejoren nombres/duplicación sin romper nada → `git commit -m "refactor: ..."`.
5. Sugerencia de ritmo: una prueba (o una parametrizada) por ciclo, no el archivo entero de golpe.

## Orden y reparto sugerido (3 integrantes → 2 historias cada uno)
| Orden | Historia | Archivos de código | Integrante |
|---|---|---|---|
| 1 | HU-01 Carrito | `errores.py`, `modelos.py`, `inventario.py`, `carrito.py` | A |
| 2 | HU-03 Volumen | `precios.py` (`redondear`, `porcentaje`, `descuento_volumen_pct`) | B |
| 3 | HU-02 IVA | `precios.py` (`iva_de_linea`), `liquidacion.py` (primera versión) | A |
| 4 | HU-05 Envío | `envio.py` + total en `liquidacion.py` | C |
| 5 | HU-04 Cupones | `cupones.py` + regla "solo el mayor" | B |
| 6 | HU-06 Puntos | `puntos.py` + ejemplo oficial | C |

Con 4 integrantes: repartan HU-01/HU-02, HU-03/HU-04, HU-05/HU-06 y la revisión cruzada + informe.
Con 2: cada uno toma 3 historias.

## Ejemplo de ciclo (HU-03)
```
test: HU-03 sin descuento por volumen bajo $200.000        (rojo: no existe descuento_volumen_pct)
feat: descuento por volumen devuelve 0 bajo $200.000        (verde)
test: HU-03 5 % desde $200.000                              (rojo)
feat: tramo del 5 %                                         (verde)
test: HU-03 10 % desde $500.000                             (rojo)
feat: tramo del 10 %                                        (verde)
refactor: constantes con nombre para los umbrales           (verde)
```

## Para la sustentación (20 %)
- Pueden explicar **cada línea**: lean `mercado/` y `tests/` completos antes de presentar.
- Practiquen un ciclo en vivo: p. ej. "los puntos de ORO suben a triple" → escribir la prueba, verla en rojo, cambiar una línea, verla en verde.
- Declaren el uso de IA en el informe (la actividad lo exige). Texto sugerido:
  *"Se usó Claude (Anthropic) como apoyo para generar una propuesta inicial del código, las pruebas y los documentos; el equipo revisó, ejecutó, modificó y comprende cada línea."*
