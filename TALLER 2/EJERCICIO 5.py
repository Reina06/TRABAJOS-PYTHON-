NOTA = float(input("Ingrese su nota para darle su nota cualitativa:  "))
if NOTA >= 4.6 and  NOTA <= 5.0: 
    print("Su nota es EXELENTE, FELICITACIONES ;) ")
elif NOTA >= 3.6 and NOTA < 4.6: 
    print("Su nota es Buena, Puede ser mejor sigue adelante ")
elif NOTA >= 3.0 and NOTA < 3.6: 
    print("Su nota es ACEPTABLE, pero hay que trabajar mas ")
elif NOTA >= 2.0 and NOTA < 3.0: 
    print("Su nota es INSUFICIENTE ")
elif NOTA >= 0.0 and NOTA < 2.0: 
    print("Su nota es DEFICIENTE")