# Registro de defectos

Defectos reales encontrados durante el desarrollo con TDD. D01, D02 y D03 los detectó la suite de pruebas o su conteo; D04 se detectó al revisar el código.

| ID | Descripción | Pasos para reproducir | Severidad | Estado |
|---|---|---|---|---|
| D01 | Tras el refactor «mover el cálculo del subtotal de la línea a ItemCarrito», la propiedad `subtotal` de `Carrito` quedó con una sangría de más, dentro del método `agregar`. `Carrito` perdió el atributo y la prueba del subtotal volvió a fallar. | 1. Ir al commit `3db5372`. 2. Ejecutar `python -m pytest -q`. 3. Falla `test_subtotal_del_carrito_suma_precio_por_cantidad` con `AttributeError: 'Carrito' object has no attribute 'subtotal'`. | Baja | Cerrado (`HASH_D01`) |
| D02 | La prueba parametrizada `test_iva_con_fraccion_de_peso_se_redondea_al_peso_mas_cercano` quedó con una sangría de más, anidada dentro de otra función de prueba, y pytest no la ejecutaba. La suite mostraba 23 casos en lugar de 25 y daba una falsa sensación de cobertura. | 1. Ir al commit `faa1568`. 2. Ejecutar `python -m pytest -q`. 3. Resultado: 23 pasadas, cuando debían ser 25. | Media | Cerrado (`2227ca2`) |
| D03 | El refactor «extraer constantes del cupón SABANERO10» dejó constantes usadas pero sin definir y rompió 10 pruebas de HU-04. | 1. Ir al commit `ffd06a6`. 2. Ejecutar `python -m pytest -q`. 3. Fallan 10 pruebas de cupones. | Media | Cerrado (`a419e39`) |
| D04 | `mercado/carrito.py` contenía código de prueba pegado por error en el archivo equivocado: el docstring de HU-01, `import pytest` y una función `test_agregar_de_nuevo_valida_el_stock_sobre_la_cantidad_acumulada` dentro de la clase `Carrito`. El módulo de producción dependía de pytest y tenía código muerto. | 1. Ir al commit `9da2c12`. 2. Abrir `mercado/carrito.py`. 3. Se ve `import pytest` al inicio y la función `test_...` al final de la clase. | Media | Cerrado (eliminado dentro de `cea4e20`) |

**Ciclo de vida:** Nuevo → Abierto → Asignado → Volver a probar → Verificado → Cerrado (o Reabierto).

**Lección:** ejecutar `python -m pytest -q` antes de cada commit, no solo antes del `refactor:`, y comprobar que el número de pruebas coincide con el esperado. D01 nació en un `feat:` commiteado sin confirmar el verde, D03 fue un `refactor:` sin esa verificación previa, y D02 se detectó porque el conteo de pruebas (23) no coincidía con el esperado (25). D04 se evita revisando git diff --staged antes de cada commit».

## Ambigüedades del enunciado y decisión del equipo

| ID | Ambigüedad | Decisión | Prueba |
|---|---|---|---|
| OBS-01 | ¿La cantidad acumulada al agregar de nuevo un producto debe respetar el máximo de 50 y el stock? | Sí: ambos se validan sobre la cantidad acumulada. | `test_agregar_de_nuevo_que_supera_50_acumuladas_lanza_error` y `test_agregar_de_nuevo_valida_el_stock_sobre_la_cantidad_acumulada` |
| OBS-02 | ¿Los productos con IVA del envío gratis se miden antes o después del descuento, y cuentan los de IVA 0 %? | Antes del descuento, y solo cuentan los de tarifa mayor a 0 %. | Pruebas de HU-05 |
| OBS-03 | ¿Qué pasa con SABANERO10 si el subtotal es menor a $50.000? | Se rechaza con `CuponInvalidoError`. | Prueba parametrizada de HU-04 (49.999 y 50.000) |