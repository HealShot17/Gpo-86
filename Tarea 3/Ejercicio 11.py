''' Desarrollar un programa que solicite al usuario su peso y altura, y calcule su ındice de masa corporal
(IMC).'''

peso = float(input("Ingrese el peso por favor: "))
altura = float(input("Ingrese su altura por favor: "))
imc = peso/(altura**2)

print(f"Su imc es: {imc}")