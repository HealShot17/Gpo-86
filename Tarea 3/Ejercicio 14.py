'''Escribir un programa que genere y muestre la tabla de multiplicar de un numero introducido por el
usuario.'''

numero = int(input("Introduce el numero a multiplicar por favor: "))


print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
