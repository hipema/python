"""
Queremos obtener las 5 películas "trending topic" semanal o del día en función del género de la misma.

Al usuario le preguntamos si quiere un género concreto o si los quiere todos.

Usaremos la API de themoviedb.org

Para los géneros de las películas: https://developers.themoviedb.org/3/genres/get-movie-list

Para el "trending topic": https://developers.themoviedb.org/3/trending/get-trending

REVISAR FUNCIÓN MOSTRAR_TRENDING_FILTRO
"""

# Funciones a utilizar en el programa
# Mostrar trending sin filtro
def mostrar_trending (contenido_listado):
    contador = 1
    for valor in contenido_listado['results']:
        if contador < 6:
            print(f'Nº{contador}.- {valor["title"]}')
            contador += 1

# Mostrar trending con filtro de categoría
def mostrar_trending_filtro (contenido_listado, id_genero, rango):
    contador = 1
    page = 1
    while contador < 6:
        for valor in contenido_listado['results']:
            ids = valor['genre_ids']
            if contador < 6:
                for i in range(len(ids)):
                    if ids[i] == id_genero:
                        print(f'Nº{contador}.- {valor["title"]}')
                        contador += 1
        page +=1
        respuesta = lanzar_consulta(rango, page)
        contenido_listado = respuesta.json()

def lanzar_consulta (rango, page_actual):
    key = "67e26925bd2c561a1b08002e63c8044a"
    language = "es-ES"
    page = page_actual
    # key = os.getenv('$THEMOVIEDB', 'Id no encontrada')
    parametros = {'api_key': key, 'language': language, 'page': page}
    return requests.get(rango, params=parametros)

def semanal_diario ():
    rango_elegido = (f'Deseas ver las películas trending topic "semanal" ó "diario": ')
    while rango_elegido != "semanal" and rango_elegido != "SEMANAL" and rango_elegido != "diario" and rango_elegido != "DIARIO":
        print(f'Valor introducido incorrecto.')
        rango_elegido = input(f'Señala que rango deseas ver: "semanal" ó "diario": ')
    if rango_elegido == "SEMANAL" or "semanal":
        rango_elegido = "semanal"
    else:
        rango_elegido = "diario"
    return rango_elegido

def general_especifico ():
    tipo = input(f'¿Deseas ver el listado completo o de algún género específico? (general / especifico): ')
    while tipo != "general" and tipo != "GENERAL" and tipo != "especifico" and tipo != "ESPECIFICO":
        tipo = input(f'Valor introducido incorrecto. \n'
                     f'¿Deseas ver el listado completo o de algún género específico? \n'
                     f'(general / especifico)')
    if tipo == "general" or tipo == "GENERAL":
        tipo = "general"
    else:
        tipo = "especifico"
    return tipo

def mostrar_generos (contenido_generos):
    # Lectura del listado de los géneros.
    contador = 0
    for valor in contenido_generos['genres']:
        if contador < 6:
            print(f'{valor["name"]} ', end="")
            contador += 1
        else:
            print(f'\n{valor["name"]} ', end="")
            contador = 0

def elige_genero (contenido_generos):
    genero = input(f'\nElige el género: ')
    genero_correcto = False
    for valor in contenido_generos['genres']:
        if valor['name'] == genero:
            genero_correcto = True
    while genero_correcto == False:
        genero = input(f'Género incorrecto, vuelve a introducirlo: ')
        for valor in contenido_generos['genres']:
            if valor['name'] == genero:
                genero_correcto = True
    return genero

def busqueda_genero (contenido_generos, genero):
    # búsqueda del id para el género.
    for valor in contenido_generos['genres']:
        if valor['name'] == genero:
            id_genero = valor['id']
    return id_genero

import requests
import os

# datos para hacer la petición
# Endpoint
url_movies_dia = "https://api.themoviedb.org/3/trending/movie/day"
url_movies_semanal = "https://api.themoviedb.org/3/trending/movie/week"
url_generos = "https://api.themoviedb.org/3/genre/movie/list"

# Parámetros
key = "67e26925bd2c561a1b08002e63c8044a"
language = "es-ES"
page = 1
#key = os.getenv('$THEMOVIEDB', 'Id no encontrada')
parametros = {'api_key':key, 'language':language, 'page':page}

# petición
respuesta_dia = lanzar_consulta(url_movies_dia,1)
respuesta_semanal = lanzar_consulta(url_movies_semanal,1)
respuesta_generos = lanzar_consulta(url_generos,1)

if respuesta_dia.status_code == 200:
    contenido_dia = respuesta_dia.json()    # pasamos contenido a un diccionario
    contenido_semanal = respuesta_semanal.json()
    contenido_generos = respuesta_generos.json()

# Comenzamos a presentar el programa y petición de parámetros por pantalla.
mostrar_trending_filtro(contenido_dia, "Acción",url_movies_dia)

print(f'Con esta aplicación podrás obtener un listado con las 5 películas "trending topic".')
print(f'-----------------------------------------------------------------------------------')

# Pedimos la periodicidad de la búsqueda:
rango_elegido = semanal_diario()
tipo = general_especifico()

if tipo == "general" and rango_elegido == "diario":
    mostrar_trending(contenido_dia)
elif tipo == "general" and rango_elegido == "semanal":
    mostrar_trending(contenido_semanal)
elif tipo == "especifico" and rango_elegido == "diario":
    print(f'Géneros disponibles: ')
    mostrar_generos(contenido_generos)
    genero = elige_genero(contenido_generos)
    mostrar_trending_filtro(contenido_dia, genero,url_movies_dia)
else:
    print(f'Géneros disponibles: ')
    mostrar_generos(contenido_generos)
    genero = elige_genero(contenido_generos)
    mostrar_trending_filtro(contenido_semanal, genero, url_movies_semanal)