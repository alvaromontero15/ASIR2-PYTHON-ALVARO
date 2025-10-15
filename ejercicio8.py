#Contar el número de vocales en una cadena de texto
cadena = input("Escriba una cadena de texto: ") #Pedir al usuario que ingrese una cadena de texto
vocales = "aeiouAEIOU" #Definir las vocales (mayúsculas y minúsculas)
contador = 0 #Inicializar el contador de vocales
for caracter in cadena: #Bucle for para recorrer cada caracter en la cadena
    if caracter in vocales: #Si el caracter es una vocal
        contador += 1 #Incrementar el contador
print("El número de vocales en la cadena es:", contador) #Mostrar el número de vocales al usuario