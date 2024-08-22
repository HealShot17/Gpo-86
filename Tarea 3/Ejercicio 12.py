'''Hacer un programa que genere un numero aleatorio entre 1 y 100, y pida al usuario adivinarlo, dando
pistas si el numero es mayor o menor.'''

import random

numero_secreto = random.randint(1, 100)
adivinanza = None
contador_de_intentos = 0

while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número entre 1 y 100: "))
    contador_de_intentos += 1
    
    if adivinanza < numero_secreto:
        print("El número es mayor. Intentalo de nuevo.")
    elif adivinanza > numero_secreto:
        print("El número es menor. Intentloa de nuevo.")
    else:
        print(f"¡Felicidades! Has adivinado despues de {contador_de_intentos}") 
        print(f"¿eres adivino? o ya sabias que era {numero_secreto}")

