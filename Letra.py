class Letra:

    def __init__(self, p_letra: str):
        """
        Crea una nueva letra a partir de un carácter dado.
        :param p_letra: Variable de tipo str que representa un carácter para inicializar la letra.
        """
        self.letra = p_letra.lower() #la letra se guarda e minuscula para facilitar conmparaciones

    def dar_letra(self) -> str:
        """
        Devuelve el carácter que representa la letra.
        :return: Un carácter con la letra.
        """
        return self.letra
    
    def es_igual(self, otra_letra: 'Letra') -> bool:
        """
        Indica si dos letras son iguales, sin importar si una está en mayúscula y otra en minúscula.
        :param otra_letra: La letra para comparar.
        :return: True si las letras son iguales sin importar mayúsculas/minúsculas, False de lo contrario.
        """
        return self.letra == otra_letra.letra #se compara ls letras en min paara ignorar may/min
    
