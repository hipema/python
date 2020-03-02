"""
Prueba de escritura de un archivo
Los ficheros se utilizan para guardar información de manera persistente.
"""
import os
# print(os.system("pwd")) --> sirve para ver en que posición se encuentra para ejecutar Python y desde donde va la ruta.
f = open("github/ejemplos/prueba01.txt", "w") # open (cadena_nombre, modo) --> r (lectura), w (escritura, si no existe el
                                              # archivo se crea el archivo, si existe lo machaca), a (añadir información
                                              # si el archivo no existe, se crearía) x, (añadir información si el archivo no existe,
                                              # da un error)
                                              # r+ (lectura/escritura puntero al principio y da error si archivo no existe)
                                              # w+ (lectura/escritura crearia archivo)
                                              # a+ (lectura/escritura al final del archivo)

print("Primera línea del fichero", file=f) # print mete siempre un salto de línea al final.
f.tell()
print("Segunda línea del fichero", file=f)
f.tell()

f = open("github/ejemplos/prueba01.txt", "a")
f.writelines("Esta es la tercera línea") # no incluye salto de línea al final.
f.flush()
f.writelines("¿y esta donde va?") # Escribe a continuación, sin salto de línea ni separador de ningún tipo.

f2 = open("github/ejemplos/prueba02.txt", "r")
l = f2.readlines()
f.writelines(l)

#l2 = [1, 2, 3, 5, 6]
# f.writelines(l2) --> daría error porque no es el mismo tipo de datos, tendría que ser texto, no binario.

f.close()