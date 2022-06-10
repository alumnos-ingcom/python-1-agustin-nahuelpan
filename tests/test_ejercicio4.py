################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio4 import suma_lenta

"""
Describir aquí que es lo que se esta probando.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""


def test_suma_lenta_negativos():
    """
    Una breve descripción del caso de prueba aplicado a la función
    """
    numero = -8
    otro_numero = -6
    resultado = suma_lenta(numero, otro_numero)
    respuesta = numero + (otro_numero)
    assert resultado == respuesta, "El programa realiza la suma apropiadamente con numeros negativos."
    
    pass

def test_suma_lenta_positivos():
    """
    Una breve descripción del caso de prueba aplicado a la función
    """
    numero = 7
    otro_numero = 15
    resultado = suma_lenta(numero, otro_numero)
    respuesta = numero + (otro_numero)
    assert resultado == respuesta, "El programa realiza la suma apropiadamente con numeros positivos."
    
    pass