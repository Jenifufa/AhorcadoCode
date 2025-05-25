#!/usr/bin/env python3
"""
Juego del Ahorcado - Versión por Consola
"""

from src.JuegoAhorcado import JuegoAhorcado, Estado
from src.Letra import Letra

def mostrar_estado_juego(juego, num_letras=None):
    """Muestra el estado actual del juego"""
    print("\n" + "="*50)
    print("JUEGO DEL AHORCADO")
    print("="*50)
    
    # Mostrar palabra actual (con letras adivinadas)
    ocurrencias = juego.dar_ocurrencias()
    palabra_mostrar = " ".join(ocurrencias)
    print(f"Palabra: {palabra_mostrar}")
    
    # Mostrar cantidad de letras de manera discreta
    if num_letras:
        print(f"         ({num_letras} letras)")
    
    # Mostrar intentos disponibles
    print(f"Intentos restantes: {juego.dar_intentos_disponibles()}")
    
    # Mostrar letras jugadas
    jugadas = juego.dar_jugadas()
    if jugadas:
        letras_jugadas = [letra.dar_letra() for letra in jugadas]
        print(f"Letras jugadas: {', '.join(letras_jugadas)}")
    
    print("-"*50)

def dibujar_ahorcado(intentos_restantes):
    """Dibuja el ahorcado según los intentos restantes"""
    dibujos = [
        # 0 intentos - ahorcado completo
        """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
        """,
        # 1 intento
        """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
        """,
        # 2 intentos
        """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
        """,
        # 3 intentos
        """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
        """,
        # 4 intentos
        """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
        """,
        # 5 intentos
        """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
        """,
        # 6 intentos - solo la horca
        """
     +---+
     |   |
         |
         |
         |
         |
    =========
        """
    ]
    
    print(dibujos[intentos_restantes])

def main():
    """Función principal del juego"""
    juego = JuegoAhorcado()
    palabras_usadas = set()  # Set para almacenar palabras ya usadas
    
    print("¡Bienvenido al Juego del Ahorcado!")
    print("Adivina la palabra letra por letra.")
    print("Tienes 6 intentos para lograrlo.")
    
    while True:
        # Obtener una nueva palabra que no haya sido usada
        intentos_busqueda = 0
        max_intentos = 50  # Evitar bucle infinito
        palabra_repetida = False
        
        while intentos_busqueda < max_intentos:
            juego.iniciar_juego()
            palabra_actual = ''.join([letra.dar_letra() for letra in juego.dar_palabra_actual().dar_letras()])
            
            if palabra_actual not in palabras_usadas:
                break
            else:
                palabra_repetida = True
                intentos_busqueda += 1
        
        # Si se agotaron todos los intentos, limpiar el set
        if intentos_busqueda >= max_intentos:
            print("\n¡Has jugado con todas las palabras disponibles!")
            print("Reiniciando lista de palabras...")
            palabras_usadas.clear()
            juego.iniciar_juego()
            palabra_actual = ''.join([letra.dar_letra() for letra in juego.dar_palabra_actual().dar_letras()])
            palabra_repetida = False
        
        # Obtener número de letras para mostrar discretamente
        num_letras = len(palabra_actual)
        
        # Informar si la palabra ya había sido usada (solo si se detectó repetición)
        if palabra_repetida and intentos_busqueda < max_intentos:
            print(f"\nNota: Se seleccionó una nueva palabra (la anterior ya había sido jugada)")
        
        while juego.dar_estado() == Estado.JUGANDO:
            mostrar_estado_juego(juego, num_letras)
            dibujar_ahorcado(juego.dar_intentos_disponibles())
            
            # Solicitar letra al usuario
            try:
                entrada = input("\nIngresa una letra (o 'salir' para terminar): ").strip().lower()
                
                if entrada == 'salir':
                    print("¡Gracias por jugar!")
                    return
                
                if len(entrada) != 1 or not entrada.isalpha():
                    print("Por favor, ingresa solo una letra válida.")
                    continue
                
                letra = Letra(entrada)
                
                # Verificar si la letra ya fue utilizada
                if juego.letra_utilizada(letra):
                    print(f"Ya has usado la letra '{entrada}'. Intenta con otra.")
                    continue
                
                # Jugar la letra
                acierto = juego.jugar_letra(letra)
                
                if acierto:
                    print(f"¡Bien! La letra '{entrada}' está en la palabra.")
                else:
                    print(f"La letra '{entrada}' no está en la palabra.")
                
            except KeyboardInterrupt:
                print("\n¡Gracias por jugar!")
                return
            except Exception as e:
                print(f"Error: {e}")
                continue
        
        # Agregar la palabra a las usadas
        palabras_usadas.add(palabra_actual)
        
        # Mostrar resultado final
        mostrar_estado_juego(juego, num_letras)
        dibujar_ahorcado(juego.dar_intentos_disponibles())
        
        estado_final = juego.dar_estado()
        if estado_final == Estado.GANADOR:
            print("🎉 ¡Has adivinado la palabra!.")
        elif estado_final == Estado.AHORCADO:
            print("💀 ¡Has sido ahorcado! 💀")
            palabra_completa = ''.join([letra.dar_letra() for letra in juego.dar_palabra_actual().dar_letras()])
            print(f"La palabra era: {palabra_completa}")
        
        # Preguntar si quiere jugar otra vez
        while True:
            respuesta = input("\n¿Quieres jugar otra vez? (s/n): ").strip().lower()
            if respuesta in ['s', 'si', 'sí', 'y', 'yes']:
                break
            elif respuesta in ['n', 'no']:
                print("¡Gracias por jugar!")
                return
            else:
                print("Por favor, responde 's' para sí o 'n' para no.")

if __name__ == "__main__":
    main()