################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio8 import es_primo

"""
Prueba si la función es capaz de reconocer un numero palindromo de uno que no lo es.
"""
def test_es_primo_no_primo():
    """
    Esta función prueba que sucede cuando el numero no es primo. Prueba que el programa reconoce cuando no es
    primo.
    """
    numero = 50
    salida = es_primo(numero)
    assert isinstance(salida, int), "El resultado es un numero entero. "
    assert salida == False, "El programa muestra correctamente cuando un numero no es primo."

def test_es_primo():
    """
    Esta funcion prueba si puede reconocer a un numero primo.
    """
    numero = 7
    salida = es_primo(numero)
    assert isinstance(salida, int), "El resultado "
    assert salida == True, "El resultado es correcto."