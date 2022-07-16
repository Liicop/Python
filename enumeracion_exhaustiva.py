import time

objetivo = int(input("Ingrese un numero para hallar su raiz cuadrada: "))
respuesta = 1
tiempo_inicial = time.time()

while respuesta**2 < objetivo:
    respuesta +=1

if respuesta**2 == objetivo:
    print(f'{objetivo} tiene raiz exacta y es {respuesta}')
else:
    print(f'{objetivo} no tiene raiz exacta')

print(f'El programa demoró {round(time.time() - tiempo_inicial,3)} segundos ')