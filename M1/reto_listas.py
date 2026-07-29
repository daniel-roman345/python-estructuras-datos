# Gestión de inventario

inventario = [
    ["Laptop", 10, 3500],
    ["Mouse", 25, 80],
    ["Teclado", 15, 150]
]

# Actualizar precio

def actualizar_precio(nombre, nuevo_precio):

    for producto in inventario:
        if producto[0] == nombre:
            producto[2] = nuevo_precio

# Registrar venta

def registrar_venta(nombre, cantidad):

    for producto in inventario:
        if producto[0] == nombre:

            if producto[1] >= cantidad:
                producto[1] = producto[1] - cantidad
            else:
                print("Stock insuficiente")

# Añadir producto

def añadir_producto(nombre, cantidad, precio):

    for producto in inventario:
        if producto[0] == nombre:
            producto[1] = producto[1] + cantidad
            return

    inventario.append([nombre, cantidad, precio])

# Mostrar inventario

def mostrar_inventario():

    print("\nInventario")

    for producto in inventario:
        print(
            "Producto:", producto[0],
            "| Cantidad:", producto[1],
            "| Precio:", producto[2]
        )

# Pruebas

actualizar_precio("Mouse", 90)

registrar_venta("Laptop", 2)

añadir_producto("Monitor", 8, 900)

añadir_producto("Mouse", 5, 90)

mostrar_inventario()
