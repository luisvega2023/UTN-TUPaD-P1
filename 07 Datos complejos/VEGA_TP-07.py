#Actividad 1 : Diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Anana': 2500, 'Melón': 3000, 'Uva': 1450}
#Se almacenan nuevos datos en el diccionario.
precios_frutas['Naranja']=1200
precios_frutas['Manzana']=1500
precios_frutas['Pera']=2300
print(precios_frutas)

#Actividad 2 : Actualizacion de datos.
precios_frutas['Banana']=1330
precios_frutas['Manzana']=1700
precios_frutas['Melón']=2800
print(precios_frutas)

#Actividad 3 : Nueva lista con las keys del diccionario precios_frutas
precios_frutas= precios_frutas.keys()
print(precios_frutas)

#Actividad 4 : 
#se crea un diccionario vacio
dict={}
#se crea un bucle for que pida 5 nombres y numeros de asociado.
for i in range(5):
    nombre=input("Ingrese el nombre del contacto: ")
    numero=input("Ingrese el numero del contacto: ")
    dict[nombre]=numero
#se consulta al usuario, el contacto que busca.
consulta=input("Ingrese el nombre que busca: ")
#se verifica si el contacto ingresado esta agendado.
if consulta in dict:
    #se imprime el numero de asociado del contacto.
    print(f"El numero de {consulta} es: {dict[consulta]}")
else:
    print("El nombre ingresado no se encuentra agendado.")

#Actividad 5 : 
#Funcion que cuenta las palabras dentro de una frase
def contar_palabras(frase):
    frase_separada=frase.split() #Funcion encargada de separar las palabras en una lista.
    dict={}#Diccionario vacio.
    while len(frase_separada) > 0: #Bucle while que funcione mientras la lista tengas items.
        text=frase_separada[0] #variable que guarde el primer item de la lista.
        if text in dict: #condicional doble que verifica si el primer item de la lista esta en el diccionario le suma 1.
            dict[text]+=1
        else:# Si no, agrega el item.
            dict[text]=1
        frase_separada.remove(text)#borra el primer item.
    print(dict)

frase=input("Ingrese una frase: ")
contar_palabras(frase)

#Actividad 6 :
dict={}
for i in range(3):
    nombre=input("Ingrese el nombre del alumno: ")
    nota1=input("Ingrese la primera nota: ")
    nota2=input("Ingrese la segunda nota: ")
    nota3=input("Ingrese la tercer nota: ")
    tuple=(nota1,nota2,nota3)
    dict[nombre]=tuple
    print(dict)

#Actividad 7 :
