#       |CONTADOR DE PALABRAS |

num_words = input("ingrese una frase: ")

num_words.strip()
sol = num_words.count(' ') + 1
print("el número de palabras en su frase es", sol)

#para este ejercicio de contar las palabras de una frase, usamos el metodo para .count() para los str
#que se encarga de contar el número de veces que se repite el argumento que ingresemos; en este caso
#contamos el número de espacios en blanco más uno, y así sabremos cuantas palabras contiene la frase.