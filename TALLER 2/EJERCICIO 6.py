Bonifacacion = float(input("Ingrese su bonifacion para ayudarle en su compra :) "))
if Bonifacacion == 10000 and Bonifacacion < 50000 :
    print("Puede comprar una Camara Web ")
elif Bonifacacion > 50000 and Bonifacacion <= 200000: 
    print("Puede comprar un subwoofer")
elif Bonifacacion > 200000 and Bonifacacion <= 500000: 
    print("Puede comprar un Disco Duro externo ")
elif Bonifacacion > 500000 and Bonifacacion  <= 1000000: 
    print ("Puede comprar una impresora funcional ")
elif Bonifacacion > 1000000: 
    print ("Puede comprar un proyector ")
else:
    print("Su bonificacion no le permite comprar nada")