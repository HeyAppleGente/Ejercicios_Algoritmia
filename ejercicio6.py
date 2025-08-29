#Entradas:
#   edad: Solicita la edad,
#   nacionalidad: Solicita la nacionalidad.

#Salidas: 
#   print: Muestra "puede votar" o "no puede votar"

#Proceso:
# La variable cumple con la condición
edad = int(input("ingrese edad"))
nacionalidad =str(input("nacionalidad"))
if edad >= 18 and nacionalidad =="COLOMBIAN@":
    print ("puede votar")
else:
    print ("no puede votar")    

