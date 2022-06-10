################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#import pytest
#from src.ejercicio3 compara

"""
Describir aquí que es lo que se esta probando.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""


def test_compara_primero_chico():
    """
    Una breve descripción del caso de prueba aplicado a la función
    """
    numero = 5
    otro_numero = 6
    regreso = compara(numero, otro_numero)
    assert regreso == -1, "El resultado es correcto. El primer número es más chico que el segundo."
    
    pass

def test_compara_primero_grande():
    """
    Una breve descripción del caso de prueba aplicado a la función
    """
    numero = 8
    otro_numero = 6
    regreso = compara(numero, otro_numero)
    assert regreso == 1, "El resultado es correcto. El segundo número es más chico que el primero."
    
    pass

def test_compara_igualdad():
    """
    Una breve descripción del caso de prueba aplicado a la función
    """
    numero = 6
    otro_numero = 6
    regreso = compara(numero, otro_numero)
    assert regreso == 0, "El resultado es correcto. Los resultados son identicos."
    
    pass