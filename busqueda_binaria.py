import time
import random

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
    print(f'Timepo estimado de busqueda {round(time.time() - start_time,5)} segundos')

#raiz = int(input("Ingrese un entero para hallar su raiz cuadrada: "))
#busqueda_binaria(raiz)
#help(busqueda_binaria)

busqueda_binaria(299666666699)

"""  


def busqueda_binaria(lista, comienzo, final, objetivo):
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        return False

    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo)


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
"""