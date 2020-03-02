"""
Excepciones.

TIPOS DE ERRORES:
- Compilación / Sintaxis (fáciles de solucionar, porque hasta que no lo haces no va el programa).

- Ejecución.

    try
    except <tipo_es_opcional>
    else (cosas a hacer si el proceso salió bien y no se produjo excepción)
    finally (este código se realizará igualmente, haya habido fallos o no)
"""
print("Introducción a las excepxiones.")
try:
    numero = int(input("Introducir un número: "))
    factorial = 1
    for num in range(1,numero+1):
        factorial *= num

    print (factorial)

except:
    print("Debe introducir un número entero")

print("----------------------------------")
print("2ª Prueba:")

try:  # Bloque de código a “vigilar”
    texto = input('Teclear :')  # introducir un dato

except KeyboardInterrupt:  # captura excepción de interrupción
    print('\nSe ha pulsado ctrl+c')  # Interrupción al presionar Ctrl+c

else:  # se ejecuta si no hay error
    print('Ha tecleado {}'.format(texto))  # muestra cadena introducida

finally:  # se ejecuta tanto si hay error como si no
    print('fin de programa')  # muestra mensaje final

print("----------------------------------")
print("3ª Prueba, excepciones a medida:")


# Define clase a partir de Exception
class LongPassw(Exception):
    '''Excepción definida por usuario'''

    def __init__(self, longitud):  # define método constructor ...
        Exception.__init__(self)  # … de excepción ...
        self.longitud = longitud  # … y con atributo longitud


try:  # bloque de código a vigilar
    clave = input('Teclear contraseña: ')  # introducir una cadena
    if len(clave) < 6:  # si longitud de cadena es menor de 6
        raise LongPassw(len(clave))  # llama a excepción de usuario

except LongPassw as lp:  # excepción de usuario
    print(f'LongPassw: Error por longitud: {0}'.format(lp.longitud))

else:  # se ejecuta si no hay error
    print('No se ha producido error.')  # muestra mensaje