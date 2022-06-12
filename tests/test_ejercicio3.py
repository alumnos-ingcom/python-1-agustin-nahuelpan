################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio3 import compara

"""
El test compara si la función puede sealar cuando un numero es más grande, más chico, o igual que otro
"""


def test_compara_primero_chico():
    """
    Prueba si devuelve que el primero es más chico que el segundo.
    """
    numero = 5
    otro_numero = 6
    regreso = compara(numero, otro_numero)
    assert regreso == -1, "El resultado es correcto. El primer número es más chico que el segundo."
    
    pass

def test_compara_primero_grande():
    """
    Prueba si devuelve que el primero es más grande que el segundo.
    """
    numero = 8
    otro_numero = 6
    regreso = compara(numero, otro_numero)
    assert regreso == 1, "El resultado es correcto. El segundo número es más chico que el primero."
    
    pass

def test_compara_igualdad():
    """
    Prueba si devuelve que son iguales.
    """
    numero = 6
    otro_numero = 6
    regreso = compara(numero, otro_numero)
    assert regreso == 0, "El resultado es correcto. Los resultados son identicos."
    
    pass