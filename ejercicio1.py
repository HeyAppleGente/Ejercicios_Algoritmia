#Entradas:
#   lado1: Solicita el primer lado del triangulo,
#   lado2: Solicita el segundo lado del triangulo,
#   lado3: Solicita el tercer lado del triangulo

#Salidas:
#   print: Muestra los diferentes tipos de triangulos si cumple con una de las 3 condiciones.

#Proceso: 
#   Si las variables ingresadas por el usuario cumple con una de las tres condiciones mostrará el tipo de triangulo al que pertenece


print("Ingrese la medida del triangulo")
lado1=int(input("Lado 1: "))
lado2=int(input("Lado 2: "))
lado3=int(input("Lado 3: "))
if lado1==lado2 & lado2 == lado3:
    print("Es un triangulo equilatero")
elif lado1 == lado2 or lado2==lado3:
    print ("Es un triangulo isoseles")
else:
    print("Es un triangulo escaleno")