#Ejercicio 2: Número Arbitrario de argumentos#
"""Hacer una función que reciba un número arbitrario de argumentos y devuelva su suma"""
def suma_total(*numeros):
    return sum(numeros)


print(suma_total(5, 2, 1))
print(suma_total(3, 10, 7))
