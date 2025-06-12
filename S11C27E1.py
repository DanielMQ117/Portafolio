"""Adivina el número. Implementar un juego donde el usuario debe
adivinar un número secreto entre 1 y 10. El programa debe continuar hasta
que el usuario acierte."""

import random
secreto = random.randint(1, 10)
adivinanza = 0  # Variable inicial

while adivinanza != secreto:
    adivinanza = int(input("Adivina el número (1-10): "))
    if adivinanza < secreto:
        print("Es un número mayor.")
    elif adivinanza > secreto:
        print("Es un número menor.")

print("¡Felicidades! Adivinaste el número.")
