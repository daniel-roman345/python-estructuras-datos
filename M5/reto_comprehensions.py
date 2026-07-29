# Dataset

ventas = [
    {"producto": "Laptop", "categoria": "Tecnología", "unidades": 20, "precio": 800},
    {"producto": "Teclado", "categoria": "Tecnología", "unidades": 50, "precio": 25},
    {"producto": "Mouse", "categoria": "Tecnología", "unidades": 30, "precio": 15},
    {"producto": "Monitor", "categoria": "Tecnología", "unidades": 10, "precio": 200},
    {"producto": "Silla", "categoria": "Muebles", "unidades": 8, "precio": 120}
]

# 1. Valor total por producto

valor_total = [
    i["unidades"] * i["precio"]
    for i in ventas
]

print("Valor total por producto:")
print(valor_total)

# 2. Productos con valor mayor a 1000

productos_valiosos = [
    i["producto"]
    for i in ventas
    if i["unidades"] * i["precio"] > 1000
]

print("\nProductos de alto valor:")
print(productos_valiosos)

# 3. Producto -> información

producto_info = {
    i["producto"]: {
        "valor": i["unidades"] * i["precio"],
        "unidades": i["unidades"]
    }
    for i in ventas
}

print("\nInformación de productos:")
print(producto_info)

# 4. Ranking premium

ranking_premium = {
    i["producto"]: i["unidades"] * i["precio"]
    for i in sorted(
        ventas,
        key=lambda x: x["unidades"] * x["precio"],
        reverse=True
    )
    if i["precio"] > 50
}

print("\nRanking premium:")
print(ranking_premium)

# 5. Categorías y productos baratos

categorias_unicas = {
    i["categoria"]
    for i in ventas
}

productos_baratos = {
    i["producto"]
    for i in ventas
    if i["precio"] <= 50
}

print("\nCategorías:")
print(categorias_unicas)

print("\nProductos baratos:")
print(productos_baratos)

# 6. Resumen y total

resumen_formateado = [
    f'{i["producto"]}: ${i["unidades"] * i["precio"]}'
    for i in ventas
]

gran_total = sum(valor_total)

print("\nResumen:")

for dato in resumen_formateado:
    print(dato)

print("\nGran total:", gran_total)