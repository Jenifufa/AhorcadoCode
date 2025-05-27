__author__ = "Jenifer U. C. Andres B. C. , Zara C. B."
__version__ = "1.0.0"
__license__ = "GPL"
__email__ = "jenifer.urbano@campusucc.edu.co"

class Letra:

    ### constructor
    def __init__(self, p_letra: str):
        self.letra = p_letra.lower() #la letra se guarda e minuscula para facilitar conmparaciones


    
    ### métodos
    
    __method__ = "dar_letra"
    __params__ = "None"
    __return__ = "letra"
    __description__ = "Método que sirve para dar la letra"
    def dar_letra(self) -> str:
        return self.letra
    
    __method__ = "es_igual"
    __params__ = "otra_letra"
    __return__ = "bool"
    __description__ = "Método que sirve para comparar dos letras sin importar mayúsculas o minúsculas"
    def es_igual(self, otra_letra: 'Letra') -> bool:
        return self.letra.lower() == otra_letra.letra.lower() #se compara ls letras en min paara ignorar may/min
    
