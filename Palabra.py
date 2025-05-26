from typing import List
from src.Letra import Letra

class Palabra:
    """
    Clase para representar una palabra del juego.
    letras : lista [Letra] - lista de objetos Letra que forman la plabra.
    """

    ### constructor
    def __init__(self, p_palabra: str):
        self.letras = []
        for caracter in p_palabra :
            self.letras.append(Letra(caracter))


    
    ### métodos
    
    __method__ = "esta_completa"
    __params__ = "p_jugadas"
    __return__ = "bool"
    __description__ = "Indica si con las letras jugadas ya es posible conocer la palabra completa"
    def esta_completa(self, p_jugadas: List[Letra]) -> bool:
        for letra in self.letras:
            if not self._buscar_letra_en_lista(letra, p_jugadas):
                return False  #si la letra no ha sido juagda, la palabra no está completa
        return True  #todas las letras han sido jugadas


    __method__ = "buscar_letra_en_lista"
    __params__ = "p_letra, lista_letras"
    __return__ = "bool"
    __description__ = "Indica si una letra se encuentra en una lista dada"
    def _buscar_letra_en_lista(self, p_letra: Letra, lista_letras: List[Letra]) -> bool:
        for letra in lista_letras:
            if letra.es_igual (p_letra):
                return True  #la letra  se encontró en la lista
        return False #la letra no se encontró en la lista


    __method__ = "esta_letra"
    __params__ = "p_letra"
    __return__ = "bool"
    __description__ = "Indica si una letra está en la palabra"
    def esta_letra(self, p_letra: Letra) -> bool:
        for letra in self.letras:
            if letra.es_igual(p_letra):  # Usamos el método es_igual de Letra
                return True
        return False


    __method__ = "dar_ocurrencias"
    __params__ = "p_jugadas"
    __return__ = "List[Letra]"
    __description__ = "Devuelve una lista con las letras jugadas correctamente, reemplazando las no adivinadas con '_'."
    def dar_ocurrencias(self, p_jugadas: List[Letra]) -> List[Letra]:
        ocurrencias = []
        for letra in self.letras:
            if self._buscar_letra_en_lista(letra, p_jugadas):
                ocurrencias.append(letra.dar_letra())  #si la letra ha sido jugada, se muestra en la lista de ocurrencias
            else:
                ocurrencias.append("_")
        return ocurrencias

    __method__ = "dar_letras"
    __params__ = "None"
    __return__ = "List[Letra]"
    __description__ = "Devuelve el arreglo con las letras de la palabra."
    def dar_letras(self) -> List[Letra]:
        """
        Devuelve el arreglo con las letras de la palabra.
        :return: Lista de letras que componen la palabra.
        """
        return self.letras
