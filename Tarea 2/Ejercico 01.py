'''La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2
(primera parte), solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas
de 3 números o no sabemos cuantos números son. Escribir una función max_in_list() que
tome una lista de números y devuelva el mas grande.'''


Tamano = int(input("Ingrese la cantidad de elementos en la lista: "))
numeros = []

for i in range(Tamano):
    elemento = int(input(f"Ingrese el elemento {i+1} de la lista: "))
    numeros.append(elemento)

def max_in_list(lista):
    maximo = lista[0]
    for elemento in lista:
        if elemento > maximo:
            maximo = elemento
    
   
    return maximo


print("El número máximo en la lista es: ",max_in_list(numeros))

