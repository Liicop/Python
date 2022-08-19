import random

def busqueda_lineal(lista, objetivo):
    match = False
    for elemento in lista:  # O(n) --> complejidad lineal
        if elemento == objetivo:
            match = True
            break
    return match

if __name__ == '__main__':
    list_size = int(input('Defina el tamaño de la lista  '))
    objetivo = int(input('Ingrese el objetivo  '))

    lista = [random.randint(0, 100) for i in range(1, list_size)]
    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    if encontrado:
        print(lista.index(objetivo))
    print(f'El elemento {objetivo} {"está" if encontrado else "no está"} en la lista')


