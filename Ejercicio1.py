"""
Escribe un programa que te pida una frase, y pase la frase como parámetro a una 
función. Ésta debe devolver si es palíndroma o no, y el programa principal 
escribirá el resultado por pantalla:
"""
frase=input("Escribe una frase:\n")

def palindroma(frase):
    lista=[]
    lista2=[]
    for letra in frase:
        if letra != " ":
            lista.append(letra)
    print(lista)
    for i in range(len(frase)-1,-1,-1):
        if frase[i] != " ":
            lista2.append(frase[i])
    print(lista2)
    if lista==lista2:
        resultado=print("La frase es palíndroma")
    else:
        resultado=print("La frase NO ES palíndroma")
    return resultado

palindroma(frase)
