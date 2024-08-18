'''Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene
que evaluar la cadena y decir cuantas letras mayúsculas tiene.'''


Dato = input("Ingrese una cadena: ")

def contar_mayusculas(cadena):
    
    contador_mayusculas = 0
    for caracter in cadena:
        if caracter.isupper():
            contador_mayusculas += 1
    return contador_mayusculas

resultado = contar_mayusculas(Dato)


print(f"La cadena contiene {resultado} letras mayúsculas.")
