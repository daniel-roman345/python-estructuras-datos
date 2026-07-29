# Tiendas

tienda_centro = {"Laptop", "Mouse", "Teclado", "Monitor"}
tienda_norte = {"Mouse", "Monitor", "Impresora"}
tienda_sur = {"Laptop", "Parlantes", "Monitor"}

# Catálogo completo

catalogo_completo = tienda_centro.union(tienda_norte).union(tienda_sur)

print("Catálogo completo:")
print(catalogo_completo)

# Productos comunes

productos_comunes = tienda_centro.intersection(tienda_norte).intersection(tienda_sur)

print("\nProductos comunes:")
print(productos_comunes)

# Productos exclusivos

print("\nExclusivos centro:")
print(tienda_centro.difference(tienda_norte))

print("\nExclusivos norte:")
print(tienda_norte.difference(tienda_sur))

print("\nExclusivos sur:")
print(tienda_sur.difference(tienda_centro))

# Solapamiento

print("\nCentro y Norte sin productos iguales:")
print(tienda_centro.isdisjoint(tienda_norte))

# Usuarios

usuario1 = {"Acción", "Comedia", "Aventura"}
usuario2 = {"Comedia", "Drama", "Romance"}
usuario3 = {"Acción", "Aventura", "Ciencia ficción"}

print("\nGéneros comunes:")
print(usuario1 & usuario3)

print("\nTodos los géneros:")
print(usuario1 | usuario2)

print("\nSolo usuario 1:")
print(usuario1 - usuario2)

print("\nDiferencias usuario 2 y usuario 3:")
print(usuario2 ^ usuario3)

print("\n¿Usuario 3 es subconjunto del usuario 1?")
print(usuario3 <= usuario1)

print("\nResumen")

print("Catálogo completo:", catalogo_completo)
print("Productos comunes:", productos_comunes)
print("Géneros comunes:", usuario1 & usuario3)
print("Todos los géneros:", usuario1 | usuario2)