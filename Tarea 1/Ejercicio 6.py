"""Definir una función inversa() que calcule la inversión de una cadena. 
Por ejemplo,la cadena "estoy probando" deberia devolver la cadena "odnaborp yotse"""""

def inversa(cadena):
    cadena_alreves = cadena[::-1] # Intento de rebanado-1 para invertir la cadena.
    return cadena_alreves

# El uso de la funcion
cadena_original =str(input("Ingrese la cadena de caracteres por favor: "))
cadena_alreves = inversa(cadena_original)


print(cadena_alreves)  


    
