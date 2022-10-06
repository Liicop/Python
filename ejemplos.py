from datetime import datetime
import math
import time
import random
import os
from tablero import tablero, board 


"""


rango = [0,0]
rango[0] = int(input('Ingrese el limite inferior --> '))
rango[1] = int(input('Ingrese el limite superior --> '))



with open("datos.txt", "a", encoding="utf-8") as f:
    f.write(str(rango))                 #definicion de las columnas --> rango
    f.write('       ' + 'seno')         #definicion de las columnas --> seno
    f.write('       ' + 'coseno')       #definicion de las columnas --> coseno
    f.write('\n')                       #salto de linea
    for i in range(rango[0],rango[1]+1):
        seno = round(math.sin(i),3)    #hallar seno de cada número del rango, redondeado
        coseno = round(math.cos(i),3)  #hallar coseno de cada número del rango, redondeado
        f.write(str(i))                #Número al que se le halla el seno y coseno
        f.write('           ' + str(seno)) #Resultado del seno con el número i del rango  
        f.write('       ' + str(coseno))   #Resultado del coseno con el número i del rango 
        f.write('\n')                  #salto de linea
    f.close()                          #se cierra el archivo

"""
"""
Alfabeto = {
    ['A','E','I','L','N','O','R','S','T','U'] : 1,
    ['D','G'] : 2,
    ['B','C','M','P'] : 3,
    ['F','H','V','W','Y'] : 4,
    ['K'] : 5,
    ['J','X'] : 6,
    ['Q','Z'] : 7
}

Alfabeto = {
    'AEILNORSTU' : 1,
    'DG' : 2,
    'BCMP' : 3,
    'FHVWY': 4,
    'K' : 5,
    'JX' : 6,
    'QZ' : 7
}
"""

'''palabra = input('Ingrese una palabra --> ')
palabra = palabra.upper()  #convertir la palabra a mayúscula para evitar errores
puntaje = 0

for i in palabra:           #recorrer las letras de la plabra
    for j in Alfabeto:      #recorre cada llave del diccionario
        if i in j:          #condicional que verifica si la letra está en la llave del diccionario
            puntaje += Alfabeto[j]      #acumula el puntaje de cada letra

print(f'El puntaje es {puntaje}')'''






#polinomio x**3 + 2x**2 -4x + 3, 3.42

'''
def enu_exhaustiva(lim_infe, lim_supe):
        start = time.time()
        repeticiones = 0
        epsilon = 0.01
        delta = 0.0001
        base = lim_infe

        while base>=lim_infe and base<=lim_supe:
            raiz = base**3 + 2*base**2 - 4*base + 3
            repeticiones += 1
            base += delta
            if abs(raiz) <= epsilon:
                break
    
        result = [base, repeticiones,start]
        return result

# 5 - 12 = 7/2 = 3.5   8.5    
def biseccion(lim_infe,lim_supe):
    start = time.time()
    a = lim_infe        # no cambian para que el intervalo original permanezca inalterable en el while
    b = lim_supe        # no cambian para que el intervalo original permanezca inalterable en el while

    epsilon = 0.01  # mide la presición del algoritmo, entre más pequeño sea más preciso el resultado
    repeticiones = 0
    medio = lim_infe
    while medio >= a and medio <= b:

        repeticiones += 1
        medio = (max(lim_supe,lim_infe) - min(lim_infe,lim_supe)) / 2 + min(lim_infe,lim_supe)  
        # medio: valor que varia los intervalos de busqueda de la raíz 
        # a medio se le suma el limite inferior para establecer el valor medio entre los limites

        result = medio**3 + 2*medio**2 - 4*medio + 3  # resultado de la operacion polinomio

        if abs(result) <= epsilon:   # prueba si se encontró la raíz
            break

        
        elif result > epsilon:     # como en el limite superior no está la raíz se reduce el rango de busqueda
            lim_supe = medio        

            

        elif result < epsilon:  # como en el limite inferior no está la raíz se reduce el rango de busqueda
            lim_infe = medio

    
    raiz = [medio, repeticiones,start]
    return raiz

lim_infe = -4
lim_supe = -3

print('Enumeración exhaustiva')
print('Repeticiones: ', enu_exhaustiva(lim_infe, lim_supe)[1])
print('Raíz = ', enu_exhaustiva(lim_infe, lim_supe)[0])
print(f'Time: {round(-time.time()+enu_exhaustiva(lim_infe, lim_supe)[2],4)}')
print('-'*100)
print('Busqueda binaria')
print('Repeticiones: ', biseccion(lim_infe, lim_supe)[1])
print('Raíz = ', biseccion(lim_infe, lim_supe)[0])
print(f'Time: {round(-time.time()+biseccion(lim_infe, lim_supe)[2],4)}')

      '''

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('Duración del juego:', round(time_elapsed.total_seconds(),2), 'segundos', '\n')
    return wrapper

