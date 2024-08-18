'''Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a"
tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra.'''




palabra = input("Ingrese una palabra: ")

def contar_vocales(palabra):
    conteo_vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    palabra = palabra.lower()
    for letra in palabra:
        if letra in conteo_vocales:
            conteo_vocales[letra] += 1
    
    return conteo_vocales

conteo = contar_vocales(palabra)
print("\nConteo de vocales en la palabra:")
for vocal, cantidad in conteo.items():
    print(f"Vocal '{vocal}': {cantidad}")


