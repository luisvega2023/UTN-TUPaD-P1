#Actividad 1:
for i in range(1,101):
    print(i)

#Actividad 2:
cont=0 #Inicializamos la variable contador.
num=int(input("Ingrese un numero Entero: "))#se solicita al usuario un numero entero.
if num >=0:#se verifica que el numero ingresado sea positivo para no generar un error, con una condicional doble.
    if num >0:
        while num >0: #bucle while con un contador.
            num=num//10
            cont+=1
    else: # 0 = 1 digito.
            cont=1
    print(f"El numero tiene {cont} digitos")
else:
    print("Por favor ingrese un numero entero positivo.")

#Actividad 3: 
suma=0 #Inicializamos la variable acumulador.
#se solicita al usuario los datos.
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
#condicional doble que verifica los datos.
if num1<num2:
    for i in range(num1,num2+1):#bucle que suma los numeros enteros compredidos entre los datos ingresados.
        suma+=i
elif num1>num2:
    for i in range(num2,num1+1):
        suma+=i
print(f"La suma de todos los numeros enteros comprendidos entre {num1} y {num2} es: {suma}")

#Actividad 4:
suma=0 #Inicializamos la variable acumulador.
num=int(input("ingrese un numero entero: ")) #se solicita al usuario un numero entero.
while num != 0:#bucle while, este se detiene si ingresas el numero 0.
    suma+=num 
    num=int(input("ingrese otro numero entero: "))
print(f"El total acumulado de los numeros ingresados es: {suma}")

#Actividad 5:
from random import * #se importa la biblioteca random
num_random=randint(0,9)#se declara un numero random entre el 0 y el 9.
num=int(input("Ingrese un numero entre el 0 y 9: "))#se le pide al usuario un numero entero entre el 0 y 9.
cont=1 #Inicializamos la variable contador.
while num !=num_random: #bucle while que se detiene cuando el numero ingresado sea igual al numero random.
    num=int(input("Ingrese otro numero entre el 0 y 9: "))
    cont+=1
print(f"Ustedes necesito {cont} intentos para acertar.")

#Actividad 6:
for i in range(100,0,-2):
    print(i)

#Actividad 7:
suma=0 #Inicializamos la variable acumulador.
num=int(input("Ingrese un numero positivo: ")) # se solicita al usuario un numero positivo.
for i in range(0,num): #bucle for con rango 0 al numero ingresado.
    suma+=i
print(f"La suma de todos los numeros comprendidos del 0 al {num} es: {suma}")

#Actividad 8:
# Inicializamos la variables contador.
positivo=0
negativo=0
impar=0
par=0
#////////////////////
for i in range(100): #bucle for con condicionales y contadores.
    num=int(input("ingrese un numero: "))
    if num!=0:
        if num >0:
            positivo+=1
        elif num <0:
            negativo+=1
        if num%2==0:
            par+=1
        else:
            impar+=1
    else:
        print("Ingresaste el numero 0, este es neutro.")
print(f"los numeros positivos ingresados son: {positivo}")
print(f"los numeros negativos ingresados son: {negativo}")
print(f"los numeros par ingresados son: {par}")
print(f"los numeros impar ingresdos son: {impar}")
#Actividad 9:
suma=0 # Inicializamos la variable acumulador.
for i in range (100): #bucle for, que suma los datos ingresados.
    num=int(input("ingrese un numero: "))
    suma+=num
print(f"La media de los numeros ingresados es {suma/100}") #resultado con el promedio
#Actividad 10:
num = int(input("Ingresa un número: "))# se solicita al usuario un numero.
numero_invertido = 0 #se declara la variable donde se almacenara el numero invertido.
while num!=0:
    digito=num%10 #calculo que extrae el ultimo numero.
    numero_invertido=numero_invertido*10+digito #calculo donde almacena el ultimo numero, lo multiplica x10 y le suma el siguiente.
    num=num//10 # Division entera por 10 que elimina el ultimo digito.

print("Número invertido:", numero_invertido)