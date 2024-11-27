NumeroInicio = int(input("Ingrese el número de la registradora al iniciar el día: "))
NumeroFinal = int(input("Ingrese el número de la registradora al terminar el día: "))
ValorPasaje = float(input("Ingrese el valor del pasaje: "))
TotalPasajeros = NumeroFinal - NumeroInicio
TotalRecaudado = TotalPasajeros * ValorPasaje
LiquidacionEmpresa = TotalRecaudado * (3 / 4)
LiquidacionConductor = TotalRecaudado * (1 / 4)
print("\nResultados de la liquidación:")
print(f"Total de pasajeros transportados: {TotalPasajeros}")
print(f"Valor liquidado al conductor: ${LiquidacionConductor:.2f}")
print(f"Valor liquidado a la empresa: ${LiquidacionEmpresa:.2f}")