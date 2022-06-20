################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################
"""
1. Conversión de temperaturas
#Se quiere transformar temperaturas en grados fahrenheit a grados centígrados y
viceversa.
Escribir las funciones para convertir la temperatura en grados centigrados en
fahrenheit como un número decimal, utilice esta formula para calcular los grados
centígrados y retorne el resultado obtenido. Y viceversa.

"""
def convertir_a_fahrrenheit(centigrados):
    """
    Esta función convierte grados centigrados a grados fahrrenheit.
    Precondiciones:Se debe ingresar un numero que expresa una temperatura en grados
    centigrados.
    Poscondiciones:Se devolvera un número que representara una temperatura en grados
    fahrrenheit.
    """
    salida = centigrados * 1.8 + 32
    return salida
        
def convertir_a_centigrados(fahrrenheit):
    """
    Esta función convierte grados fahrrenhiet a grados centigrados.
    Precondiciones:Se debe ingresar un numero que expresa una temperatura en grados
    centigrados.
    Poscondiciones:Se devolvera un número que representara una temperatura en grados
    fahrrenheit.
    """
    salida = (fahrrenheit -32)/1.8
    return salida

def principal():
    """
    Esta función es la parte interactiva. Pide a que tipo de escala se quiere convertir
    los grados, pide el numero de los grafos a convertir, y desvuelve la conversión.
    """
    print ("Bienvenido al convertidor interactivo de tempetaras.")
    decision = int(input("Ingrese: 1. Para convertir centigrados a fahrrenheit. Ingrese 2. Para convertir grados fahrrenheit a centigrados: "))
    if decision == 1:
        centigrados = int(input("Ingrese el numero de grados centigrados a convertir: "))
        principio = centigrados
        salida = convertir_a_fahrrenheit(centigrados)
        desde = "centigrados"
        hasta = "fahrrenheit"
    else:
        fahrrenheit = int(input("Ingrese el numero de grados centigrados a convertir: "))
        principio = fahrrenheit
        salida = convertir_a_centigrados(fahrrenheit)
        desde = "fahrrenheit"
        hasta = "centigrados"
    print (f"La conversion de {principio} grados {desde} da como resultado:{salida} grados {hasta}.")
        
    
if __name__ == "__main__":
    principal()
    convertir_a_fahrrenheit(centigrados)
    convertir_a_centigrados(fahrrenheit)