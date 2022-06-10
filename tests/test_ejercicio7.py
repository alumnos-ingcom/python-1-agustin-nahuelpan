################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Se prueba la salida de los tres datos: horas, minutos y segundos, convertidos a segundos. Y se prueba un numero siendo convertido a grados, minutos y segundos.
"""


def test_sexadecimal_a_decimal(horas, minutos, segundos):
    """
    Este caso de prueba introduce tres variables de numeros enteros, y espera recibir un numero entero.
    """
    horas = 13
    minutos = 65
    segundos = 68
    devolver = sexadecimal_a_decimal(horas, minutos, segundos)
    assert isinstance(devolver, int)
    assert isinstance
    
    pass

def test_decimal_a_sexadecimal(numero):
    """
    La prueba revisa si puede convertir una tupla: en horas, minutos y segundos.
    """
    numero = 6584656
    devolver = decimal_a_sexadecimal(numero)
    assert isinstance(devolver, str), "El numero fue convertido adecuadamente."
    
    pass
