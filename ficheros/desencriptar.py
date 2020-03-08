"""
3. Haz un programa que reciba como parámetro un fichero encriptado con el método César y y almacene el resultado en otro, que también pasamos como parámetro, de manera que:

Si el programa no recibe dos parámetros termina con un error 1.
Si el programa recibe un solo parámetro guardará la información encriptada en el mismo archivo del que lee, pero antes advertirá al usuario de que machacará el archivo origen, dando opción a que la operación no se haga.
Si el fichero origen no existe (da error al abrirlo como lectura) el programa termina con un mensaje de error y código 2.
Si en el fichero destino no se puede escribir da error al abrirlo como lectura) el programa termina con un mensaje de error y código 2.
Para desencriptar necesitas una clave que debes pedir al usuario.
¿Se te ocurre alguna forma de desencriptar este archivo sin pedir clave? Coméntala, y si te atreves... ¡impleméntala!
"""

# Creamos excepciones.

class Sintaxis_incorrecta(Exception):
    '''Excepción que captura la introducción de una sintaxis incorrecta'''
    def __init__(self):
        Exception.__init__(self)

def desencriptar_fichero(file_read, file_write):
    clave=""
    while clave =="":
        try:
            clave = -(int(input("Indica clave a utilizar en el fichero: ")))
        except:
            print("La clave debe ser un número entero")

    diccionario_principal = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789"
    long_diccionario = len(diccionario_principal)
    # Leemos archivo recibido
    try:
        f = open(f"github/ficheros/encriptado/{file_read}", "r")
    except:
        print("Archivo no encontrado")
        exit(1)
    lectura =""
    for i in f:
        lectura += i
    posicion = f.tell()
    f.close()
    f = open(f"github/ficheros/encriptado/{file_write}", "w")
    # recorremos la cadena lectura carácter a carácter:
    escritura = ""
    #for i in range (posicion):
    i=0
    while i < len(lectura):
        print("posicion total: ", len(lectura)-1)
        print("posicion de i: ", i)
        print(lectura[i])
        if lectura[i] in diccionario_principal:
            indice = diccionario_principal.index(lectura[i])
            if (indice+clave)>= 0:
                escritura += diccionario_principal[indice+clave]
            else:
                escritura += diccionario_principal[(long_diccionario+clave+indice)]
        else:
            escritura += lectura[i]
        i = i + 1
    f.write(escritura)
    f.close()
    print("Archivo desencriptado correctamente.")


import os
import sys
try:
    if (len(sys.argv) == 2):
        opcion =""
        while not (opcion == "s" or opcion == "S" or opcion =="n" or opcion =="N"):
             opcion = input(f'La información encriptada se guardará en el mismo archivo de origen.\n'
              f'¿Desea continuar? (s/n')
        if opcion == "s" or opcion == "S":
            desencriptar_fichero(sys.argv[1], sys.argv[1])
        else:
            exit(0)
    elif len(sys.argv) ==3:
        desencriptar_fichero(sys.argv[1], sys.argv[2])
    else:
        raise Sintaxis_incorrecta()

except Sintaxis_incorrecta:
    print("El programa requiere dos parámetros.")
    exit(1)
