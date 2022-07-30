import time

def busqueda_aproximacion(objetivo):
    """Esta función permite encontrar una raiz cuadrada 
    aproximada de un numero entero, sin importar si tiene 
    una exacta o no, todas seran aproximaciones. Con un epsilon
    que va a ser el indice de error de la aproximacion; entre mas chico
    sea, mas aproximado sera, aunque con poca eficacia debido a su
    estructura.

    Args:
        objetivo (integer): es la variable a la cual vamos a 
        hallarle su raiz cuadrada aproximada, con diez decimales.
    """
    start_time = time.time()
    epsilon = 0.1
    respuesta = 0

    while abs(objetivo - respuesta**2) >= epsilon and respuesta <= objetivo:
        respuesta += epsilon**2

    print(respuesta)
    print(f'Tiempo estimado de respuesta: {round(time.time() - start_time,4)} segundos')


#raiz = int(input("Ingrese un numero para hallar su raiz cuadrada aproximada: "))
#busqueda_aproximacion(raiz)
help(busqueda_aproximacion)