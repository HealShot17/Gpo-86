"""Escribir un programa que solicite al usuario su nombre y edad, y luego imprima un mensaje de bienvenida
que incluya ambos.
"""
nombre=(input("Ingrese el nombre de la persona por favor: "))
nombre_titulado=nombre.title()
edad=int(input(f"Ingrese la edad de {nombre_titulado} edad por favor: "))
print(f"Bienvenido {nombre_titulado}. \nTe felicitamos en este pais es complicado cumplir {edad} años ")
