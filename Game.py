import random

print("=== Juego: Piedra, Papel o Tijera ===")

# Lista de opciones permitidas
opciones = ["piedra", "papel", "tijera"]

# Bucle repetitivo: el juego continúa hasta que el usuario decida salir
while True:
    # Solicitar jugada al usuario
    usuario = input("\nElige piedra, papel o tijera (o escribe 'salir'): ").lower()

    # Punto lógico: condición de salida del juego
    if usuario == "salir":
        print("Saliendo del juego...")
        break  # rompe el bucle

    # Validar entrada del usuario
    if usuario not in opciones:
        print("Entrada no válida. Intenta de nuevo.")
        continue  # vuelve al inicio del while

    # La computadora elige aleatoriamente
    computadora = random.choice(opciones)

    print("Tú elegiste:", usuario)
    print("La computadora eligió:", computadora)

    # --- LÓGICA DEL GANADOR ---
    # Esta estructura compara todas las posibilidades.
    # Usamos condiciones compuestas para determinar qué opción vence a cuál.
    if usuario == computadora:
        print("Resultado: Empate")
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "tijera" and computadora == "papel") or \
         (usuario == "papel" and computadora == "piedra"):
        print("Resultado: ¡Ganaste!")
    else:
        print("Resultado: Perdiste")

print("Juego finalizado.")
