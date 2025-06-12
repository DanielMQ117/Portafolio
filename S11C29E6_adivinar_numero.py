"""Mini-Proyecto: Juego de Adivinanza con while Anidado. Requisitos:

• Crear un juego donde el usuario debe adivinar un número entre 1 y 5 en 3 intentos.
• Si adivina, el juego pregunta si quiere jugar otra vez.
• Si falla, le dice el número correcto y ofrece reiniciar el juego."""


import random


def pedir_adivinanza(intentos) -> int:
    """Solicita al usuario una adivinanza válida."""
    while True:
        try:
            adivinanza = int(
                input(f"Tienes {intentos} intentos. Ingresa tu número: "))
            if 1 <= adivinanza <= 5:
                return adivinanza
            print("\n ❗ Por favor, ingresa un número entre 1 y 5.\n")
        except ValueError:
            print("\n 🚫 Entrada inválida. Por favor, ingresa un número entero.\n")


def jugar_una_vez():
    """Ejecuta una ronda del juego de adivinanza."""
    intentos = 3
    numero_secreto = random.randint(1, 5)
    while intentos > 0:
        adivinanza = pedir_adivinanza(intentos)
        if adivinanza == numero_secreto:
            print("\n ✅ ¡Felicidades! Adivinaste el número.\n")
            return True
        else:
            intentos -= 1
            print("\n ❌ Incorrecto.\n")
    print(
        f"Lo siento, no te quedan intentos. El número era {numero_secreto}.\n")
    return False


def adivinar_numero():
    """Función principal del juego de adivinanza."""
    print("\n¡Bienvenido al juego de adivinanza!")
    print("Adivina un número entre 1 y 5. Tienes 3 intentos.")
    while True:
        jugar_una_vez()
        jugar_otra_vez = input(
            "\n -> ¿Quieres jugar otra vez? (s/n): ").strip().lower()
        if jugar_otra_vez != 's':
            print("\nGracias por jugar. ¡Hasta luego!")
            break


# Llamada a la función principal para iniciar el juego
adivinar_numero()
