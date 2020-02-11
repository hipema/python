from github.juego21.jugadores21 import Jugadores21


class Reglas21:
    """
    Partes de la partida del 21.
    """

    def __init__ (self):
        __jugadores = list()
        __num_jugadores = 0
        __jugadores_empatados = list()
        __resultado_ronda = list()

    @property
    def jugadores_empatados(self):
        return self.__jugadores_empatados

    @jugadores_empatados.setter
    def jugadores_empatados(self, value):
        self.__jugadores_empatados = value

    @property
    def num_jugadores(self):
        return self.__num_jugadores

    @num_jugadores.setter
    def num_jugadores(self, value):
        self.__num_jugadores = value

    @property
    def jugadores(self):
        return self.__jugadores

    @jugadores.setter
    def jugadores(self, value):
        self.__jugadores = value

    @property
    def resultado_ronda(self):
        return self.__resultado_ronda

    @resultado_ronda.setter
    def resultado_ronda(self, value):
        self.__resultado_ronda = value

    # Métodos de la clase
    def alta_jugadores (self, num_jugadores):
        jugadores = list()
        for i in range(num_jugadores):
            nombre_jugador = f'j{i + 1}: ' + input(f'Introduce nombre del jugador {i + 1}: ')
            jugadores.append(Jugadores21(nombre_jugador))
        self.__jugadores = jugadores
        self.__num_jugadores = num_jugadores

    def listado_jugadores(self):
        for i in range(self.__num_jugadores):
            print(f'Jugador {i + 1}: {self.jugadores[i]}')

    def buscar_empatados(self):
        self.__jugadores_empatados = list()
        maximo = 0
        contador = 0
        empatados = list()
        for i in range (self.__num_jugadores):
            if maximo < self.__jugadores[i].resultado_ronda:
                maximo = self.__jugadores[i].resultado_ronda
        for i in range (self.__num_jugadores):
            if maximo == self.__jugadores[i].resultado_ronda:
                empatados.append(self.__jugadores[i])
                contador += 1
        if contador > 1:
            self.jugadores_empatados = empatados
        else:
            self.jugadores_empatados = empatados

    def mostrar_empatados(self):
        self.buscar_empatados()
        if (len(self.__jugadores_empatados)) == 1:
            self.ganador_ronda()
        else:
            for i in range (len(self.__jugadores_empatados)):
                print(f'{self.__jugadores_empatados[i]}')

    def tirar_todos_un_dado (self):
        for i in range (self.num_jugadores):
            self.__jugadores[i].tirada_un_dado()

    def tirar_todos_dos_dados (self):
        for i in range (self.num_jugadores):
            self.__jugadores[i].tirada_dos_dados()

    def resultado_ronda_dados (self):
        resultado = list()
        for i in range (self.num_jugadores):
            resultado.append(self.jugadores[i].resultado_ronda)
        self.resultado_ronda = resultado

    def resetear_resultado_ronda (self):
        for i in range(self.num_jugadores):
            self.jugadores[i].borrar_resultado()

    def empatados_un_dado (self):
        self.buscar_empatados()
        self.resetear_resultado_ronda()
        for i in range (len(self.__jugadores_empatados)):
            self.jugadores_empatados[i].tirada_un_dado()

    def mostrar_resultados_empatados (self):
        """
        Función para mostrar el resultado tras un lanzamiento de los jugadores empatados.
        :return:
        """
        if len(self.jugadores_empatados) == 1:
            print(end="")
        else:
            for i in range(len(self.jugadores_empatados)):
                if self.jugadores_empatados[i].resultado_ronda == 0:
                    print(end="")
                else:
                    print(f'Jugador {i + 1}: {self.resultado_ronda[i]}')

    # Pendiente comprobar esta función
    def desempatar_apertura (self):
        self.buscar_empatados()
        i = len(self.jugadores_empatados)
        while i > 1:
            print('Nuevo lanzamiento')
            self.empatados_un_dado()
            self.buscar_empatados()
            self.mostrar_resultados_empatados()
            i = len(self.jugadores_empatados)
            self.resetear_resultado_ronda()

    def ganador_ronda (self):
        if len(self.jugadores_empatados) == 1:
            print(f'Máxima puntuación {self.jugadores_empatados[0].nombre}')
            self.jugadores_empatados[0].sumar_victoria()
        else:
            print('Aún no hay un ganador, varios jugadores  están empatados.')

    """
    Debemos seguir desarrollando las funciones, ahora para realizarlas con los jugadores en caso de empate
    """


    # Función para realizar el sorteo de los turnos y ordenar los jugadores.
    def sorteo_turnos(self):
        contador = (len(self.__jugadores_empatados))
        auxiliar = contador
        self.buscar_empatados()

        numero_ronda = 1
        while contador > 1:
            print(f'\nLanzamiento {numero_ronda}')
            auxiliar = contador
            contador = 0
            puntuacion = list()
            maximo = 0
            desempate = list()
            for i in range(auxiliar):
                self.__jugadores_empatados[i].tirada_un_dado()
                print(f'Lanza dado {self.__jugadores_empatados[i].nombre}: '
                      f'{self.__jugadores_empatados[i].resultado_dados}')
                puntuacion.append(self.__jugadores_empatados[i].resultado_dados)
                if self.__jugadores_empatados[i].resultado_dados > maximo:
                    maximo = self.__jugadores_empatados[i].resultado_dados
                for i in range (auxiliar):
                    if self.__jugadores_empatados[i].resultado_dados == maximo:
                        contador += 1
                        desempate.append(self.jugadores[i])

            for i in range(auxiliar):
                if maximo == puntuacion[i]:
                    desempate[contador] = self.__jugadores_empatados[i]
                    contador += 1
            self.__jugadores_empatados.clear()
            for i in range(contador):
                self.__jugadores_empatados[i] = desempate[i]
            numero_ronda += 1