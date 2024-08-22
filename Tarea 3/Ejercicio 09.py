'''Crear un programa que pida al usuario su nombre y luego lo imprima invertido.'''

Nombre =str(input("Ingrese el nombre por favor: "))
def inversa(cadena):
    cadena_alreves = cadena[::-1] 
    return cadena_alreves

print(f"El nombre al reves es {inversa(Nombre)}")  