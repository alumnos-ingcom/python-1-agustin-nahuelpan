 ################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#import pytest
#from src.ejercicio1 import convertir_a_fahrrenheit convertir_a_centigrados

"""
Se prueba que la salida de los programas sea un numero.
"""


def test_convertir_a_fahrrenheit():
    """
    Revisa que devuelva un numero con coma.
    """
    numero = 4562
    resultado = convertir_a_fahrrenheit(numero)
    assert isinstance(resultado, float), "El resutado es un numero con coma."
    
    
def test_convertir_a_centigrados():
    """
    Revisa que devuelva un numero con coma.
    """
    numero = 235
    resultado = convertir_a_centigrados(numero)
    assert isinstance(resultado, float), "El resutado es un numero con coma."
    
    
    pass
