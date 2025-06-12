"""Calculadora básica. Solicitar dos números al
usuario y mostrar la suma, resta, multiplicación y división."""

if __name__ == '__main__':
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    suma = num1 + num2
    resta = num1 - num2
    producto = num1 * num2
    division = num1 / num2

    print("")
    print("===== Resultados =====")
    print(num1, " + ", num2, " = ", suma)
    print(num1, " - ", num2, " = ", resta)
    print(num1, " * ", num2, " = ", producto)
    print(num1, " / ", num2, " = ", division)
    print("======================")
