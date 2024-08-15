''' 
Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente
todos los números de una lista. Por ejemplo: sum([1,2,3,4]) deberia devolver 10 y multip ([1,2,3,4]) 
deberia devolver 24.
'''

Numeros =[int(input("Ingrese el primer número por favor:")),
          int(input("Ingrese el segundo número por favor:")),
          int(input("Ingrese el tercer número por favor:")),
          int(input("Ingrese el cuarto número por favor:"))]
x = 0   #x es la cantidad de la suma
y = 1   #y es la cantidad de la multiplicacion
for elemento in Numeros:
    x += elemento 
    y *= elemento 

print( x,y)

