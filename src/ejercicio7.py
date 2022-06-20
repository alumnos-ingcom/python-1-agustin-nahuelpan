################
# Nombre - @agustin-nahuelpan
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
7. Transformación de un número
Escribir un programa que permita transformar un número solicitado expresado en grados, minutos
y segundos a segundos a segundos. Y otra que haga el cambio en el sentido contrario, devolviendo
una tupla.
Recuerden que un grado son 60 minutos y un minuto son 60 segundos.
"""

def principal():
    """
    Esta función pide los datos necesarios para: pasar segundos a horas, minutos y segundos,
    o para pasar horas, minutos y segundos a segundos.
    Precondiciones: se deben ingresar tres numeros que representen tres valores diferentes en
    grados, minutos y segundos.
    Poscondiciones: Se regresara un valor en segundos con la suma de los tres valores ingresados. 
    """
    print ("Eliga que desea convertir:")
    decision = int(input("1. Para convertir: horas, minutos y segundos a segundos. 2. Para convertir segundos a: horas, minutos y segundos: "))
    if decision == 1:
        horas = int(input("Ingrese el primer numero: la/s hora/s: "))
        minutos = int(input("Ingrese el segundo numero: lo/s minuto/s: "))
        segundos = int(input("Ingrese el tercer numero: lo/s segundo/S: "))
        devolver = sexadecimal_a_decimal(horas, minutos, segundos)
        print (f"La conversion de {horas}, {minutos}, {segundos} es: {devolver} ")
    elif decision == 2:
        numero = int(input("Ingrese un numero en segundos para convertirlo: "))
        devolver = decimal_a_sexadecimal(numero)
        print (f"La conversion de {numero} convertido a horas, minutos y segundos es:{devolver}.")
    

def sexadecimal_a_decimal(horas, minutos, segundos):
    """
    Esta función pasa tres numetos ingresados en: horas, minutos y segundos, a segundos.
    Precondiciones: se deben ingresar tres numeros que representen tres valores diferentes en grados, minutos y segundos.
    Poscondiciones: Se regresara un valor en segundos con la suma de los tres valores ingresados. 
    """
    devolver = (horas * 60) * 60
    devolver = devolver + (minutos * 60)
    devolver = devolver + segundos
    return devolver
    
def decimal_a_sexadecimal(numero):
    """
    Esta función cambia un numero ingresado en segundos a: horas, minutos y segundos.
    Precondiciones: Se debe ingresar un numero.
    Poscondiciones: Se devolveran el numero convertido en horas, minutos y segundos.
    """
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

if __name__ == "__main__":
    principal()
    sexadecimal_a_decimal(horas, minutos, segundos)  
    decimal_a_sexadecimal(numero)
