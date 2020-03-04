"""
1. Modifica el ejercicio 1 del tema anterior de manera que:

El programa admita dos parámetros:
El primero es la ciudad de la que vamos a sacar el pronóstico de la temperatura, si la ciudad es errónea el programa termina con un mensaje de error y código 2.
El segundo es opcional, y si existe es el directorio donde vamos a crear un fichero html con la información formateada como una tabla del pronóstico de la temperatura, si no existe la información se muestra por pantalla. Consideraciones:
este fichero tendrá por nombre: {CIUDAD}_{FECHA-INICIO}_{FECHA_FIN}, ejemplo: "Cordoba_2020-02-27-12:00:00_2020-03-03-09:00:00.html"
si el fichero no se puede crear el programa termina con un mensaje de error y código 3.
Si el programa no recibe ningún parámetro o recibe más de dos terminará con un mensaje de error (código 1) diciendo que la sintaxis es incorrecta.
Si el programa recibe un solo parámetro y este es "-h" el programa muestra un texto explicando qué hace.

LOGICA DEL PROGRAMA:
1.- Petición al usuario de parámetros:
    - Parámetro 1: Ciudad -->   comprobar si ciudad existe, sino mostrar error (Código 2) -(utilizar Try)
    - Parámetro 2 (opcional):   crea directorio donde guardar el archivo. Si el archivo no existe lo guarda con el formato indicado.
                                {CIUDAD}_{FECHA-INICIO}_{FECHA_FIN}, ejemplo: "Cordoba_2020-02-27-12:00:00_2020-03-03-09:00:00.html
                                Si el archivo no se puede crear, el programa termina con un error (Código 3)
    - Si parámetro 1 está vacío  --> mensaje de error (Código 1: La sintaxis es incorrecta)
    - Si parámetro 1 es "-h" el programa muestra una explicación de su funcionamiento.

    Pedimos parámetro 1:
        - si "" --> error Codigo 1: La sintaxis incorrecta -- realizado
        - si "-h" --> enviamos explicación funcionamiento (función) -- realizado
        - si otro parámetro
            - comprobamos si requests.response != 200 --> Código 2 -- realizado
            - si requests.response == 200. continúa el programa -- realizado
    Pedimos parámetro 2:
        - si "" --> continúa el programa mostrando datos por pantalla. -- realizado
        - si /directorio:
            - comprobamos si directorio ya existe
                    - NO existe: crea el directorio
                    - Si existe: continúa programa
            - guardamos fichero con el formato indicado.: {CIUDAD}_{FECHA-INICIO}_{FECHA_FIN}, ejemplo: "Cordoba_2020-02-27-12:00:00_2020-03-03-09:00:00.html
            si en este proceso da error: muestra mensaje de error código 3
"""

# Funciones a utilizar en el programa
# Creamos excepciones.
class Ciudad_incorrecta(Exception):
    '''Excepción que indica que el valor de la ciudad es incorrecto.'''

    def __init__(self, ciudad):  # define método constructor ...
        Exception.__init__(self)  # … de excepción ...
        self.ciudad = ciudad  # … y con atributo longitud
class Sintaxis_incorrecta(Exception):
    '''Excepción que captura la introducción de una sintaxis incorrecta'''
    def __init__(self):
        Exception.__init__(self)

class Mediciones_existentes(Exception):
    def __init__(self):
        Exception.__init__(self)

def inicio_archivo():
    inicio = (f'<!DOCTYPE html>\n<html lang="es">\n<head>\n\t<meta charset="UTF-8">\n\t<meta name="viewport" '
          f'content="width=device-width, initial-scale=1.0">\n\t<title>Lectura de temperaturas en {ciudad}</title>\n</head>\n<body>\n\t<center><p>'
              f'Este programa nos muestra los resultados de las mediciones para los próximos 5 días en {ciudad}\n\t\t<table>\n\t\t\t<tr>\n'
          f'\t\t\t\t<th>Día</th>\n\t\t\t\t<th>Temperatura Media</th>\n\t\t\t\t<th>Temperatura Mínima</th>\n\t\t\t\t<th>Temperatura Máxima</th>'
          f'\n\t\t\t\t<th>Nº Mediciones</th>\n        </tr>\n')
    return inicio

def final_archivo():
    final = (f'</table>\n</center> </body >\n </html>')
    return final
def mostrar_ayuda():
    print(f'\nEste programa muestra la temperatura de los próximos cinco días en una ciudad indicada por \n'
          f'el usuario siguiendo los siguientes detalles:\n'
          f'- En el primer parámetro, incluye la ciudad (no introducir tildes), en caso de una ciudad\n'
          f'  cuyo nombre se corresponda con otra de otro país, incluya la indicación del país. "ej: Cordoba,es".\n'
          f'- En el segunda parámetro, incluya la dirección donde desee guardar el archivo html donde se incluirá\n'
          f'  la información de las mediciones. Si no incluye ninguna dirección, la información se mostrará\n'
          f'  directamente en pantalla.\n')
    input('Pulse "Intro" para continuar con el programa')

import requests
import os
from datetime import datetime

