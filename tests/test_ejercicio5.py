################
# Nombre - @usuario_github
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio5 import division_lenta

"""
Se esta probando si la función división lenta devuelve un resultado adecuado para la división de los numero
recibidos. 
"""
def test_division_lenta():
    """
    Se define el dividiendo y el divisor y se los envia a la función. Luego, comprueba que lo que devuelve sea el
    resto y la división comparandolos con una cuenta directa.
    """
    dividiendo = 86 
    divisor = 7
    cociente = division_lenta(dividiendo, divisor)
    resto = division_lenta(dividiendo, divisor)
    prueba_resto = dividiendo % divisor
    prueba_cociente = dividiendo // divisor
    prueba_final = (prueba_cociente, prueba_resto)
    assert prueba_final == cociente, "El resto y el cociente que otorga la función es correcto."
    
def test_division_lenta_negativos():
    """
    Se define el dividiendo y el divisor y se los envia a la función. Luego, comprueba que lo que devuelve sea el resto y la división comparandolos con una cuenta directa.
    """
    dividiendo = -56 
    divisor = -3
    cociente, resto = division_lenta(dividiendo, divisor)
    #resto = division_lenta(dividiendo, divisor)
    prueba_resto = dividiendo % divisor
    prueba_cociente = dividiendo // divisor
    prueba_final = (prueba_cociente, prueba_resto)
    assert prueba_final == (cociente, resto), "El resto y el cociente que otorga la función es correcto."