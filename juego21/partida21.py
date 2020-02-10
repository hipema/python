"""
Clase relacionada con el desarrollo de la partida al 21, utilizando los dados y la clase Jugadores.
"""

from github.juego21.jugadores21 import Jugadores21

# Comienza la partida, elegimos cantidad de Jugadores
numero_jugadores = int (input('¿Cuantos jugadores sois? '))
jugadores = [None]*numero_jugadores
rondas = 2

# Creamos Jugadores y damos nombre.
for i in range(numero_jugadores):
    nombre_jugador = f'j{i+1}: ' + input(f'Introduce nombre del jugador {i+1}: ')
    jugadores[i] = Jugadores21(nombre_jugador)

# Repasamos nombre de los jugadores
print(f'\nEstos son los jugadores que participarán: ')
for i in range(numero_jugadores):
    print(f'Jugador {i+1}: {jugadores[i].nombre}')


# Variables que vamos a necesitar para hacer el array de inicio:
# contador = iniciamos con el número inicial de jugadores. Una vez entre en el while, se pasa a 0. Después contabilizará los empates.
# auxiliar = se inicia igual a contador.
# puntuacion[] = Se inicia al principio de cada ronda del while, con el número de valores equivalente a "contador"
# empatados[] = tendrá el máximo de tamaño igual a contador, en él se almacenarán únicamente los valores máximos
# máximo = se debe inicializar a cada ronda del while a cero.

contador = (numero_jugadores)
auxiliar = contador
empatados = [None]*numero_jugadores

for i in range (numero_jugadores):
    empatados[i] = jugadores[i]

numero_ronda = 1
while contador > 1:
    print(f'\nRonda {numero_ronda}')
    auxiliar = contador
    contador = 0
    puntuacion = [None]*auxiliar
    maximo = 0
    for i in range(auxiliar):
        empatados[i].tirada_un_dado()
        print(f'Lanza dado {empatados[i].nombre}: {empatados[i].resultado_dados}')
        puntuacion[i] = empatados[i].resultado_dados
        if empatados[i].resultado_dados > maximo:
            maximo = empatados[i].resultado_dados
    desempate = [None]*auxiliar
    for i in range(auxiliar):
        if maximo == puntuacion[i]:
         desempate[contador] = empatados[i]
         contador += 1
    empatados = [None]*contador
    for i in range (contador):
        empatados[i]=desempate[i]
    numero_ronda +=1

# Ahora realizamos un array con el orden correcto de los jugadores, primero buscamos la posición del que empezará:
comienza = 0
for i in range (numero_jugadores):
    if empatados[0].nombre ==jugadores[i].nombre:
        comienza = i

print(f'Comienza {empatados[0].nombre}')
print(f'Comienza {comienza+1}')
print(f'\nEl orden de la partida será:')

orden_correcto = [None]*numero_jugadores
j=0
for i in range (numero_jugadores):
    if (i+comienza) < numero_jugadores:
        orden_correcto[i]=jugadores[i+comienza]
    else:
        orden_correcto[i]=jugadores[j]
        j +=1

for i in range (numero_jugadores):
    print(f'Lanza nº {i+1} {orden_correcto[i].nombre}')

# Reseteamos contadores
for i in range (numero_jugadores):
    orden_correcto[i].borrar_resultado()

    # Hasta aquí está el inicio del juego, con la ronda inicial para ver el orden de la partida.

print(f'\n\nComenzamos la partida.')
print(f'----------------------')
ronda = 1
contador = 0
while ronda <= rondas:
    print(f'\n\nRonda {ronda}')
    puntuacion = list()
    maximo = 0
    contador = 0
    for i in range (numero_jugadores):
        # Se debe ir dando la opción de lanzar de nuevo los dados o plantarse.
        # Primer lanzamiento
        print(f'\nTurno de {orden_correcto[i].nombre}:')
        puntuacion.append(orden_correcto[i].jugar_ronda())
        if puntuacion[i] > maximo and puntuacion[i]<=21:
            maximo = puntuacion[i]

    print('\nResultados de la tirada:')
    for i in range (numero_jugadores):
        if puntuacion[i] > 21:
            print(f'{orden_correcto[i].nombre}: {orden_correcto[i].resultado_ronda} - Eliminado')
        else:
            print(f'{orden_correcto[i].nombre}: {orden_correcto[i].resultado_ronda}')

    for i in range (numero_jugadores):
        if maximo == puntuacion[i]:
            contador += 1
    empatados.clear()
    while contador > 1:
        print(f'\nRealizamos el desempate entre: ')
        for i in range(numero_jugadores):
            if maximo == orden_correcto[i].resultado_ronda:
                print(f'{orden_correcto[i].nombre}')
                empatados.append(i)
            orden_correcto[i].borrar_resultado()

        auxiliar = contador
        contador = 0
        puntuacion.clear()
        maximo = 0

        for i in range(auxiliar):
            print(f'\nTurno de {orden_correcto[empatados[i]].nombre}:')
            puntuacion.append(orden_correcto[empatados[i]].jugar_ronda())
            if maximo < puntuacion[i] < 21:
                maximo = puntuacion[i]
        for i in range(numero_jugadores):
            if maximo == len(puntuacion):
                contador += 1

    for i in range (numero_jugadores):
        if maximo == orden_correcto[i].resultado_ronda:
            orden_correcto[i].sumar_victoria()
            print(f'El ganador es: {orden_correcto[i].nombre}\n')
        orden_correcto[i].borrar_resultado()

    ronda += 1

puntuacion.clear()
maximo = 0
contador = 0
ganadores = list()
for i in range (numero_jugadores):
    if orden_correcto[i].contador_victorias >= maximo:
        maximo = orden_correcto[i].contador_victorias
for i in range (numero_jugadores):
    if orden_correcto[i].contador_victorias == maximo:
        ganadores.append(orden_correcto[i].nombre)
        contador += 1

if contador == 1:
    print(f'El ganador de la PARTIDA  es {ganadores[0]} con {maximo} victorias. ')
else:
    print (f'Los ganadores son:')
    for i in range (len(ganadores)):
        print(f'- {ganadores[i]} con {maximo} victorias.')