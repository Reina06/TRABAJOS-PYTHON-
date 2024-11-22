A = int(input("Ingrese un numero "))
B = int(input("Ingrese un numero "))
if A > B:
    print(F"El numero menor es {B}")
    print(f"El numero mayor es {A}")
elif A < B:
    print (f"El numero menor es {A}")
    print (f"El numero mayor es {B}")
elif A == B:
    print("Los numeros son iguales no se pueden ordenar ")