class Fecha:
    """
    Creamos la clase Fecha para adaptarla al ejercicio de funciones realizado como exámen del primer Trimestre.
    Colección de funciones para manejar fechas en cadenas de caracteres.
    El formato de la cadena es: AAAAMMDD.
    Ejemplo: El 15 de diciembre de 2019 sería: "20191215"
    Colección de funciones:
    -1. fecha_correcta: dice si la fecha que se pasa como parámetro es correcta.
    2. fecha_mas_1dia: suma un día a la fecha que se pasa como parámetro y lo devuelve.
    3. fecha_mas_ndias: suma una serie de días a la fecha que se pasa como parámetro y lo devuelve.
    4. fecha_menos_1dia: resta un día a la fecha que se pasa como parámetro y lo devuelve.
    5. fecha_menos_ndias: resta una serie de días a la fecha que se pasa como parámetro y lo devuelve.
    -6. es_bisiesto: dice si la fecha que se pasa como parámetro es bisiesto.
    7. compara_fechas: recibe dos fechas y devuelve un valor negativo si la 1ª es anterior a la
      segunda, cero si son iguales, y un valor positivo si la 1ª es posterior a la segunda.
    -8. fecha_formateada: recibe un fecha y devuelve una cadena con el formato:
      DD de {MES} de AAAA     (Ejemplo: "15 de Diciembre de 2019")
    -9. año, mes, dia, nombre_mes: recibe un fecha y devuelve esos valores.
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
    def sumar_dia (self):
        dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if Fecha.es_bisiesto(self.anyo):
            dias_mes[1] = 29
        ultimo_dia_mes = dias_mes[self.mes-1]
        dia = self.dia
        mes = self.mes
        dia += 1
        if dia > ultimo_dia_mes:  # mes siguiente si no es 29/2 y bisiesto
            # mes siguiente
            dia = 1
            mes += 1
            if mes > 12:  # nos pasamos de diciembre, año siguiente
                mes = 1
                self.anyo += 1
        self.dia = dia
        self.mes = mes

    # Sumar n días a fecha.
    def sumar_n_dias (self, value):
        i = 0
        while i < value:
            self.sumar_dia()
            i +=1

    # Restar un día a fecha.
    def restar_dia (self):
        dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if Fecha.es_bisiesto(self.anyo):
            dias_mes[1] = 29
        dia = self.dia
        mes = self.mes
        dia -= 1
        if dia == 0:
            mes -= 1
            if mes < 1:  # pasamos de enero, a diciembre.
                mes = 12
                self.anyo -= 1
                dia = dias_mes[mes-1]
            dia = dias_mes[mes-1]
        self.mes = mes
        self.dia = dia

    # Restar n días a fecha.
    def restar_n_dias (self, value):
        i = 0
        while i < value:
            self.restar_dia()
            i += 1

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
        dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if Fecha.es_bisiesto(anyo):
            dias_mes[1] = 29
        return 0 < dia <= dias_mes[mes - 1] # dia > 0 and dia <= dias_mes[mes-1]

    def es_bisiesto (anyo):
        return anyo % 400 == 0 or (anyo % 4 == 0 and anyo % 100 != 0)

    # Sobrecarga
    def __str__(self):
        return f"{self.dia} de {self.nombre_mes()} de {self.anyo}"

# Probamos la clase.
if __name__ == "__main__":
    f1 = Fecha(5, 2, 2020)
    print(f1)

    print("Sumamos un día a la fecha")
    f1.sumar_dia()
    print(f1)

    print("Sumamos 24 día al mes")
    f1.sumar_n_dias(24)
    print(f1)

    print("Restamos 1 día a la fecha")
    f1.restar_dia()
    print(f1)

    print("Restamos 59 dias a la fecha")
    f1.restar_n_dias(60)
    print(f1)
