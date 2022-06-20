################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
8. Números primos
Escribir una función que indique con True si un numero indicado es Primo.
"""

def principal():
    """
    Esta función pregunta que numero se desea evaluar. Y devuelve si es primo o no.
    Precondiciones:Se debe ingresar un numero entero.
    Poscondiciones: Devuelve true si el numero es primo y false en caso de que no lo sea.
    """
    numero = int(input("Introduzca un numero para saber si es primo o no. El resultado en caso de ser primo sera: True. En caso de no ser primo, sera False: "))
    resultado = es_primo(numero)
    print (f"{resultado}")

def es_primo(numero):
    """
    Esta funcion revisa si un numero es un numero primo. Es decir si solo es divisible por si mismo y
    uno.
    Precondiciones:Se debe ingresar un numero entero.
    Poscondiciones: Devuelve true si el numero es primo y false en caso de que no lo sea.
    """
    divisor=numero-1 #Cómo un numero es primo unicamente cuando es divisible por si mismo y por 1, se lo intentara dividir por los demás numeros que lo separan de 1.
    resultado = False
    while divisor > 1: #Se pruena todos los divisores posibles para corraborar que sean primo. Si ninguno da 0 antes de llegar al uno, sabemos que es primo.
        prueba=numero % divisor
        if prueba == 0:
            divisor = 0
        divisor = divisor -1
        if divisor == 1:
            resultado = True
    return resultado

if __name__ == "__main__":
    principal()
    es_primo(numero)