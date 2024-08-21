'''Crear un programa que pida al usuario dos numeros enteros y muestre su suma, resta, multiplicacion y
división.'''
N1=int(input("Ingrese el primer numero por favor: "))
N2=int(input("Ingrese el segundo numero por favor: "))
suma=(N1+N2)
resta=(N1-N2)
multiplicacion=(N1*N2)
division=(N1/N2)
division_inversa=(N2/N1)
print(f"La summa da {suma}\nLa resta da {resta} \nLa multiplicacion da {multiplicacion} \nLa division si tomamos en cuenta el primero como numeador y el segundo como divisor da {division} si no da como {division_inversa}")