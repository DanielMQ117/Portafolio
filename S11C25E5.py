"""Explicación del concepto de Índice de Masa Corporal (IMC).
El índice de masa corporal (IMC) es una medida ampliamente utilizada en la
Medicina para evaluar la adecuación del peso corporal de una persona en
relación con su altura. Representa una fórmula sencilla: el peso del individuo
en kilogramos dividido por el cuadrado de su altura en metros (kg/m²). Esta
herramienta diagnóstica se emplea para identificar categorías de peso que
pueden llevar a problemas de salud.

Interpretación de los resultados del IMC
Los resultados obtenidos se clasifican en diferentes rangos, estableciendo
una relación directa con el nivel de riesgo para la salud. Los rangos definidos
por la Organización Mundial de la Salud (OMS) son los siguientes:

-> Bajo peso (menos de 18.5)
-> Normal (18.5-24.9)
-> Sobrepeso (25-29.9)
-> Obesidad (30 o más)."""

if __name__ == '__main__':
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))

    imc = peso / (altura ** 2)

    print("-------------------------------------")
    print(f"Su IMC es: {imc:.2f}")

    if imc < 18.5:
        print("Categoría: Bajo peso")
    elif 18.5 <= imc < 25:
        print("Categoría: Normal")
    elif 25 <= imc < 30:
        print("Categoría: Sobrepeso")
    else:
        print("Categoría: Obesidad")

    print("-------------------------------------")
