################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
9. Factores Primos
Escribir una función que retorne una tuple con factores primos de un numero entero positivo.
"""

#Precondiciones: Se debe ingresar un numero entero positivo.
#Poscondiciones: Devolvera una tupla con los factores primos.

def factores_primos(numero):
    primos = [] #Se crea una tupla vacía para almacenar los factores primos.
    contador = numero
    aumento = 2 #Se establece el primer numero primo por el que va a empezar a dividir.
    while aumento < contador: #Establece los parametros para cuando debe cortar.
        if numero % aumento == 0: #Solo cuenta los numeros que pueden llegar a un resto de 0. Es decir, los factores primos del mismo.
            primos.append(aumento) #Se agrega a la tupla el numero capaz de hacerlo.
            contador = contador / aumento #Se divide el numero para seguir con la cuenta, pero asegurando que eventualemnte vaya a terminar.
        aumento = aumento + 1 #Progresivamente va aumentando para encontrar a los factores primos.
    primos = tuple(primos)
    return primos

    pass

if __name__ == "__main__":
    factores_primos(numero)