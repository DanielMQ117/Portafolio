""". Conversión de temperatura. Convertir
grados Celsius a Fahrenheit con la fórmula: F = (C × 9/5) + 32."""

if __name__ == '__main__':
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = (celsius*9/5)+32
    print("")
    print("=" * 35)
    print(celsius, "°C equivalen a ", fahrenheit, "°F")
