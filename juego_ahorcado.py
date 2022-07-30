import os

def solo_letras():
    pass


def play_hangman(palabra, adivina):
    igual = ''
    while(igual!=palabra):
        print(f'Adivina la palabra de {len(palabra)-1} letras')
        for i in range(len(palabra)-1):
            print(adivina[i], end=" ")
        print('\n')
        
        letter = input("Ingrese una letra: ")
        letter = letter.upper()
        if letter in palabra:
            for i in range(len(palabra)-1):
                if palabra[i] == letter:
                    adivina[i] = letter

        igual = ''.join(adivina)
        igual += '\n'
        os.system("clear")

def ahorcado(palabra):
    adivina = ['_' for i in palabra if i != '\n']
    play_hangman(palabra, adivina)
    

def run():
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