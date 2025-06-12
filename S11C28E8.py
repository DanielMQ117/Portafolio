"""Mini-Proyecto. Tablas de multiplicar con diccionarios: Generar y mostrar una
tabla de multiplicar en un diccionario:

-> Pedir al usuario que ingrese un número.
-> Usar un diccionario para almacenar los resultados de la tabla de multiplicar del 1 al 10.
-> Recorrer el diccionario con for y mostrar la tabla."""

numero = int(input("Ingresa un número para ver su tabla de multiplicar: "))

tabla = {}

for i in range(1, 11):
    tabla[i] = numero * i

print(f"\nTabla de multiplicar del {numero}:\n")
for i in tabla:
    print(f" {numero} x {i} = {tabla[i]}")
