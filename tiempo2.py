class Tiempo:
    """
    Versión 3.0 - corrección en clase
    Primer ejercicio de POO en Python.
    Autor: Manuel Hidalgo Pérez
    Fecha: 14-01-2020

    Ejercicio:
    Crea la clase Tiempo. Los objetos de la clase Tiempo son intervalos de tiempo y se crean de la forma:

    t = Tiempo(1, 20, 30)

    donde los parámetros que se le pasan al constructor son las horas, los minutos y los segundos respectivamente.

    Crea métodos para:
    Sumar y restar otro objeto de la clase Tiempo.
    Sumar y restar segundos, minutos y/o horas.
    Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10h 35m 5s.

    Modificaciones:
    - Método __str__ para pasa el objeto como cadena
    - Quitar self.__segundos_total que no se utilizaba
    - Quitamos setters y para comprobar si los valores son incorrectos, lanzamos un "assert", algo que debe cumplirse
      sí o sí.
    - Los setters no siempre hay que ponerlos, sólo cuando sea necesario que modifiquen "directamente" los objetos.
    - Quitamos inicialización a 0 ya que no se le dará valor directamente más que en la creación del objeto.
    - Reestructuración de funciones, para mayor legibilidad.
    - El método "convierte_a_segundos" hay que hacerlo como estático, para que sea utilizable por otros objetos, pero no
      público. --> esto bajo mi punto de vista complica el código, pero es más correcto al no crear metodos públicos
      no solicitados.
    - Queda pendiente realizar las funciones de suma y resta de dos objetos.
    """

    def __init__(self, horas, minutos, segundos):
        """
        Constructor de la clase
        :param horas: número de horas recibidas
        :param minutos: número de minutos
        :param segundos: número de segundos
        """
        #   assert dará error si no se cumplen las condiciones que marca, debería mostrar en pantalla el error
        #   en vez de fallar el programa, pero esto se hará mediante el uso de excepciones que se verán más adelante.
        assert horas >= 0 and 0 <= minutos < 60 and 0 <= segundos < 60
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos

    # Propiedades
    @property
    def horas(self):
        return self.__horas

    @property
    def minutos(self):
        return self.__minutos

    @property
    def segundos(self):
        return self.__segundos

    # Métodos (funcionalidades)
    def sumar_segundos_objetos (self, otro):
        tiempo_segundos = Tiempo.__segundos_total(self) + Tiempo.__segundos_total(otro)
        assert tiempo_segundos >= 0
        suma_tiempos = Tiempo.__segundos_a_tiempo(tiempo_segundos)
        self.__horas, self.__minutos, self.__segundos = suma_tiempos.horas, suma_tiempos.minutos, suma_tiempos.segundos

    def restar_segundos_objetos(self, otro):
        tiempo_segundos = Tiempo.__segundos_total(self) - Tiempo.__segundos_total(otro)
        assert tiempo_segundos >= 0
        resta_tiempos = Tiempo.__segundos_a_tiempo(tiempo_segundos)
        self.__horas, self.__minutos, self.__segundos = resta_tiempos.horas, resta_tiempos.minutos, resta_tiempos.segundos
        
    def sumar_horas(self, valor_horas):
        """
        Suma horas al objeto, si el resultado es negativo lanza una excepción.
        :param valor_horas:
        """
        assert self.__horas + valor_horas >= 0
        self.__horas += valor_horas

    def sumar_minutos(self,valor_minutos):
        """
        Suma minutos al objeto, si las horas finales son negativas lanza una excepción.
        :param valor_horas:
        """
        seg = Tiempo.__segundos_total(self)+valor_minutos*60
        assert seg > 0 # si los segundos son negativos el estado es inconsistente y lanza una excepción.
        resultado = Tiempo.__segundos_a_tiempo(seg)
        self.__horas, self.__minutos, self.__segundos = resultado.horas, resultado.minutos, resultado.segundos

    def sumar_segundos(self,valor_segundos):
        seg = Tiempo.__segundos_total(self) + valor_segundos
        assert seg > 0  # si los segundos son negativos el estado es inconsistente y lanza una excepción.
        resultado = Tiempo.__segundos_a_tiempo(seg)
        self.__horas, self.__minutos, self.__segundos = resultado.horas, resultado.minutos, resultado.segundos

    def restar_horas(self, valor_horas):
        """
        reutilizamos la función sumar horas, aunque se podría haber hecho de forma similar igualmente.
        :param valor_horas:
        """
        self.sumar_horas(-valor_horas)

    def restar_minutos(self,valor_minutos):
        self.sumar_minutos(-valor_minutos)

    def restar_segundos(self,valor_segundos):
        self.sumar_segundos(-valor_segundos)

    # Esta función permite que cuando se llame al objeto como si fuese una cadena, recurra a ella.
    def __str__(self):
        return f"{self.__horas}h {self.__minutos}m {self.__segundos}s."

    @staticmethod
    def comprueba_minutos_segundos(value):
        return type(value) == type(1) and value >=0 and value <60

    @staticmethod
    def __segundos_total(t):
        return t.horas*3600 + t.minutos*60 + t.segundos

    @staticmethod
    def __segundos_a_tiempo(seg):
        horas = (seg) // 3600
        minutos = ((seg) - (horas * 3600)) // 60
        segundos = (seg) - horas * 3600 - minutos * 60
        return Tiempo(horas, minutos, segundos)

if __name__ == "__main__":
    print("Tiempo1:")
    t1 = Tiempo(1, 25, 30)
    print(t1)

    h = int (input(f"Horas a sumar a {t1}: "))
    t1.sumar_horas(h)
    print(f"Ahora t1 es {t1}")

    m = int(input(f"Minutos a sumar a {t1}: "))
    t1.sumar_minutos(m)
    print(f"Ahora t1 es {t1}")

    s = int(input(f"Segundos a sumar a {t1}: "))
    t1.sumar_segundos(s)
    print(f"Ahora t1 es {t1}")

    h = int (input(f"Horas a restar a {t1}: "))
    t1.restar_horas(h)
    print(f"Ahora t1 es {t1}")

    m = int(input(f"Minutos a restar a {t1}: "))
    t1.restar_minutos(m)
    print(f"Ahora t1 es {t1}")

    s = int(input(f"Segundos a restar a {t1}: "))
    t1.restar_segundos(s)
    print(f"Ahora t1 es {t1}")

    t1 = Tiempo(1, 10, 20)
    t2 = Tiempo(0, 2, 30)
    print(f"t1 = {t1}")
    print(f"t2 = {t2}")
    t1.sumar_segundos_objetos(t2)
    print(f"suma de t1 y t2 = {t1}")

    print("Ahora volvemos a restar t2")
    t1.restar_segundos_objetos(t2)
    print(t1)

