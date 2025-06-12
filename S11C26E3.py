"""Mostrar el mes correspondiente según un número con matchcase."""

if __name__ == '__main__':
    numero = int()
    while True:  # no hay 'repetir' en python
        print("Ingrese un número del 1 al 12 para saber el mes correspondiente: ")
        numero = int(input())
        if numero == 1:
            print("Enero")
        elif numero == 2:
            print("Febrero")
        elif numero == 3:
            print("Marzo")
        elif numero == 4:
            print("Abril")
        elif numero == 5:
            print("Mayo")
        elif numero == 6:
            print("Junio")
        elif numero == 7:
            print("Julio")
        elif numero == 8:
            print("Agosto")
        elif numero == 9:
            print("Septiembre")
        elif numero == 10:
            print("Octubre")
        elif numero == 11:
            print("Noviembre")
        elif numero == 12:
            print("Diciembre")
        else:
            print("Número no válido. Intente nuevamente.")
        if numero >= 1 and numero <= 12:
            break