def imprimir(board):  #imprimir tablero
    for i in range(1,10):
        print(board[i-1],' | ', end='')
        if i%3 == 0:
            print('')

def aleatorio(board):  # ubicación random
    while True:
        ran = random.randint(0, 8)  # .randint()
        if board[ran] == ' ':  # si encuentra un espacio vacio pone una o
            board[ran] = 'o'
            break


def filas(board):  # impedir que gane en las filas

    if board[:3].count('x') == 2 and board[:3].count(' ') == 1: 
        # .count cuenta las x y si hay dos en esa fila pone una o para evitar que gane
        a = board[:3].index(' ') # .index encuentra el espacio vacio y ahí pone la o
        board[a] = 'o'
    elif board[3:6].count('x') == 2 and board[3:6].count(' ') == 1:
        a = board[3:6].index(' ')
        a+=3
        board[a] = 'o'
    elif board[6:].count('x') == 2 and board[6:].count(' ') == 1:
        a = board[6:].index(' ')
        a+=6
        board[a] = 'o'
    else:
        return False
    return True

def columnas(board):
    columns = [            # lista que contiene las columnas del juego
    [board[0],board[3],board[6]], 
    [board[1],board[4],board[7]], 
    [board[2],board[5],board[8]]
    ]

    if (columns[0].count('x') == 2 or columns[0].count('o') == 2) and columns[0].count(' ') == 1:
        # .count cuenta las x y si hay dos en esa columnas pone una o para evitar que gane
        a = columns[0].index(' ') * 3   # .index encuentra el espacio vacio y ahí pone la o
        board[a] = 'o'
    elif (columns[1].count('x') == 2 or columns[1].count('o') == 2) and columns[1].count(' ') == 1:
        a = columns[1].index(' ') * 3 + 1
        board[a] = 'o'
    elif (columns[2].count('x') == 2 or columns[2].count('o') == 2) and columns[2].count(' ') == 1:
        a = columns[2].index(' ') * 3 + 2
        board[a] = 'o'
    else:
        return False
    return True

def diagonal(board):
    diagonales = [   # lista con  las diagonales
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]]
    ]

    if (diagonales[0].count('x') == 2 or diagonales[0].count('o') == 2) and diagonales[0].count(' ') == 1:
         # .count cuenta las x y si hay dos en esa diagonales pone una o para evitar que gane
        a = diagonales[0].index(' ') * 4  # .index encuentra el espacio vacio y ahí pone la o
        board[a] = 'o'
    elif (diagonales[1].count('x') == 2 or diagonales[1].count('o') == 2) and diagonales[1].count(' ') == 1:
        a = diagonales[1].index(' ') * 2 + 2
        board[a] = 'o'
    else:
        return False
    return True




def ganador(board):
    
    tablero = [   # lista con las filas, columnas y diagonales
        [board[0],board[1],board[2]],
        [board[3],board[4],board[5]],
        [board[6],board[7],board[8]],
        [board[0],board[3],board[6]], 
        [board[1],board[4],board[7]], 
        [board[2],board[5],board[8]],
        [board[0],board[4],board[8]],
        [board[2],board[4],board[6]]
    ]
    
    for i in range(8):
        if tablero[i].count('x') == 3:  
            # verifica si hay tres x  en la misma significa que alguien ganó
            print('\nGanaste')
            return True
        elif tablero[i].count('o') == 3:
             # verifica si hay tres o en la misma significa que alguien ganó
            print('\nSigue intentándolo')
            return True
    return False

location = {   #corregir ubicación del tablero
    0:7,
    1:8,
    2:9,
    3:4,
    4:5,
    5:6,
    6:1,
    7:2,
    8:3
}


#inicio juego
@execution_time
def main(board):  # función que contiene el juego

    while True:

        imprimir(board) 
        
        if ganador(board):
            break

        while True:  #ciclo para pedir al usuario su movimiento
            user = int(input('Ingrese la casilla de su jugada: ')) # variable para número de la casilla
            user -= 1
            user = location[user]
            if board[user-1] != ' ': #verificar que esté libre
                print('\nCasilla ocupada')     
            else:
                board[user-1] = 'x' #asigna
                break

        if ganador(board):
            break
        
        if filas(board):
            continue
        elif columnas(board):
            continue
        elif diagonal(board):
            continue
        elif board.count(' ') == 0:
            print('\nEl juego ha terminado en empate\n')
            break    
        else:
            aleatorio(board)

    imprimir(board)
    print('\nJuego finalizado')

while True:
    continuar = input('Desea jugar Tic Tac Toe y/n --> ')
    os.system('clear')
    if continuar == 'y':
        board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']  #tablero
        main(board)
    elif continuar == 'n':
        print('Juego terminado')
        break
