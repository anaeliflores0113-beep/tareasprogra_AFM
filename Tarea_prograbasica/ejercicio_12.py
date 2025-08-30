#ejercicio 12#
"""Ordenar los numero del menor al mayor de una lista ingresada por el usuario"""

numeros = input("Ingrese números separados por comas: ")
lista = [int(n) for n in numeros.split(',')]
lista.sort()
print("La lista ordenada del menor al mayor es:", lista)