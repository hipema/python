"""
Queremos obtener las 5 películas "trending topic" semanal o del día en función del género de la misma.

Al usuario le preguntamos si quiere un género concreto o si los quiere todos.

Usaremos la API de themoviedb.org

Para los géneros de las películas: https://developers.themoviedb.org/3/genres/get-movie-list

Para el "trending topic": https://developers.themoviedb.org/3/trending/get-trending
"""

# Funciones a utilizar en el programa

import requests
import os

