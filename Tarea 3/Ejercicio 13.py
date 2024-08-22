'''Hacer un programa que pida al usuario una lista de nombres y los ordene alfabeticamente'''

num_nombres = int(input("Menciona la cantidad de nombres que ingresaras por favor: "))
nombres = []

for i in range(num_nombres):
    nombre = input(f"Introduce el nombre {i + 1}: ")
    nombres.append(nombre.strip())
nombres_ordenados = sorted(nombres)

print("Nombres ordenados alfabéticamente:")
for nombre in nombres_ordenados:
    print(nombre)

