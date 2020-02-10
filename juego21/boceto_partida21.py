"""
El 21 en Dados. Utilizamos la clase dado y dados realizadas por Rafael del Castillo.

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

"""
Clases necesarias:
    - dado
    - dados
    - jugadores: numero jugador, nombre, contador puntos ronda, contador victorias, dados.
    - partida21:
"""

""" 
Elegimos número de jugadores, asignamos nombres.

- Creamos dos dados para cada jugador y un contador punto ronda como de victorias.

Comenzamos el juego
- Cada jugador tira un dado y se acumula en contador punto ronda.
    * Se selecciona los jugadores con el > contador punto ronda.
    * Si hay empate, tiran un dado cada uno de los jugadores empatados.
        Se selecciona los jugadores con el > contador punto ronda.
    * Cuando sólo quede un jugador, ese será el que empezará la partida.
    * Reordenaremos el número de salida para la partida, siendo el primero el que mayor puntuación haya obtenido, a partir
        de ahí seguirá el orden ascendente, y se incluirá en el array al final los números del 1 hasta X.
    
- Tira el jugador X:
    * Comprobamos puntuación de suma de los dos dados y añadimos al contador puntos ronda.
    * Si puntuación es inferior a 14, debe elegir si volver a tirar o no (con los dos dados).
        Si decide tirar se realiza la suma al contador puntos ronda.
    * Si puntuación es 14 ó +, puede elegir si volver a tirar o no, pero con ún solo dado.
        Si decide tirar se realiza la suma al contador puntos ronda.
    * Cuando decide no volver a tirar (se planta) se guarda su contador puntos ronda y se pasa el turno al siguiente jugador.
  
- Repetimos proceso anterior con cada uno de los jugadores.
- Finalizado el turno de todos los jugadores, se realiza la comprobación del ganador.
    *   Jugador con > 21 puntos - pierde.
    *   Si hay un jugador sólo con el contador puntos ronda más algo, gana directamente.
        Si número de jugadores con puntuación más alta > 1 (Pasan al desempate)
            - Se repite tirada entre los jugadores con más puntos.
            - Una vez tiran todos los jugadores empatados, se vuelve a comprobar el resultado.
"""
