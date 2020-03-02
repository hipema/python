"""
El 21 en Dados.
@author: Manuel Hidalgo Pérez, David Pérez Ruiz
@date: 28 Febrero 2020
@version: 2.0
"""

from github.juego21_v2.dados import DadoSimple

"""
Esta clase creará jugadores para el Juego de Dados "El 21".
Para su funcionamiento se valdrá de las clases Dado y Dados realizados por Rafael del Castillo.

Necesitaremos realizar que cada objeto Jugador disponga de:
    nombre (str)
    dado1, dado2 (Dado)
    tirar_un_dado (metodo)
    tirar_dos_dados (metodo)
    resultado_dados
    resultado_ronda
    borrar_resultado (metodo)
    contador_victorias
"""
class Jugadores21:
    def __init__(self, nombre):
        """
        Constructor de la clase.
        :param nombre: Nombre para el jugador creado
        """
        self.__nombre = nombre
        self.__resultado_ronda = 0
        self.__resultado_dados = 0
        self.__contador_victorias = 0
        self.__dado1 = DadoSimple()
        self.__dado2 = DadoSimple()

    #Propiedades.
    @property
    def nombre(self):
        return self.__nombre
    @property
    def resultado_ronda(self):
        return self.__resultado_ronda

    @resultado_ronda.setter
    def resultado_ronda(self, value):
        self.__resultado_ronda = value

    @property
    def resultado_dados(self):
        return self.__resultado_dados

    @resultado_dados.setter
    def resultado_dados(self, value):
        self.__resultado_dados = value

    @property
    def contador_victorias(self):
        return self.__contador_victorias

    # Métodos
    def sumar_victoria(self):
        self.__contador_victorias += 1
    def tirada_un_dado (self):
        self.__dado1.tirada()
        self.__resultado_dados = self.__dado1.cara
        self.__resultado_ronda += self.__resultado_dados

    def tirada_dos_dados (self):
        self.__dado1.tirada()
        self.__dado2.tirada()
        self.__resultado_dados = self.__dado1.cara + self.__dado2.cara
        self.__resultado_ronda += self.__resultado_dados

    def borrar_resultado (self):
        self.__resultado_ronda = 0

    def jugar_ronda(self):
        lanzar = input(f'pulsa "A" para lanzar dados. ')
        while not (lanzar != "A" or lanzar != "a"):
            lanzar = input(f'Opción no encontrada, pulse "A" para realizar su tirada. ')
        self.tirada_dos_dados()
        print(f'Resultado tirada: {self.resultado_dados}')
        print(f'Resultado acumulado en esta ronda: {self.resultado_ronda}\n')

        while self.resultado_ronda < 14:
            lanzar = input (f'¿Deseas volver a lanzar? (si deseas Lanzar pulsa "A", si deseas plantarte pulsa "B" ')
            while (lanzar != "A" and lanzar != "a" and lanzar != "B" and lanzar != "b"):
                lanzar = input(f'Opción no encontrada, pulse "A" para realizar su tirada o "B" SI deseas plantarte. ')
            if lanzar == "A" or lanzar == "a":
                self.tirada_dos_dados()
                print(f'Resultado de tirada: {self.resultado_dados}')
                print(f'Resultado acumulado en esta ronda: {self.resultado_ronda}\n')
            else:
                print(f'Resultado final de ronda: {self.resultado_ronda}\n')
                return self.resultado_ronda
        while self.resultado_ronda <= 21:
            if self.resultado_ronda == 21:
                print(f'Has logrado la puntuación máxima.\n')
                return self.resultado_ronda
            print(f'Estás muy cerca del límite, a partir de ahora, tirarás con un único dado.\n')
            lanzar = input(f'¿Deseas volver a lanzar? (si deseas Lanzar pulsa "A", si deseas plantarte pulsa "B" ')
            while (lanzar != "A" and lanzar != "a" and lanzar != "B" and lanzar != "b"):
                lanzar = input(f'Opción no encontrada, pulse "A" para realizar su tirada o "B" SI deseas plantarte. ')
            if lanzar == "A" or lanzar == "a":
                self.tirada_un_dado()
                print(f'Resultado de tirada: {self.resultado_dados}')
                print(f'Resultado acumulado en esta ronda: {self.resultado_ronda}\n')
            else:
                print(f'Resultado final de ronda: {self.resultado_ronda}\n')
                return self.resultado_ronda

        print(f'Has superado el límite de 21, quedas eliminado automáticamente.\n')
        return self.resultado_ronda

    # Sobrecargamos métodos
    def __str__(self):
        return f'{self.nombre}'

if __name__ == "__main__":
    j1 = Jugadores21("Manolo")
    j2 = Jugadores21("Pepe")
    print(f'Probamos la clase Jugador con j1: {j1.nombre} y j2: {j2.nombre}')

    j1.tirada_un_dado()
    print(f'El resultado del dado lanzado: {j1.resultado_dados}')
    print(f'El resultado de la ronda es: {j1.resultado_ronda}')
    print(f'\nVolvemos a lanzar 1 dado.')
    j1.tirada_un_dado()
    print(f'El resultado del dado lanzado: {j1.resultado_dados}')
    print(f'El resultado sumado de la ronda es: {j1.resultado_ronda}')

    j1.borrar_resultado()
    print(f'Borramos el contador de ronda:')
    j1.tirada_dos_dados()
    print(f'Ahora lanzamos dos dados, la suma de los dados es: {j1.resultado_dados}')
    print(f'El resultado de la ronda es: {j1.resultado_ronda}')
    j1.tirada_dos_dados()
    print(f'Volvemos a lanzar dos dados, la suma de los dados es: {j1.resultado_dados}')
    print(f'El resultado de la ronda es: {j1.resultado_ronda}')


    # Sobrecarga de funciones
    def __lt__(self, other):
        """
        Comprueba si jugador tiene menor puntuación que otro
        :param other:
        :return:
        """
        assert isinstance(other, Jugadores21)  # comprueba si other es un objeto Jugador21.
        return self.__contador_victorias < other.contador_victorias


    def __le__(self, other):
        """
        Comprueba si un rectángulo es menor o igual a otro.
        :param other:
        :return:
        """
        assert isinstance(other, Jugadores21)
        return self.__contador_victorias <= other.contador_victorias


    def __eq__(self, other):
        """
        Comprueba si un rectángulo es igual a otro.
        :param other:
        :return:
        """
        assert isinstance(other, Jugadores21)
        return self.__contador_victorias == other.contador_victorias