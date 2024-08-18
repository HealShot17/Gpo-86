"""Definir un procedimiento histograma() que tome una lista de números enteros e imprima un histograma
en la pantalla. Ejemplo: histograma ([4,9,7]) deberia imprimir lo siguiente
 ****
 *********
 *******
 """
#Datos=[int(input("Ingrese el dato 1 del histograma: ")),int(input("Ingrese el dato 2 del histograma: ")),int(input("Ingrese el dato 3 del histograma: "))]
Tamano = int(input("Ingrese la cantidad de elementos en la lista: "))
Datos = []
for i in range(Tamano):
    elemento = int(input(f"Ingrese el elemento {i+1} de la lista: "))
    Datos.append(elemento)
def histograma(lista):
    for numero in lista:
        print('*' * numero)


histograma(Datos)

