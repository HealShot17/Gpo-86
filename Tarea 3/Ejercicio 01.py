"""Escribir un programa que solicite al usuario su nombre y edad, y luego imprima un mensaje de bienvenida
que incluya ambos.
"""
nombre=(input("Ingrese el nombre de la persona por favor: "))
edad=int(input(f"Ingrese la edad de {nombre} edad por favor: "))
print(f"Bienvenido {nombre}. \nTe felicitamos en este pais es complicado cumplir {edad} años ")