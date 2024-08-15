"""Definir una función que calcule la longitud de una lista o una cadena dada. 
(Es cierto que Python tiene la funcion len() incorporada, para escribirla por 
nosotros mismos resulta muy buen ejercicio)."""

Datos =[(input("Ingrese el primer dato por favor:")),
          (input("Ingrese el segundo dato por favor:")),
          (input("Ingrese el tercer dato por favor:")),
          (input("Ingrese el cuarto dato por favor:"))]
x = 0   #x es la cantidad de la suma

for elemento in Datos:
    x= x+1

print("La cantidad de valores en la lista es")
print(x)