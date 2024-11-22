Lado1 = int(input("Ingrese el valor del lado A: "))
Lado2 = int(input("Ingrese el valor del lado B: "))
Lado3 = int(input("Ingrese el valor del lado C: "))

if Lado1 + Lado2 > Lado3 and Lado1 + Lado3 > Lado2 and Lado2 + Lado3 > Lado1:
    if Lado1 == Lado2 and Lado2 == Lado3:
        print("El triángulo es equilátero.")
    elif Lado1 != Lado2 and Lado2 != Lado3 and Lado1 != Lado3:
        print("El triángulo es escaleno.")
else:
    print("Los valores ingresados no permiten formar un triángulo.")