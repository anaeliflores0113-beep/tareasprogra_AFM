#Ejercicio 14: Calculadora de polinomios#
"""Hacer una función que reciba coeficientes de un polinomio y un valor de x, y calcule el 
valor del polinomio"""
def evaluar_polinomio(coeficientes, x):
    resultado = 0
    grado = len(coeficientes) - 1
    for i, coef in enumerate(coeficientes):
        resultado += coef * (x ** (grado - i))
    return resultado


print(evaluar_polinomio([4,2, 2, 1], 3)) 