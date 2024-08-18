''' 
Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente
todos los números de una lista. Por ejemplo: sum([1,2,3,4]) deberia devolver 10 y multip ([1,2,3,4]) 
deberia devolver 24.
'''
cantidad_datos = int(input("Ingrese la cantidad de datos: "))
datos = []


for i in range(cantidad_datos):
    numero = float(input(f"Ingrese el número {i+1}: "))
    datos.append(numero)


def sumar(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

def multiplicar(lista):
    producto = 1
    for numero in lista:
        producto *= numero
    return producto




print("La suma de los números ingresados es: ",sumar(datos))
print("El producto de los números ingresados es: ",multiplicar(datos))


"""
Numeros =[int(input("Ingrese el primer número por favor:")),
          int(input("Ingrese el segundo número por favor:")),
          int(input("Ingrese el tercer número por favor:")),
          int(input("Ingrese el cuarto número por favor:"))]
x = 0   #x es la cantidad de la suma
y = 1   #y es la cantidad de la multiplicacion
for elemento in Numeros:
    x += elemento 
    y *= elemento 

print("La cantidad sumada es")
print(x)
print("La cantidad multiplicada es")
print(y)
"""

