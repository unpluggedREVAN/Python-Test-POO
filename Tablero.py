"""
Tarea de introducción a los objetos
Jose Pablo Agüero Mora (2021126372) - Grupo 2
Clase de tablero y main
"""

import random
from Ficha import *

class Tablero:

    #Definición de los atributos del tablero
    casillas = 0
    fichas = []
    ganador = ""

    #Inicialización de los atributos
    def __init__(self, casi, lfich):
        self.casillas = casi
        self.fichas = lfich

    #Definición de los métodos
    def orden(self, fich): #Ordena de forma aleatoria la lista registrada
        shuffle(self.fichas)

    def ganar(self): #Verifica si ya existe un ganador
        for elem in self.fichas:
            if elem.posicion >= self.casillas:
                self.ganador = elem.color

    def partida(self, elem): #Activa la partida del jugador actual
        elem.avanzar()



class main(): #Ciclo de juego principal

    def ingresaObjeto(col): #Método para registrar objetos ficha
        ficha = Ficha(col)
        ficha.color = col
        listaGeneral.append(ficha)

    cantcas = int(input("Ingrese la cantidad de casillas: ")) #Guarda cantidad de casillas

    cantfi = int(input("Ingrese la cantidad de fichas: ")) #Se ingresan los jugadores
    for i in range(cantfi):
        print("Ficha", i)

        col = input("Ingrese el color: ")
        ingresaObjeto(col)
    
    tab = Tablero(cantcas, listaGeneral) #Inicializa el tablero
    tab.orden(listaGeneral) #Se ordena aleatoriamente la lista de fichas

    i = 0 #Se inicializa un contador para el ciclo
    while tab.ganador == "": #El ciclo termina cuando el valor de ganador cambia
        este = i
        if este >= len(tab.fichas): #Sistema para repetir el orden de la lista
            while este >= len(tab.fichas):
                este -= len(tab.fichas)

        print ("")
        print("Turno del:", tab.fichas[este].color) #Impresiones en consola
        tab.partida(tab.fichas[este]) #Hace que el jugador actual use su turno

        tab.ganar() #Verifica si hay un ganador
        i += 1

    print("El ganador es:", tab.ganador) #Al salir del ciclo muestra el ganador del juego


