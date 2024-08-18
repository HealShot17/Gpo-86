"""Definir una función max de tres() que tome tres numeros como argumentos y devuelva el mayor de ellos"""

N1= int (input('Ingrese el primer número por favor: '))
N2= int (input('Ingrese el segundo número por favor: '))
N3= int (input('Ingrese el tercer número por favor: '))

def max_de_tres(N1,N2,N3):
    
    if N1==N2 and N1==N3:
        print("Todos los numeros son iguales")
    elif N2==N1 and N2>N3:
        print("Los numeros mas grandes son el primero y el segundo")
    elif N2==N3 and N2>N1:
        print("Los numeros mas grandes son el segundo y el tercero ")
    elif N1==N3 and N1>N2:
        print("Los numeros mas grandes son el pri2mero y el tercero ")
    elif N1>N3 and N1>N2:
        print("El numero mas grande es el primero ")
    elif N2>N1 and N2>N3:
        print("El primero mas grande es el segundo ")
    else: 
        print("el número más grande es el tercero")
max_de_tres(N1,N2,N3)