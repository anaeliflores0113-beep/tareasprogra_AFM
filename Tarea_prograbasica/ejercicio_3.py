#Ejercicio 3#
"""Determinar si el número dado por el usuario es primo o no"""

numero = int(input("Ingresu un número"))
if numero <= 2:
    print("No es número primo")
else:
    es_primo = True
    for i in range(2, int(numero**0.5)+1):
        if numero % i == 0:
            es_primo = False
            print("No es un número primo")
        if es_primo:
            print(f"{numero} es un número primo")