import random

def insertion_sort(lista):

    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        posicion_actual = indice

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual
    
       
    return lista

if __name__ == '__main__':

    list_size = int(input('Ingrese el tamaño de la lista --> '))
    lista = [random.randint(0, 100) for i in range(list_size)]
    print(lista)

    print(insertion_sort(lista))