import time

def es_palindromo_bucle(palabra):
    n = len(palabra)
    for i in range(n // 2):
        if palabra[i] != palabra[n - 1 - i]:
            return False
    return True

def es_palindromo(palabra):
    return palabra == palabra[::-1]
#Algoritmo 1
text= "reconocer"
start= time.time()
resultado1= es_palindromo_bucle(text)
end= time.time()
print(f" Resultado {(end-start)*1000}")

#Algoritmo 2
start= time.time()
resultado1= es_palindromo(text)
end= time.time()
print(f" Resultado {(end-start)*1000}")