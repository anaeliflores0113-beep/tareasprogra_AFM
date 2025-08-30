#Ejercicio 2#
"""Calcular el factorial de un número dado por el usuario del uno al veinte usando un
ciclo while"""

n = int(input("Ingreso un número del 1 al 20: "))
if n >= 1 and n <= 20:
    factorial = 1
    contador = 1
    while contador <= n:
        factorial *= contador
        contador += 1
    print(f"El factorial de {n} es: {factorial}")    
else:
    print("Ese número no es válido.")    