'''Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la
letra a.
También se puede hacer elegir al usuario la letra a buscar. (Un poco mas emocionante)'''

cantidad_nombres = int(input("Ingrese la cantidad de nombres de la lista por favor: "))
nombres = []
for i in range(cantidad_nombres):
    nombre = input(f"Ingrese el nombre {i+1} por favor: ")
    nombres.append(nombre) 
letra_buscar = input("Ingrese la letra con la cual buscar los nombres por favor: ")
def contar_nombres_por_letra(nombres, letra):
    letra = letra.lower()
    contador = 0
    for nombre in nombres:
        if nombre.lower().startswith(letra):
            contador += 1
    
    return contador


cantidad = contar_nombres_por_letra(nombres, letra_buscar)
    

print(f"Cantidad de nombres que comienzan con la letra '{letra_buscar}': {cantidad}")