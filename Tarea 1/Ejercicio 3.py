"""Definir una función que calcule la longitud de una lista o una cadena dada. 
(Es cierto que Python tiene la funcion len() incorporada, para escribirla por 
nosotros mismos resulta muy buen ejercicio)."""

elemento= str(input("Ingrese la cande que requiere: "))
Contador = 0
def longitud(elemento):
    
    for dato in elemento:
        Contador = Contador + 1
    return Contador






print(longitud(elemento))  
