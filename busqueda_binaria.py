import time

objetivo = int(input("Ingrese un entero para hallar su raiz cuadrada: "))
epsilon = 0.001
bajo = 0
alto = max(1.0,objetivo)
resultado = (alto + bajo) / 2

start_time = time.time()

while abs(resultado**2 - objetivo) >= epsilon:
    #print(f'bajo={bajo}  alto={alto}  resultado={resultado}')
    if resultado**2 < objetivo:
        bajo = resultado
    else: 
        alto = resultado
    
    resultado = (alto + bajo) / 2

print(f'La raiz cuadrada de {objetivo} es aproximadamente {resultado}')
print(f'Timepo estimado de busqueda {round(time.time() - start_time,4)} segundos')
