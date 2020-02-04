class Fecha:
    """
    Creamos la clase Fecha para adaptarla al ejercicio de funciones realizado como exámen del primer Trimestre.
    Colección de funciones para manejar fechas en cadenas de caracteres.
    El formato de la cadena es: AAAAMMDD.
    Ejemplo: El 15 de diciembre de 2019 sería: "20191215"
    Colección de funciones:
    -1. fecha_correcta: dice si la fecha que se pasa como parámetro es correcta.
    -2. fecha_mas_1dia: suma un día a la fecha que se pasa como parámetro y lo devuelve.
    -3. fecha_mas_ndias: suma una serie de días a la fecha que se pasa como parámetro y lo devuelve.
    -4. fecha_menos_1dia: resta un día a la fecha que se pasa como parámetro y lo devuelve.
    -5. fecha_menos_ndias: resta una serie de días a la fecha que se pasa como parámetro y lo devuelve.
    -6. es_bisiesto: dice si la fecha que se pasa como parámetro es bisiesto.
    -7. compara_fechas: recibe dos fechas y devuelve un valor negativo si la 1ª es anterior a la
      segunda, cero si son iguales, y un valor positivo si la 1ª es posterior a la segunda.
    -8. fecha_formateada: recibe un fecha y devuelve una cadena con el formato:
      DD de {MES} de AAAA     (Ejemplo: "15 de Diciembre de 2019")
    -9. año, mes, dia, nombre_mes: recibe un fecha y devuelve esos valores.

    MODIFICACIONES: cambiamos los métodos de de sumar, y restar días para ponerlos privados.
                    las funciones de sumar y restar días debe devolver nuevos objetos, no modificar los valores
                    del actual.
                    Eliminamos funciones de sumar y restar n días al sobrecargar operadores.

    """

# Variables.
    #dia, mes, año
# Constructor.
    def __init__(self, dia, mes, anyo):
        assert Fecha.fecha_correcta(dia, mes, anyo)
        self.__dia = dia
        self.__mes = mes
        self.__anyo = anyo

    # Propiedades
    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, value):
        assert Fecha.fecha_correcta(value, self.mes, self.anyo)
        self.__dia = value

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, value):
        assert Fecha.fecha_correcta(self.dia, value, self.anyo)
        self.__mes = value

    @property
    def anyo(self):
        return self.__anyo

    @anyo.setter
    def anyo(self, value):
        assert Fecha.fecha_correcta(self.dia, self.mes, value)
        self.__anyo = value

    # Métodos
    def nombre_mes (self):
        meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
                 "Noviembre", "Diciembre"]
        return meses[self.__mes - 1]

    # Sumar un día
    def __sumar_dia (self):
        """
        Suma un día a la fecha.
        :return: Fecha almacenada + 1 día.
        """
        dia = self.dia +1
        mes = self.mes
        anyo = self.anyo
        if dia > Fecha.dias_mes(self.__mes, self.__anyo): # mes siguiente si no es 29/2 y bisiesto
            # mes siguiente
            dia = 1
            mes += 1
            if mes > 12:  # nos pasamos de diciembre, año siguiente
                mes = 1
                anyo += 1
        return Fecha(dia, mes, anyo)

    # Restar un día a fecha.
    def __restar_dia (self):
        dia = self.dia -1
        mes = self.mes
        anyo = self.anyo
        if dia == 0:
            mes -= 1
            if mes < 1:  # pasamos de enero, a diciembre.
                mes = 12
                anyo -= 1
            dia = Fecha.dias_mes(mes,anyo)
        return Fecha(dia, mes, anyo)

    def fecha_numerica (self):
        return int(f"{self.anyo}{self.mes}{self.dia}")

    # Compara fechas
    def compara_fechas (self, otra):
        fecha1 = (int)(f"{self.anyo}{self.mes}{self.dia}")
        fecha2 = (int)(f"{otra.anyo}{otra.mes}{otra.dia}")
        return fecha1 - fecha2

    # Métodos estáticos (de la clase)
    @staticmethod
    def fecha_correcta (dia, mes, anyo):
        # tipo de dato correcto
        if not isinstance(dia,int) or not isinstance(mes,int) or not isinstance(anyo,int): # sería igual a
            # type(dia) != type(1) or type(mes) != type(1) or type(anyo) != type(1):
            return False
        # año correcto
        if anyo < 0:
            return False
        # mes correcto
        if mes < 1 or mes > 12:
            return False
        # dia correcto
        return 0 < dia <= Fecha.dias_mes(mes, anyo) # dia > 0 and dia <= dias_mes[mes-1]

    @staticmethod
    def dias_mes(mes, anyo):
        """
        Devuelve el número de días que tiene el mes actual.
        :return:
        """
        dias_mes_ = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if Fecha.es_bisiesto(anyo):
            dias_mes_[1] = 29
        return dias_mes_[mes - 1]

    def es_bisiesto (anyo):
        return anyo % 400 == 0 or (anyo % 4 == 0 and anyo % 100 != 0)

    # Sobrecarga
    def __str__(self):
        return f"{self.dia} de {self.nombre_mes()} de {self.anyo}"

    def __eq__(self, other):
        """
        Comprueba si una fecha es igual a otra.
        :param other: objeto fecha recibido para la comprobación.
        :return: devuelve verdadero o falso.
        """
        return self.compara_fechas(other) == 0

    def __lt__(self, other):
        """
        Comprueba si una fecha es menor que otra.
        :param other: objeto fecha recibido para la comprobación.
        :return: devuelve verdadero o falso
        """
        return self.compara_fechas(other) < 0

    def __add__(self, value):
        fecha = self
        for i in range (value):
            fecha = fecha.__sumar_dia()
        return fecha

    def __radd__(self, value):
        return self + value

    def __sub__(self, value):
        fecha = self
        for i in range (value):
            fecha = fecha.__restar_dia()
        return fecha

    def __rsub__(self, value):
        return self + value

# Probamos la clase.
if __name__ == "__main__":
    f1 = Fecha(5, 2, 2020)
    print(f1)

    print("Sumamos un día a la fecha")
    print(f1+1)

    print("Sumamos 24 día al mes")
    print(f1+24)

    print("Restamos 1 día a la fecha")
    print(f1-1)

    print("Restamos 59 dias a la fecha")
    print(f1-59)

    print("Sumamos 5 días a f1")
    print(f1+5)

    print("Restamos 5 días a f1")
    print(f1-5)

    print("Comparamos fecha1 (01-02-2009) y fecha2 (02-03-2005")
    f1 = Fecha(1,2,2010)
    f2 = Fecha(1,2,2009)
    print("Comparamos fechas:")
    print(f"El resultado es: {f1.compara_fechas(f2)}")

    print(f"¿Es mayor f1 que f2?: {f1>f2}")