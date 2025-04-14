from statistics import mode, median, mean
import random
#Actividad n°1
edad=int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad.")
#Actividad n°2
nota=int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")
#Actividad n°3
num=int(input("Ingrese un numero par: "))
if num % 2 == 0:
    print("Ha ingresado un numero par.")
else:
    print("Por favor, ingrese un numero par.")
#Actividad n°4
edad=int(input("Ingrese su edad: "))
if edad < 12:
    print("Usted pertenece a la categoria: Niño/a")
elif edad >=12 and edad < 18:
    print("Usted pertenece a la categoria: Adolecente")
elif edad >= 18 and edad < 30:
    print("Usted pertenece a la categoria: Adulto/a joven")
else:
    print("Usted pertenece a la categoria: Adulto/a")
#Actividad n°5
password=input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
num=len(password)
if num >= 8 and num <=14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")
#Actividad n°6
num_aleatorio=[random.randint(1,100) for i in range (50)]
moda=mode(num_aleatorio)
mediana=median(num_aleatorio)
media=mean(num_aleatorio)
if media>mediana>moda:
    print("Hay sesgo positivo.")
elif media<mediana<moda:
    print("hay sesgo negativo.")
else:
    print("No hay sesgo.")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")
#Actividad n°7
frase=input("Ingrese una frase o palabra: ")
ultimaLetra=frase[len(frase)-1]
if ultimaLetra in "aeiou" or ultimaLetra in "AEIOU":
    print(f"{frase}!")
#Actividad n°8
nombre=input("ingrese su nombre: ")
print("Opciones:")
print("Precione 1 si desea su nombre en mayúsculas.")
print("Precione 2 si desea su nombre en minúsculas.")
print("Precione 3 si desea su nombre con la primera letra en mayúsculas.")
opcion=input("ingrese la opcion: ")
if opcion=="1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
#Actividad n°9
magnitud=int(input("Ingrese la magnitud de el terremoto: "))
if magnitud<3:
    print("Muy Leve (imperceptible).")
elif magnitud>=3 and magnitud<4:
    print("Leve (ligeramente perceptible).")
elif magnitud>=4 and magnitud<5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud>=5 and magnitud<6:
    print("Fuerte (puede causar daños en estructuras debiles).")
elif magnitud>=6 and magnitud<7:
    print("Muy Fuerte (puede causar daños significativos).")
elif magnitud>=7:
    print("Extremo (Puede Causar graves daños a gran escala)")
#Actividad n°10
hemis = input("Ingrese en qué hemisferio se encuentra: ").upper()
mm = int(input("Ingrese el mes (en número): "))
aaaa = int(input("Ingrese el año: "))
dd = int(input("Ingrese el dia: "))
if hemis == "NORTE":
    if (mm == 12 and dd >= 21) or mm == 1 or mm == 2 or (mm == 3 and dd <= 20):
        print("Invierno")
    elif (mm == 3 and dd >= 21) or mm == 4 or mm == 5 or (mm == 6 and dd <= 20):
        print("Primavera")
    elif (mm == 6 and dd >= 21) or mm == 7 or mm == 8 or (mm == 9 and dd <= 20):
        print("Verano")
    else:
        print("Otoño")
elif hemis == "SUR":
    if (mm == 12 and dd >= 21) or mm == 1 or mm == 2 or (mm == 3 and dd <= 20):
        print("Verano")
    elif (mm == 3 and dd >= 21) or mm == 4 or mm == 5 or (mm == 6 and dd <= 20):
        print("Otoño")
    elif (mm == 6 and dd >= 21) or mm == 7 or mm == 8 or (mm == 9 and dd <= 20):
        print("Invierno")
    else:
        print("Primavera")
