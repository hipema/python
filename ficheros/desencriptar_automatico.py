"""
Desencriptado automático. Corrección clase. Comprobando conexión con RAE

2. Crea un programa que encripte un fichero que le pasamos como parámetro y almacene el resultado en otro, que también pasamos como parámetro, de manera que:
        ARCHIVO EXISTENTE PARA HACER PRUEBA DE LECTURA: prueba01.txt
-- Si el programa no recibe dos parámetros termina con un error 1.--
-- Si el programa recibe un solo parámetro guardará la información encriptada en el mismo archivo del que lee, pero antes advertirá al usuario de que machacará el archivo origen, dando opción a que la operación no se haga.
Si el fichero origen no existe (da error al abrirlo como lectura) el programa termina con un mensaje de error y código 2.
Si en el fichero destino no se puede escribir da error al abrirlo como lectura) el programa termina con un mensaje de error y código 2.
Para encriptar usa el método César (sólo con los caracteres alfabéticos normales, sin tildes ni Ñ), necesitarás una clave que debes pedir al usuario.
"""
import string
import requests

MAX_PALABRAS = 25
PORCENTAJE_EXITO = 0.75
LETRAS = string.ascii_letters +"áéíóúüÁÉÍÓÚÜ"

def encripta_cesar(cadena, desplazamiento):
    """
    Encripta la cadena recibida como parámetro.
    :param cadena:
    :param desplazamiento:
    :return:
    """

    letras = string.ascii_letters +"áéíóúüÁÉÍÓÚÜ"
    cadena_encriptada = ""
    for linea in cadena:
        for caracter in linea:# si el carácter es alfabético, encriptamos
            if caracter in letras:
                posicion_donde_esta = letras.index(caracter)
                # esta función sustituiría a la habitual que venía utilizando en las líneas 45 y siguientes de la versión 1.
                # es más efectiva, ya que si pones una clave muy grande no da error.
                posicion_caracter_encriptado = (posicion_donde_esta + desplazamiento) % len(letras)
                if posicion_caracter_encriptado < 0:
                    posicion_caracter_encriptado = len(letras) + posicion_caracter_encriptado
                caracter_encriptado = letras[posicion_caracter_encriptado]
            else:
                caracter_encriptado = caracter
            # chr (caracter) indicaría el valor ASCII de caracter
            # chr (65) indicaría el valor ASCII corresponiente a esa posición, ej: A
            #caracter_encriptado = chr(ord(caracter) + desplazamiento)
            cadena_encriptada += caracter_encriptado
    return cadena_encriptada

def palabras_en_rae(lista, max_palabras):
    palabras = []
    aciertos = 0

    # separo las palabras de cada línea y las añado
    palabras.extend(lista_palabras(lista)) # este método extiende la lista con el contenido de otra lista, no añade una lista dentro de otra.
    # ¿tenemos palabras suficientes?
    if len(palabras) >= max_palabras:
        palabras = palabras[:max_palabras] # recorta la lista al máximo de 25 que vamos a comprobar.

    for palabra in palabras:
        if palabra_en_rae(palabra):
            aciertos +=1

    return aciertos / len(palabras) # tasa de aciertos

def lista_palabras(cadena):
    palabras = []
    palabra = ""

    for caracter in cadena:
        if caracter in LETRAS:
            palabra += caracter
        elif palabra != "":
            palabras.append(palabra)
            palabra = ""
    return palabras

def palabra_en_rae(palabra):
    response = requests.get("https://dle.rae.es/?w=" + palabra)
    if response.status_code != 200:
        print ("Error al acceder a la RAE.", file=sys.stderr)
        exit(5)

    # Devolvemos si la cadena no se encuentra en la url
    return not "Aviso: <span>La palabra <b>"+ palabra + "</b> no está en el Diccionario." in response.text

import sys

# ¿Número de parámetros correcto?
if len(sys.argv) < 2 or len(sys.argv) > 3:
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
    print("No se ha podido abrir", fichero_origen, file=sys.stderr)
    exit(2)

# Leemos fichero de origen.
origen = manejador_origen.readlines()
manejador_origen.close()

# Abrir fichero destino (donde encriptaremos)
try: # ¿puedo escribir en el fichero?
    manejador_destino = open(f"github/ficheros/encriptado/{fichero_destino}", "w")
except PermissionError or FileNotFoundError:
    print("No se ha podido abrir para escritura.", fichero_destino, file=sys.stderr)
    exit(2)

# Probamos a desencriptar y buscamos opción
solucion_encontrada = False
for desplazamiento in range (len(LETRAS)):
    print("Probando con desplazamiento", desplazamiento, "...")
    posible_solucion = encripta_cesar(origen, -desplazamiento)
    if palabras_en_rae(posible_solucion, MAX_PALABRAS) >= PORCENTAJE_EXITO:
        solucion_encontrada = True
        break
# Si no ha encontrado solución:
if not solucion_encontrada:
    print("No se ha podido desencriptar el archivo", file=sys.stderr)
    exit(4)

for linea in origen:
    manejador_destino.write(encripta_cesar(linea, -desplazamiento))
print(f"Archivo encriptado correctamente.")
manejador_destino.close()