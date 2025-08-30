#Ejercicio 1#
"""Escribir un programa que sume todods los números pares del uno al cien usando 
un ciclo for"""

suma = 0
for i in range(2,101,2):
    suma += i
print(f"La suma de los números pares del uno al cien es: {suma}")