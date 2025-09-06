#Ejercicio 15: Juego de adivinanza#
"""Hacer una función que implemente una adivinanza sobre un número generado aleatorieamente
por la computadora que debe adivinar el usuario. Se debe dar pistas si el número ingresado 
es mayor o menor que el objetivo"""
import random

def juego_adivinanza():
    numero_objetivo = random.randint(1, 100)
    intento = None

    print("Adivina un número entre 1 y 100")

    while intento != numero_objetivo:
        try:
            intento = int(input("Intenta: "))
            if intento < numero_objetivo:
                print("El numero es mayor, intenta con un número mayor.")
            elif intento > numero_objetivo:
                print("El numero es menor, intenta con un número menor.")
            else:
                print("¡Felicidades! Adivinaste el número.")
        except ValueError:
            print("Por favor, ingresa un número válido.")


juego_adivinanza()
