# Estructuras de datos en Python

Actividad práctica que recorre las principales estructuras de datos de Python (listas, tuplas, diccionarios, conjuntos y comprehensions) mediante ejemplos guiados y un reto por módulo.

## Contenido del repositorio

El proyecto está organizado en cinco módulos, cada uno con un archivo de teoría/ejemplos y un archivo con el reto resuelto.

| Módulo | Tema | Ejemplos | Reto |
| ------ | ---- | -------- | ---- |
| M1 | Listas | [`M1/listas.py`](M1/listas.py) | [`M1/reto_listas.py`](M1/reto_listas.py) |
| M2 | Tuplas | [`M2/tuplas.py`](M2/tuplas.py) | [`M2/reto_tuplas.py`](M2/reto_tuplas.py) |
| M3 | Diccionarios | [`M3/diccionarios.py`](M3/diccionarios.py) | [`M3/reto_diccionarios.py`](M3/reto_diccionarios.py) |
| M4 | Conjuntos | [`M4/conjuntos.py`](M4/conjuntos.py) | [`M4/reto_conjuntos.py`](M4/reto_conjuntos.py) |
| M5 | Comprehensions | [`M5/comprehensions.py`](M5/comprehensions.py) | [`M5/reto_comprehensions.py`](M5/reto_comprehensions.py) |

## Cómo ejecutar los retos

Requisitos: Python 3.8 o superior.

Desde la raíz del repositorio se puede ejecutar cualquiera de los retos con:

```bash
python M1/reto_listas.py
python M2/reto_tuplas.py
python M3/reto_diccionarios.py
python M4/reto_conjuntos.py
python M5/reto_comprehensions.py
```

## Descripción de los retos

### M1 · Listas — Gestión de inventario
Se modela un inventario como una lista de listas, donde cada producto guarda su nombre, cantidad y precio. Incluye funciones para actualizar el precio, registrar ventas (con validación de stock), añadir nuevos productos (o sumar cantidad si ya existe) y mostrar el inventario completo.

### M2 · Tuplas — Catálogo de películas
Se construye un catálogo inmutable con tuplas de películas y se practica el desempaquetado con `*resto`, la búsqueda por director y el cálculo de estadísticas (mínima, máxima y promedio de puntuaciones) devolviendo múltiples valores en una tupla.

### M3 · Diccionarios — Análisis de ventas por región
Se trabaja con un diccionario anidado de ventas trimestrales por región. Se calculan totales anuales, se identifica la región con mayores ventas usando `max` con `key`, se acumulan las ventas por trimestre, se obtienen los porcentajes con un dict comprehension y se genera un reporte ordenado.

### M4 · Conjuntos — Catálogo de tiendas y géneros de usuarios
Se aplican operaciones de conjuntos (`union`, `intersection`, `difference`, `isdisjoint`) para consolidar el catálogo entre varias tiendas y detectar productos comunes y exclusivos. También se usan los operadores `&`, `|`, `-`, `^` y `<=` para comparar los géneros favoritos de tres usuarios.

### M5 · Comprehensions — Análisis de ventas
Se procesa una lista de diccionarios de ventas usando list, dict y set comprehensions: valor total por producto, filtrado de productos valiosos, ranking premium ordenado, categorías únicas, productos baratos y un resumen formateado con el gran total.

## Capturas de ejecución

Se incluyen capturas de la ejecución de los cinco retos.

### M1 · Listas
![Reto listas 1](Captura%20de%20pantalla%202026-07-28%20195958.png)
![Reto listas 2](Captura%20de%20pantalla%202026-07-28%20200010.png)

### M2 · Tuplas
![Reto tuplas 1](Captura%20de%20pantalla%202026-07-28%20200030.png)
![Reto tuplas 2](Captura%20de%20pantalla%202026-07-28%20200040.png)

### M3 · Diccionarios
![Reto diccionarios 1](Captura%20de%20pantalla%202026-07-28%20200049.png)
![Reto diccionarios 2](Captura%20de%20pantalla%202026-07-28%20200058.png)

### M4 · Conjuntos
![Reto conjuntos 1](Captura%20de%20pantalla%202026-07-28%20200107.png)
![Reto conjuntos 2](Captura%20de%20pantalla%202026-07-28%20200117.png)

### M5 · Comprehensions
![Reto comprehensions 1](Captura%20de%20pantalla%202026-07-28%20200126.png)
![Reto comprehensions 2](Captura%20de%20pantalla%202026-07-28%20200134.png)

## Autor

Daniel Roman
