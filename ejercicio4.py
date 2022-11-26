"""
Aprovechando el potencial de los diccionarios, escribe un programa que llame a 
un procedimiento, que recibe como parámetro la fecha en números y devuelve la 
fecha  con el nombre del mes. Comentario: no es necesario validar si la es 
correcta, damos por hecho que lo será. 
"""
#Definimos la función con el parametro fecha
def queMes(fecha):
    #Creamos un diccionario que corresponde cada mes con su número
    meses={"01":"Enero","02":"Febrero","03":"Marzo","04":"Abril","05":"Mayo","06":"Junio","07":"Julio","08":"Agosto","09":"Septiembre","10":"Octubre","11":"Noviembre","12":"Diciembre"}
    #Creamos una Lista de la fecha con el separador /
    fechaLista=fecha.split("/")
    #Sustituimos el segundo valor de la lista(el número del mes) por el elemento del diccionario
    fechaLista[1]=meses[fechaLista[1]]
    #Creamos una variable que guardará la Lista en string y reemplazara las comas por "de"
    fechaNueva=str(fechaLista).replace(',',' de')
    #Creamos otra variable que reemplazara las comillas por nada y eliminará el primer y último elemento
    fechaNueva2=fechaNueva.replace("'","")[1:-1]
    return print(fechaNueva2)
#Pedimos al usuario la fecha
fecha=input("Introduce una fecha en formato dd/mm/aaaa:\n")
#Si la fecha es incorrecta le pediremos que la introduzca de nuevo
if fecha[1]=="/" or fecha[4]=="/":
    fecha=input("Error, Vuelva a introducir la fecha en formato dd/mm/aaaa:\n")
#LLamamos a la función
queMes(fecha)

