#Ejercicio 6#
"""Hacer una tabla de multiplicar dependiendo el número que ingrese el usuario"""

numero = int(input("Ingrese el número que desee: "))
print ("La tabla de multipicar es: ")
for i in range (1, 11):
    print(f"{numero} x {i} = {numero*i}")