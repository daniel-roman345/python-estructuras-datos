# Análisis de ventas por región

ventas_por_region = {
    "Norte": {
        "Q1": 12000,
        "Q2": 15000,
        "Q3": 14000,
        "Q4": 18000
    },
    "Sur": {
        "Q1": 10000,
        "Q2": 11000,
        "Q3": 13000,
        "Q4": 15000
    },
    "Centro": {
        "Q1": 17000,
        "Q2": 16000,
        "Q3": 18000,
        "Q4": 20000
    }
}

# Total anual por región

totales = {}

for region, ventas in ventas_por_region.items():
    totales[region] = sum(ventas.values())

print("Total anual por región")

for region, total in totales.items():
    print(region, ":", total)

# Región con mayores ventas

mayor = max(totales, key=lambda r: totales[r])

print("\nRegión con mayores ventas:")
print(mayor, "-", totales[mayor])

# Acumular ventas por trimestre

trimestres = {
    "Q1": 0,
    "Q2": 0,
    "Q3": 0,
    "Q4": 0
}

for ventas in ventas_por_region.values():
    for trimestre, valor in ventas.items():
        trimestres[trimestre] += valor

print("\nVentas por trimestre")

for trimestre, total in trimestres.items():
    print(trimestre, ":", total)

# Porcentajes

gran_total = sum(totales.values())

porcentajes = {
    region: round(total / gran_total * 100, 2)
    for region, total in totales.items()
}

print("\nPorcentaje por región")

for region, porcentaje in porcentajes.items():
    print(region, ":", porcentaje, "%")

# Reporte ordenado

print("\nReporte final")

for region, total in sorted(
    totales.items(),
    key=lambda x: x[1],
    reverse=True
):
    print(region, "-", total, "-", porcentajes[region], "%")