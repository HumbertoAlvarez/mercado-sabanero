# Plan de pruebas ágil · Mercado Sabanero

## 1. Información general
| Campo | Valor |
|---|---|
| Proyecto | Módulo de liquidación de compras · Mercado Sabanero |
| Objetivo | Garantizar que cada regla de dinero (IVA, descuentos, cupones, envío, puntos) esté respaldada por pruebas unitarias automatizadas |
| Alcance | Solo lógica de negocio. **Incluye:** HU-01 a HU-06. **Excluye:** interfaz gráfica, base de datos, el servicio real de inventario |
| Responsables | _(nombres de los integrantes y qué historias llevó cada uno)_ |
| Fecha | _(fecha de elaboración)_ |
| Docente | Laudyt María Lambraño Pérez |

## 2. Estrategia
- **TDD** para todas las unidades: cada regla nace de una prueba en rojo (`test:`), se implementa lo mínimo (`feat:`) y se mejora el diseño (`refactor:`).
- **ATDD:** los criterios de aceptación Dado/Cuando/Entonces de cada historia se convierten en pruebas; cada criterio tiene al menos una prueba (ver matriz).
- **Pirámide:** base de pruebas unitarias rápidas; una prueba de "integración ligera" (ejemplo oficial) que recorre carrito → liquidación completa.
- **Dobles de prueba:** el inventario externo se reemplaza con `unittest.mock.MagicMock(spec=Inventario)`.
- **Técnicas:** valores límite (0, 1, 50, 51; $49.999/$50.000; $199.999/$200.000; $499.999/$500.000; $149.999/$150.000), pruebas parametrizadas, pruebas de error.

## 3. Tipos de prueba y herramientas
| Tipo | Qué valida | Herramienta |
|---|---|---|
| Unitaria (Q1) | Cada regla de negocio aislada | pytest |
| Doble de prueba | Interacción con inventario | unittest.mock |
| Integración ligera | Ejemplo oficial de punta a punta | pytest |
| Cobertura | % de líneas ejecutadas por las pruebas | pytest-cov / coverage.py |
| Control de versiones | Evidencia del ciclo TDD | Git + GitHub |

**Justificación:** Python y pytest tienen sintaxis corta (menos código repetitivo), parametrización nativa con `@pytest.mark.parametrize` y mocks integrados en la biblioteca estándar; el equipo ya los conoce.  _(Ajusta esta frase a la realidad de tu equipo.)_

## 4. Plan de ejecución
| Cuándo | Qué se ejecuta |
|---|---|
| Antes de cada commit `feat:` / `refactor:` | Todas las pruebas (`pytest`) |
| Al cierre de cada historia | Pruebas + reporte de cobertura |
| Al cierre del sprint | Informe de resultados (planificados / ejecutados / exitosos / fallidos) |

**Criterio de éxito:** 100 % de las pruebas en verde, incluido el ejemplo oficial ($250.515 y 250 puntos); cobertura de líneas ≥ 80 % en `mercado/`; todos los criterios de aceptación con al menos una prueba.

## 5. Gestión de riesgos
| # | Riesgo | Prob. | Impacto | Mitigación |
|---|---|---|---|---|
| R1 | Errores de redondeo al peso | Alta | Alto | Aritmética entera con función única `redondear`; pruebas con .25 y .5 |
| R2 | Valores límite mal interpretados (≥ vs >) | Alta | Alto | Pruebas en cada frontera (199.999/200.000, etc.) |
| R3 | Sumar cupón + descuento por volumen | Media | Alto | Prueba explícita de "solo el mayor" |
| R4 | Ambigüedades del enunciado (cantidad acumulada, "productos con IVA") | Media | Medio | Supuestos documentados en el README; consultar a la docente |
| R5 | Integrante sin commits propios | Media | Alto | Reparto de ≥ 2 historias por persona y revisión cruzada |
| R6 | Dependencia del inventario externo | Baja | Medio | Doble de prueba (mock) |

## 6. Mantenimiento
El plan se actualiza al cerrar cada historia y cuando cambie el backlog. Los defectos se registran en `docs/REGISTRO_DEFECTOS.md` con ID, descripción, pasos, severidad y estado.
