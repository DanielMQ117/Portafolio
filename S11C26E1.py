""" Determinar si un número es par o impar con if-else."""

# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número entero: "))

# Verificar si el número es par o impar
if numero % 2 == 0:
    print(f"El número {numero} es PAR.")
else:
    print(f"El número {numero} es IMPAR.")
