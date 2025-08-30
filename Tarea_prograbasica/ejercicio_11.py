#Ejercicico 11#
"""se suman los digitos de un numero que ingrese el usuario"""

numero = input("Ingrese un número entero mayor de 10: ")
suma = sum(int(d) for d in numero if d.isdigit())
print("La suma de dígitos es: ", suma)