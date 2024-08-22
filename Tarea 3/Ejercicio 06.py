'''Escribir un programa que pida al usuario un archivo de texto y luego muestre el contenido del archivo
en la pantalla'''

nombre_archivo = input("Introduce el nombre del archivo de texto (con su extensión, por ejemplo, archivo.txt): ")


with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read()
    print("\nContenido del archivo:")
    print(contenido)
