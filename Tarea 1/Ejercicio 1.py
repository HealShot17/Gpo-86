"""Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
(Es cierto que Python tiene la función max() incorporada, pero hacerla nosotros mismos es 
 muy buen ejercicio)"""

N1= int (input('Ingrese el primer número por favor: '))
N2= int (input('Ingrese el segundo número por favor: '))

if N1==N2:
    print("Los numeros son iguales")
elif N1>N2:
    print("El numero mas grande es el primero ")
else: 
    print("el número más grande es el segundo")