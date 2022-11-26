"""
Escribe un programa que te pida una frase, y pase la frase como parámetro a una 
función. Ésta debe devolver si es palíndroma o no, y el programa principal 
escribirá el resultado por pantalla:
"""
frase=input("Escribe una frase:\n")

def palindromo(frase):
    # Eliminamos los espacios en blanco porque sino nos daría error 
    frase = frase.replace(" ", "")
    # Si frase es igual a frase con el orden inverso, es palindromo
    if frase == frase[::-1]:
        print("Es palindromo")
    else: 
        print("No es palindromo")
palindromo(frase)

"""Version: Jouat"""