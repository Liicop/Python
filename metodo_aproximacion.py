import time

objetivo = int(input("Ingrese un numero para hallar su raiz cuadrada aproximada: "))
start_time = time.time()
epsilon = 0.1
respuesta = 0

while abs(objetivo - respuesta**2) >= epsilon and respuesta <= objetivo:
    respuesta += epsilon**2

print(respuesta)
print(f'Tiempo estimado de respuesta: {round(time.time() - start_time,4)} segundos')