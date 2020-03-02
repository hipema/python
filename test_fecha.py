"""
Probamos la clase fecha.
"""
from github.fecha_excepciones import FechaErronea, Fecha

while True:
    try:
        # Pido la fecha
        dia = int(input("Dia para construir la fecha: "))
        mes = int(input("Mes para construir la fecha: "))
        anyo = int(input("Año para construir la fecha: "))
        # Construyo la fecha
        fecha = Fecha(dia, mes, anyo)
        print(f"La fecha introducida es: {fecha}")
    except FechaErronea:
        input("Ha introducido una fecha inválida, vuelva a intentarlo.")
    except:
        input("Ha introducido valores para día, mes o año que no son enteros.")
    else: # si son correctos los valores
        break
