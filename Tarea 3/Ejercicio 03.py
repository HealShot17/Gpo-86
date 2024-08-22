'''Desarrollar un script que solicite una frase y luego la imprima en mayusculas, minusculas y con la
primera letra de cada palabra en mayuscula.
'''

Dato = input("Introduce una frase por favor: ")
mayusculas = Dato.upper()
minusculas = Dato.lower()
titulada = Dato.title()
print(f"Frase en mayúsculas: {mayusculas} \nFrase en minusculas: {minusculas} \nFrase bien escrota: {titulada}")

