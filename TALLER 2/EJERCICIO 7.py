Matematica = float(input(" Ingrese el puntaje obtenido en la prueba de matematicas "))
Lenguaje = float(input(" Ingrese el puntaje obtenido en la prueba de Lenguaje "))
if Matematica > Lenguaje:
    print (f"Su nota mayor fue en Matematicas : {Matematica}")
elif Matematica < Lenguaje:
    print(f"Su nota mayor fue en Lenguaje : {Lenguaje}")
elif Matematica == Lenguaje:
    print("Usted tuvo el mismo puntaje en las mismas pruebas ")