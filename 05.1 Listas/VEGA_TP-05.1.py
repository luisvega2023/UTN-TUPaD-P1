# Actividad 1.
# Crear una lista con números del 1 al 100 que sean múltiplos de 4.
lista1al100 = list(range(4, 101, 4))
print(lista1al100)

# Actividad 2.
# Imprimir el penúltimo elemento de una lista.
lista = ["elemento1", "elemento2", "elemento3", "elemento4", "elemento5"]
print(f"El penúltimo elemento es: {lista[-2]}")

# Actividad 3.
# Crear una lista vacía.
lista_vacia = []
# Agregar tres elementos tipo string a la lista.
lista_vacia.append("agregar")
lista_vacia.append("tres")
lista_vacia.append("palabras")
print(f"La lista resultante es: {lista_vacia}")

# Actividad 4.
# Lista inicial de animales.
animales = ["perro", "gato", "conejo", "pez"]
print(f"Valores sin actualizar: {animales}")
# Reemplazar el segundo y último valor de la lista.
animales[1] = "loro"   # Segundo valor (índice 1).
animales[-1] = "oso"   # Último valor (índice -1).
print(f"Valores actualizados: {animales}")

# Actividad 5.
# Eliminar el valor más alto de la lista.
numeros = [8, 15, 3, 22, 7]
# La función max(numeros) devuelve el elemento con el valor más alto dentro de la lista.
numeros.remove(max(numeros))  # Elimina el número 22, que es el mayor.
print(numeros)

# Actividad 6.
# Crear una lista de números del 10 al 30 (sin incluir el 31), con intervalos de 5.
lista10al30 = list(range(10, 31, 5))
# Imprimir el primer y segundo valor de la lista.
print(lista10al30[0:2])

# Actividad 7.
# Lista de autos.
autos = ["sedan", "polo", "suran", "gol"]
# Reemplazar los valores en los índices 1 y 2 con valores booleanos.
autos[1] = False
autos[2] = True

# Actividad 8.
# Crear una lista vacía.
dobles = []
# Agregar el doble de los números 5, 10 y 15.
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
# Imprimir la lista.
print(dobles)

# Actividad 9.
# Lista de listas que representan compras de tres clientes.
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# Agregar "jugo" a la lista del tercer cliente.
compras[2].append("jugo")
# Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines"
# Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")
# Imprimir la lista modificada.
print(compras)

# Actividad 10.
# Lista anidada con distintos tipos de datos.
# Posición lista_anidada[0]: 15
# Posición lista_anidada[1]: True
# Posición lista_anidada[2][0]: 25.5
# Posición lista_anidada[2][1]: 57.9
# Posición lista_anidada[2][2]: 30.6
# Posición lista_anidada[3]: False
lista_anidada = [15, True, [25.5, 57.9, 30.6], False]
print(lista_anidada)
