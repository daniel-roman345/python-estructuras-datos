# Tuplas inmutables

coordenadas = (10, 20)

try:
    coordenadas[0] = 15
except TypeError as e:
    print(f"Error: {e}")

# Contenido mutable dentro de una tupla

config = ("config_v1", [1, 2, 3])
config[1].append(4)
print(config)

# Tuplas como claves de diccionario

ubicaciones = {
    (40.7128, -74.0060): "Nueva York",
    (34.0522, -118.2437): "Los Ángeles"
}

print(ubicaciones[(40.7128, -74.0060)])

# Las listas no son hashables

try:
    d = {[40.71, -74.00]: "NY"}
except TypeError as e:
    print(f"Error: {e}")

# Crear tuplas

numeros = (1, 2, 3, 4, 5)
coords = 10, 20, 30
vacia = ()
singleton = (42,)

desde_lista = tuple([1, 2, 3])
desde_str = tuple("Python")
desde_rango = tuple(range(5))

print(type((42)))
print(type((42,)))

# Acceso a elementos

datos = ("Python", 3.9, 2023, "Tuplas")

print(datos[0])
print(datos[-1])

# Slicing

nums = (0,1,2,3,4,5,6,7,8,9)

print(nums[2:6])
print(nums[::2])
print(nums[::-1])

# count() e index()

t = (1,2,3,2,4,2,5)

print(t.count(2))
print(t.index(3))

# Desempaquetado

producto = ("Laptop XPS",1299.99,"Dell")

nombre, precio, fabricante = producto

print(nombre)
print(precio)

# Intercambio de variables

a = 5
b = 10

a, b = b, a

print(a, b)

# Operador *

numeros = (1,2,3,4,5)

primero, *resto = numeros
print(primero, resto)

primero, *medio, ultimo = numeros
print(primero, medio, ultimo)

*iniciales, ultimo = numeros
print(iniciales, ultimo)

# Ignorar valores

datos = ("Juan","Pérez",35,"Madrid","Ingeniero")

nombre, _, edad, _, profesion = datos

print(f"{nombre}, {edad}, {profesion}")

# Recorrer tuplas

estudiantes = [
    ("Ana",22,9.5),
    ("Carlos",20,8.7)
]

for nombre, edad, nota in estudiantes:
    print(f"{nombre}: {nota}")

# Retornar múltiples valores

def estadisticas(nums):
    return min(nums), max(nums), sum(nums)/len(nums)

minima, maxima, promedio = estadisticas([4,7,2,9,5])

print(f"min={minima}")
print(f"max={maxima}")
print(f"promedio={promedio:.2f}")