#Ejercicio 4: Función para calcular una factorial#
"""Hacer una función que calcule el factorial de un número usando ciclos"""
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


print(factorial(7))
print(factorial(4))
