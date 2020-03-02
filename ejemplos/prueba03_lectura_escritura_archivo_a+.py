"""
Prueba de lectura / escritura de un archivo
Los ficheros se utilizan para guardar información de manera persistente.
"""
import os
# print(os.system("pwd")) --> sirve para ver en que posición se encuentra para ejecutar Python y desde donde va la ruta.
f = open("github/ejemplos/prueba03.txt", "a+") # open (cadena_nombre, modo) --> r (lectura), w (escritura, si no existe el
                                              # archivo se crea el archivo, si existe lo machaca), a (añadir información
                                              # si el archivo no existe, se crearía) x, (añadir información si el archivo no existe,
                                              # da un error)
                                              # r+ (lectura/escritura puntero al principio y da error si archivo no existe)
                                              # w+ (lectura/escritura crearia archivo)
                                              # a+ (lectura/escritura al final del archivo)

f.tell()
f.write("TRES") # Lo añade al final directamente, no permite cambiar el puntero de escritura.
f.seek(0)
l = f.readline()

f.close()