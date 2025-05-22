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

#Actividad 7: 

def contar_bloques(num):
    # caso base
    if num == 0:
        return 1
    # llamada recursiva
    else:
        return num + contar_bloques(num-1)
    

print(contar_bloques(4))
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

n=int(input("Ingrese un numero al que quiera sumar sus digitos: "))
print(f"La suma de los digitos del numero {n} es: {suma_digitos(n)}")

#Actividad 7: