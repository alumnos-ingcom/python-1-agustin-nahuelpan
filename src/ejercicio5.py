################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Divisiones
Escribir una función que mediante restas sucesivas, obtenga el valor del cociente y resto de dos números enteros.

"""
#Precondiciones: las entradas deben ser numeros; el dividiendo debe ser mayor que el divisor.
#Poscondiciones: la salida seran dos numeros enteros; 

def division_lenta(dividiendo, divisor):
    cociente = 0 # El cociente queda establecido como 0 para que el bucle while no tenga problemas.
    resto = 0 #El resto queda establecido desde el inicio como 0 en el caso de que la división sea exacta.
    while dividiendo > divisor:
        dividiendo = dividiendo - (divisor) #Se realizan las restas sucesivamente mientras el bucle funcione.
        cociente = cociente + 1 #Por cada vez que el divisor resta al dividiendo, el cociente aumenta en 1.
        if dividiendo < divisor: #En el caso de que el resto no sea 0, esta condicional seala cuanto es.
            resto = dividiendo 
    return cociente, resto

    pass

if __name__ == "__main__":
    division_lenta(dividiendo, divisor)