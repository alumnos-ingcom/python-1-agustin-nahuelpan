################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
4. Suma lenta
Escribir una función que haga la suma entre dos números enteros sin hacer la operación de manera directa. Esto quiere decir que para hacer la suma entre 4 y 3, las operaciones resultantes deberán ser 4+1+1+1.
La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.
"""

#Precondiciones: Se deben ingresar dos numeros.
#Poscondiciones: Devolvera la salida de los números después de que haya sido sumado por partes.

def suma_lenta(numero, otro_numero):
    resultado = numero
    if otro_numero > 0: #Si el segundo numero ingresado es positivo sigue este camino.
        while otro_numero > 0:
            resultado = resultado + 1 #Suman uno por uno.
            otro_numero = otro_numero - 1
    else: #Si el numero ingresado es negativo sigue este otro camino.
        while otro_numero < 0:
            resultado = resultado +(-1) #Resta uno por uno.
            otro_numero = otro_numero +1
    return resultado

if __name__ == "__main__":
    suma_lenta(numero, otro_numero)