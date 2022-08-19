import os

def bienvenida():
    with open("Archivos/Bienvenido_a_hangman.txt") as f:
        for line in f:
            print(line)
        print('\n')

def adivina_la_palabra():
    with open("Archivos/adivina_la_palabra.txt") as f:
        for line in f:
            print(line)
        print('\n')

def play_hangman(palabra, adivina):
    igual = ''
    while(igual!=palabra):
        print(f'Adivina la palabra de {len(palabra)-1} letras')
        for i in range(len(palabra)-1):
            print(adivina[i], end=" ")
        print('\n')
        try:
            letter = input("Ingrese una letra: ")
            if len(letter) > 1:
                raise ValueError("Ingrese solo una letra")
            elif not letter.isalpha():
                raise ValueError("Ingrese solo letras")
            letter = letter.upper()
            if letter in palabra:
                for i in range(len(palabra)-1):
                    if palabra[i] == letter:
                        adivina[i] = letter

            igual = ''.join(adivina)
            igual += '\n'
            os.system("clear")
            adivina_la_palabra()
        except ValueError as error:
            os.system("clear")
            print(error)

        

def ahorcado(palabra):
    adivina = ['_' for i in palabra if i != '\n']
    play_hangman(palabra, adivina)
    

def run():
    bienvenida()
    
    with open("Archivos/data.txt") as f:
        for word in f:
            ahorcado(word.upper())
            print(word.upper())
            seguir = input("Desea continuar jugando y/n ")
            os.system("clear")
            if seguir=='n':
                break
            
    f.close()

if __name__ == '__main__':
    run()