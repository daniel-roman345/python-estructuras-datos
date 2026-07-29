# List Comprehension

cuadrados = [n ** 2 for n in range(10)]

print(cuadrados)

pares = [n for n in range(10) if n % 2 == 0]

print(pares)

celsius = [0, 10, 20, 30, 40]

fahr = [(9 / 5) * t + 32 for t in celsius]

print(fahr)

usuarios = [
    {"nombre": "Ana", "edad": 28},
    {"nombre": "Carlos", "edad": 35}
]

nombres = [u["nombre"] for u in usuarios]

print(nombres)

# Dict Comprehension

cuadrados = {n: n ** 2 for n in range(5)}

print(cuadrados)

stock = {
    "manzanas": 10,
    "platanos": 3,
    "naranjas": 25,
    "peras": 0
}

disponibles = {
    f: c
    for f, c in stock.items()
    if c > 0
}

print(disponibles)

original = {
    "a": 1,
    "b": 2,
    "c": 3
}

invertido = {
    v: k
    for k, v in original.items()
}

print(invertido)

estudiantes = [
    {"id": 1, "nombre": "Ana"},
    {"id": 2, "nombre": "Carlos"}
]

id_nombre = {
    e["id"]: e["nombre"]
    for e in estudiantes
}

print(id_nombre)

# Set Comprehension

numeros = [1, 2, 2, 3, 4, 3, 5, 5, 1]

unicos = {n for n in numeros}

print(unicos)

palabras = [
    "manzana",
    "banana",
    "mango",
    "mora",
    "naranja"
]

iniciales = {
    p[0]
    for p in palabras
}

print(iniciales)

texto = "python es un lenguaje versátil"

vocales = {
    l
    for l in texto.lower()
    if l in "aeiou"
}

print(vocales)

pares_cuad = {
    n ** 2
    for n in range(10)
    if n % 2 == 0
}

print(pares_cuad)

# Ejemplo de ventas

ventas = [
    {"producto": "laptop", "unidades": 20, "precio": 800},
    {"producto": "teclado", "unidades": 50, "precio": 25},
    {"producto": "mouse", "unidades": 30, "precio": 15},
    {"producto": "monitor", "unidades": 10, "precio": 200}
]

valor_por_producto = [
    i["unidades"] * i["precio"]
    for i in ventas
]

print(valor_por_producto)

alto_valor = [
    i["producto"]
    for i in ventas
    if i["unidades"] * i["precio"] > 1000
]

print(alto_valor)

resumen = {
    i["producto"]: i["unidades"] * i["precio"]
    for i in ventas
}

print(resumen)

gran_total = sum(valor_por_producto)

print(gran_total)

# Generador

gen = (n ** 2 for n in range(1000000))

print(next(gen))