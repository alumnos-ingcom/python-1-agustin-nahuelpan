################
# Nombre - @usuario_github
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#import pytest
#from src.ejercicio5 import división_lenta

"""
Se esta probando si la función división lenta devuelve un resultado adecuado para la división de los numero recibidos. 
"""


def test_division_lenta():
    """
    Se define el dividiendo y el divisor y se los envia a la función. Luego, comprueba que lo que devuelve sea el resto y la división comparandolos con una cuenta directa.
    """
    dividiendo = 86 
    divisor = 7
    cociente = división_lenta(dividiendo, divisor)
    resto = division_lenta(dividiendo, divisor)
    assert dividiendo % divisor == resto, "El resto que otorga la función es correcto."
    assert dividiendo // divisor == cociente, "El cociente de la división es correcto."
    
    pass