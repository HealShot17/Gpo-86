''' Desarrollar un programa que solicite al usuario su peso y altura, y calcule su ındice de masa corporal
(IMC).'''

peso = float(input("Ingrese el peso por favor en kilos: "))
altura = float(input("Ingrese su altura por favor en metros: "))
imc = peso/(altura**2)

print(f"Su imc es: {imc:.2f}")
if imc <= 15:
    print("comele papito tas con delgades muy severa")
elif imc < 16:
    print ("Comele papito traes delgadez severa")
elif imc < 18.5:
    print ("Comele papito tras delgado")
elif imc < 25:
    print("Sigue asi estas en un peso saludable")
elif imc < 30:
    print("Intenta comer mejor estas con algo de sobrepeso")
elif imc < 35:
    print("Intenta comer mejor y empezar con ejercicio estas obesidad moderada")
elif imc < 40:
    print("Intente comer mejor y empezar con ejercicio sin impactos")
else:
    print("Intenta empezar con algo de ejercicio y comer mejor presentas obesidad muy severa")