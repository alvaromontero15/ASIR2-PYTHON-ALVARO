#Invertir una cadena de texto usando un bucle for
cadena = input("Escriba una cadena de texto: ") #Pedir al usuario que ingrese una cadena de texto
cadena_invertida = "" #Inicializar la variable para la cadena invertida
for caracter in cadena: #Bucle for para recorrer cada caracter en la cadena
    cadena_invertida = caracter + cadena_invertida #Agregar el caracter al inicio de la cadena invertida
print("La cadena invertida es:", cadena_invertida) #Mostrar la cadena invertida al usuario