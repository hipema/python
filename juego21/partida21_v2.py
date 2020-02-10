from github.juego21.reglas21 import Reglas21
"""
Partida del 21
"""

# Comienza la partida, elegimos cantidad de Jugadores
print('Bienvenido al JUEGO DEL 21.\n'
      'Este juego consiste en tirar dados hasta aproximarse lo máximo posible al número 21\n'
      'sin pasarse, si se pasa queda eliminado. Gana el jugador que más se acerque.')
print('------------------------------------------------------------------------------------\n')
partida = Reglas21()

# Elección del número de jugadores
jugadores = partida.alta_jugadores(int(input('¿Cuántos jugadores son?')))

# Listado de jugadores que participan

# Sorteo de turnos
partida.sorteo_turnos()