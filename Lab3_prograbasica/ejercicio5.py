#Ejercicio 5: Función para calcular el promedio#
"""Hacer una funcion que reciba una lista de calificaciones y devuelva el promedio"""
def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)


print(calcular_promedio([10, 9, 10]))
print(calcular_promedio([9, 7, 9, 8]))
