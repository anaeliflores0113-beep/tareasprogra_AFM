#Ejercicio 7: Función para calcular la mediana#
"""Hacer una función que calcule la mediana de una lista de números. Usando .sort de lista 
para ordenar la lista"""
def mediana(lista):
    lista_ordenada = lista.copy()
    lista_ordenada.sort()  
    n = len(lista_ordenada)
    medio = n // 2

    if n % 2 == 0:
        return (lista_ordenada[medio - 1] + lista_ordenada[medio]) / 2
    else:
        return lista_ordenada[medio]


print(mediana([6, 3, 5]))      
print(mediana([2, 9, 3, 5]))  

