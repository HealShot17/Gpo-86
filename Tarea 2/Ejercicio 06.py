"""Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla."""


ano_actual = int(input("Ingrese el año en curso: "))
personas = []

def calcular_edad(ano_actual, ano_nacimiento):
    
    return ano_actual - ano_nacimiento


for i in range(3):
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
    ano_nacimiento = int(input(f"Ingrese el año de nacimiento de {nombre}: "))
    personas.append((nombre, ano_nacimiento))
print("\nEdad que cumplirán durante el año en curso:")
for nombre, ano_nacimiento in personas:
    edad = calcular_edad(ano_actual, ano_nacimiento)
    print(f"{nombre} cumplirá {edad} años en {ano_actual}.")



