#Trabajo Practico n°1
#Alumno: Vega Luis Fernando
#Comision: 22
#1°
print("Hola Mundo!")
#2°
nombre=input("ingrese su nombre: ")
print(f"Hola {nombre}!")
#3°
nombre=input("ingrese su nombre: ")
apellido=input("ingrese su apellido: ")
edad=input("ingrese su edad: ")
Residencia=input("ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {Residencia}")
#4°
radio=int(input("ingrese el Radio del circulo que desea calcular: "))
pi=3.14
Perimetro= pi*(2*radio)
area=pi*radio**2
print(f"El Perimetro es: {Perimetro} y el area es: {area}")
#5°
segundos=int(input("ingrese la cantidad de segundos que desea convertir en horas: "))
minutos=segundos/60
hora=minutos/60
print(f"la cantidad de hora es: {hora}")
#6°
numero=int(input("Ingrese el numero: "))
for i in range(1,11):
    print(i*numero)
#7°
num1=int(input("ingrese el primer numero: "))
num2=int(input("ingrese el segundo numero: "))
print(num1+num2)
print(num1/num2)
print(num1*num2)
print(num1-num2)
#8°
altura=float(input("ingrese su altura: "))
peso=float(input("ingrese su peso: "))
IMC=peso/altura**2
print(f"el indice de masa corporal es de: {IMC}")
#9°
Celsius=float(input("ingrese la temperatura Celsius: "))
fahr=Celsius*1.8+32
print(f"El equivalente en grados Fahrenheit es: {fahr}")
#10°
num1=int(input("ingrese el primer numero: "))
num2=int(input("ingrese el segundo numero: "))
num3=int(input("ingrese el tercer numero: "))
promedio=num1+num2+num3/3
print(f"el promedio es: {promedio}")