# datos para hacer la petición
# Endpoint
url = "http://api.openweathermap.org/data/2.5/forecast"
# Parámetros
key = os.environ['OPENWEATHERID']
#key = "56e22addb36fca28311139f89294b092"
# Para crear la variable de entorno, vamos a "Run/Edit Cofigurations/Enviroment" y ahí añadimos el valor.
try:
    ciudad = "-h"
    while ciudad == "-h":
        ciudad = input(f'Introduce la ciudad que deseas buscar: ')
        parametros = {'q': ciudad, 'appid': key, 'units': 'metric'}
        respuesta = requests.get(url, params=parametros)
        if ciudad == "-h":
            mostrar_ayuda()
    if ciudad == "":
        raise Sintaxis_incorrecta ()
    if respuesta.status_code != 200:
        raise Ciudad_incorrecta(ciudad)

except Ciudad_incorrecta:
    print("No se encuentra la ciudad introducida.")
    exit(2)
except Sintaxis_incorrecta:
    print("Sintaxis incorrecta, Debe incluir la ciudad.")
    exit(1)

# Petición del segundo parámetro

try:
    directorio = input(f'Indica el directorio en el que deseas guardar el archivo.\n'
                       f'Deja vacío y Pulsa Intro para mostrar en pantalla.\n')
    existe_directorio = os.path.isdir('github/ficheros/temperaturas/'+directorio)
    if not existe_directorio:
        os.mkdir('github/ficheros/temperaturas/'+directorio)
except:
    print("Se ha producido un error al crear la ruta de destino.")

# petición
datos = respuesta.json()
# Cálculos
dias = dict() # diccionario con clave del día y valor, la lista de medicones del día.
totales = {'temp':[], 'temp_min':[], 'temp_max':[]} #lista de mediciones de todos los días donde almacenamos los valores obtenidos.
for medicion in datos['list']:
    # fecha y temperatura de la medición
    dia = medicion['dt_txt'][:10] #devuelve la cadena con los caracteres indicados, truncamos la fecha.
    temp = float(medicion['main']['temp']) # pasamos a número real, el valor obtenido.
    temp_min = float(medicion['main']['temp_min'])  # pasamos a número real, el valor obtenido.
    temp_max = float(medicion['main']['temp_max'])  # pasamos a número real, el valor obtenido.
    # si no tenemos datos de ese día creamos una nueva entrada en el dicionario
    if not dias.get(dia):
        dias[dia] = {'temp':[], 'temp_min':[], 'temp_max':[]} # en este caso, tiene un diccionario con tres listas vacías, diferencia respeto v2
    # añadimos medición (aquí si existe la clave de este día, bien porque ya exista o bien porque se acabaría de crear)
    dias[dia]['temp'].append(temp)
    dias[dia]['temp_min'].append(temp_min)
    dias[dia]['temp_max'].append(temp_max)
    totales['temp'].append(temp)
    totales['temp_min'].append(temp_min)
    totales['temp_max'].append(temp_max)

if directorio == "":
    # resultados
    print()
    for dia,temps in dias.items(): # recorremos los pares (dia para recorrer las claves, temps para recorrer los valores) items (recorre los pares)
        #\t --> realiza un tabulador - sum --> calcula el máximo de la lista - min --> calcula el mínimo de la lista
        print(f'Día {dia[8:]}-{dia[5:7]}-{dia[0:4]}: \tTemperatura media: {(sum(temps["temp"])/len(temps["temp"])):.2f}º\t'
              f'mínima: {min(temps["temp_min"])}º  \tmáxima {max(temps["temp_max"])}º. \t'
              f'Mediciones: {len(temps["temp"])}')
    print()
    print(f'TOTALES:\t\tTemperatura media: {(sum(totales["temp"])/len(totales["temp"])):.2f}º,'
          f'mínima: {min(totales["temp_min"])}º y máxima: {max(totales["temp_max"])}')

else:
    # Nombre del archivo: {CIUDAD}_{FECHA-INICIO}_{FECHA_FIN}, ejemplo: "Cordoba_2020-02-27-12:00:00_2020-03-03-09:00:00.html
    try:
        file_name = ciudad+"_"+(datos["list"][0]["dt_txt"][:10])+"_"+(datos["list"][0]["dt_txt"][11:])+"_"+(datos["list"][39]["dt_txt"][:10]+".html")
        existe_archivo = os.path.isfile('github/ficheros/temperaturas/'+directorio+'/'+file_name)
        if existe_archivo:
            raise Mediciones_existentes()
        #creamos_archivo()
        f = open(f"github/ficheros/temperaturas/{directorio}/{file_name}", "a")
        f.write(inicio_archivo())
        texto = ""
        for dia,temps in dias.items(): # recorremos los pares (dia para recorrer las claves, temps para recorrer los valores) items (recorre los pares)
            #\t --> realiza un tabulador - sum --> calcula el máximo de la lista - min --> calcula el mínimo de la lista
            texto +=(f'<tr>\n<td><center>{dia[8:]}-{dia[5:7]}-{dia[0:4]}</center></td>\n<td><center>{(sum(temps["temp"])/len(temps["temp"])):.2f}º</center></td>\n'
                   f'<td><center>{min(temps["temp_min"])}º</center></td>\n<td><center>{max(temps["temp_max"])}º</center></td>\n<td><center>{len(temps["temp"])}</center></td></tr>')
        f.write(texto)
        f.write(final_archivo())
        f.close()
    except Mediciones_existentes:
        print("\nYa dispone de la mediciones de esta ciudad.")
        exit(3)