'''Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.'''

Tamano = int(input("Ingrese la cantidad de elementos en la lista: "))
ListaDePalabras = []
for i in range(Tamano):
    elemento = input(f"Ingrese el elemento {i+1} de la lista: ")
    ListaDePalabras.append(elemento)

def mas_larga(lista_palabras):
    if not lista_palabras:  
        return None  
    
    palabra_larga = lista_palabras[0]
    
    for palabra in lista_palabras:
        if len(palabra) > len(palabra_larga):
            palabra_larga = palabra
    
    return palabra_larga

resultado = mas_larga(ListaDePalabras) 
if resultado:  
    print(f"La palabra más larga es: {resultado}")
else:
    print("La lista está vacía.")

