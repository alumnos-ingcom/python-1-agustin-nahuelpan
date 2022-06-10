################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#import pytest
#from src.ejercicio6 import ordenar_menor_a_mayor ordenar_mayor_a_menor

"""
Describir aquí que es lo que se esta probando.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""


def test_factores_primos_verdadero():
    """
    Una breve descripción del caso de prueba aplicado a la función
    """
    numero = 935
    primos =  factores_primos(numero)
    assert isinstance(primos, tuple), "Devuleve una tupla."
    
    pass

