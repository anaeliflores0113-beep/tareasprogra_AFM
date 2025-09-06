#Ejercicio 11: Calcular una determinante de una matriz#
"""Hacer una función que calcule la determinante de una matriz de 3x3"""
def determinante_3x3(m):
    a, b, c = m[0]
    d, e, f = m[1]
    g, h, i = m[2]
    return a*e*i + b*f*g + c*d*h - c*e*g - a*f*h - b*d*i


matriz = [
    [1, 4, 6],
    [0, 2, 4],
    [3, 7, 0]
]
print(determinante_3x3(matriz))  
