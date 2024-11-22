print('Algoritmo para enchapar baño')
Alto = float(input('ingrese el alto de su baño en metros'))
Ancho = float(input('Ingrese el ancho de su baño en metros'))
Area = Alto * Ancho 
Area_Cuadrado  = 3.5   
print('El Area de su baño es de ', Area , 'm2' )
Numero_Cajas = Area//Area_Cuadrado 
print(f"Necesita {Numero_Cajas} Para enchapar su baño")