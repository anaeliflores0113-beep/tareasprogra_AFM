#Ejercicio 7#
"""Sume los elementos de una lista de numeros dada por el usuario"""

numeros = input("Ingrese números separados por comas: ")
lista = [int(n) for n in numeros.split(",")]
print("La suma de los números que dio es: ", sum(lista))