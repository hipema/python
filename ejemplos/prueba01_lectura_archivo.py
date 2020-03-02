"""
Prueba de lectura de un archivo
Los ficheros se utilizan para guardar información de manera persistente.
"""
import os
print(os.system("pwd"))
f = open("github/ejemplos/prueba01.txt", "r") # open (cadena_nombre, modo) --> r (lectura), w (escritura, si no existe el
                                              # archivo se crea el archivo, si existe lo machaca), a (añadir información
                                              # si el archivo no existe, se crearía) x, (añadir información si el archivo no existe,
                                              # da un error)
                                              # r+ (lectura/escritura puntero al principio y da error si archivo no existe)
                                              # w+ (lectura/escritura crearia archivo)
                                              # a+ (lectura/escritura al final del archivo)

l = f.readlines() # Lee el fichero ccompleto desde donde se encuentre el puntero.

print(l)

f.seek(0) # situa el puntero (manejador) del archivo en la posición que se le indica.

f.tell() # te indica la posición en la que se encuentra el puntero.

linea = f.readline()    # Leer fichero línea a línea, leería en la que se encuentra situado.
                        # Cuando llega al final del archivo devuelve "" (<EOF>), si es una línea en blanco, devuelve "\n".
print(linea)
print(f.tell())
d = f.read(9) # Con esto indicaríamos cuantos bytes tiene que leer.
print(d)

c = f.read() # devuelve la lectura del archivo como si fuese una cadena.
f.close() # Cierra el fichero