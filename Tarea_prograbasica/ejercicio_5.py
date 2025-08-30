#Ejercicio 5#
"""Cuente las vocales del texto ingresado por el usuario"""

texto = input("ingrese un texto u oración: ").lower()
vocales = "a e i o u"
contador = sum(1 for letra in texto if letra in vocales)
print("El número de vocales en su texto es: ", contador)
