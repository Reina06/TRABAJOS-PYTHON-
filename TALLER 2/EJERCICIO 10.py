nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
Sexo = input("Ingrese su SEXO:  ")
Sexo1 = Sexo.upper()
EstadoCivil = input("Ingrese su estado civil: ")
EstadoCivil1= EstadoCivil.upper()
if edad < 18:
    print("Eres menor de edad, aun no puedes votar ;( ")
elif edad >= 18 and Sexo1 == "FEMENINO" and EstadoCivil1 == "CASADA": 
    print(f"{nombre} Tu votas en la mesa #1")
elif edad >= 18 and Sexo1 == "FEMENINO" and EstadoCivil1 == "SOLTERA": 
    print(f"{nombre} Tu votas en la mesa #2")
elif edad >= 18 and Sexo1 == "FEMENINO" and EstadoCivil1 == "SEPARADA":
    print(f"{nombre} Tu votas en la mesa #3")
elif edad >= 18 and Sexo1 == "FEMENINO" and EstadoCivil1 == "OTRO":  
    print(f"{nombre} Tu votas en la mesa #4")
elif edad >= 18 and Sexo1 == "MASCULINO" and EstadoCivil1 == "CASADO": 
    print(f"{nombre} Tu votas en la mesa #5")
elif edad >= 18 and Sexo1 == "MASCULINO" and EstadoCivil1 == "SOLTERO": 
    print(f"{nombre} Tu votas en la mesa #6")
elif edad >= 18 and Sexo1 == "MASCULINO" and EstadoCivil1 == "SEPARADO":
    print(f"{nombre} Tu votas en la mesa #7")
elif edad >= 18 and Sexo1 == "MASCULINO" and EstadoCivil1 == "OTRO":
    print(f"{nombre}  Tu votas en la mesa #8") 
else:
    print("Los datos ingresados no son validos")