#Entradas:
#   rol: Solicita el rol (admin o usuario)

#Salidas:
#   print: Muestra "acceso permitido" o "acceso no permitido"

#Proceso:
# La variable cumple con la condición.

rol = str(input("ingrese su rol admin/usua"))
if rol == ("admin"):
    print ("acceso permitido")
else:
    print ("acceso no permitido")    



