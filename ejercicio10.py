#Entradas:
#   temperatura: Solicita la temperatura.

#Salidas:
# print: Muestra "temperatura adecuada" o "temperatura no adecuada"

#Proceso:
# La variable cumple con la condición.


temperatura =int(input("verificar temperatura para congelar"))
if temperatura <= 0:
    print ("temperatura adecuada")
else:
    print ("temperatura no adecuada")    