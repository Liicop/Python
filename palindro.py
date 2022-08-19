#       | DETERMINAR PALABRAS PALINDROMOS |
phrase = input("ingrese una palabra y le diremos si es palindromo o no: ")
revphrase = ''
for i in range(-len(phrase)+1,1):
    revphrase += phrase[i*-1]

if phrase == revphrase:
    print(phrase, "es palindromo")
else: print(phrase, "no es palindromo")  
print(revphrase)  

#este ejercicio nos permite saber si una palabra es palindromo o no, es decir que se escribe igual 
#de izquierda a derecha que de derecha a izquierda.



