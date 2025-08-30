#Ejercicio 8#
"""Encontrar el número mayor y el menor en una lista de números dada por el usuario"""

numeros = input("ingrese números separados por comas: ")
lista = [int(n) for n in numeros.split(',')]
print("El número mayor es: ", max(lista))
print("El numero menor es: ", min(lista))