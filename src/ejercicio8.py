################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
8. Números primos
Escribir una función que indique con True si un numero indicado es Primo.
"""

#Precondiciones:Se debe ingresar un numero.
#Poscondiciones: Devuelve true si el numero es primo y false en caso de que no lo sea.

def es_primo(numero):
    divisor=numero-1 #Cómo un numero es primo unicamente cuando es divisible por si mismo y por 1, se lo intentara dividir por los demás numeros que lo separan de 1.
    resultado = "false"
    while divisor > 1: #Se pruena todos los divisores posibles para corraborar que sean primo. Si ninguno da 0 antes de llegar al uno, sabemos que es primo.
        prueba=numero % divisor
        if prueba == 0:
            divisor = 0
        divisor = divisor -1
        if divisor == 1:
            resultado = True
    return resultado

    pass

if __name__ == "__main__":
    es_primo(numero)