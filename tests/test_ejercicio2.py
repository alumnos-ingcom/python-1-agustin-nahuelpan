################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio2 import signo

"""
Este test probara si la función devuelve el resultado esperado segun los numeros que se le ingresen.
"""
def test_signo_neutro():
    """
    Prueba si devuelve que el numero ingresado es 0.
    """
    numero = 0
    prueba = 0
    regreso = signo(numero)
    assert prueba == regreso, "La función responde adecuadamente.El numero ingresado es 0."
    assert isinstance(regreso, int), "El resultado es un numero entero."

def test_signo_negativo():
    """
    Prueba si devuelve que el numero es negativo.
    """
    numero = -56
    prueba = -1
    regreso = signo(numero)
    assert prueba == regreso, "La función responde adecuadamente. El numero ingresado es negativo." 
    assert isinstance(regreso, int), "El resultado es un numero entero."

def test_signo_positivo():
    """
    Prueba si el numero ingresado es positivo.
    """
    numero = 84
    prueba = 1
    regreso = signo(numero)
    assert prueba == regreso, "La función responde adecucuadamente. El numero ingresado es positivo."
    assert isinstance(regreso, int), "El resultado es un numero entero."