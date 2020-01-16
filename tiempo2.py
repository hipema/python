class Tiempo:
    """
    Versión 2.0
    Primer ejercicio de POO en Python.
    Autor: Manuel Hidalgo Pérez
    Fecha: 14-01-2020
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
        self.__segundos_total = 0

        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos
        self.__segundos_total = self.convierte_a_segundos()

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
        if Tiempo.comprueba_minutos_segundos(valor_minutos):
            self.__minutos = valor_minutos
        else:
            print("ERROR: Minutos incorrectos")

    @property
    def segundos(self):
        return self.__segundos

    @segundos.setter
    def segundos(self, valor_segundos):
        if Tiempo.comprueba_minutos_segundos(valor_segundos):
            self.__segundos = valor_segundos
        else:
            print("ERROR: segundos incorrectos")

    # Métodos (funcionalidades)
    def convierte_a_segundos(self):
        return self.__horas *3600 + self.__minutos * 60 + self.__segundos

    def convierte_en_tiempo(self, valor_segundos):
        self.__horas = (valor_segundos)//3600
        self.__minutos = ((valor_segundos)-(self.__horas*3600))//60
        self.__segundos = (valor_segundos) - self.__horas*3600 - self.__minutos * 60

    def sumar_segundos_objetos (self, otro):
        return self.convierte_a_segundos()+otro.convierte_a_segundos()

    def restar_segundos_objeto(self, otro):
        return self.convierte_a_segundos()-otro.convierte_a_segundos()

    def sumar_horas(self, valor_horas):
        return self.convierte_en_tiempo(self.convierte_a_segundos()+valor_horas*3600)

    def sumar_minutos(self,valor_minutos):
        return self.convierte_en_tiempo(self.convierte_a_segundos()+valor_minutos*60)

    def sumar_segundos(self,valor_segundos):
        return self.convierte_en_tiempo(self.convierte_a_segundos()+valor_segundos)

    def restar_horas(self, valor_horas):
        return self.convierte_en_tiempo(self.convierte_a_segundos()-valor_horas*3600)

    def restar_minutos(self,valor_minutos):
        return self.convierte_en_tiempo(self.convierte_a_segundos()-valor_minutos*60)

    def restar_segundos(self,valor_segundos):
        return self.convierte_en_tiempo(self.convierte_a_segundos()-valor_segundos)

    def muestra_cadena(self):
        print(f"{self.__horas}h {self.__minutos}m {self.__segundos}s.")

    @staticmethod
    def comprueba_minutos_segundos(value):
        return type(value) == type(1) and value >=0 and value <60


if __name__ == "__main__":
    print("Tiempo1:")
    t1 = Tiempo(1, 25, 30)
    print(t1.horas, " horas, ", t1.minutos, " minutos, ", t1.segundos, " segundos.")

    print("\nTiempo1 en segundos:")
    print(t1.convierte_a_segundos())
    print(t1.horas, " horas, ", t1.minutos, " minutos, ", t1.segundos, " segundos.")

    print("\nTiempo 2:")
    t2 = Tiempo(2, 25, 10)
    print(t2.horas, " horas, ", t2.minutos, " minutos, ", t2.segundos, " segundos.")

    print("\nTiempo2 en segundos:")
    print(t2.convierte_a_segundos())
    print(t2.horas, " horas, ", t2.minutos, " minutos, ", t2.segundos, " segundos.")

    print("\nSuma de dos tiempos:")
    print(f"Tiempo en segundos {t1.sumar_segundos_objetos(t2)}")
    t1.convierte_en_tiempo(t1.sumar_segundos_objetos(t2))
    print(t1.horas, " horas, ", t1.minutos, " minutos, ", t1.segundos, " segundos.")

    print("\nResta dos tiempos:")
    t1.convierte_en_tiempo(t1.restar_segundos_objeto(t2))
    print(t1.horas, " horas, ", t1.minutos, " minutos, ", t1.segundos, " segundos.")

    print("\nSumar 2 horas a un tiempo:")
    t1.sumar_horas(2)
    print(t1.horas, " horas, ", t1.minutos, " minutos, ", t1.segundos, " segundos.")

    print("\nSumar 40 minutos a un tiempo:")
    t1.sumar_minutos(40)
    print(t1.horas, " horas, ", t1.minutos, " minutos, ", t1.segundos, " segundos.")

    print("\nSumar 40 segundos a un tiempo:")
    t1.sumar_segundos(40)
    print(t1.horas, " horas, ", t1.minutos, " minutos, ", t1.segundos, " segundos.")

    print("\nRestar 2 horas a un tiempo:")
    t1.restar_horas(2)
    print(t1.horas, " horas, ", t1.minutos, " minutos, ", t1.segundos, " segundos.")

    print("\nRestar 40 minutos a un tiempo:")
    t1.restar_minutos(40)
    print(t1.horas, " horas, ", t1.minutos, " minutos, ", t1.segundos, " segundos.")

    print("\nRestar 40 segundos a un tiempo:")
    t1.restar_segundos(40)
    print(t1.horas, " horas, ", t1.minutos, " minutos, ", t1.segundos, " segundos.")

    print("\nMuestra el objeto tiempo en el formato solicitado:")
    t1.muestra_cadena()