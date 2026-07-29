# Catálogo de películas

catalogo = (
    ("Interestelar", "Christopher Nolan", 2014, 8.7),
    ("Avatar", "James Cameron", 2009, 7.9),
    ("Titanic", "James Cameron", 1997, 7.8),
    ("El Padrino", "Francis Ford Coppola", 1972, 9.2)
)

# Mostrar películas

print("CATÁLOGO")

for titulo, director, anio, puntuacion in catalogo:
    print(f"{titulo} - {director} - {anio} - {puntuacion}")

# Primera película y resto

primera, *resto = catalogo

print("\nPrimera película:")
print(primera)

print("\nResto:")

for pelicula in resto:
    print(pelicula)

# Buscar por director

def buscar_por_director(director):

    coincidencias = ()

    for pelicula in catalogo:
        if pelicula[1] == director:
            coincidencias += (pelicula,)

    return coincidencias

print("\nPelículas de James Cameron")

resultado = buscar_por_director("James Cameron")

for pelicula in resultado:
    print(pelicula)

# Estadísticas

def obtener_estadisticas():

    puntuaciones = ()

    for pelicula in catalogo:
        puntuaciones += (pelicula[3],)

    return (
        min(puntuaciones),
        max(puntuaciones),
        sum(puntuaciones) / len(puntuaciones)
    )

minima, maxima, promedio = obtener_estadisticas()

print("\nEstadísticas")

print("Mínima:", minima)
print("Máxima:", maxima)
print("Promedio:", round(promedio,2))