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
partida.alta_jugadores(int(input('¿Cuántos jugadores son? ')))

# Listado de jugadores que participan
#print(f'\nListamos los jugadores: ')
#print(f'----------------------- ')
#partida.listado_jugadores()

# Tirar 1 dado
partida.tirar_todos_un_dado()

# Resultado ronda de dados
partida.resultado_ronda_dados()

# Mostrar resultado dados
print(f'\nMostramos resultado de una tirada de todos con un dado: ')
print(f'------------------------------------------------------')
for i in range (partida.num_jugadores):
    print(f'Jugador {i+1}: {partida.resultado_ronda[i]}')

# Comprobamos la función "Buscar empatados"
print(f'\nMostrar empatados: ')
print(f'----------------')
# Mostramos los empatados con el valor máximo.
partida.mostrar_empatados()
#partida.desempatar_apertura()
partida.mostrar_resultados_empatados()
"""
# Desempatar
print(f'\nRealizamos rondas hasta desempatar y sólo quedar uno: ')
print(f'-----------------------------------------------------')
partida.desempatar_apertura()
partida.mostrar_empatados()
partida.mostrar_resultados_empatados()
"""
"""
# Tira un dado los empatados
print(f'\nMostramos resultado de tirada empatados con 1 dado: ')
print(f'--------------------------------------------------')
partida.empatados_un_dado()
partida.resultado_ronda_dados()
partida.mostrar_resultados_empatados()


# Desempatar
print(f'\nRealizamos rondas hasta desempatar y sólo quedar uno: ')
print(f'-----------------------------------------------------')
partida.desempatar_apertura()
partida.mostrar_resultados_empatados()


# Reseteamos contadores de ronda

partida.resetear_resultado_ronda()
# Tirar todos 2 dados
partida.tirar_todos_dos_dados()
# Resultado ronda de dados
partida.resultado_ronda_dados()

# Mostrar resultado dados
print(f'\nMostramos resultado de una tirada de todos con dos dados: ')
print(f'------------------------------------------------------')
for i in range (partida.num_jugadores):
    print(f'Jugador {i+1}: {partida.resultado_ronda[i]}')

# Sorteo de turnos
print(f'\nSorteamos los turnos de tirada: ')
print(f'------------------------------ ')
#partida.sorteo_turnos()
"""