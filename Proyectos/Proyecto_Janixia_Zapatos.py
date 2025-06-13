if __name__ == '__main__':
    talla = float()
    cantidad = float()
    precio = float()
    total = float()
    total_general = float()
    color = str()
    opcion = str()
    i = int()
    total_general = 0
    i = 1

    while True:  # no hay 'repetir' en python
        print("")
        print("Venta ", i)
        print("Ingrese la talla del zapato:")
        talla = float(input())

        # Asignar precio según talla
        if talla >= 20 and talla <= 29:
            precio = 400
        else:
            if talla >= 30 and talla <= 36:
                precio = 550
            else:
                if talla >= 37 and talla <= 42:
                    precio = 700
                else:
                    print("Talla no disponible. Solo se aceptan tallas del 20 al 42.")

        print("Ingrese el color del zapato:")
        color = input()
        print("Ingrese la cantidad de pares comprados:")

        cantidad = float(input())
        total = cantidad * precio
        total_general = total_general + total

        print("Venta ", i)
        print(": Talla ", talla)
        print(", Color ", color)
        print(", Cantidad ", cantidad)
        print("Precio por par: C$", precio, ", Total: C$", total)
        print("¿Desea registrar otra venta? (s/n):")
        opcion = input()
        i = i+1

        if opcion != "s" and opcion != "S":
            break

    print("")
    print("Total a pagar: C$", total_general, "cordobas")
