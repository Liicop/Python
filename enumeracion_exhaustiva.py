import time

def enumeracion_exhaustiva(objetivo):
    """Este programa encuentra la raiz cuadrada de un numero
    recorriendo todos los posibles valores antes de hallarla,
    si no tiene, se imprimira eso mismo.

    Args:
        objetivo (integer): este es el numero al cual hallaremos su 
        raiz cuadrada, o no.
    """
    respuesta = 1
    tiempo_inicial = time.time()

    while respuesta**2 < objetivo:
        respuesta +=1

    if respuesta**2 == objetivo:
        print(f'{objetivo} tiene raiz exacta y es {respuesta}')
    else:
        print(f'{objetivo} no tiene raiz exacta')

    print(f'El programa tardó {round(time.time() - tiempo_inicial,3)} segundos ')

#raiz = int(input("Ingrese un numero para hallar su raiz cuadrada exacta (si tiene): "))
#enumeracion_exhaustiva(raiz)
help(enumeracion_exhaustiva)
