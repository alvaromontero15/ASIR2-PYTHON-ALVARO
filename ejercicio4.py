#Verificar si un número es positivo, negativo o cero

numero= float(input("Escriba un número: ")) #Solicitar al usuario que ingrese un número
if numero > 0: #Condición para verificar si el número es positivo
    print("El número es positivo") #Imprimir resultado si el número es positivo
elif numero < 0: #Condición para verificar si el número es negativo
    print("El número es negativo") #Imprimir resultado si el número es negativo
else: #Si el número no es positivo ni negativo, es cero
    print("El número es cero") #Imprimir resultado si el número es cero