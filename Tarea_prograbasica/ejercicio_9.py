#Ejercicio 9#
"""Contar las palabras de un texto dado por el usuario"""

def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)
cadena = input("Ingrese un texto: ")
print("Número de palabras es:", contar_palabras(cadena))