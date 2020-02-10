from github.juego21.jugadores21 import Jugadores21


class Reglas21:
    """
    Partes de la partida del 21.
    """

    def __init__ (self):
        __jugadores = list()

    @property
    def jugadores (self):
        return self.__jugadores

    @jugadores.setter
    def jugadores (self, value):
        self.__jugadores.append(value)

    # Métodos de la clase
    def alta_jugadores (self, num_jugadores):
        for i in range(num_jugadores):
            nombre_jugador = f'j{i + 1}: ' + input(f'Introduce nombre del jugador {i + 1}: ')
            self.jugadores(Jugadores21(nombre_jugador))
        return self.__jugadores

