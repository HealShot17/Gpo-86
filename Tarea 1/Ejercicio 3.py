"""Definir una función que calcule la longitud de una lista o una cadena dada. 
(Es cierto que Python tiene la funcion len() incorporada, para escribirla por 
nosotros mismos resulta muy buen ejercicio)."""
cadena_usuario = input("Ingrese una cadena: ")
def calcular_longitud(elemento):
    contador = 0
    for _ in elemento:
        contador += 1
    return contador





print("La longitud de la cadena ingresada es: ",calcular_longitud(cadena_usuario))






 
