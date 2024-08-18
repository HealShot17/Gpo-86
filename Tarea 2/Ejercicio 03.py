'''Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y
devuelva las palabras que tengan mas de n caracteres.'''

Tamano = int(input("Ingrese la cantidad de elementos en la lista: "))
n = int(input("Ingrese el número mínimo de caracteres: "))
ListaDePalabras = []
for i in range(Tamano):
    elemento = input(f"Ingrese el elemento {i+1} de la lista: ")
    ListaDePalabras.append(elemento)
def filtrar_palabras(lista_palabras, n):
    palabras_filtradas = []
    
    for palabra in lista_palabras:
        if len(palabra) > n:
            palabras_filtradas.append(palabra)
    
    return palabras_filtradas

resultado = filtrar_palabras(ListaDePalabras, n)


print(f"Las palabras con más de {n} caracteres son: {resultado}")
