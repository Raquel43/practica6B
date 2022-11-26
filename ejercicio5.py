"""
Desarrolla un programa, que nos sirva para gestionar nuestros contactos 
(la información a gestionar será el teléfono, nombre, apellido1, apellido2 y 
correo electrónico. El programa tendrá un menú, con las siguientes opciones: 
añadir contacto, consultar contacto a partir de la clave, consultar todos los 
contactos y eliminar contacto. Aprovecha lo que has aprendido hasta el momento 
(diccionarios, funciones, procedimientos…).
"""
#Importamos la libreria time para emplearla para hacer paradas al mostrar los resultados
import time
#Definimos un array donde meteremos diccionarios
lista=[]
#Procedimiento con atributos que nos crea un registro en la agenda
def agenda(id,telefono,nombre,apellido1,apellido2,email):
    registro={"id":id,"telefono":telefono,"nombre":nombre,"apellido1":apellido1,"apellido2":apellido2,"email":email}
    lista.append(registro)
    print(f"Elemento de la agenda creado con id: {id}")
#Procedimiento que nos muestra todos los registros de la agenda
def imprimir():
    if len(lista)==0:
            print("No existe ningún contacto, cree uno")
    else:
            print("Esta es la lista de contactos:")
            for i in lista:
                    for key, value in i.items():
                        print(key, ':', value)

#Función que nos muestra un registro por su id
def imprimirId(id):
    if len(lista)==0:
            print("No existe ningún contacto, cree uno")
    else:
        print(f"El contacto correspondiente al {id} es:")
        for i in lista:
            if i["id"]==id:
                for key, value in i.items():
                        print(key, ':', value)
                return True
            # elif id not in i:
            #     print(f"El contacto con id {id} no existe")
            #     time.sleep(2)
            #     print(" ")
            #     False
                
            
            
#Procedimiento que borra un contacto por su id
def borrar(id):
    for i in lista:
        if i["id"]==id:
        # for item in i.items():
        #     if item[1] == id:
            lista.remove(i)

#Función que comprueba si la clave introducida para editar existe
def key(clave):
    for i in lista:
        for elemento in i.items():
            if clave=="telefono" or clave=="nombre" or clave=="apellido1" or clave=="apellido2" or clave=="email":
                return True
            else:
                print(f"El elemento {clave} no existe!")
                time.sleep(1)
                return False

# def actualiza(id,clave,palabra):
#     for i in lista:
#         if i["id"]==id:
#             for elemento in i.items():
#                 if clave in elemento[0]:
#                     print(elemento[0])
#                     i[clave]=palabra
#                     print(f"Elemento {clave}actualizado a {palabra}")
#                 else:
#                     print(elemento[0])
#                     print(f"El elemento {clave} es incorrecto")

#Procedimiento que actualiza un contacto según la clave introducida
def actualiza(id,clave,palabra):
    for i in lista:
        if i["id"]==id:
            i[clave]=palabra
            print(f"Elemento {clave} actualizado a {palabra}")
            time.sleep(1)

#Función que comprueba si un contacto existe por su id
def existe(id):
    for i in lista:
            if i["id"]==id:
                existencia=True
            elif id not in i:
                existencia=False
            return existencia
#Procedimiento que para pedir al usuario si quiere borrar el contacto o no
def seguro(id):
    seguridad= input("Realmente quiere borrar el contacto de la agenda? Y or N: ")
    if seguridad == "N" or seguridad == "n":
            print("NO se ha borrado ningún contacto")
            time.sleep(3)
            print(" ")
    elif seguridad == "Y" or seguridad == "y":
            borrar(id)
            print(f"Contacto {id} borrado correctamente!!!")

#Definimos las variables globales
id=0
seleccion="" 
seguridad=""
continuar=True
#Bucle para definir el menú y sus acciones
while seleccion!="0":
    print("******************* MENU *******************")
    print("1.- Crear contacto en la agenda")
    print("2.- Mostrar todos los contactos")
    print("3.- Mostrar contacto segun su identificador")
    print("4.- Eliminar contacto")
    print("5.- Editar contacto")
    print("0.- Salir")
    print("********************************************")
    seleccion=input("Selecciona un número del menú: ")

    #Estructura de control que permite crear un contacto
    if seleccion == "1":
        id+=1
        telefono=input("Introduzca un telefono: ")
        nombre=input("Introduzca un nombre: ")
        apellido1=input("Introduzca el primer apellido: ")
        apellido2=input("Introduzca el segundo apellido: ")
        email=input("Introduzca el correo electronico: ")
        agenda(id,telefono,nombre,apellido1,apellido2,email)
        time.sleep(2)
        print(" ")
    #LLama a la función de mostrar todos los contactos
    elif seleccion == "2":
        imprimir()
        time.sleep(3)
        print(" ")

    #LLama a la función de mostrar un elemento por su id
    elif seleccion == "3" and continuar==True:
        identificador=int(input("Introduzca una id: "))
        if existe(identificador)==False:
            print(f"El identificador {identificador} no existe")
            time.sleep(2)
            print(" ")
        else:
            imprimirId(identificador)
            time.sleep(3)
            print(" ")
    #Llama a la función de borrar un contacto
    elif seleccion == "4" and continuar==True:
        identificador= int(input("Introduzca el id que quiere borrar: "))
        imprimirId(identificador)
        continuar=existe(identificador) 
        
        time.sleep(2)
        if len(lista)==0:
            continuar=False
        else:
            seguro(id)
            time.sleep(2)
            print(" ")
    
    #LLama a la función de editar un contacto según su clave
    elif seleccion=="5":
        identificador=int(input("Introduzca una id: "))
        comprobacion=imprimirId(identificador)
        if comprobacion==True:
            print("Que quieres actualizar?")
            clave=input("(telefono, nombre, apellido1, apellido2, email):\n")
            if key(clave)==True:
                palabra=input("Por que dato lo quieres cambiar? ")
                actualiza(identificador,clave,palabra)
        else:
            print(f"El elemento con id {identificador} no existe")
            time.sleep(2)
            print(" ")
                
"""Autor: Raquel Arques Toro"""       


#https://thispointer.com/python-4-ways-to-print-items-of-a-dictionary-line-by-line/
