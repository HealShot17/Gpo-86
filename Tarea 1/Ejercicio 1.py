"""Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
(Es cierto que Python tiene la función max() incorporada, pero hacerla nosotros mismos es 
 muy buen ejercicio)"""

N1= int (input('Ingrese el primer número por favor: '))
N2= int (input('Ingrese el segundo número por favor: '))
N3= ("Ambos numeros son iguales")
def max(Dato1,Dato2):
    
    if Dato1==Dato2:
        return N3
    elif Dato1>Dato2:
        return Dato1
    else: 
        return Dato2

print("EL o los datos mayores es: ",max(N1,N2))