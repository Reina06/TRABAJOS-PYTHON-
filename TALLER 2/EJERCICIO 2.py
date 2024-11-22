print("Se va realizar la siguiente ecuacion:  P=(r-2)3")
r= int(input("Ingrese un numero para r ")) 
p= 0
if r != 2:
    p=(r-2)**3
    print(f"El resultado de la ecuacion  es = {p}" )
else: 
    p = 1 
    print(f"P es igual a {p}")