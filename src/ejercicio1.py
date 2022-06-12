################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
1. Conversión de temperaturas
#Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y viceversa.
#Escribir las funciones para convertir la temperatura en grados centigrados en fahrenheit como un número decimal, utilice esta formula para calcular los grados centígrados y retorne el resultado obtenido. Y viceversa.

Precondiciones:Se debe ingresar un numero que expresa una temperatura en grados centigrados.
Poscondiciones:Se devolvera un número que representara una temperatura en grados fahrrenheit.
"""
def convertir_a_fahrrenheit(centigrados):
    salida = centigrados * 1.8 + 32
    """Esta función convierte grados centigrados a grados fahrrenheit."""
    return salida
    
    pass
    
def convertir_a_centigrados(fahrrenheit):
    salida = (fahrrenheit -32)/1.8
    """Esta función convierte grados fahrrenhiet a grados centigrados."""
    return salida

    pass

if __name__ == "__main__":
    convertir_a_fahrrenheit(centigrados)
    convertir_a_centigrados(fahrrenheit)