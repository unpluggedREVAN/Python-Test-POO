"""
Tarea de introducción a los objetos
Jose Pablo Agüero Mora (2021126372) - Grupo 2
Clase de dado
"""

from random import *

class Dado:

    caras=0

    #este atributo no estaba en el modelo explícitamente
    #pero lo necesitamos para poder crear los números aleatorios
    #normalmente deberíamos esconderlo para que no sea accesible (encapsulamiento)
    rnd=Random(42)

    def __init__(self, numCaras):
        self.caras=numCaras
    
    def lanzar(self):
        return self.rnd.randint(1, self.caras) #Los números se repiten en cada ejecución
