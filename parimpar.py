#       | PAR I IMPAR |
incognita = int(input("ingrese un número entre 1 y 1000 y le diremos si es par ó impar: "))
if incognita <= 1000 and incognita >= 1:
    print(incognita, "es un número par") if incognita % 2 == 0 else print(incognita, "es un número impar")     
else:
    print("Ingrese un número dentro del rango pedido")

#este es un ejercicio para descubrir si un número es par o impar, el principal autor de este codigo 
#es el modulo, representado por %, lo que hace es arrojar el residuo de la división, en este caso
#entre 2; así sabemos si el número es divisible entre 2 (par) o no (impar).

# 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