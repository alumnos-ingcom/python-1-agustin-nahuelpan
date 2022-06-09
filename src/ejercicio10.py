################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
10. Palíndromo
Escribir una función que indique con True si una palabra o frase ingresada se trata de un palindromo. Palíndromo, es si se lee igual de derecha a izquierda que de izquierda a derecha.
Precondiciones: debe recibir una cadena o frase almacenada.
Poscondiciones: Devuelve true o false dependiendo si es o no un palindromo.
"""
def es_palindromo(palindromo):
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
    devolver = False
    while prueba > 0:
        if palindromo[palindromo_prueba] == palindromo[largo_de_palindromo]:
            palindromo_prueba = +1
            largo_de_palindromo = -1
            if largo_de_palindromo == -1:
                prueba = 0
                devolver = True
    return devolver

    pass

if __name__ == "__main__":
    es_palindromo(palindromo)