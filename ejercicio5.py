#Entradas:
#   multiplo: Solicita el numero

#Salidas: 
#   print: Muestra si "el numero es multiplo de 5" o "no es multiplo de 5"

#Proceso
#   La variable cumple con la condición
multiplo = int(input("ingrese un numero"))
if multiplo % 5 == 0:
    print ("el numero es multiplo de 5")
else:
    print ("no es multiplo de 5")    