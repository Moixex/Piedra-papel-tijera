import random  # Se importa random para que la computadora elija al azar

# Función que muestra un mensaje de bienvenida al iniciar el juego
def mostrar_introduccion():
    print("======================================")
    print(" Juego: Piedra, Papel o Tijera ")
    print(" Simulación de decisiones automatizadas")
    print(" Impacto de la tecnología en el entretenimiento")
    print("======================================")

# Función que pide al usuario su elección
def obtener_jugada_usuario():
    # Se convierte a minúsculas para evitar errores al escribir
    return input("\nElige piedra, papel o tijera (o escribe 'salir'): ").lower()

# Función que genera la jugada de la computadora
def obtener_jugada_computadora(opciones):
    # La computadora elige una opción de forma aleatoria
    return random.choice(opciones)

# Función que decide quién gana
def determinar_ganador(usuario, computadora):
    # Si ambos eligen lo mismo, es empate
    if usuario == computadora:
        return "Empate"
    # Condiciones donde el usuario gana
    elif (usuario == "piedra" and computadora == "tijera") or \
         (usuario == "tijera" and computadora == "papel") or \
         (usuario == "papel" and computadora == "piedra"):
        return "¡Ganaste!"
    # En cualquier otro caso, gana la computadora
    else:
        return "Perdiste"

# Función principal que controla el flujo del juego
def iniciar_juego():
    # Lista con las opciones válidas del juego
    opciones = ["piedra", "papel", "tijera"]
    
    # Se muestra la introducción del juego
    mostrar_introduccion()

    # El juego se repite hasta que el usuario decida salir
    while True:
        usuario = obtener_jugada_usuario()

        # Opción para terminar el juego
        if usuario == "salir":
            print("\nGracias por jugar. La tecnología también sabe cuándo detenerse.")
            break

        # Validación de la entrada del usuario
        if usuario not in opciones:
            print("Entrada no válida. Intenta de nuevo.")
            continue

        # La computadora realiza su jugada
        computadora = obtener_jugada_computadora(opciones)

        # Se muestran las elecciones
        print("Tú elegiste:", usuario)
        print("La computadora eligió:", computadora)

        # Se determina y muestra el resultado
        resultado = determinar_ganador(usuario, computadora)
        print("Resultado:", resultado)

# Llamada a la función principal para iniciar el programa
iniciar_juego()
