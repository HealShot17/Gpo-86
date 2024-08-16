'''Escribir una funcion in list() que tome una lista de numeros y devuelva el mas grande'''
x= 0
n=int(input("¿Me podrias mencionar cuantos caracteres quieres ingresar? "))
x=n

while n>0:
    x = int(input("¿Cual es el numero que quieres ingresar?"))
    lista=[x]
    n-=1
    x-=1

print(lista)
    
