'''Escribir un programa que reciba una serie de calificaciones y luego imprima el promedio'''
N_Calificaciones = int(input("Ingresa cuantas calidaciones vamos a promediar por favor: "))
x = 0
for i in range(N_Calificaciones):
    y = int(input(f"Ingrese la calificacion {i+1}: "))
    x = x+y
    y = 0
promedio = x/N_Calificaciones
print(f"El promedio es {promedio}")
    