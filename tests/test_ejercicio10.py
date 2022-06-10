################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio10 import es_palindromo

"""
Se esta probando si la función puede identificar que es un palidromo de algo que no lo es. Es decir el funcionamiento.
"""


#def test_es_palindromo():
#    """
#    Prueba realizada para comprobar si la función puede identificar que no es un palindromo.
#    """
#    palindromo = "Y comprobamos que esto ciertamente no puede considerar un palindromo"
#    devolver = es_palindromo(palindromo)
#    assert devolver == False, "El palindromo indica que la palabra no es palindromo adecuadamente."  
    
#    pass

def test_es_palindromo():
    """
    Prueba si la función consigue identificar un palindromo efectivamente.
    """
    palindromo = "Yo hago yoga hoy"
    devolver = es_palindromo(palindromo)
    assert devolver == True, "La función consigue identificar un palindromo."
    
    pass