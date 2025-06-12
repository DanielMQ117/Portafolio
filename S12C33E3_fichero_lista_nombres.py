"""Ejercicio completo. Escriba un programa que realice lo siguiente:

-> Crear un archivo de texto que contenga una lista de nombres.
-> Leer el archivo y mostrar todos los nombres que contenga.
-> Añadir al archivo el nombre de una persona ingresado por el usuario.
-> Modificar el archivo para que todos los nombres sean en mayúsculas."""

import pickle


nombres = []


def save_data(datos):
    """Guarda los nombres en un archivo."""
    print("***** GUARDAR DATOS *****")
    with open('nombres.pkl', 'wb') as file:
        pickle.dump(datos, file)
    print("Datos guardados exitosamente!")


def load_data() -> list:
    """Carga los datos desde un archivo."""
    print("***** CARGAR DATOS *****")
    try:
        with open('nombres.pkl', 'rb') as file:
            datos = pickle.load(file)
            file.close()
        print("Datos cargados exitosamente!")
        return datos if len(datos) > 0 else []
    except FileNotFoundError:
        print("No se encontraron datos guardados!")
    except Exception as e:
        print(f" >> Error al cargar los datos: {e}")


while True:
    print("")
    print(" Menú de opciones ".center(40, "*"), end="\n\n")
    print("1. Agregar nombre.")
    print("2. Leer nombres.")
    print("3. Pasar a mayusculas.")
    print("4. Salir\n")

    opcion = input(" -> Seleccione una opción: ")
    print("")

    if opcion == "1":
        print(" Agregar nombre ".center(40, "*"), end="\n\n")
        nombre = input("Ingrese un nuevo nombre: ").strip()
        if nombre:
            nombres.append(nombre)
            save_data(nombres)
            print(f"Nombre '{nombre}' agregado exitosamente.")
        else:
            print("No se ingresó un nombre válido.")

    elif opcion == "2":
        print(" Leer nombres ".center(40, "*"), end="\n\n")
        nombres = load_data()
        if nombres:
            print("Lista de nombres:")
            for nombre in nombres:
                print(f"- {nombre}")
        else:
            print("No hay nombres para mostrar.")

    elif opcion == "3":
        print(" Pasar a mayúsculas ".center(40, "*"), end="\n\n")
        nombres = load_data()
        if nombres:
            nombres = [nombre.upper() for nombre in nombres]
            save_data(nombres)
            print("Todos los nombres han sido convertidos a mayúsculas.")
        else:
            print("No hay nombres para convertir.")

    elif opcion == "4":
        print("\n Saliendo del programa!\n")
        break

    else:
        print("Opción no válida, por favor intente nuevamente.")
