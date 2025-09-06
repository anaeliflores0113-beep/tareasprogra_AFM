#Ejercicio 10: Función para calcular MCD#
"""Hacer una función que calcule el máximo común divisor de dos números"""
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a


print(mcd(30, 15))  
