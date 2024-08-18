""" Escribir una función que tome un carácter y devuelva True si es una vocal,
de lo contrario devuelve False."""

lista = ['a','e','i','o','u']

Caracter = str(input("Ingrese un carcter: "))
def Num_Car(Caracter):
    if Caracter in lista:
        print("True")
    
    else:
        print("False")
Num_Car(Caracter)
