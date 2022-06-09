#Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Números positivos y negativos
Escribir una función que reciba un número e indique si el mismo es positivo, negativo o cero utilizando sumas y restas.
"""
#Precondiciones:Se debe ingresar un numero.
#Poscondiciones:Se suministrara una cadena de texto que indica el tipo de número ingresado.

def signo(numero):
    """Está función dice si el número ingresado es positivo, negativo o 0"""
    positivo = numero #Guarda numero dentro de una variable positivo para realizar operaciones.
    negativo = numero #También guarda numero dentro de otra variable para realizar operaciones.
    inicio = 1 #Una variable creada para mantener el while.
    while  inicio > 0:
        positivo = positivo + 1 #La variable con el mismo valor que el numero ingresado se le suma un 1. Si llega a 0 es porque el numero era positivo.
        negativo = negativo - 1 #La variable con el mismo valor que el numero ingresado se le suma un 1. Si llega a 0 significa que era negativo.
        if positivo == 0:
            regreso = "El numero ingresado negativo"
            inicio = 0
        elif negativo == 0:
            regreso = "El numero ingresado es positivo"
            inicio = 0
        elif negativo == -1 and positivo ==1: #La única forma que estos valores ocurran en simultaneo es si el numero ingresado es 0.
            regreso = "El numero ingresado es 0"
            inicio = 0
    return regreso
    
    pass

if __name__ == "__main__":
    signo(numero)

