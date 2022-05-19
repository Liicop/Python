#       | CODIFICADOR DE PALABRAS |
word = input("ingrese una palabra a codificar: ")
number = int(input("ingrese un número menor que 26 para codificar: "))
word = word.lower()     
abecedario = 'abcdefghijklmnopqrstuvwxyz'

encphrase = ''
for i in word:
    codi = abecedario.index(i) #funciona con .find() y con .index()
    if codi + number > 26:
        number2 = number - (26 - codi)
    else:
        number2 = codi + number    
    encphrase += abecedario[number2]

print(encphrase)

#este ejercicio codifica palabras, corriendo el número de letras del abecedario que el usuario indique