"""
Escribir un programa que lea una frase, y pase ésta como parámetro a una función
que debe contar el número de palabras que contiene. El resultado se debe imprimir
en el programa principal. 
Asume que cada palabra está separada por un solo blanco.
No se sabe cómo están separadas las palabras. Pueden estar separadas por más de 
un blanco o por signos de puntuación.
"""

frase=input("Escribe una frase:\n")
def contarPalabras(frase):
    if " " in frase:
        palabras=frase.split()
    elif "," in frase and " ":
        palabras=frase.split(","," ")
    elif "." in frase and " " in frase:
        palabras=frase.split("."," ")
    elif "," in frase and "." in frase and " " in frase:
        palabras=frase.split(".",","," ") 
        print(palabras)
    print(f"La frase tiene {len(palabras)} palabras")

contarPalabras(frase)

#https://es.stackoverflow.com/questions/39726/python-conversi%C3%B3n-de-un-string-a-tipo-lista-sin-tener-los-caracteres-separados

    