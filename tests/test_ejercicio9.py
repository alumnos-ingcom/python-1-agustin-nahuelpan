################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio9 import factores_primos

"""
Prueba si devuelve los factores primos de un numero, y si identifica un numero primo.
"""
def test_factores_primos_verdadero():
    """
    Prueba si devuelve los factores primos de un numero.
    """
    numero = 935
    primos =  factores_primos(numero)
    resultado = (5, 11)
    assert isinstance(primos, tuple), "Devuleve una tupla."
    assert resultado == primos, "La función devuelve un resultado verdadero."

def test_factores_primos_verdadero():
    """
    Prueba si devuelve los factores primos de un numero.
    """
    numero = 2963
    primos =  factores_primos(numero)
    resultado = ()
    assert isinstance(primos, tuple), "Devuleve una tupla."
    assert resultado == primos, "La función devuelve un resultado verdadero. Identifica cuando un numero es primo."