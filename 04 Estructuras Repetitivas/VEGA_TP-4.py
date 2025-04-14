#Actividad 1:
for i in range(1,101):
    print(i)

#Actividad 2:
cont=0
num=int(input("Ingrese un numero Entero: "))
if num >=0:
    if num >0:
        while num >0:
            num=num//10
            cont+=1
    else: # 0 = 1 digito.
            cont=1
    print(f"El numero tiene {cont} digitos")
else:
    print("Por favor ingrese un numero entero positivo.")

#Actividad 3: 
suma=0
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
if num1<num2:
    for i in range(num1,num2+1):
        suma+=i
elif num1>num2:
    for i in range(num2,num1+1):
        suma+=i
print(f"La suma de todos los numeros enteros comprendidos entre {num1} y {num2} es: {suma}")

#Actividad 4:
suma=0
num=int(input("ingrese un numero entero: ")) 
while num != 0:
    suma+=num 
    num=int(input("ingrese otro numero entero: "))
print(f"El total acumulado de los numeros ingresados es: {suma}")

#Actividad 5:
from random import * 
num_random=randint(0,9)
num=int(input("Ingrese un numero entre el 0 y 9: "))
cont=1
while num !=num_random:
    num=int(input("Ingrese otro numero entre el 0 y 9: "))
    cont+=1
print(f"Ustedes necesito {cont} intentos para acertar.")

#Actividad 6:
for i in range(100,0,-2):
    print(i)

#Actividad 7:
suma=0
num=int(input("Ingrese un numero positivo: "))
for i in range(0,num):
    suma+=i
print(f"La suma de todos los numeros comprendidos del 0 al {num} es: {suma}")

#Actividad 8:
positivo=0
negativo=0
impar=0
par=0
for i in range(100):
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
suma=0
for i in range (10):
    num=int(input("ingrese un numero: "))
    print(num)
    suma+=num
print(f"La media de los numeros ingresados es {suma/10}")
#Actividad 10:
num = int(input("Ingresa un número: "))
numero_invertido = 0

while num!=0:
    digito=num%10
    numero_invertido=numero_invertido*10+digito
    num=num//10

print("Número invertido:", numero_invertido)