#Ejercicio 4#
"""Números fibonacci"""

n = int(input("Ingrese un valor del uno al cincuenta: "))
if n >= 1 and n <= 50:
    fibo = [0, 1]
    for i in range (2, n):
        fibo.append(fibo[-1]+fibo[-2])
    print("La secuencia de Fibonacci es: ", fibo )
else:
    print("Ese número no es válido")    