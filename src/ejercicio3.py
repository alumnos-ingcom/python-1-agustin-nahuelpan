################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Comparación de números
Escribir una función que utilizando sumas y restas, reciba dos valores y retorne:
Retornar -1 si el primero es menor que el segundo
Retornar 0 si son iguales
Retornar 1 si el primero es mayor que el segundo
"""

def principal():
    """
    Esta función recibe los numetos que el usuario quiere compara y devuelve un resultado acorde
    al resultado de la operación.
    """
    print ("Bienvenido, por favor, ingrese 2 numeros para comparar. El resultado de la comparación sera: 0 en caso de ser iguales, 1 en caso de que el primero sea más grande que el segundo, y -1 si el segundo es más grande que el primero.")
    numero = int(input("Ingresa el primer numero: "))
    otro_numero = int(input("Ingresa el segundo numero: "))
    regreso = compara(numero, otro_numero)
    print (f"{regreso}")

def compara(numero, otro_numero):
    """
    Esta función compara numeros y devuelve tres opciones: si el primero es menor que el
    segundo con un -1. Si son iguales con un 0. Y si el primero es mayor que el segundo con un 1.
    Precondiciones: Se deben ingresar dos numeros.
    Poscondiciones:Se retornara un numero.
    """
    primera = numero + (otro_numero) #Cómo el enunciado decía que necesitaba utilizar sumas y restas decidi sumar ambos numeros al inicio.
    segunda = primera + (numero) #Vuelvo a sumar los números indendientemente al resultado ya obtenido.
    tercera = primera + (otro_numero)
    if segunda > tercera:  #Si el resultado de la suma de los numeros más el primero es más grande, devuelve que el primero es más grande.
        regreso = 1
    elif tercera > segunda:#Si el resultado de la suma de los numeros más el segundo es más grande, devuelve el segundo como más grande.
        regreso = -1
    else:#Y en caso de que no sea ninguna de las opciones devuelve que son iguales.
        regreso = 0
    return regreso

if __name__ == "__main__":
    principal()
    compara(numero, otro_numero)