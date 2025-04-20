#/////// Definicion de funciones /////////
#Actividad 1. Imprime "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")
#Actividad 2. Saluda al usuario con su nombre.
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
#Actividad 3. Muestra informacion personal del usuario.
def informacion_personal(nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
#Actividad 4. 
# Calcula y muestra el area de un circulo.
def calcular_area_circulo(radio):
    area=3.14 * radio **2
    print(f"El area de el circulo es: {area}")
# Calcula y muestra el perimetro de un circulo.
def calcular_perimetro_circulo(radio):
    perimetro= 2*3.14*radio
    print(f"El perimetro de el circulo es: {perimetro}")
#Actividad 5. Convierte segundos a horas
def segundos_a_horas(segundos):
    return int(segundos)/3600 
#Actividad 6. muestra la tabla de multiplicar del numero ingresado.
def tabla_multiplicar(numero):
    for i in range(1,11):
        mult= numero*i
        print(f"{numero} x {i}= {mult}")
#Actividad 7. Realiza operaciones basicas entre dos numeros.
def operaciones_basicas(num1,num2):
    suma=num1+num2
    resta=num1-num2
    mult=num1*num2
    if num2!=0 :
        div=num1/num2
    else:
        div="No se puede dividir entre cero"
    return suma,resta,mult,div
#Actividad 8. Calcula el indice de masa corporal (IMC).
def calcular_imc(num1,num2):
    return num1/(num2**2)
#Actividad 9. Convierte temperatura de celsius a fahrenheit.
def celsius_a_fahrenheit(num):
    return (num*9/5)+32
#Actividad 10. Calcula el promedio de tres numeros.
def calcular_promedio(num1,num2,num3):
    return (num1+num2+num3)/3

#//////// Programas principales /////////
#Actividad 1.
imprimir_hola_mundo()
#Actividad 2.
saludar_usuario("luis")
#Actividad 3.
nombre=input("Ingrese su nombre: ")
apellido=input("ingrese su apellido: ")
edad=input("Ingrese su edad: ")
residencia=input("Ingrese su residencia: ")
informacion_personal(nombre,apellido,edad,residencia)
#Actividad 4.
radio=int(input("ingrese el radio del circulo: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)
#Actividad 5.
segundos=input("Ingrese la cantidad de segundos que desea convertir: ")
hora=segundos_a_horas(segundos)
print(f"es: {hora} hora")
#Actividad 6.
numero=int(input("Ingrese un numero que desee ver la tabla de multiplicar: "))
tabla_multiplicar(numero)
#Actividad 7.
a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
print(f"Se mostrara de la siguiente manera (suma, resta, multiplicacion, division) los resultados de {a} y {b}: {operaciones_basicas(a,b)}")
#Actividad 8.
kg=float(input("Ingrese su peso corporal en kilogramos: "))
altura=float(input("Ingrese su altura en metros: "))
imc=calcular_imc(kg,altura)
print(f"su indice de masa corporal (IMC) es de: {imc}")
#Actividad 9.
celsius=float(input("Ingrese la temperatura en celsius que desee convertir a fahrenheit: "))
fahrenheit=celsius_a_fahrenheit(celsius)
print(f"grado celsius ({celsius}°C) = grado fahrenheit ({fahrenheit}°F)")
#Actividad 10.
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
num3=int(input("Ingrese el tercer numero: "))
promedio=calcular_promedio(num1,num2,num3)
print(f"El promedio es de: {promedio}")