################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#import pytest
#from src.ejercicio6 import ordenar_menor_a_mayor ordenar_mayor_a_menor

"""
Comprueba que devuelve True cuando se introduce los numeros adecuados, y que no lo haga cuando se introducen numero erroneos.
"""


def test_es_multiplo():
    """
    Este test comprueba que devuelva el valor True con los numeros adecuados.
    """
    numero = 5
    multiplo = 100
    devolver = es_multiplo(numero, multiplo)
    assert devolver == True, "Devuelve el valor true cuando se le introducen los valores correctos."
    
    pass

def test_es_multiplo_no():
    """
    Este test comprueba que no devuelve el valor True con cualquier valor.
    """
    numero = 6
    multiplo = 98
    devolver = es_multiplo(numero, multiplo)
    assert devolver != True, "Devuelve otra cosa que no es true cuando los numeros ingresados no son correctos." 
    
    pass