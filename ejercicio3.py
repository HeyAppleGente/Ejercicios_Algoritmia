#Entradas:
#   anio: Solicita el año

#Salidas:
# print: Muestra "El año es bisiesto" o "El año no es bisiesto"

#Proceso:
# La variable cumple con alguna de las condiciones.

anio = int(input("Ingrese el año"))
if(anio % 4 == 0 and anio % 100 !=  0) or (anio % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")