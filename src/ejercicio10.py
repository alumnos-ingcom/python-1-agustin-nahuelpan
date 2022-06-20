################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
10. Palíndromo
Escribir una función que indique con True si una palabra o frase ingresada se trata de un palindromo. Palíndromo, es si se lee igual de derecha a izquierda que de izquierda a derecha.
"""

def principal():
    """
    Esta función se encarga de pedir los datos y devolver si la cadena ingresada es o no es un
    palindromo.
    Precondiciones: debe recibir una cadena o frase almacenada.
    Poscondiciones: Devuelve true o false dependiendo si es o no un palindromo.
    """
    print ("Esta funcion devolvera True si la cadena ingresada es un palindromo, o False si no lo es.")
    palindromo = input("Ingrese una cadena para saber si es palindromo: ")
    devolver = es_palindromo(palindromo)
    print (f"El resultado con la operación realizada con la cadena {palindromo}, es {devolver}. ")

def es_palindromo(palindromo):
    """
    Esta función revisa que la cadena ingresada es o no un palindromo.
    Precondiciones: debe recibir una cadena o frase almacenada.
    Poscondiciones: Devuelve true o false dependiendo si es o no un palindromo.
    """
    palindromo = palindromo.lower()
    palindromo = palindromo.replace(" ", "")
    palindromo = palindromo.replace("á", "a")
    palindromo = palindromo.replace("é", "e")
    palindromo = palindromo.replace("í", "i")
    palindromo = palindromo.replace("ó", "o")
    palindromo = palindromo.replace("ú", "u")
    largo_de_palindromo = len(palindromo)-1 
    palindromo_prueba = 0
    prueba = 1
    while prueba > 0:
        if palindromo[palindromo_prueba] == palindromo[largo_de_palindromo]:
            palindromo_prueba = +1
            largo_de_palindromo = -1
            if largo_de_palindromo == -1:
                prueba = 0
                devolver = True
        elif palindromo[palindromo_prueba] != palindromo[largo_de_palindromo]:
            devolver = False
            prueba = 0
    return devolver

if __name__ == "__main__":
    principal()
    es_palindromo(palindromo)