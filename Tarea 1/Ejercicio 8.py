"""Definir una función superposicion() que tome dos listas y devuelva True si tienen 
al menos un miembro en común o devuelva True si tiene al menos un miembro en común o devuelva 
False de lo contrario. Escribir la función usando el bucle for anidado."""


lista1=[str(input('Primer caracter por favor ')),str(input('Segundo caracter por favor ')),str(input('Tercer caracter por favor ')),str(input('Cuarto caracter por favor '))]
lista2=[str(input('Primer caracter por favor ')),str(input('Segundo caracter por favor ')),str(input('Tercer caracter por favor ')),str(input('Cuarto caracter por favor '))]


if lista1 in lista2:
    print("True")
    
else:
    print("False")

'''
n= elemento
for elemento in lista:
    print(elemento,"lista en for")
'''