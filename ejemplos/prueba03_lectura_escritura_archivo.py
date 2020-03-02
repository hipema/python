"""
Prueba de lectura / escritura de un archivo
Los ficheros se utilizan para guardar información de manera persistente.
"""
import os
# print(os.system("pwd")) --> sirve para ver en que posición se encuentra para ejecutar Python y desde donde va la ruta.
f = open("github/ejemplos/prueba03.txt", "r+") # open (cadena_nombre, modo) --> r (lectura), w (escritura, si no existe el
                                              # archivo se crea el archivo, si existe lo machaca), a (añadir información
                                              # si el archivo no existe, se crearía) x, (añadir información si el archivo no existe,
                                              # da un error)
                                              # r+ (lectura/escritura puntero al principio y da error si archivo no existe)
                                              # w+ (lectura/escritura crearia archivo)
                                              # a+ (lectura/escritura al final del archivo)

#r+ mantiene un puntero para lectura, y otro de escritura.

print("Primera línea del fichero", file=f) # print mete siempre un salto de línea al final.
l = f.readline()
print(l)
f.seek(0) # Hay que reposicionar el puntero para que escriba en esa posición.
f.writelines("TRES")
#f.write("DOS") # lo que escribe write es una cadena y no texto como writelines.

f.flush() # vacia el buffer.

f.close()