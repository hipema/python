from rectangulo import Rectangulo # se importa porque hace falta utilizar la clase rectángulo, no ponemos EjerciciosClase para poder ejecutarlo desde terminal.

"""
En este ejercicio utilizaremos la herencia
"""

class Cuadrado(Rectangulo):
    """
    Implementamos la clase Cuadrado partiendo de la clase Rectángulo.
    Consideraremos que un cuadrado es un rectángulo con base==altura.
    """
    def __init__(self, lado):
        super().__init__(lado,lado) # super() llama a las propiedades del objeto superior.

    #si pones "prop" directamente te crea property con setter para tu crear la funcion que quieras con esas propiedades
    @property
    def lado(self, value):
        return self.base

    @lado.setter
    def lado(self, value):
        self.base = value
        self.altura = value