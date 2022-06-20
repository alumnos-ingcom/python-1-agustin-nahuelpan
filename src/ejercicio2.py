#Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Números positivos y negativos
Escribir una función que reciba un número e indique si el mismo es positivo, negativo o cero utilizando sumas y restas.
"""

def signo(numero):
    """
    Está función dice si el número ingresado es positivo, negativo o 0
    Precondiciones:Se debe ingresar un numero.
    Poscondiciones:Se suministrara una cadena de texto que indica el tipo de número ingresado.
    """
    positivo = numero #Guarda numero dentro de una variable positivo para realizar operaciones.
    negativo = numero #También guarda numero dentro de otra variable para realizar operaciones.
    inicio = 1 #Una variable creada para mantener el while.
    while  inicio > 0:
        positivo = positivo + 1 #La variable con el mismo valor que el numero ingresado se le suma un 1. Si llega a 0 es porque el numero era positivo.
        negativo = negativo - 1 #La variable con el mismo valor que el numero ingresado se le suma un 1. Si llega a 0 significa que era negativo.
        if positivo == 0:
            regreso = -1
            inicio = 0
        elif negativo == 0:
            regreso = 1
            inicio = 0
        elif negativo == -1 and positivo ==1: #La única forma que estos valores ocurran en simultaneo es si el numero ingresado es 0.
            regreso = 0
            inicio = 0
    return regreso
    
def principal():
    """
    Esta función es la parte interactiva del ejercicio. Pide el numero para analizar y devuelve el resultado.
    """
    numero = int(input("Ingrese un numero para señalar si es cero, positivo, o negativo: "))
    regreso = signo(numero)
    if regreso == 1:
        print ("El numero ingresado es positivo.")
    elif regreso == -1:
        print ("El numero ingresado es negativo.")
    elif regreso == 0:
        print ("El numero ingresado es 0")
    
    
if __name__ == "__main__":
    principal()
    signo(numero)

