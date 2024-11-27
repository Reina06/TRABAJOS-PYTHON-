Taller1 = float(input("Ingrese la nota del Taller 1: "))
Taller2 = float(input("Ingrese la nota del Taller 2: "))
PrimeraNota = (Taller1 + Taller2) / 2
Evaluacion1 = float(input("Ingrese la nota de la Evaluación 1: "))
Evaluacion2 = float(input("Ingrese la nota de la Evaluación 2: "))
Evaluacion3 = float(input("Ingrese la nota de la Evaluación 3: "))
SegundaNota = (Evaluacion1 + Evaluacion2 + Evaluacion3) / 3
TrabajoFinal = float(input("Ingrese la nota del Trabajo Final: "))
TerceraNota = TrabajoFinal
Quiz1 = float(input("Ingrese la nota del Quiz 1: "))
Quiz2 = float(input("Ingrese la nota del Quiz 2: "))
Quiz3 = float(input("Ingrese la nota del Quiz 3: "))
Quiz4 = float(input("Ingrese la nota del Quiz 4: "))
CuartaNota = (Quiz1 + Quiz2 + Quiz3 + Quiz4) / 4
NotaDefinitiva = (PrimeraNota * 0.15) + (SegundaNota * 0.30) + (TerceraNota * 0.30) + (CuartaNota * 0.25)
print("\nLa nota definitiva del estudiante es:", round(NotaDefinitiva, 2))