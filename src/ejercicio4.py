################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
4. Suma lenta
Escribir una función que haga la suma entre dos números enteros sin hacer la operación de manera
directa. Esto quiere decir que para hacer la suma entre 4 y 3, las operaciones resultantes
deberán ser 4+1+1+1.
La funcion debe ser capaz de sumar cualquier numero entero positivo y negativo.
"""

def principal():
    """
    Esta función se encarga de pedir los numeros a sumar, y devuelve el resultado.
    Precondiciones: Se deben ingresar dos numeros.
    Poscondiciones: Devolvera la salida de los números después de que haya sido sumado por partes.
    """
    print ("Ingrese dos numeros para sumar.")
    numero = int(input("Ingrese el primer numero: "))
    otro_numero = int(input("Ingrese el segundo numero: "))
    resultado = suma_lenta(numero, otro_numero)
    print (f"El resultado de la suma es: {resultado}")
    

def suma_lenta(numero, otro_numero):
    """
    Esta función se encarga de realizar una suma lenta.
    Precondiciones: Se deben ingresar dos numeros.
    Poscondiciones: Devolvera la salida de los números después de que haya sido sumado por partes.
    """
    final = numero
    resultado = str(numero)
    if otro_numero > 0: #Si el segundo numero ingresado es positivo sigue este camino.
        while otro_numero > 0:
            final = final + 1 #Suman uno por uno.
            resultado = resultado + ("+1")
            otro_numero = otro_numero - 1
    else: #Si el numero ingresado es negativo sigue este otro camino.
        while otro_numero < 0:
            final = final +(-1) #Resta uno por uno.
            resultado = resultado + ("+(-1)")
            otro_numero = otro_numero +1
    final = str(final)
    resultado = resultado + ("=") + final
    return resultado

if __name__ == "__main__":
    principal()
    suma_lenta(numero, otro_numero)