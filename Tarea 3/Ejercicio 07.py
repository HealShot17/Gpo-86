''' Desarrollar un programa que lea una lista de numeros separados por comas y luego imprima la suma
de esos numeros'''

entrada = input("Introduce una lista de números separados por comas por favor: ")
numeros_cadenas = entrada.split(',')
numeros = [int(num.strip()) for num in numeros_cadenas]
suma = sum(numeros)
print(f"La suma de los números es: {suma}")
