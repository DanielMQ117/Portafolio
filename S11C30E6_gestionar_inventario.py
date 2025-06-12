"""Desafío final: crear un programa en Python que gestione un inventario de
productos utilizando listas y diccionarios. Requisitos:

-> Crear una lista de diccionarios donde cada diccionario represente un producto con "nombre", "precio" y "stock".
-> Permitir agregar nuevos productos, solicitando los datos por teclado.
-> Permitir actualizar el stock de un producto, solicitando al usuario el nombre del producto a actualizar.
-> Mostrar la lista de productos actualizada.
-> Las opciones anteriores deben poder ser seleccionadas a través de un menú de opciones."""

# Inventatorio inicial
inventario = [
    {"nombre": "Laptop", "precio": 800, "stock": 5},
    {"nombre": "Mouse", "precio": 20, "stock": 50},
]


while True:
    print("")
    print(" Menú de opciones ".center(40, "*"), end="\n\n")
    print("1. Agregar nuevo producto")
    print("2. Actualizar stock de un producto")
    print("3. Mostrar inventario")
    print("4. Salir\n")

    opcion = input(" -> Seleccione una opción: ")
    print("")

    if opcion == "1":
        print(" Agregar nuevo producto ".center(40, "*"), end="\n\n")
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))
        inventario.append({"nombre": nombre, "precio": precio, "stock": stock})
        print(f"\nProducto '{nombre}' agregado exitosamente.")

    elif opcion == "2":
        print(" Actualizar stock de un producto ".center(40, "*"), end="\n\n")
        nombre_producto = input(
            "Ingrese el nombre del producto a actualizar: ")
        for producto in inventario:
            if producto["nombre"].lower() == nombre_producto.lower():
                nuevo_stock = int(
                    input(f"Ingrese el nuevo stock para '{nombre_producto}': "))
                producto["stock"] = nuevo_stock
                print(
                    f"\nStock de '{nombre_producto}' actualizado a {nuevo_stock}.")
                break
        else:
            print(f"\nProducto '{nombre_producto}' no encontrado.")

    elif opcion == "3":
        print(" Inventario de actual productos ".center(40, "*"), end="\n\n")
        for i, producto in enumerate(inventario):
            item = list(producto.values())
            print(f"{i+1}) {item[0]} Precio: {item[1]}$ - Stock: {item[2]}")

    elif opcion == "4":
        print("\n Saliendo del programa!\n")
        break

    else:
        print("Opción no válida, por favor intente nuevamente.")
