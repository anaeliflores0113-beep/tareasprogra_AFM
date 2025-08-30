#Ejercicio 14#
"""generar una lista de n numeros aleatorios del uno al cien, y n es dada por el usuario"""

import random

n = int(input("Ingrese la cantidad de números aleatorios del 1 al 100: "))
if 1 <= n <= 100:
    aleatorios = [random.randint(1, 100) for _ in range(n)]
    print("La lista de números aleatorios es:", aleatorios)
else:
    print("El número debe estar entre 1 y 100")