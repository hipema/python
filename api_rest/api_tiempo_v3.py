"""
Versión 2.0 - Ejercicio corregido en clase.
IMPORTANTE: no es necesario crear las funciones calculo_media, calculo_max y calculo_min ya que hay funciones que lo permiten directamente.

1. Usando esta API de OpenWeather que nos da el pronóstico del tiempo para una ciudad que se le pide al usuario de los siguientes cinco días, mostrar:

Temperatura media, mínima y máxima (en grados Celsius) para cada día y global.
Tened en cuenta que las respuestas de esta api referentes a los días y horas usan el tiempo en formato UNIX (UTC).
"""

# Funciones a utilizar en el programa

import requests
import os
from datetime import datetime

# datos para hacer la petición
# Endpoint
url = "http://api.openweathermap.org/data/2.5/forecast"
# Parámetros
ciudad = input(f'Introduce la ciudad que deseas buscar: ')
#key = "56e22addb36fca28311139f89294b092"
# Para crear la variable de entorno, vamos a "Run/Edit Cofigurations/Enviroment" y ahí añadimos el valor.
key = os.environ['OPENWEATHERID']
parametros = {'q':ciudad, 'appid':key, 'units':'metric'}

# petición
respuesta = requests.get(url, params=parametros)
if respuesta.status_code != 200:
    print("Error al hacer la petición", respuesta.status_code)
    exit(1)
datos = respuesta.json()

# Cálculos
dias = dict() # diccionario con clave del día y valor, la lista de medicones del día.
totales = list() #lista de mediciones de todos los días.

for medicion in datos['list']:
    # fecha y temperatura de la medición
    dia = medicion['dt_txt'][:10] #devuelve la cadena con los caracteres indicados, truncamos la fecha.
    temp = float(medicion['main']['temp']) # pasamos a número real, el valor obtenido.
    # si no tenemos datos de ese día creamos una nueva entrada en el dicionario
    if not dias.get(dia):
        dias[dia] = list()
    # añadimos medición (aquí si existe la clave de este día, bien porque ya exista o bien porque se acabaría de crear)
    dias[dia].append(temp)
    totales.append(temp)

# resultados
print()
for dia,temps in dias.items(): # recorremos los pares (dia para recorrer las claves, temps para recorrer los valores) items (recorre los pares)
    #\t --> realiza un tabulador - sum --> calcula el máximo de la lista - min --> calcula el mínimo de la lista
    print(f'Día {dia[8:]}-{dia[5:7]}-{dia[0:4]}: \tTemperatura media: {(sum(temps)/len(temps)):.2f}º,'
          f'mínima: {min(temps)}º y máxima {max(temps)}º')
print()
print(f'TOTALES:\t\tTemperatura media: {(sum(totales)/len(totales)):.2f}º,'
      f'mínima: {min(totales)}º y máxima: {max(totales)}')