"""
Queremos obtener las 5 películas "trending topic" semanal o del día en función del género de la misma.

Al usuario le preguntamos si quiere un género concreto o si los quiere todos.

Usaremos la API de themoviedb.org

Para los géneros de las películas: https://developers.themoviedb.org/3/genres/get-movie-list

Para el "trending topic": https://developers.themoviedb.org/3/trending/get-trending
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

# Lectura del listado de los géneros.
contenido_generos = respuesta_generos.json()
contador = 0
lista_generos =""
for valor in contenido_generos['genres']:
    if contador < 6:
        lista_generos += valor["name"], ', end=""'
        contador += 1
    else:
        lista_generos += "\n",valor["name"], ', end=""'
        contador = 0

if respuesta_dia.status_code == 200:
    contenido_dia = respuesta_dia.json()    # pasamos contenido a un diccionario
    contenido_semanal = respuesta_semanal.json()

# Comenzamos a presentar el programa y petición de parámetros por pantalla.
print(f'Con esta aplicación podrás obtener un listado con las 5 películas "trending topic".')
rango_elegido = input(f'Señala que rango deseas ver: "semanal" ó "diario": ')

while  rango_elegido != "semanal" and rango_elegido != "SEMANAL" and rango_elegido != "diario" and rango_elegido != "DIARIO":
    print(f'Valor introducido incorrecto.')
    rango_elegido = input(f'Señala que rango deseas ver: "semanal" ó "diario": ')

if rango_elegido == "semanal" or rango_elegido == "SEMANAL":
    tipo = input(f'¿Deseas ver el listado completo o de algún género específico? (general / especifico)')
    while tipo != "general" and "GENERAL" and "especifico" and "ESPECIFICO":
        tipo = input(f'Valor introducido incorrecto. \n'
                     f'¿Deseas ver el listado completo o de algún género específico? \n'
                     f'(general / especifico)')
    if tipo == "general" or "GENERAL":
        # Mostramos trending topic semanal sin filtro
        print(f'\nMostramos las películas "trending topic" semanal:')
        mostrar_trending(contenido_semanal)
    else:


        genero = input(f'\nElige el género: ')

        # búsqueda del id para el género.
        for valor in contenido_generos['genres']:
            if valor['name'] == genero:
                id_genero = valor['id']
        print(id_genero)

    else:
        tipo = input(f'¿Deseas ver el listado completo o de algún género específico? (general / especifico)')
        while not tipo == "general" or "GENERAL" or "especifico" or "ESPECIFICO":
            tipo = input(f'Valor introducido incorrecto. \n'
                         f'¿Deseas ver el listado completo o de algún género específico? \n'
                         f'(general / especifico)')
        if tipo == "general" or "GENERAL":
            # Mostramos trending topic hoy sin filtro
            print(f'\nMostramos las películas "trending topic" semanal:')
            mostrar_trending(contenido_semanal)

elif rango_elegido == "diario" or rango_elegido == "DIARIO":
    tipo = input(f'¿Deseas ver el listado completo o de algún género específico? (general / especifico)')
    while tipo != "general" and "GENERAL" and "especifico" and "ESPECIFICO":
        tipo = input(f'Valor introducido incorrecto. \n'
                     f'¿Deseas ver el listado completo o de algún género específico? \n'
                     f'(general / especifico)')
    if tipo == "general" or "GENERAL":
        # Mostramos trending topic semanal sin filtro
        print(f'\nMostramos las películas "trending topic" de hoy:')
        mostrar_trending(contenido_semanal)
    else:
        tipo = input(f'¿Deseas ver el listado completo o de algún género específico? (general / especifico)')
        while not tipo == "general" or "GENERAL" or "especifico" or "ESPECIFICO":
            tipo = input(f'Valor introducido incorrecto. \n'
                         f'¿Deseas ver el listado completo o de algún género específico? \n'
                         f'(general / especifico)')
        if tipo == "general" or "GENERAL":
            # Mostramos trending topic hoy sin filtro
            print(f'\nMostramos las películas "trending topic" de hoy:')
            mostrar_trending_filtro(contenido_dia,1)



opcion = input(f'Con esta aplicación podrás obtener un listado con las 5 películas "trending topic" \n'
               f'semanal o diario según el género de la película o completo. ¿Deseas ver un listado general? (S/N)')

print(f'\n¿Quiéres ver algún género en concreto? Elige entre el listado de géneros disponibles:\n'
      f'(Escribe el género exactamente como aparece, se distinguen entre mayúsculas y minúsculas)')





# Si la opción es N ó n, realizar la muestra del listado de géneros y su id.

# Mostramos trending topic de hoy con filtro
print(f'\nMostramos las películas "trending topic" de hoy del género {genero}:')
mostrar_trending_filtro(contenido_dia,id_genero, url_movies_dia)

# Mostramos trending topic semanal con filtro
print(f'\nMostramos las películas "trending topic" semanal del género "{genero}":')
mostrar_trending_filtro(contenido_semanal, id_genero, url_movies_semanal)