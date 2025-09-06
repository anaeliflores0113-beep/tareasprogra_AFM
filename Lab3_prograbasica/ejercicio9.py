#Ejercicio 9: Función para encontrar el segundo mayor de una lista#
"""Hacer una función que identifique el segundo elemento mayor de una lista de números"""
def segundo_mayor(lista):
    lista = list(set(lista)) 
    lista.sort(reverse=True)
    return lista[1] if len(lista) > 1 else None


print(segundo_mayor([2, 3, 9, 7, 4, 3]))  
