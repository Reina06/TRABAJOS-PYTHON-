print("algoritmo para dividir herencia")
Herencia = int(input("Ingrese el valor de la herencia "))
HerenciaMadre = Herencia * 0.40
print(F"La herencia que le corresponde a la madre es de: {HerenciaMadre}")
HerenciaRestante = Herencia - HerenciaMadre 
HerenciaHijo1 =   HerenciaRestante * 0.30
HerenciaHijo2 = HerenciaRestante * 0.20
HerenciaHijo3 = HerenciaRestante * 0.40 
HerenciaHijo4 = HerenciaRestante * 0.10
print(F"Y la herencia restante es de: {HerenciaRestante}")
print(F"La herencia que le corresponde a la madre es de: {HerenciaMadre}")
print(f"La herencia que le corresponde al primer hijo es de: {HerenciaHijo1 }")  
print(f"La herencia que le corresponde al segundo hijo es de: {HerenciaHijo2 }")  
print(f"La herencia que le corresponde al tercer hijo es de: {HerenciaHijo3 }")  
print(f"La herencia que le corresponde al cuarto hijo es de: {HerenciaHijo4 }")  