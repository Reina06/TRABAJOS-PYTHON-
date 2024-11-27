AreaTotal = float(input("Ingrese el área total del terreno en metros cuadrados: "))
AreaCultivos = AreaTotal * 0.40
AreaVivienda = AreaTotal * 0.25
AreaZonasVerdes = AreaTotal * 0.15
AreaRestante = AreaTotal - (AreaCultivos + AreaVivienda + AreaZonasVerdes)
print("\nDistribución del terreno:")
print(f"Área para cultivos: {AreaCultivos:.2f} m²")
print(f"Área para construir vivienda: {AreaVivienda:.2f} m²")
print(f"Área para zonas verdes: {AreaZonasVerdes:.2f} m²")
print(f"Área disponible para otros proyectos: {AreaRestante:.2f} m²")