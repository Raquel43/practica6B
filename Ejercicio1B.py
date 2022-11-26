"""
Escribe un programa que te pida una frase, y pase la frase como parámetro a una 
función. Ésta debe devolver si es palíndroma o no, y el programa principal 
escribirá el resultado por pantalla:
"""

def palindroma(palabra):
    girada =""
    palabratmp=""
    #quitamos los blancos
    for i in range(0, len(palabra)):
        if palabra[i]== " ":
            palabratmp=palabratmp + ""
        else:
            palabratmp=palabratmp+palabra[i]
            #print(palabratmp, "palabratmp")
    #le damos la vuelta a la palabra
    for i in range(0,len(palabratmp)):
        girada = palabratmp[i]+ girada
        #print(girada, "girada")
    if palabratmp == girada:
        return print ("%s es capicua o palindroma" %(palabra))
    else:
        return print ("%s NO es capicua o palindroma" %(palabra))

frase=input("Escribe una frase:\n")
palindroma(frase)

"""Version: Máximo"""
