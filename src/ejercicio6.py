################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
6. Ordenar 3 valores
Escribir una función que a partir de tres variables de tipo entero retorne una tupla con dichos valores ordenados de menor a mayor. Y Viceversa
"""

#Precondiciones: Se deben ingresar tres numeros.
#Poscondiciones: Se retornara una tupla con los tre numeros ingresados en un orden creciente o decreciente.

def ordenar_mayor_a_menor(uno, dos, tres):
    if uno > dos and uno > tres:
        if dos > tres:
            orden = [uno, dos, tres]
        elif tres > dos:
            orden = [uno, tres, dos]
    elif dos > uno and dos > tres:
        if uno > tres:
            orden = [dos, uno, tres]
        elif tres > uno:
            orden = [dos, tres, uno]
    elif tres > uno and tres > dos:
        if uno > dos:
            orden = [tres, uno, dos]
        elif dos > uno:
            orden = [tres, dos, uno]
    return orden        
    
    pass

if __name__ == "__main__":
    ordenar_mayor_a_menor(uno, dos, tres)    
    
    
def ordenar_menor_a_mayor(uno, dos, tres):
    if uno < dos and uno < tres:
        if dos < tres:
            orden = [uno, dos, tres]
        elif tres < dos:
            orden = [uno, tres, dos]
        
    elif dos < uno and dos < tres:
        if uno < tres:
            orden = [dos, uno, tres]
        elif tres < uno:
            orden = [dos, tres, uno]
    elif tres < uno and tres < dos:
        if uno < dos:
            orden = [tres, uno, dos]
        elif dos < uno:
            orden = [tres, dos, uno]
    return orden
    
    pass

if __name__ == "__main__":
    ordenar_menor_a_mayor(uno, dos. tres)