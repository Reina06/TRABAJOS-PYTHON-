partido1= int(input("ingrese los goles anotados en el partido 1 "))
partido2= int(input("ingrese los goles anotados en el partido 2 "))
partido3= int(input("ingrese los goles anotados en el partido 3 "))
partido4= int(input("ingrese los goles anotados en el partido 4  "))
Goles = partido1 + partido2 + partido3 + partido4 
if Goles > 10: 
    Goles = Goles / 4 
    print(f"El promedio de goles es de {Goles}")
else: 
    print("No se pide determinar el promedio, esfuersesce para hacer mas goles ") 