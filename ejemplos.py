"""
import math

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

Alfabeto = {
    ['A','E','I','L','N','O','R','S','T','U'] : 1,
    ['D','G'] : 2,
    ['B','C','M','P'] : 3,
    ['F','H','V','W','Y'] : 4,
    ['K'] : 5,
    ['J','X'] : 6,
    ['Q','Z'] : 7
}

"""Alfabeto = {
    'AEILNORSTU' : 1,
    'DG' : 2,
    'BCMP' : 3,
    'FHVWY': 4,
    'K' : 5,
    'JX' : 6,
    'QZ' : 7
}
"""

palabra = input('Ingrese una palabra --> ')
palabra = palabra.upper()  #convertir la palabra a mayúscula para evitar errores
puntaje = 0

for i in palabra:           #recorrer las letras de la plabra
    for j in Alfabeto:      #recorre cada llave del diccionario
        if i in j:          #condicional que verifica si la letra está en la llave del diccionario
            puntaje += Alfabeto[j]      #acumula el puntaje de cada letra

print(f'El puntaje es {puntaje}')


















