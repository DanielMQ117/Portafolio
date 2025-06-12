"""Crear una versión invertida del triángulo."""

altura = int(input("\n -> Ingrese la altura del triángulo: "))
print("")

for i in range(altura, 0, -1):
    print("*" * i)
