import time

def busqueda_binaria(objetivo):
    """Es un algoritmo eficiente para encontrar un elemento
    en una lista ordenada de elementos. Funciona al dividir 
    repetidamente a la mitad la porción de la lista que podria 
    contener al elemento, hasta reducir las ubicaciones posibles 
    a solo una. En este caso, se usa para la hallar la raiz cuadrada 
    aproximada de un entero, de manera eficaz, en terminos de rendimiento.

    Args:
        objetivo (integer): varaible a la cual le hallamos la raiz
        cuadrada aproximada.
    """
    epsilon = 0.0001
    bajo = 0
    alto = max(1.0,objetivo)
    resultado = (alto + bajo) / 2

    start_time = time.time()

    while abs(resultado**2 - objetivo) > epsilon:
        #print(f'bajo={bajo}  alto={alto}  resultado={resultado}')
        if resultado**2 < objetivo:
            bajo = resultado
        else: 
            alto = resultado
        
        resultado = (alto + bajo) / 2
    if(int(resultado) < resultado):
        if((resultado + epsilon) > (int(resultado) + 1)):
            resultado = int(resultado) + 1
    else:
        if((resultado - epsilon) < int(resultado)):
            resultado = int(resultado)


    print(f'La raiz cuadrada de {objetivo} es aproximadamente {resultado}')
    print(f'Timepo estimado de busqueda {round(time.time() - start_time,4)} segundos')

#raiz = int(input("Ingrese un entero para hallar su raiz cuadrada: "))
#busqueda_binaria(raiz)
help(busqueda_binaria)