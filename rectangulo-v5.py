class Rectangulo:
    """
    Versión 3.01.
    Esta clase representa objetos de tipo rectángulo.
    Acciones: cálculo del perímetro, área, dibujar, comparar.
    Mejoras respecto a la versión 1:
    - Quitamos getters y setters estilo Java y los sustituimos por propiedades.
    - Usaremos métodos privados y estáticos.
    - Usaremos variables de instancia de clase.

    Mejoras de la clase 3.1
    - Añadimos destructor para cambiar el contador de __num_creados.
    - Ponemos assert
    - sobrecargamos operador *
    """

    # Variables de instancia (propiedades comunes que pueden tener dos objetos distintos)
    lado_maximo = 10 # lado máximo del rectángulo (esta puede ser modificada por el usuario)
    __num_creados = 0 # contador de rectángulos creados (esta es privada y no se puede modificar por el usuario)

    def __init__(self, base, altura):
        """
        Constructor de la clase.
        :param base: base del rectángulo.
        :param altura: altura del rectángulo.
        """
        self.__base = 1
        self.__altura = 1
        Rectangulo.__num_creados += 1
        # por si hubiera errores en los parámetros hemos dado valor inicial
        self.base = base
        self.altura = altura

    def __del__(self):
        """
        Quita un objeto de memoria y resta uno en el contador.
        :return:
        """
        Rectangulo.__num_creados -=1

    # propiedades

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, value):
        assert self.es_lado_correcto(value)
        self.__base = value

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, value):
        assert Rectangulo.es_lado_correcto(value)
        self.__altura = value

    # resto métodos

    @staticmethod
    def num_rectangulos():
        return Rectangulo.__num_creados

    @staticmethod
    def es_lado_correcto(value):
        return type(value) == type(1) and 0 < value <= Rectangulo.lado_maximo

    def perimetro(self):
        """
        :return: perímetro del rectángulo.
        """
        return 2 * (self.base + self.altura)

    def area(self):
        """
        :return: área del rectángulo.
        """
        return self.base * self.altura

    def compara(self, otro):
        """
        Compara nuestro rectángulo con otro.
        :param otro: objeto con el que comparamos el actual.
        :return: >0 si mayor, 0 si igual, <0 si menor.
        """
        return self.area() - otro.area()

    def es_gemelo(self, otro):
        """
        Comprueba si el objeto pasado es el mismo rectángulo, o sea,
        tiene la misma base y altura.
        :param otro: objeto con el que comparamos el actual.
        :return: True o False
        """
        return self.base == otro.base and self.altura == otro.altura

    def muestra(self):
        """
        Muestra en pantalla el rectángulo.
        """
        print(self)

    # métodos sobrecargados

    def __str__(self):
        str = ""
        for i in range(self.altura):
            str += "*" * self.base
            str += "\n"
        str = str[:-1]
        return str

    """
    Las siguientes funciones se aplican para poder "interpretar" las funciones utilizando los operadores *, <, <=...
    Implementando los <, <= e ==, python automáticamente implementa >, >= y !=.
    """
    def __mul__(self, other):
        """
        Multiplica la base si nose pasa del lado máximo, en ese caso, lo hace con la altura.
        :param other: este es el número que se le manda por el que se ha de multiplicar.
        :return: Otro rectángulo con la superficie original * other
        """
        assert type(other)==type(1) and other > 0 # comprueba que el operando sea correcto.
        assert self.base * other <= Rectangulo.lado_maximo or self.altura*other <= Rectangulo.lado_maximo
        if self.base * other <= Rectangulo.lado_maximo:
            return Rectangulo(self.base*other,self.altura)
        else:
            return Rectangulo(self.base, self.altura * other)

    def __rmul__(self, other):  # Esta función es igual que la anterior, pero sirve para multiplicar cuando el parámetro
                                # se pasa antes que el objeto.
        return self * other

    def __lt__(self, other):
        """
        Comprueba si un rectángulo es menor que otro (área)
        :param other:
        :return:
        """
        assert isinstance(other, Rectangulo) #comprueba si other es un objeto Rectangulo.
        return self.area() < other.area()

    def __le__(self, other):
        """
        Comprueba si un rectángulo es menor o igual a otro.
        :param other:
        :return:
        """
        assert isinstance(other, Rectangulo)
        return self.area() <= other.area()

    def __eq__(self, other):
        """
        Comprueba si un rectángulo es igual a otro.
        :param other:
        :return:
        """
        assert isinstance(other, Rectangulo)
        return self.area() == other.area()

if __name__ == "__main__":
    r1 = Rectangulo(8, 1)
    r2 = Rectangulo(3, 2)
    print(f"Probamos clase rectángulo con r1: ({r1.base},{r1.altura}) y "
          f"r2: ({r2.base},{r2.altura})\n")
    # mostramos
    r1.muestra()
    print()
    r2.muestra()
    # comparamos
    print("Resultado de comparar r1 con r2:", r1.compara(r2))
    print("¿Son gemelos?", r1.es_gemelo(r2))
    # magnitudes
    print("Área r1:", r1.area(), "Perímetro r1:", r1.perimetro())
    print("Área r2:", r2.area(), "Perímetro r2:", r2.perimetro())
    # accedemos a variables de instancia de clase
    print("Rectángulos creados", Rectangulo.num_rectangulos())

    print("Eliminamos el rectángulo 1")
    del r1
    # print(r1) si lo ponemos visto, daría error porque ya se ha borrado el objeto.
    print("Multiplicamos el r2 * 2")
    print(2*r2)