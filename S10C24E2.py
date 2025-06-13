"""Los estudiantes deben hacer un programa
que pida al usuario una cantidad de dinero en córdobas. Luego este debe
imprimir el valor de esa cantidad en dólares."""

if __name__ == '__main__':
    c = float(input("Ingrese la cantidad de dinero en córdobas: "))
    d = c / 36.5
    print("-------------------------------------")
    print("Cantidad en dólares: ", d, "dólares.")
    print("-------------------------------------")
