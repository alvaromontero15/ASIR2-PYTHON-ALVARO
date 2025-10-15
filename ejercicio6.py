#Calcular el factorial de un número usando un bucle while
numero = int(input("Escriba un número para calcular su factorial: ")) #Pedir al usuario que ingrese un número
factorial = 1 #Inicializar la variable factorial
contador = 1 #Inicializar el contador
while contador <= numero: #Bucle while para calcular el factorial
    factorial *= contador #Multiplicar el factorial por el contador
    contador += 1 #Incrementar el contador
print("El factorial de", numero, "es", factorial) #Mostrar el resultado al usuario