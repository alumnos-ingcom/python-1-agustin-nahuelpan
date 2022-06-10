################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

#import pytest
#from src.ejercicio6 import ordenar_menor_a_mayor ordenar_mayor_a_menor

"""
Este test prueba el orden que devuelve las funciones: ordenar_menor_a_mayor y ordenar_mayor_a_menor.
La cantidad de funciones esta pensadas para probar todos los caminos posibles.
"""


def test_ordenar_menor_a_mayor():
    """
    Primer camino. El orden de salida debería ser (tres, dos, uno)
    """
    uno = 1
    dos = 2
    tres = 3
    comparacion = (tres, dos, uno)
    orden = ordenar_menor_a_mayor(uno, dos, tres)
    assert comparación == orden, "No hay problema con el orden de la tupla."
    assert isinstance(orden, str)
    
    pass

def test_ordenar_menor_a_mayor():
    """
    Segundo camino. El orden de salida debería ser (tres, uno, dos)
    """
    uno = -6
    dos = -10
    tres = 6
    comparacion = (tres, uno, dos)
    orden = ordenar_menor_a_mayor(uno, dos, tres)
    assert comparación == orden, "No hay problema con el orden de la tupla."
    assert isinstance(orden, str)
    
    pass


def test_ordenar_menor_a_mayor():
    """
    Primer camino. El ordem de salida debería ser (dos, tres, uno)
    """
    uno = 1
    dos = 15
    tres = -3
    comparacion = (dos, tres, uno)
    orden = ordenar_menor_a_mayor(uno, dos, tres)
    assert comparación == orden, "No hay problema con el orden de la tupla."
    assert isinstance(orden, str)
    
    pass

def test_ordenar_menor_a_mayor():
    """
    Primer camino. El ordem de salida debería ser (dos , uno, tres)
    """ 
    uno = 1
    dos = 2
    tres = 3
    comparacion = (dos , uno, tres)
    orden = ordenar_menor_a_mayor(uno, dos, tres)
    assert comparación == orden, "No hay problema con el orden de la tupla."
    assert isinstance(orden, str)
    
    pass

def test_ordenar_menor_a_mayor():
    """
    Primer camino. El ordem de salida debería ser (uno , tres, dos)
    """
    uno = 1
    dos = 2
    tres = 3
    comparacion = (uno , tres, dos)
    orden = ordenar_menor_a_mayor(uno, dos, tres)
    assert comparación == orden, "No hay problema con el orden de la tupla."
    assert isinstance(orden, str)
    
    pass

def test_ordenar_menor_a_mayor():
    """
    Primer camino. El ordem de salida debería ser (uno, dos, tres)
    """
    uno = 1
    dos = 2
    tres = 3
    comparacion = (uno, dos, tres)
    orden = ordenar_menor_a_mayor(uno, dos, tres)
    assert comparación == orden, "No hay problema con el orden de la tupla."
    assert isinstance(orden, str)
    
    pass

def test_ordenar_mayor_a_menor():
    """
    Primer camino. El ordem de salida debería ser (tres, dos, uno)
    """
    uno = 1
    dos = 2
    tres = 3
    comparacion = (tres, dos, uno)
    orden = ordenar_menor_a_mayor(uno, dos, tres)
    assert comparación == orden, "No hay problema con el orden de la tupla."
    assert isinstance(orden, str)
    
    def test_ordenar_mayor_a_menor():
    """
    Primer camino. El orden de salida debería ser (tres, uno, dos) """
    uno = 1
    dos = 2
    tres = 3
    comparacion = (tres, uno, dos)
    orden = ordenar_menor_a_mayor(uno, dos, tres)
    assert comparación == orden, "No hay problema con el orden de la tupla."
    assert isinstance(orden, str)
    
    def test_ordenar_mayor_a_menor():
    """
    Primer camino.El ordem de salida debería ser (dos, tres ,uno)
    """
    uno = 1
    dos = 2
    tres = 3
    comparacion = (dos, tres ,uno)
    orden = ordenar_menor_a_mayor(uno, dos, tres)
    assert comparación == orden, "No hay problema con el orden de la tupla."
    assert isinstance(orden, str)
    

def test_ordenar_mayor_a_menor():
    """
    Primer camino. El ordem de salida debería ser (dos , uno, tres)
    """
    uno = 1
    dos = 2
    tres = 3
    comparacion = (dos , uno, tres)
    orden = ordenar_menor_a_mayor(uno, dos, tres)
    assert comparación == orden, "No hay problema con el orden de la tupla."
    assert isinstance(orden, str)
    
    pass

def test_ordenar_mayor_a_menor():
    """
   Primer camino. El ordem de salida debería ser (uno , tres , dos)
    """
    uno = 1
    dos = 2
    tres = 3
    comparacion = (uno , tres , dos)
    orden = ordenar_menor_a_mayor(uno, dos, tres)
    assert comparación == orden, "No hay problema con el orden de la tupla."
    assert isinstance(orden, str)
    
    pass

def test_ordenar_mayor_a_menor():
    """
    Primer camino. El ordem de salida debería ser (uno, dos, tres)
    """
    uno = 1
    dos = 2
    tres = 3
    comparacion = (uno, dos, tres)
    orden = ordenar_menor_a_mayor(uno, dos, tres)
    assert comparación == orden, "No hay problema con el orden de la tupla."
    assert isinstance(orden, str)
    
    pass