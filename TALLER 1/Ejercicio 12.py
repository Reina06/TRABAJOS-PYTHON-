print("----- Programa para defenir areas de su terreno ------- ")
AreaTotal = float(input("\n ingrese area total de su terreno: "))
AreaCultivo = AreaTotal * 0.40 
AreaVivienda = AreaTotal * 0.25
AreaVerde = AreaTotal * 0.15
AreaRestante =  (AreaCultivo + AreaVivienda + AreaVerde) 
AreaRestanteFinal = AreaTotal - AreaRestante 
Porcentaje = AreaRestanteFinal / 100
AreaRestantePorcentaje = Porcentaje * AreaTotal 
print(F"El Area Para el Cultivo es de {AreaCultivo}") 
print(F"\n El Area Para la Vivienda  es de {AreaVivienda}") 
print(F"\n El Area Para Zonas Verdes es de {AreaVerde}") 
print(F"\n El Area restante es de  {AreaRestanteFinal} %") 
print({AreaRestantePorcentaje})