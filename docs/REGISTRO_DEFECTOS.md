# Registro de defectos

> Registren aquí **los defectos reales** que encuentren mientras desarrollan (una prueba que falla por un bug
> en el código, un error de interpretación, etc.). No inventen defectos: la docente evalúa que sean verdaderos.

| ID | Descripción | Pasos para reproducir | Severidad | Estado |
|---|---|---|---|---|
| D01 | _(ej.: el IVA se calculaba sobre el valor sin descuento)_ | _(1. Carrito con $250.000 IVA 19 %. 2. Liquidar. 3. IVA = 47.500 en vez de 45.125)_ | Alta | Cerrado |

**Ciclo de vida:** Nuevo → Abierto → Asignado → Volver a probar → Verificado → Cerrado (o Reabierto).

## Ambigüedades del enunciado detectadas (consultar a la docente)
1. ¿La cantidad acumulada al re-agregar un producto también debe respetar el máximo de 50 y el stock?
2. ¿"Productos con IVA suman $150.000" es antes o después del descuento, y los productos con IVA 0 % cuentan?
3. ¿Qué pasa si se aplica SABANERO10 con subtotal menor a $50.000: error o se ignora el cupón?
