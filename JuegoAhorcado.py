import random
from enum import Enum
from typing import List
from src.Palabra import Palabra
from src.Letra import Letra


class Estado(Enum):
    NO_INICIADO = 1
    JUGANDO = 2
    GANADOR = 3
    AHORCADO = 4

class JuegoAhorcado:
    TOTAL_PALABRAS = 12
    MAX_INTENTOS = 6

    def __init__(self):
        self.diccionario: List[Palabra] = [
            Palabra("algoritmo"),
            Palabra("contenedora"),
            Palabra("avance"),
            Palabra("ciclo"),
            Palabra("indice"),
            Palabra("instrucciones"),
            Palabra("arreglo"),
            Palabra("vector"),
            Palabra("inicio"),
            Palabra("cuerpo"),
            Palabra("recorrido"),
            Palabra("patron"),
        ]
    
        self.palabra_actual = None  # No hay palabra seleccionada al inicio
        self.jugadas = []  # Lista vacía de jugadas
        self.intentos_disponibles = self.MAX_INTENTOS  # Empezamos con el máximo de intentos
        self.estado = Estado.NO_INICIADO  # El juego no ha comenzado

        

    def iniciar_juego(self):
        indice_aleatorio = random.randint(0, self.TOTAL_PALABRAS - 1) # primero, se selecciona una palabra aleatoriamente del diccionario
        self.palabra_actual = self.diccionario[indice_aleatorio]
        
        
        self.jugadas = []  # Se reiniciae el estado del juego, se limpia las jugadas anteriores
        self.intentos_disponibles = self.MAX_INTENTOS  # Restauracion los intentos
        self.estado = Estado.JUGANDO  # Se cambia el estado a jugando


    def jugar_letra(self, letra: Letra) -> bool:
    
        if self.estado != Estado.JUGANDO:  # Solo se puede jugar si el juego está en estado JUGANDO
            return False
        
        if self.letra_utilizada(letra): # Se verifica si la letra ya fue utilizada
            return False  # No se puede repetir letras
        
        self.jugadas.append(letra) # se agrega la letra a las jugadas
        
        if self.palabra_actual.esta_letra(letra): # Se verifica si la letra está en la palabra
            # La letra está en la palabra - acierto

            if self.palabra_actual.esta_completa(self.jugadas):
                self.estado = Estado.GANADOR  # se verifica es si el jugador ha ganado
            return True
        else:
            
            self.intentos_disponibles -= 1  # La letra no está en la palabra - fallo, entonces pierde un intento
            
            if self.intentos_disponibles == 0: # se verficasi el jugador ha perdido
                self.estado = Estado.AHORCADO
            return False


    def dar_palabra_actual(self) -> Palabra:
        return self.palabra_actual


    def dar_palabra(self, posicion: int) -> Palabra:
        if 0 <= posicion < len(self.diccionario):
            return self.diccionario[posicion]
        else:
            return None


    def dar_intentos_disponibles(self) -> int:
        return self.intentos_disponibles


    def dar_jugadas(self) -> List[Letra]:
        return self.jugadas


    def dar_ocurrencias(self) -> List[Letra]:
        if self.palabra_actual is None :
            return []  #lista con las letras adivinadas o _ para las que no se han adivinado
        else:
            return self.palabra_actual.dar_ocurrencias(self.jugadas)  #letras visibles de la pálabra actual


    def dar_estado(self) -> Estado:
        return self.estado


    def letra_utilizada(self, letra: Letra) -> bool:
        for jugada in self.jugadas :
            if jugada == letra:
                return True #la letra ya fue utilizada
        return False #la letra ha sido utilizada

    def metodo1(self) -> str:
        return "Respuesta 1" 

    def metodo2(self) -> str:
        return "Respuesta 2" 