################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio7 import sexadecimal_a_decimal
from src.ejercicio7 import decimal_a_sexadecimal

"""
Se prueba la salida de los tres datos: horas, minutos y segundos, convertidos a segundos. Y se prueba un numero siendo convertido a grados, minutos y segundos.
"""


def test_sexadecimal_a_decimal():
    """
    Este caso de prueba introduce tres variables de numeros enteros, y espera recibir un numero entero.
    """
    horas = 13
    minutos = 65
    segundos = 68
    comparacion = (horas * 60) * 60
    comparacion = comparacion + (minutos * 60)
    comparacion = comparacion + segundos
    devolver = sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(devolver, int), "La función devuelve un numero entero."
    assert comparacion == devolver, "La función desarrolla bien el calculo."
    
    pass

def test_decimal_a_sexadecimal():
    """
    La prueba revisa si puede convertir una tupla: en horas, minutos y segundos.
    """
    numero = 6584656
    devolver = decimal_a_sexadecimal(numero)
    assert isinstance(devolver, tuple), "La función devuelve uuna tupla."
    
    pass
