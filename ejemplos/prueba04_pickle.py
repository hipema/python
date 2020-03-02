"""
Escritura de archivos binarios
Los ficheros se utilizan para guardar información de manera persistente.

Esto es muy interesante para guardar en ficheros con muy pocas instrucciones listas de objetos y poderlos recuperar.
Ver después
"""
import os
import pickle # Importa módulo pickle

# Declara lista
lista = ['Perl', 'Python', 'Ruby']

# Abre archivo binario para escribir
archivo = open('github/ejemplos/lenguajes.txt', 'wb')

# Escribe lista en archivo
pickle.dump(lista, archivo)

# Cierra archivo
archivo.close()

# Borra de memoria la lista
del lista

# Abre archivo binario para leer
archivo = open('lenguajes.txt', 'rb')

# carga lista desde archivo
lista = pickle.load(archivo)

# Muestra lista
print(lista)

# Cierra archivo
archivo.close()
lista = ["hola", "Pájaro", "Perro"]