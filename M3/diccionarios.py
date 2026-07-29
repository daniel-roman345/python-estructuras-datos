# Crear diccionarios

contactos = {
    "Ana": "612345678",
    "Carlos": "698765432"
}

print(contactos["Ana"])
print(contactos.get("Elena", "No encontrado"))

# Claves válidas

valido = {
    "nombre": "Juan",
    42: "respuesta",
    (1, 2): "coord"
}

# Claves inválidas

try:
    invalido = {
        [1, 2]: "x"
    }
except TypeError as e:
    print(f"Error: {e}")

# Crear diccionarios de diferentes formas

colores = dict(
    rojo="#FF0000",
    verde="#00FF00",
    azul="#0000FF"
)

claves = ["nombre", "edad", "ciudad"]
valores = ["Ana", 28, "Madrid"]

persona = {k: v for k, v in zip(claves, valores)}

print(persona)

# Diccionario anidado

usuario = {
    "nombre": "Miguel",
    "edad": 30,
    "direccion": {
        "calle": "Calle Mayor",
        "ciudad": "Madrid"
    }
}

ciudad = usuario["direccion"]["ciudad"]
print(ciudad)

# Métodos

califs = {
    "Mates": 85,
    "Historia": 72
}

califs.update({
    "Inglés": 88,
    "Mates": 87,
    "Arte": 95
})

print(califs)

vendido = califs.pop("Inglés")
print(vendido)

par_final = califs.popitem()
print(par_final)

contador = {}

contador.setdefault("hola", 0)
contador["hola"] += 1

print(contador)

materias = ["Mates", "Historia", "Arte"]

notas = dict.fromkeys(materias, 0)

print(notas)

d1 = {
    "nombre": "Carlos",
    "edad": 28
}

d2 = {
    "email": "c@e.com"
}

unido = d1 | d2

print(unido)

# Recorrer diccionarios

califs = {
    "Mates": 85,
    "Historia": 72,
    "Ciencias": 90
}

for asig, nota in califs.items():
    print(f"{asig}: {nota}")

for asig in sorted(califs):
    print(f"{asig}: {califs[asig]}")

# Eliminar mientras se recorre

d = {
    "a": 1,
    "b": 2,
    "c": 3
}

for k in list(d.keys()):
    if k == "b":
        del d[k]

print(d)

# Comprensiones

precios = {
    "laptop": 899,
    "tablet": 349
}

rebaja = {
    p: round(v * 0.9, 2)
    for p, v in precios.items()
}

print(rebaja)

stock = {
    "manzanas": 10,
    "peras": 0,
    "naranjas": 25
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

gran_total = sum(precios.values())

pct = {
    p: round(v / gran_total * 100, 1)
    for p, v in precios.items()
}

print(pct)