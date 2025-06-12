"""Iterando sobre listas y cadenas: convertir una lista de números
en una lista con sus cuadrados."""

numeros = [1, 2, 3, 4, 5]

cuadrados = []

for numero in numeros:
    cuadrados.append(numero ** 2)

# Imprimir la lista de cuadrados
print("Cuadrados:", cuadrados)
