################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
11. Multiplos de
Escribir una función que indique con True si un número entero es multiplo de otro, utilizando
sumas y restas.
"""

def principal():
    """
    Esta funcion se encarga de pedir los numetos y devolver si uno es multiplo del otro.
    #Precondiciones: Deben ser dos numeros enteros.
    Poscondiciones: Devolvera un valor lógico, o una cadena indicando que es falso.
    """
    print ("Ingrese un numero y después un segundo numero para verificar si este multiplo.")
    numero = int(input("Ingrese el primer numero: "))
    multiplo = int(input("Ingrese el segundo numero: "))
    devolver = es_multiplo(numero, multiplo)
    print (f"La prueba de verificación para averiguar si {multiplo} es multiplo de {numero} dio como resultado: {devolver}.")
    

def es_multiplo(numero, multiplo):
    """
    
    Precondiciones: Deben ser dos numeros enteros.
    Poscondiciones: Devolvera un valor lógico.
    """
    cuenta = 1 #Necesaria para mantener el bucle while.
    devolver = False #A menos que se prueba que el segundo numero es multiplo del primero, la función devolvera que es falso.
    while cuenta == 1:
        multiplo = multiplo - numero #Si llego a 0 restando el primer numero al segundo querra decir que este último es multiplo.
        if multiplo == 0:
            devolver = True
            cuenta = 0
        elif multiplo < numero: #En caso de que me pase del 0, sabre que el segundo numero no es multiplo.
            cuenta = 0
    return devolver

if __name__ == "__main__":
    principal()
    es_multiplo(numero, multiplo)