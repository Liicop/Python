import random

def bubble_sort(lista):
    n = len(lista)

    for i in range(n): # O(n)
        for j in range(n-i-1): # O(n)   complejidad total --> O(n) * O(n) = O(n²)
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    
    return lista

if __name__ == '__main__':
    list_size = int(input('Ingrese el tamaño de la lista --> '))

    lista = [random.randint(0, 100) for i in range(list_size)]
    print(lista)

    lista_ordenanda = bubble_sort(lista)
    print(lista_ordenanda)

