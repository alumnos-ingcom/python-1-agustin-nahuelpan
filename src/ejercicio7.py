################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
7. Transformación de un número
Escribir un programa que permita transformar un número solicitado expresado en grados, minutos y segundos a segundos a segundos. Y otra que haga el cambio en el sentido contrario, devolviendo una tuple.

Recuerden que un grado son 60 minutos y un minuto son 60 segundos."""

#sexadecimal_a_decimal
#precondiciones: se deben ingresar tres numeros que representen tres valores diferentes en grados, minutos y segundos.
#poscondiciones: Se regresara un valor en segundos con la suma de los tres valores ingresados. 

#decimal_a_sexadecimal
#Precondiciones: Se debe ingresar un numero.
#Poscondiciones: Se devolveran el numero convertido en horas, minutos y segundos.

def sexadecimal_a_decimal(horas, minutos, segundos):
    devolver = (horas * 60) * 60
    devolver = devolver + (minutos * 60)
    devolver = devolver + segundos
    return devolver

    pass
    
def decimal_a_sexadecimal(numero):
    grados=0
    minutos=0
    segundos=numero
    if numero < 60: #Por si el numero no supera el minuto, se deja un condicional listo para sealar que son segundos.
        devolver = (grados, minutos, segundos)
    elif numero > 60:#Si el numero supera el minuto, las operaciones para transformarlo se ponen en marcha.
        minutos = numero // 60
        segundos = numero % 60
        if minutos < 60:
            devolver = (grados, minutos, segundos)
        elif minutos > 60: #Por si supera 1 grado.
            grados = minutos // 60
            minutos = minutos % 60
            devolver = (grados, minutos, segundos)
    return devolver
    pass 

if __name__ == "__main__":
    sexadecimal_a_decimal(horas, minutos, segundos)  

if __name__ == "__main__":
    decimal_a_sexadecimal(numero)
