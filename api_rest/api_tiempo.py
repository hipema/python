"""
1. Usando esta API de OpenWeather que nos da el pronóstico del tiempo para una ciudad que se le pide al usuario de los siguientes cinco días, mostrar:

Temperatura media, mínima y máxima (en grados Celsius) para cada día y global.
Tened en cuenta que las respuestas de esta api referentes a los días y horas usan el tiempo en formato UNIX (UTC).
"""

# Funciones a utilizar en el programa

def calculo_media (temperaturas):
    sumatorio = 0
    for i in range (len(temperaturas)):
        sumatorio += temperaturas[i]
    return sumatorio / len(temperaturas)

def calculo_max (temperaturas):
    maximo = -273.15
    for i in range (len(temperaturas)):
        if maximo < temperaturas[i]:
            maximo = temperaturas[i]
    return maximo

def calculo_min (temperaturas):
    minimo = 100
    for i in range (len(temperaturas)):
        if minimo > temperaturas[i]:
            minimo = temperaturas[i]
    return minimo

import requests
import os
from datetime import datetime

# datos para hacer la petición
# Endpoint
url = "http://api.openweathermap.org/data/2.5/forecast"
# Parámetros
ciudad = input(f'Introduce la ciudad que deseas buscar: ')
key = "56e22addb36fca28311139f89294b092"
#key = os.getenv('$OPENWEATHERID', 'Id no encontrada')
parametros = {'q':ciudad, 'appid':key, 'units':'metric'}

# petición
respuesta = requests.get(url, params=parametros)

# Variables donde almacenaremos los resultados obtenidos en la api:
temp = list() # temperatura en cada momento de la medición
temp_max = list() # temperatura máxima de cada lectura.
temp_min = list() # temperatura mínima de cada lectura.

# Variables donde almacenaremos lo cálculos obtenidos en la api:
temp_media_global = list() # almacenará la temperatura media en cada cambio de día.
temp_max_global = list() # almacenará los valores máximos de la temperatura de cada día.
temp_min_global = list() # almacenará los valores minimos de la temperatura de cada día

if respuesta.status_code == 200:
    contenido = respuesta.json()    # pasamos contenido a un diccionario
    dia = datetime.utcfromtimestamp(int(contenido['list'][0]['dt'])).strftime('%d-%m-%Y')

    for valor in contenido['list']:
        # Comprobamos el día que lee en la iteración para ver si coincide con el día almacenado
        dia_leido = datetime.utcfromtimestamp(valor['dt']).strftime('%d-%m-%Y')

        if dia_leido == dia:
            # si coincide con el día almacenado, vamos añadiendo los valores a los arrays correspondientes.
            temp.append(valor['main']['temp'])
            temp_max.append((valor['main']['temp_max']))
            temp_min.append((valor['main']['temp_min']))
        else:
            # Si el día no coincide, claculamos los valores a mostrar (temp. media, max y mínima)
            temp_media_diaria = calculo_media(temp)
            temp_maxima_diaria = calculo_max(temp_max)
            temp_minima_diaria = calculo_min(temp_min)

            print(f'El día {dia} se prevén los siguientes valores en {ciudad}: \n'
                  f'Temperatura media: {temp_media_diaria} \n'
                  f'Temperatura mínima: {temp_minima_diaria} \n'
                  f'Temperatura máxima: {temp_maxima_diaria} \n')

            # Almacenamos los valores en los arrays globales
            temp_media_global.append(temp_media_diaria)
            temp_min_global.append(temp_minima_diaria)
            temp_max_global.append(temp_maxima_diaria)

            # Limpiamos las listas diarias, para volver a calcular los datos del nuevo día.
            temp = list()
            temp_max = list()
            temp_min = list()

            # Actualiamos el valor del día en curso
            dia = dia_leido

            # Añadimos valores del día en curso
            temp.append(valor['main']['temp'])
            temp_max.append((valor['main']['temp_max']))
            temp_min.append((valor['main']['temp_min']))

    # Una vez leídos todos los días, calculamos resultados globales:
    res_temp_med_global = calculo_media(temp_media_global)
    res_temp_max_global = calculo_max(temp_max_global)
    res_temp_min_global = calculo_min(temp_min_global)

    # Mostramos resultados globales:
    print(f'Estos son los valores obtenidos en ({ciudad}) para los próximos 5 días:\n'
          f'Temperatura media: {res_temp_med_global}\n'
          f'Temperatura mínima: {res_temp_min_global}\n'
          f'Temperatura máxima: {res_temp_max_global}')
else:
    print(f'La consulta ha fallado, vuelva a intentarlo introduciendo un valor correcto.')