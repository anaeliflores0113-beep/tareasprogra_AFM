#Ejercicio 1: Función de valores por omisión#
"""Hacer una función que reciba el nombre y la edad de una persona y mande un mensaje.
Si la edad no se proporciona que se asuma que la edad es 18 """
def mensaje(nombre, edad=18):
    print(f"Hola {nombre}, tienes {edad} años.")


mensaje("Anaeli", 19)
mensaje("Regina")