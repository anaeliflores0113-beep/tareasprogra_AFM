#Ejercicio 13: Verificación de año bisiesto#
"""Hacer una función que verifique si un año es bisiesto o no"""
def bisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)


print(bisiesto(2006))  
print(bisiesto(2016))  