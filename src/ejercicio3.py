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
#precondiciones: Se deben ingresar dos numeros.
#poscondiciones:Se retornara un numero.

def compara(numero, otro_numero):
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
    compara(numero, otro_numero)
