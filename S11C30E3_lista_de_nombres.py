"""Ejercicio práctico:

-> Crear una lista con nombres de 5 amigos.
-> Agregar un nuevo amigo a la lista.
-> Eliminar el segundo amigo de la lista.
-> Imprimir la lista final."""

amigos = ["Alice", "Emilio", "Juan", "David", "Jose"]

while True:
    print("")
    print(" Menú de opciones ".center(40, "*"), end="\n\n")
    print("1. Agregar nuevo amigo")
    print("2. Eliminar un amigo")
    print("3. Mostrar lista de amigos")
    print("4. Salir\n")

    opcion = input(" -> Seleccione una opción: ")
    print("")

    if opcion == "1":
        print(" Agregar nuevo amigo ".center(40, "*"), end="\n\n")
        nuevo_amigo = input("Ingrese el nombre del amigo: ").strip()
        nuevo_amigo = nuevo_amigo.title()
        amigos.append(nuevo_amigo)
        print(f"\nAmigo '{nuevo_amigo}' agregado exitosamente.")

    elif opcion == "2":
        print(" Eliminar un amigo ".center(40, "*"), end="\n\n")
        nombre_amigo = input("Ingrese el nombre del amigo: ").strip()
        nombre_amigo = nombre_amigo.title()

        if nombre_amigo in amigos:
            amigos.remove(nombre_amigo)
            print(f"\nAmigo '{nombre_amigo}' eliminado.")
        else:
            print(f"\nAmigo '{nombre_amigo}' no encontrado.")

    elif opcion == "3":
        print(" Lista final de amigos ".center(40, "*"), end="\n\n")
        for i, amigo in enumerate(amigos):
            print(f"{i + 1}. {amigo}")

    elif opcion == "4":
        print("\n Saliendo del programa!\n")
        break

    else:
        print("Opción no válida, por favor intente nuevamente.")
