# Crear listas

tareas = ["estudiar", "ejercicio", "programar", "descansar"]

# Acceder a elementos

primera = tareas[0]
ultima = tareas[-1]
penultima = tareas[-2]

print(primera)
print(ultima)
print(penultima)

# Operaciones básicas

print(len(tareas))
print("programar" in tareas)
print(tareas.count("ejercicio"))
print(tareas.index("programar"))

# Agregar elementos

tareas.append("leer")
print(tareas)

# Modificar elementos

tareas[1] = "caminar"
print(tareas)

# Eliminar elementos

tareas.remove("descansar")
print(tareas)

# Recorrer la lista

for tarea in tareas:
    print(tarea)