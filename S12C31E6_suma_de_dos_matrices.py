"""Desafío final: desarrollar un programa que calcule la suma de dos matrices
numéricas representadas como listas de listas. Se debe solicitar por teclado las
dimensiones de las matrices, así como sus elementos."""

print("\nLas filas y columnas deben ser mayor a cero '0'.\n")
filas = int(input("Ingrese el numero de filas: ").strip())
columnas = int(input("Ingrese el numero de columnas: ").strip())


def llenar_matriz_con_ceros(filas, columnas) -> list[list[int]]:
    return [[0 for _ in range(columnas)] for _ in range(filas)]


def llenar_matriz(nombre: str, matriz: list):
    filas, columnas = obtener_dimensiones_matriz(matriz)
    print(f"\nMatriz: {nombre}")
    for i in range(filas):
        print("")
        for j in range(columnas):
            num = input(f"Fila {i+1}, Columna {j+1}: ").strip()
            valor = int(num if num.isdigit() else 0)
            matriz[i][j] = valor


def obtener_dimensiones_matriz(matriz: list[list[int]]) -> tuple[int, int]:
    filas = len(matriz)
    columnas = len(matriz[0])

    return filas, columnas


def sumar_matrices(matriz1: list, matriz2: list) -> list[list[int]]:
    filas, columnas = obtener_dimensiones_matriz(matriz1)
    resultado = llenar_matriz_con_ceros(filas, columnas)
    for i in range(filas):
        for j in range(columnas):
            resultado[i][j] = matriz1[i][j] + matriz2[i][j]

    return resultado


A = llenar_matriz_con_ceros(filas, columnas)
B = llenar_matriz_con_ceros(filas, columnas)

llenar_matriz("A", A)
llenar_matriz("B", B)


print("\nMatriz A:")
for fila in A:
    print(fila)

print("\nMatriz B:")
for fila in B:
    print(fila)

C = sumar_matrices(A, B)

print("\nResultado de la suma de matrices A y B:")
for fila in C:
    print(fila)
