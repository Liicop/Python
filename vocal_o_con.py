#       | VOCAL O CONSONANTE |
word = input("ingrese una letra y le diremos si es consonante o vocal: ")

x = word.isalpha()
while len(word) > 1 or x == False :
    print("su ingreso es invalido")
    print("ingrese una letra")
    word = input("letra: ")
    x = word.isalpha()

vocales = 'aeiou'
word1 = word.lower()
print(word ," es una vocal") if word1 in vocales else print(word, "es una consonante")

# este programa al ingresar una letra nos dice si es vocal o consonante.