"""
Ejercicio corregido y comentando en clase.

2. Crea un programa que encripte un fichero que le pasamos como parámetro y almacene el resultado en otro, que también pasamos como parámetro, de manera que:
        ARCHIVO EXISTENTE PARA HACER PRUEBA DE LECTURA: prueba01.txt
-- Si el programa no recibe dos parámetros termina con un error 1.--
-- Si el programa recibe un solo parámetro guardará la información encriptada en el mismo archivo del que lee, pero antes advertirá al usuario de que machacará el archivo origen, dando opción a que la operación no se haga.
Si el fichero origen no existe (da error al abrirlo como lectura) el programa termina con un mensaje de error y código 2.
Si en el fichero destino no se puede escribir da error al abrirlo como lectura) el programa termina con un mensaje de error y código 2.
Para encriptar usa el método César (sólo con los caracteres alfabéticos normales, sin tildes ni Ñ), necesitarás una clave que debes pedir al usuario.
"""
import string

def encripta_cesar(cadena, desplazamiento):
    """
    Encripta la cadena recibida como parámetro.
    :param cadena: 
    :param desplazamiento: 
    :return: 
    """

    letras = string.ascii_letters
    cadena_encriptada = ""
    for caracter in cadena:
        # si el carácter es alfabético, encriptamos
        if caracter in letras:
            posicion_donde_esta = letras.index(caracter)
            # esta función sustituiría a la habitual que venía utilizando en las líneas 45 y siguientes de la versión 1.
            # es más efectiva, ya que si pones una clave muy grande no da error.
            posicion_caracter_encriptado = (posicion_donde_esta + desplazamiento) % len(letras)
            caracter_encriptado = letras[posicion_caracter_encriptado]
        else:
            caracter_encriptado = caracter
        # chr (caracter) indicaría el valor ASCII de caracter
        # chr (65) indicaría el valor ASCII corresponiente a esa posición, ej: A
        #caracter_encriptado = chr(ord(caracter) + desplazamiento)
        cadena_encriptada += caracter_encriptado
    return cadena_encriptada

import sys

# ¿Número de parámetros correcto?
if len(sys.argv) < 2 or len(sys.argv) > 3:
    # mandamos el mensaje a la salida de error: sys.stderr (por defecto es sys.stdout)
    # si ponemos ls > borram.txt en la terminal, no se muestra nada en pantalla, y lo que debería haber salido, se guarda en ese archivo.
    # en este caso lo que hacemos, es, que en caso de que haya más parámetros de la cuenta o menos, que mande el mensaje con el formato
    # que corresponde a la salida de errores.
    print("Error en el número de parámetros.", file=sys.stderr)
    exit(1)

# Averiguamos fichero origen y destino
fichero_origen = sys.argv[1]
if len(sys.argv)==2:
    fichero_destino = fichero_origen
    # Advertimos de la sobreescritura del archivo en caso de continuar.
    print(f"Tenga en cuenta que sólo ha indicado un nombre de archivo: {fichero_origen}\n"
          f"esta operación machacará los datos de este fichero.")
    while True:
        respuesta = input("¿Desea continuar? (S/N)").upper()
        if respuesta in ("S", "N"):
            break
    if respuesta == "N":
        exit(0)
else:
    fichero_destino = sys.argv[2]

# Abrimos fichero de origen.
try: # ¿existe el fichero?
    manejador_origen = open(f"github/ficheros/encriptado/{fichero_origen}", "r")
except FileNotFoundError:
    print("No se ha podido abrir", fichero_origen)
    exit(2)

# Leemos fichero de origen.
origen = manejador_origen.readlines()
manejador_origen.close()

# Pedimos desplazamiento para el método César
desplazamiento = ""
while True:
    try:
        desplazamiento = int(input(f"Clave para la encriptación usando César: "))
    except ValueError:
        print(f"Tiene que introducir un valor entero.")
    else:
        break

# Abrir fichero destino (donde encriptaremos)
try: # ¿puedo escribir en el fichero?
    manejador_destino = open(f"github/ficheros/encriptado/{fichero_destino}", "w")
except PermissionError or FileNotFoundError:
    print("No se ha podido abrir para escritura.", fichero_destino)
    exit(2)

# Encriptamos y escribimos.
for linea in origen:
    manejador_destino.write(encripta_cesar(linea, -desplazamiento))
print(f"Archivo encriptado correctamente.")
manejador_destino.close()