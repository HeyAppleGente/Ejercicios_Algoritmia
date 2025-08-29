#Entradas:
#   numer: Solicita un numero

#Salidas:
#   print: Si la variable cumple con la primera condición muestra "El numero es negativo", si la variable cumple con la segunda condición muestra "El numero es cero", si la variable no cumple con ninguna de las condiciones mostrará "El numero es positivo"

#Proceso: 
# La variable cumple con algunas de las condiciones.
numer = int(input("Ingrese el numero: "))
if numer < 0:
 print ("el numero es negativo")
elif numer == 0:
  print("el numero es cero")
else:
 print("el numero es positivo")
