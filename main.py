print("Calculadora")
print("")












opcion = int(input("Seleccione su opcion: "))

if opcion == 1:
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    suma(num1, num2)
elif opcion == 2:
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    resta(num1, num2)
elif opcion == 3:
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    multiplicacion(num1, num2)
elif opcion == 4:
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    division(num1, num2)
elif opcion == 5:
    print("Hasta luego")
    break
else:
    print("opcion erronea, vuelva a seleccionar")