################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio4 import suma_lenta

"""
El test prueba si el la función suma correctamente los numeros.
"""
def test_suma_lenta_negativos():
    """
    Prueba si el programa puede sumar numeros negativos.
    """
    numero = -8
    otro_numero = -6
    resultado = suma_lenta(numero, otro_numero)
    respuesta = "-8+(-1)+(-1)+(-1)+(-1)+(-1)+(-1)=-14"
    assert resultado == respuesta, "El programa realiza la suma apropiadamente con numeros negativos."

def test_suma_lenta_positivos():
    """
    Prueba si el programa puede sumar numeros positivos.
    """
    numero = 7
    otro_numero = 15
    resultado = suma_lenta(numero, otro_numero)
    respuesta = "7+1+1+1+1+1+1+1+1+1+1+1+1+1+1+1=22"
    assert resultado == respuesta, "El programa realiza la suma apropiadamente con numeros positivos."