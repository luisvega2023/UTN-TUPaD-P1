#from modulos_tp6 import *
#Actividad 1: Crea una funcion recursiva que calcule el factorial de un numero.
def factorial(num):
    # caso base
    if num == 0:
        return 1
    # llamada recursiva
    else:
        return num * factorial(num-1) 

#Actividad 2: Crea una funcion recursiva que calcule el valor de la serie de fibonacci.
def fibonacci_recursivo(posicion):
    # caso base
    if posicion==0:
        return 0
    elif posicion==1:
        return 1
    else:
        return fibonacci_recursivo(posicion-1)+fibonacci_recursivo(posicion-2)
    
#Actividad 3: Crea una funcion recursiva que calcule la potencia de un numero base elevado a un exponente.

def potencia_recursivo(n,m):
    # caso base
    if m ==0:
        return 1
    else:
        return n * potencia_recursivo(n, m - 1)
    
#Actividad 4: Funcion de representar numero decimal a binario.

def binario(n):
    # caso base
    if n==0:
        return ""
    else:
        binar=str(n%2)#
        return binario(n//2) + binar

#Actividad 5: determina si una palabra es palindromo.

def es_palindromo(palabra):
    #verifica si la palabra tiene mas de una letra
    if len(palabra)<1:
        return True
    #verifica si la primera y ultima letra son iguales.
    elif palabra[0] ==palabra[-1]:
        #llamado recursivo sin la primera y ultima letra.
        return es_palindromo(palabra[1:-1])
    else:
        return False

#Actividad 6: funcion recursiva que reciba un numero entero positivo y devuelva la suma de todos sus digitos.

def suma_digitos(n):
    if n < 10 :
        return n
    else:
        return suma_digitos(n//10) + n%10

#Actividad 7: funcion que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.

def contar_bloques(num):
    # caso base
    if num == 0:
        return 0
    # llamada recursiva
    else:
        return num + contar_bloques(num-1)

#Actividad 8: Funcion que reciba un número entero positivo, un dígito y que devuelva cuantas veces aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:  # Caso base: si el número es 0, no quedan más dígitos por analizar
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)


#///////////////////////////////////////////////////////////////////
#Actividad 1: 
#se pide al usuario un numero maximo, del cual se mostrara del 1 al max.
num=int(input("ingrese hasta que numero desea que se muestre el factorial: "))
for i in range(1,num+1):
    #se imprime por pantalla el factorial de todos los numeros enteros entre 1 y el numero que indico el usuario.
    print(f" el factorial de {i} es: {factorial(i)}")

#Actividad 2:
num=int(input("Inque hasta que posicion termina la seria: "))
for i in range(num):
    print(f"En la posicion {i} obtenemos el valor de fibonacci: {fibonacci_recursivo(i)}")

#Actividad 3:
base=int(input("Ingrece la base: "))
exponente=int(input("Ingrese el exponente: "))
print(f"{base} elevado a la {exponente} es {potencia_recursivo(base, exponente)}")

#Actividad 4:

decimal=int(input("Ingrese un número entero positivo en base decimal: "))
print(f"la representacion del numero decimal {decimal} a binario es: {binario(decimal)}")

#Actividad 5:

palabra=input("ingrese una palabra para verificar si es palindromo: ")
if es_palindromo(palabra)==True:
    print("La palabra que ingreso es palindromo")
else:
    print("La plabra que ingreso no es palindromo")

#Actividad 6:

num=int(input("Ingrese un numero al que quiera sumar sus digitos: "))
print(f"La suma de los digitos del numero {num} es: {suma_digitos(num)}")

#Actividad 7:

num=int(input("Ingrese la cantidad de niveles que tiene la piramide: "))
print(f"La cantidad de bloques que tiene los {num} niveles son: {contar_bloques(num)}")

#Actividad 8:

num=int(input("Ingrese un número entero positivo: "))
digito=int(input("Ingrese un digito que desea saber cuántas veces aparece en el número: "))
print(f"El digito {digito} aparece {contar_digito(num,digito)} en el numero {num}")