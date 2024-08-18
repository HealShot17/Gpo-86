'''Definir una tupla con 10 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.'''


edades = []
for i in range(10):
    edad = int(input(f"Ingrese la edad de la persona {i+1}: "))
    edades.append(edad)
    
edades = tuple(edades)
cantidad_superiores_20 = sum(edad > 20 for edad in edades)
print(f"Cantidad de personas con edades superiores a 20: {cantidad_superiores_20}")


