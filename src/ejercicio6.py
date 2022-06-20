################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
6. Ordenar 3 valores
Escribir una función que a partir de tres variables de tipo entero retorne una tupla con dichos valores ordenados de menor a mayor. Y Viceversa
"""

def principal():
    """
    Esta es la función interactiva que pide y devuelve el resultado.
    Precondiciones: Se deben ingresar tres numeros.
    Poscondiciones: Se retornara una tupla con los tre numeros ingresados en un orden creciente o decreciente.
    """
    print ("Ingrese 3 numeros para ordenarlos.")
    uno = int(input("Ingrese un numero: "))
    dos = int(input("Ingrese un numero: "))
    tres = int (input("Ingrese un numero: "))
    orden = int(input("Para ordenar de mayor a menor ingrese un 1. Para ordenarlos de menor a mayor ingrese 2."))
    if orden == 1:
        orden = ordenar_mayor_a_menor(uno, dos, tres)
        eleccion = "mayor a menor"
    elif orden ==2:
        orden = ordenar_menor_a_mayor(uno, dos, tres)
        eleccion = "menor a mayor"
    print (f"El orden eligido fue: {eleccion}.Y el resultado es: {orden}")

def ordenar_mayor_a_menor(uno, dos, tres):
    """
    Esta función ordena los numeros recibidos de mayor a menor.
    Precondiciones: Se deben ingresar tres numeros.
    Poscondiciones: Se retornara una tupla con los tre numeros ingresados en un orden decreciente
    """
    if uno > dos and uno > tres:
        if dos > tres:
            orden = (uno, dos, tres)
        elif tres > dos:
            orden = (uno, tres, dos)
    elif dos > uno and dos > tres:
        if uno > tres:
            orden = (dos, uno, tres)
        elif tres > uno:
            orden = (dos, tres, uno)
    elif tres > uno and tres > dos:
        if uno > dos:
            orden = (tres, uno, dos)
        elif dos > uno:
            orden = (tres, dos, uno)
    return orden            
    
def ordenar_menor_a_mayor(uno, dos, tres):
    """"
    Esta función ordena los numeros de menor a mayor.
    Precondiciones: Se deben ingresar tres numeros.
    Poscondiciones: Se retornara una tupla con los tre numeros ingresados en un orden creciente.
    """
    if uno < dos and uno < tres:
        if dos < tres:
            orden = (uno, dos, tres)
        elif tres < dos:
            orden = (uno, tres, dos)
    elif dos < uno and dos < tres:
        if uno < tres:
            orden = (dos, uno, tres)
        elif tres < uno:
            orden = (dos, tres, uno)
    elif tres < uno and tres < dos:
        if uno < dos:
            orden = (tres, uno, dos)
        elif dos < uno:
            orden = (tres, dos, uno)
    return orden
    
if __name__ == "__main__":
    principal()
    ordenar_menor_a_mayor(uno, dos, tres)
    ordenar_mayor_a_menor(uno, dos, tres)    