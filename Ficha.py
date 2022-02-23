"""
Tarea de introducción a los objetos
Jose Pablo Agüero Mora (2021126372) - Grupo 2
Clase de ficha
"""

import random
from Dado import *

listaGeneral = []

class Ficha:
    color = ""
    posicion = 0

    #no era parte del modelo, pero la Ficha necesita usar un dado
    #este atributo se define cuando definimos relaciones entre clases
    #lo que veremos más adelante en el curso
    dado = Dado(6)
    
    
    def __init__(self, color):
        self.color = color
        self.posicion = 0
    
    def avanzar(self):
        #aquí se vuelve claro por qué necesitamos un dado
        pasos = self.dado.lanzar()
        self.posicion += pasos
        print ("Se mueve:", pasos)
        print("Casilla actual:", self.posicion)
    


    
