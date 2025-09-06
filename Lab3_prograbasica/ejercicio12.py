#Ejercicio 12: Calcular la moda#
"""Hacer una función que calcule la moda de una lista de números"""
from collections import Counter

def moda(lista):
    contador = Counter(lista)
    max_freq = max(contador.values())
    modas = [num for num, freq in contador.items() if freq == max_freq]
    return modas


print(moda([4, 3, 6, 4, 7])) 
