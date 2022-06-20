 ################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio1 import convertir_a_fahrrenheit 
from src.ejercicio1 import convertir_a_centigrados

"""
Se prueba que la salida de los programas sea el numero correcto.
"""
def test_convertir_a_fahrrenheit():
    """
    Revisa que devuelva un numero con coma.
    """
    numero = 4562
    comparación = 8243.6
    resultado = convertir_a_fahrrenheit(numero)
    assert isinstance(resultado, float), "El resutado es un numero con coma."
    assert comparación == resultado, "El resultado devuelto es el adecuado."
    
def test_convertir_a_centigrados():
    """
    Revisa que devuelva un numero con coma.
    """
    numero = 235
    comparación = 112.77777777777777
    resultado = convertir_a_centigrados(numero)
    assert isinstance(resultado, float), "El resutado es un numero con coma."
    assert comparación == resultado, "El numero resultante es correcto."

def test_doble():
    """
    Prueba que ambos funcione en simultaneo.
    """
    numero = 250.0
    final = 250.0
    resultado = convertir_a_centigrados(numero)
    numero = resultado
    resultado = convertir_a_fahrrenheit(numero)
    assert final == resultado, "El resultado es el mismo que el numero ingresado después de haber sido convertido de centigrados a fahrreinheit, y de fahrreinheit a centigrados."