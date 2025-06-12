"""Mini-Proyecto. Contador de vocales: pedir a los estudiantes que escriban un
programa que cuente cuántas vocales hay en una palabra ingresada por el
usuario y el número de caracteres que tiene."""

palabra = input("\nIngresa una palabra: ")

contador_vocales = 0

# Recorrer la palabra y contar vocales
for letra in palabra:
    if letra.lower() in "aeiou":
        contador_vocales += 1

# Mostrar resultados
print("\nNúmero de caracteres:", len(palabra))
print("Número de vocales:", contador_vocales)
