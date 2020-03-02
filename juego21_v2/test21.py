"""
El 21 en Dados. Utilizamos la clase dado y dados realizadas por Rafael del Castillo.

@author: Manuel Hidalgo Pérez, David Pérez Ruiz
@date: 28 Febrero 2020
@version: 2.0

Clases propias utilizadas: Partida21, Jugadores21

Jugadores: 2 ó +

Objetivo:
Alcanzar el puntaje , total de 21 puntos o aproximarse a dicha cifra, lo más posible pero sin pasarla.

Comienzo:
Cada jugador tira un dado para determinar el orden del juego. Sale primero el que saca la mayor suma.
Si dos participantes sacan el mismo número en el tiro preliminar, vuelven a tirar hasta que desempaten.
El juego prosigue en el sentido de las agujas del reloj.

Hay una ventaja estratégica en ser el Ultimo: le resulta posible ver cuanto tiene que sacar para ganar y se arriesgará
consecuentemente.

Todos los participantes apuestan la misma cantidad de dinero, determinada de antemano.

4.Desarrollo
El participante juega solo una vez por vuelta. Puede tirar los dados tantas veces como lo desee y puede plantarse en
cualquier momento mientras el puntaje no sea mayor de 21. Cada tiro se va sumando al anterior. Cuando se alcanza un total
de 14 o más, pasa a jugar con un dado. Por supuesto, que un jugador desafortunado puede fracasar con un tiro alto aun
cuando no haya tenido la oportunidad de pasar a un dado.

Si un jugador alcanza un puntaje mayor de 21 pierde inmediatamente queda fuera de juego.

Después que todos hayan intervenido, el participante cuyo total este más cerca de los 21 puntos - pero no supere dicha
cifra - gana el pozo. Si empatan dos o más competidores, seguirán tirando hasta que se determine el ganador. El último en
empatar tira primero.

5.Estrategia
La estrategia más elemental puede abreviarse de la siguiente forma:
El participante que haya alcanzado un total de 17 puntos o menos debe arriesgar otro tiro.

El que haya logrado un total de 19 puntos o más, deberá quedarse con ese total a menos que otro competidor haya obtenido
ya los 20 o 21 puntos.

Quien haya alcanzado un total de 18 puntos puede plantarse o tirar nuevamente, ya que tres posibles resultados de su
próximo tiro lo acercarán a 21 y tres lo harán pasarse de dicha cifra.

Por supuesto, los últimos participantes estarán influidos por el éxito o el fracaso de los anteriores. Por ejemplo, si
uno de los primeros jugadores ha alcanzado un total de 20 puntos, los competidores posteriores estarán forzados a tirar
nuevamente aun cuando hayan llegado a 19. En esta situación es probable que se pase de 21, pero no tiene sentido quedarse
con un total perdedor.

"""
from github.juego21_v2.partida21 import Partida21

# Comienza la partida, elegimos cantidad de Jugadores
print('Bienvenido al JUEGO DEL 21.\n'
      'Este juego consiste en tirar dados hasta aproximarse lo máximo posible al número 21\n'
      'sin pasarse, si se pasa queda eliminado. Gana el jugador que más se acerque.')
print('------------------------------------------------------------------------------------\n')

# Ejecutamos inicio de partida
partida = Partida21()

# Elección número de jugadores y alta
partida.alta_jugadores(int(input('¿Cuántos jugadores son? ')))
print("")


rondas_totales = int(input('\n¿Cuantas rondas queréis jugar? '))
print()
print("Ver jugadores en orden inicial:")
print("-------------------------------")
print(partida)

# Tirada inicial para selección de orden
partida.ronda_inicial()

print(f"\nVer jugadores ordenados:")
print(f"-----------------------")
print(partida)

# Jugamos rondas
for i in range (rondas_totales):
    print(f"Ronda {i+1}:")
    partida.jugar_ronda_todos()

# Ver clasificación
partida.ver_clasificacion()
print()
tirar = ""
while tirar != "s" or tirar != "S" or tirar != "n" or tirar != "N":
    tirar= input("¿Quieres jugar otra ronda? (s/n)")
    if tirar == "s" or tirar == "S":
        partida.jugar_ronda_todos()
    elif tirar == "n" or tirar == "N":
        print("Fin de partida, gracias por Jugar al 21")
