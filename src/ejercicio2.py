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
    resultado = 0 + numero #Cómo pedía que se utilizen sumas y restas, realiza esta cuenta, y dependiendo el resultado dice que tipo de numero es.
    if resultado > 0:
        regreso = "El número ingresado es positivo"
    elif resultado < 0:
        regreso = "El número ingresado es negativo"
    else:
        regreso = "El número ingresado es 0"
    return regreso
    
    pass

if __name__ == "__main__":
    signo(numero)

