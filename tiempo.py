class Tiempo:
    """
    Versión 1.0
    Primer ejercicio de POO en Python.
    """
    def __init__(self, horas, minutos, segundos):
        """
        Constructor de la clase
        :param horas: número de horas recibidas
        :param minutos: número de minutos
        :param segundos: número de segundos
        """
        # Inicializamos el valor en cero y los ponemos privados para que no se pueda modificar directamente.
        self.__horas = 0
        self.__minutos = 0
        self.__segundos = 0

        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    # Propiedades
    @property
    def horas(self):
        return self.__horas

    @horas.setter
    def horas(self, valor_horas):
        self.__horas = valor_horas

    @property
    def minutos(self):
        return self.__minutos

    @minutos.setter
    def minutos(self, valor_minutos):
        if valor_minutos > 59:
             self.__minutos = valor_minutos%60
             self.__horas = self.__horas + valor_minutos//60
        elif valor_minutos < 0:
             self.__minutos = abs(valor_minutos%60)
             self.__horas = self.__horas - (abs(valor_minutos//60))
        else:
             self.__minutos = valor_minutos

    @property
    def segundos(self):
        return  self.__segundos

    @segundos.setter
    def segundos(self, valor_segundos):
        if valor_segundos >59:
            self.segundos = valor_segundos%60
            self.minutos = self.minutos + valor_segundos//60
        elif valor_segundos < 0:
            self.__segundos = abs(valor_segundos%60)
            self.__minutos = self.__minutos - (abs(valor_segundos//60))
        else:
            self.__segundos = valor_segundos

    # Métodos (funcionalidades)
    def suma_horas(self, otro):
        """
        suma las horas de dos objetos
        :param otro: objeto que sumamos al actual
        :return: horas sumadas
        """
        return self.horas + otro.horas

    def suma_minutos (self, otro):
        """
        Suma los minutos de dos objetos
        :param otro: objeto que sumamos al actual
        :return: minutos sumados
        """
        return self.minutos + otro.minutos

    def suma_segundos (self, otro):
        """
        Suma los segundos de dos objetos
        :param otro: objeto que sumamos al actual
        :return: segundos sumados
        """
        return self.segundos + otro.segundos

    def suma_tiempo (self, otro):
        """
        Recibe un objeto tiempo y lo suma al actual.
        :param otro: objeto a sumar al tiempo actual.
        :return: devuelve el valor sumado de ambos tiempos.
        """
        self.horas = self.horas + otro.horas
        self.minutos = self.minutos + otro.minutos
        self.segundos = self.segundos + otro.segundos
        return self.horas, self.minutos, self.segundos

    def resta_tiempo(self, otro):
        """
        Recibe un objeto tiempo y lo resta al objeto actual.
        :param otro: objeto a restar al tiempo actual.
        :return: devuelve el valor restado de ambos tiempos.
        """
        self.horas = self.horas - otro.horas
        self.minutos = self.minutos - otro.minutos
        self.segundos = self.segundos - otro.segundos

    def sumar_horas(self, horas_a_sumar):
        """
        Suma a un objeto tiempo una cantidad de horas
        :param horas_a_sumar:
        :return: devuelve el resultado de sumar una cantidad de horas determinada al objeto tiempo
        """
        self.__horas = self.__horas + horas_a_sumar

    def sumar_minutos(self, minutos_a_sumar):
        """
        Suma a un objeto tiempo una cantidad de minutos
        :param minutos_a_sumar:
        :return: devuelve el resultado de sumar una cantidad de minutos deterninada al objeto tiempo.
        """
        if minutos_a_sumar >59:
            self.__horas = self.__horas + (minutos_a_sumar//60)
            self.__minutos = self.__minutos + (minutos_a_sumar%60)
        else:
            self.__minutos += minutos_a_sumar
            if self.__minutos > 59:
                self.__horas = self.__horas+1
                self.__minutos = self.__minutos%60

    def sumar_segundos(self, segundos_a_sumar):
        """
        Suma a un objeto tiempo una cantidad de segundos
        :param segundos_a_sumar:
        :return: devuelve el resultado de sumar una cantidad de minutos determinada al objeto tiempo.
        """
        if segundos_a_sumar >59:
            self.__minutos = self.__minutos + (segundos_a_sumar//60)
            self.__segundos = self.__segundos + (segundos_a_sumar%60)
            if self.__segundos > 59:
                self.__minutos = self.__minutos + (self.__segundos//60)
                self.__segundos = self.__segundos%60
            if self.__minutos >59:
                self.__horas = self.__horas + (self.__minutos//60)
                self.__minutos = self.__minutos%60
        else:
            self.__segundos += segundos_a_sumar
            if self.__segundos >59:
                self.__minutos +=1
                self.__segundos = self.__segundos%60
                if self.__minutos > 59:
                    self.__horas = self.__horas + (self.__minutos // 60)
                    self.__minutos = self.__minutos % 60

    def restar_horas(self, horas_a_restar):
        self.__horas = self.__horas - horas_a_restar

    def restar_minutos(self, minutos_a_restar):
        if minutos_a_restar >59:
            self.restar_horas(minutos_a_restar//60)
            self.__minutos -= minutos_a_restar%60
            if self.__minutos < 0:
                self.restar_horas(1)
                self.__minutos = 60+self.__minutos
        else:
            self.__minutos -= minutos_a_restar
            if self.__minutos < 0:
                self.restar_horas(1)
                self.__minutos = 60 + self.__minutos

    def restar_segundos(self, segundos_a_restar):
        if segundos_a_restar > 59:
            self.restar_minutos(segundos_a_restar//60)
            self.__segundos -= segundos_a_restar%60
            if self.__segundos < 0:
                self.restar_minutos(1)
                self.__segundos = 60+self.__segundos
        else:
            self.__segundos -= segundos_a_restar
            if self.__segundos < 0:
                self.restar_minutos(1)
                self.__segundos = 60 + self.__segundos

    def muestra_cadena(self):
        print(f"{self.__horas}h {self.__minutos}m {self.__segundos}s.")


if __name__ == "__main__":
    print("Tiempo1:")
    t1 = Tiempo(1, 25, 30)
    print(t1.horas," horas, ", t1.minutos," minutos, ", t1.segundos, " segundos.")

    print("\nTiempo2:")
    t2 = Tiempo(2, 40, 10)
    print(t2.horas," horas, ", t2.minutos," minutos, ", t2.segundos, " segundos.")

    print("\nSuma de tiempos:")
    t1.suma_tiempo(t2)
    print(t1.horas," horas, ", t1.minutos," minutos, ", t1.segundos, " segundos.")

    print("\nResta de tiempos:")
    t1.resta_tiempo(t2)
    print(t1.horas," horas, ", t1.minutos," minutos, ", t1.segundos, " segundos.")

    print("\nSuma de 3 horas a t1:")
    (t1.sumar_horas(3))
    print(t1.horas, " horas, ", t1.minutos, " minutos, ", t1.segundos, " segundos.")

    print("\nSuma de 90 minutos a t1:")
    (t1.sumar_minutos(90))
    print(t1.horas, " horas, ", t1.minutos, " minutos, ", t1.segundos, " segundos.")

    print("\nSuma de 330 segundos a t1:")
    (t1.sumar_segundos(330))
    print(t1.horas, " horas, ", t1.minutos, " minutos, ", t1.segundos, " segundos.")

    print("\nResta de 1 hora a t1:")
    (t1.restar_horas(1))
    print(t1.horas, " horas, ", t1.minutos, " minutos, ", t1.segundos, " segundos.")

    print("\nResta de 2 minutos a t1:")
    (t1.restar_minutos(2))
    print(t1.horas, " horas, ", t1.minutos, " minutos, ", t1.segundos, " segundos.")

    print("\nResta de 10 segundos a t1:")
    (t1.restar_segundos(10))
    print(t1.horas, " horas, ", t1.minutos, " minutos, ", t1.segundos, " segundos.")

    print("\nMuestra el objeto tiempo en el formato solicitado:")
    t1.muestra_cadena()