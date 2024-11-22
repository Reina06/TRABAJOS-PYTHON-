print("ALGORITMO PARA TENER EN CUENTA TIEMPO DE ENTRENAMIENTO SEMANAL ")
Tiempo1 = int(input("Ingrese el tiempo entrenado el primer dia en minutos "))
Distancia1 = int(input("Ingrese la distacia recorrida el primer dia en metros "))
Tiempo2 = int(input("Ingrese el tiempo entrenado el segundo dia en minutos "))
Distancia2 = int(input("Ingrese la distancia recorrida  el segundo  dia en minutos "))
Tiempo3 = int(input("Ingrese el tiempo entrenado el tercer dia en minutos "))
Distancia3 = int(input("Ingrese la distancia recorrida  el tercer  dia en minutos "))
TiempoTotal = (Tiempo1+Tiempo2)+Tiempo3 
DistanciaTotal = (Distancia1+Distancia2)+Distancia3
PromedioTiempo = TiempoTotal//3
PromedioDistancia = DistanciaTotal//3
print(f"\nEl tiempo total recorrido por 3 dias es de: {TiempoTotal} minutos")
print(f"\nLa Distancia total recorrida por 3 dias es de: {DistanciaTotal} metros")
print(f"\nSu promedio en tiempo es de: {PromedioTiempo} minutos" )
print(f"\nSu promedio en recorrido es de: {PromedioDistancia} distancia ")
