#Crear una lista de números pares del 1 al 20 usando un bucle

numeros_pares = [] #Lista vacía para almacenar los números pares
for i in range(1, 21): #Bucle que recorre los números del 1 al 20
    if i % 2 == 0: #Condición para verificar si el número es par
        numeros_pares.append(i) #Agregar el número par a la lista
print(numeros_pares) #Imprimir la lista