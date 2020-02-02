class Fraccion:
    """
    Versión 2.0
    Ejercicio POO Fracción.
    Falla en la función de simplificar fracción.

    Cambios pendientes
    - Reorganizar para colocar el método estático para obtener "fracciones" como cadena
    - Nueva función para simplificar fracción, probablemente hacer una relacionada con el mcd.
    """
    def __init__(self, numerador, denominador):
        self.__numerador = 1
        self.__denominador = 1

        self.numerador = numerador
        self.denominador = denominador

    @property
    def numerador(self):
        return self.__numerador

    @numerador.setter
    def numerador(self, valor_numerador):
        if Fraccion.comprueba_numerador(valor_numerador):
            self.__numerador = valor_numerador
        else:
            print("ERROR: el numerador debe ser un número entero")

    @property
    def denominador(self):
        return self.__denominador

    @denominador.setter
    def denominador(self, valor_denominador):
        if Fraccion.comprueba_denominador(valor_denominador):
            self.__denominador = valor_denominador
        else:
            print("ERROR: valor introducido incorrecto, comprueba que sea número entero distinto de 0.")

    def obtener_fraccion(self):
        return str(self.__numerador)+"/"+str(self.__denominador)

    def obtener_resultado (self):
        return self.__numerador/self.__denominador

    def obtener_numerador(self):
        return self.__numerador

    def obtener_denominador(self):
        return self.__denominador

    def modifica_numerador(self, nuevo_numerador):
        if self.comprueba_numerador(nuevo_numerador):
            self.__numerador = nuevo_numerador
        else:
            print("ERROR: Numerador incorrecto")

    def modifica_denominador(self, nuevo_denominador):
        if self.comprueba_denominador(nuevo_denominador):
            self.__numerador = nuevo_denominador
        else:
            print("ERROR: valor introducido incorrecto.")

    def multiplica_numero(self, numero):
        self.__numerador = self.__numerador * numero
        self.simplificar_fraccion()
        return str(self.__numerador)+"/"+str(self.__denominador)

    def multiplica_fracciones (self, otra):
        self.__numerador = self.__numerador * otra.__numerador
        self.__denominador = self.__denominador * otra.__denominador
        self.simplificar_fraccion()
        return str(self.__numerador)+"/"+str(self.__denominador)

    def sumar_fracciones (self,otra):
        self.__numerador = (self.__numerador * otra.__denominador)+(otra.__numerador * self.__denominador)
        self.__denominador = self.__denominador * otra.__denominador
        self.simplificar_fraccion()
        return str(self.__numerador)+"/"+str(self.__denominador)

    def restar_fracciones (self,otra):
        self.__numerador = (self.__numerador * otra.__denominador)-(otra.__numerador * self.__denominador)
        self.__denominador = self.__denominador * otra.__denominador
        self.simplificar_fraccion()
        return str(self.__numerador)+"/"+str(self.__denominador)

    def mcd(self):
        dividendo = self.__numerador
        divisor = self.__denominador
        resto = dividendo%divisor
        while resto != 0:
            dividendo = divisor
            divisor = resto
            resto = dividendo%divisor
        return divisor

    def simplificar_fraccion (self):
        divisor = self.mcd()
        self.__numerador = int (self.__numerador/divisor)
        self.__denominador = int (self.__denominador/divisor)

    def __str__(self):
        return f"{self.__numerador} / {self.__denominador}"

    @staticmethod
    def comprueba_denominador(value):
        return type(value) == type(1) and value != 0

    @staticmethod
    def comprueba_numerador(value):
        return type(value) ==  type(1)

if __name__ == "__main__":
    print("Creamos fracción 12/36:")
    f1 = Fraccion(12,36)

    print("Mostramos fracción: "+ f1.obtener_fraccion())

    print (f"Numerador {f1.obtener_numerador()}")
    print (f"Denominador {f1.obtener_denominador()}")

    print ("Cambiamos numerador a 4")
    f1.modifica_numerador(4)
    print(f"Nuevo numerador {f1.obtener_numerador()}")

    print("Cambiamos denominador a 8")
    f1.modifica_denominador(8)
    print(f"Nuevo denominador {f1.obtener_denominador()}")

    print(f"Resultado de la fracción: {f1.obtener_resultado()}")

    print("Multiplicar fracción por \"n\" (ej.5): ")
    print(f"La fracción resultante es {f1.multiplica_numero(5)}, cuyo resultado es {f1.obtener_resultado()}")

    print("Multiplicar fracción por otra fracción (3/6):")
    f2 = Fraccion(3,6)
    print(f"La fracción resultante es {f1.multiplica_fracciones(f2)}")

    print("Sumar dos fracciones (3/4) y (2/3)")
    f3 = Fraccion(3,4)
    f4 = Fraccion(2,3)
    print(f"Resultado de fracción1: {f3.obtener_resultado()}")
    print(f"Resultado de fracción2: {f4.obtener_resultado()}")
    print(f"Suma de resultados es: {f3.obtener_resultado()+f4.obtener_resultado()}")
    print(f"La fracción resultante es {f3.sumar_fracciones(f4)}, cuyo resultado es {f3.obtener_resultado()}")

    print("Restar dos fracciones (18/4) y (2/3)")
    f3 = Fraccion(18, 4)
    f4 = Fraccion(2, 3)
    print(f"Resultado de fracción1: {f3.obtener_resultado()}")
    print(f"Resultado de fracción2: {f4.obtener_resultado()}")
    print(f"Resta de resultados es: {f3.obtener_resultado() - f4.obtener_resultado()}")
    print(f"La fracción resultante es {f3.restar_fracciones(f4)}, cuyo resultado es {f3.obtener_resultado()}")

    f5 = Fraccion(2100, 180)
    print(f"Fracción es (2100/180), cuyo resultado es {f5.obtener_resultado()}")
    f5.simplificar_fraccion()
    print(f"Simplificamos fracción resultando {f5.obtener_fraccion()} cuyo resultado es {f5.obtener_resultado()}")

    print(f5)