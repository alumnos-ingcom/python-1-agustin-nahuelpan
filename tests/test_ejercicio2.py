################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#import pytest
#from src.ejercicio2 import signo

"""
Describir aquí que es lo que se esta probando.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""


def test_signo_como_zero():
    """
    Una breve descripción del caso de prueba aplicado a la función
    """
    numero = 0
    regreso = signo(numero)
    assert numero == 0, "El numero ingresado es ciertamente cero" #Parece obvio pero lo pongo para probar que el programa no haga minipulaciones raras.
    assert isinstance(resultado, str), "El resultado es una cadena de texto."
    
    pass

def test_signo_positivo():
    """
    Una breve descripción del caso de prueba aplicado a la función
    """
    numero = 0
    regreso = signo(numero)
    assert numero == 0, "El numero ingresado es ciertamente cero" #Parece obvio pero lo pongo para probar que el programa no haga minipulaciones raras.
    assert isinstance(resultado, str), "El resultado es una cadena de texto."
    
    pass

def test_signo_negativo():
    """
    Una breve descripción del caso de prueba aplicado a la función
    """
    numero = -35
    regreso = signo(numero)
    assert numero < 0, "El numero ingresado es negativo" #Parece obvio pero lo pongo para probar que el programa no haga minipulaciones raras.
    assert isinstance(resultado, str), "El resultado es una cadena de texto."
    
    pass

def test_signo_positivo():
    """
    Una breve descripción del caso de prueba aplicado a la función
    """
    numero = 84
    assert numero > 0, "El numero ingresado es positivo" #Parece obvio pero lo pongo para probar que el programa no haga minipulaciones raras.
    assert isinstance(resultado, str), "El resultado es una cadena de texto."
    
    pass