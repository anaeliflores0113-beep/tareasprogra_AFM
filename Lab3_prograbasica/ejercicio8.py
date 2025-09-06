#Ejercicio 8: Función para verificar palíndromo#
"""Hacer una función que determine si un texto es palíndromo o no"""
def palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]


print(palindromo("Anita lava la tina"))  
