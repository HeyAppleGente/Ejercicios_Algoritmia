#Entradas:
#   numero: Solicita el numero

#Salidas:
#   print: Muestra "Mayor a 100" o "menor a -100" o "el numero que ingreso es menor a 100"

#Proceso:
# La variable cumple con una de las 3 condiciones.

numero = int(input("ingrese un numero"))
if numero >100:
    print ("mayor a 100")
elif numero < -100:
    print ("menor a -100")
else:    
     print ("el numero que ingreso es menor a 100")