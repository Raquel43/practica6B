"""
Escribe un programa que le pida al usuario si quiere calcular si un número 
es primo deberéis utilizar for o con while, por tanto, habrá dos funciones 
que se caracterizan por hacer ese mismo cálculo de una manera (con for y sin breaks), 
o de otra (con while). Ambas funciones devolverán true (si es primo) o false 
(si no es primo). El programa principal informará del resultado. Además,
como mejora puedes calcular el tiempo que tarda en encontrar la solución 
de una manera u otra. Comentario: aprovecha el código que tienes ya creado.
"""
import time
def encontrarPrimo(num):
    momento = time.time()
    lista = []
    #Inicializamos la variable a uno, ya que no se puede dividir por cero
    inicio = 1
    # mientras el valor de inicio incrementado en uno en cada iteración
    # sea menor que el numero introducido menos 1
    # (Para que me coja el número anterior)
    while inicio < num-1:
        inicio+=1
        #Creamos una variable que almacenará el modulo de num/inicio
        busqueda = num%inicio
        #Introducimos el resultado en la lista
        lista.append(busqueda)
    #Si se encuentra un 0 en la lista querrá decir que es divisible
    #por lo que no será primo, en caso contrario será primo
    if 0 in lista: 
        print("El número",num,"NO es primo")
        fin = time.time()
        print(f"El programa con while ha tardado {fin-momento}")
        return print(False)
    else:
        print("El número",num,"es primo")
        fin = time.time()
        print(f"El programa con while ha tardado {fin-momento}")
        return print(True)


#Función que determina que número es primo
def numerosPrimos(num):
    momento = time.time()
    resultados=[]
    #Bucle en el que se crean números desde el 2 hasta el número introducido
    #Ya que ningún número es divisible por 0 y todos son divisibles por 1,
    #el siguiente es el 2. Al no poder hacer un rango con el y como es primo,
    #ya lo definimos como tal.
    if num==2:
        print("El número",num,"es primo")
       
    else:
        for i in range(2,num):
            #busqueda es el resultado del modulo entre el numero y todos los anteriores
            busqueda=num%i
                #Introducimos los números resultantes(busqueda) en resultados
            resultados.append(busqueda)
                #Ordenamos la lista para saber si esta el número 0 en ella
            resultados.sort()
            #print(resultados)
            #Si el resultado es 0, o sea el módulo, querra decir que es divisible y
            #no será primo
        if resultados[0]==0:
                print("El número",num,"NO es primo")
                fin = time.time()
                print(f"El programa con for ha tardado {fin-momento}")
                return print(False)
                
        else:
            print("El número",num,"es primo")
            fin = time.time()
            print(f"El programa con for ha tardado {fin-momento}")
            return print(True)
            

#Pedimos al usuario que introduzca un número
num=int(input("Introduzca un número\n"))
encontrarPrimo(num)
numerosPrimos(num)

