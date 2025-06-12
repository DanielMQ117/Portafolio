""" Realiza un programa para calcular e imprimir el perímetro y área
de un trapecio una vez que se hayan leído los datos necesarios."""

if __name__ == '__main__':
    basemayor = float(input("Introduce la base mayor (B): "))
    basemenor = float(input("Introduce la base menor (b): "))
    lado1 = float(input("Introduce el primer lado (lado1): "))
    lado2 = float(input("Introduce el segundo lado (lado2): "))
    altura = float(input("Introduce la altura (h): "))

    if basemenor > basemayor:
        print(" Intercambiando bases: la base menor era mayor que la mayor ??")
        temp = basemayor
        basemayor = basemenor
        basemenor = temp

    perimetro = basemayor + basemenor + lado1 + lado2
    area = ((basemayor + basemenor)/2) * altura
    print("-"*35)
    print("Perímetro del trapecio: ", perimetro)
    print("Área del trapecio: ", area)
    print("-"*35)
