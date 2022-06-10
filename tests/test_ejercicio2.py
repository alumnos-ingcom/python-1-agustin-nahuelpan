################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio2 import signo

"""
Describir aquí que es lo que se esta probando.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""

def test_signo_neutro():
    """
    Una breve descripción del caso de prueba aplicado a la función
    """
    numero = 0
    prueba = "El numero ingresado es 0"
    regreso = signo(numero)
    assert prueba == regreso, "La función responde adecuadamente demostrando que el texto enviado seala el numero ingresado adecuadamente.El numero ingresado es 0."
    assert isinstance(regreso, str), "El resultado es una cadena de texto."
    
    pass

def test_signo_negativo():
    """
    Una breve descripción del caso de prueba aplicado a la función
    """
    numero = -2
    prueba = "El numero ingresado negativo"
    regreso = signo(numero)
    assert prueba == regreso, "La función responde adecuadamente demostrando que el texto enviado seala el numero ingresado adecuadamente. El numero ingresado es negativo." 
    assert isinstance(regreso, str), "El resultado es una cadena de texto."
    
    pass

def test_signo_positivo():
    """
    Una breve descripción del caso de prueba aplicado a la función
    """
    numero = 84
    prueba = "El numero ingresado es positivo"
    regreso = signo(numero)
    assert prueba == regreso, "La función responde adecuadamente demostrando que el texto enviado seala el numero ingresado adecuadamente.El numero ingresado es positivo."
    assert isinstance(regreso, str), "El resultado es una cadena de texto."
    
    pass