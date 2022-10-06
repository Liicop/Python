import math
import time

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

      
























