"""
El 21 en Dados.
@author: Manuel Hidalgo Pérez, David Pérez Ruiz
@date: 28 Febrero 2020
@version: 2.0
"""
from github.juego21_v2.jugadores21 import Jugadores21


class Partida21:
    """
    Partes de la partida del 21.
    """
    def __init__ (self):
        __jugadores = list()

    @property
    def jugadores(self):
        return self.__jugadores

    @jugadores.setter
    def jugadores(self, value):
        self.__jugadores = value

    # Métodos
    def alta_jugadores(self, num_jugadores):
        jugadores = list()
        for i in range(num_jugadores):
            nombre_jugador = f'j{i + 1}: ' + input(f'Introduce nombre del jugador {i + 1}: ')
            jugadores.append(Jugadores21(nombre_jugador))
        self.__jugadores = jugadores

    # Jugada de inicio para el orden
    def ronda_inicial (self):
        jugadores2 = list()
        for i in range (len(self.__jugadores)):
            jugadores2.append(self.__jugadores[i])
        maximo = 0
        # Siempre que haya más de un jugador aún en este array repetiremos la tirada para romper con los desempates.
        while len(jugadores2) > 1:
            for i in range (len(jugadores2)):
                jugadores2[i].tirada_un_dado()
                print(f"Resultado de {jugadores2[i].nombre} es {jugadores2[i].resultado_ronda}")
                if jugadores2[i].resultado_ronda > maximo:
                    maximo = jugadores2[i].resultado_ronda
            i=0
            # Eliminamos de la lista los jugadores que hayan obtenido un resultado inferior al máximo
            while (len(jugadores2)) > 1 and i < (len(jugadores2)) :
                if jugadores2[i].resultado_ronda != maximo:
                    del jugadores2[i]
                else:
                    i +=1
            # Reiniciamos los contadores
            for i in range (len(jugadores2)):
                jugadores2[i].borrar_resultado()
            maximo = 0
            print("")
        # Sólo queda un jugador, empezará la partida por él.
        print(f"Empieza a jugar: {jugadores2[0]}")

        # Reordenamos el arraylist para los jugadores.
        auxiliar = list()
        indice = 0
        for i in range (len(self.__jugadores)):
            if (jugadores2[0].nombre) == (self.__jugadores[i].nombre):
                indice = i
                j = 0
        for i in range (len(self.__jugadores)):
            if (indice+i) < len(self.__jugadores):
                auxiliar.append(self.__jugadores[indice+i])
            else:
                auxiliar.append(self.__jugadores[j])
                j +=1
        self.__jugadores = auxiliar

    def jugar_ronda_todos (self):
        jugadores2 = list()
        for i in range(len(self.__jugadores)):
            self.__jugadores[i].borrar_resultado()
            jugadores2.append(self.__jugadores[i])
        maximo = 0
        # Siempre que haya más de un jugador aún en este array repetiremos la tirada para romper con los desempates.
        while len(jugadores2) > 1:
            for i in range(len(jugadores2)):
                print(f"\nTurno de {jugadores2[i].nombre}")
                jugadores2[i].jugar_ronda()
                if jugadores2[i].resultado_ronda > maximo and jugadores2[i].resultado_ronda <= 21:
                    maximo = jugadores2[i].resultado_ronda
            i = 0
            # Eliminamos de la lista los jugadores que hayan obtenido un resultado inferior al máximo
            while (len(jugadores2)) > 1 and i < (len(jugadores2)):
                if jugadores2[i].resultado_ronda != maximo:
                    del jugadores2[i]
                else:
                    i += 1
            # Reiniciamos los contadores
            for i in range(len(jugadores2)):
                jugadores2[i].borrar_resultado()
            maximo = 0
            print("")
        # Sólo queda un jugador, empezará la partida por él.
        print(f"Gana  la ronda: {jugadores2[0]}")
        jugadores2[0].sumar_victoria()

    def ver_clasificacion (self):
        self.__jugadores.sort()
        print("Clasificación:")
        print("--------------")
        print(self)

    def __str__(self):
        salida =""
        for i in range (len(self.__jugadores)):
            salida += (f"Nombre: {self.__jugadores[i].nombre} - Puntuación total: {self.__jugadores[i].contador_victorias}\n")
        return salida

