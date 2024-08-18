"""Definir una función superposicion() que tome dos listas y devuelva True si tienen 
al menos un miembro en común o devuelva True si tiene al menos un miembro en común o devuelva 
False de lo contrario. Escribir la función usando el bucle for anidado."""

n1 = int(input("Ingrese la cantidad de elementos en la primera lista: "))
n2 = int(input("Ingrese la cantidad de elementos en la segunda lista: "))
lista1 = []
lista2 = []
for i in range(n1):
    elemento = input(f"Ingrese el elemento {i+1} de la primera lista: ")
    lista1.append(elemento)


for i in range(n2):
    elemento = input(f"Ingrese el elemento {i+1} de la segunda lista: ")
    lista2.append(elemento)
    
def superposicion(lista1, lista2):
    for elemento1 in lista1:
        for elemento2 in lista2:
            if elemento1 == elemento2:
                return True
    return False

resultado = superposicion(lista1, lista2)

# Mostrar el resultado
if resultado:
    print("Las listas tienen al menos un miembro en común.")
else:
    print("Las listas no tienen ningún miembro en común.")