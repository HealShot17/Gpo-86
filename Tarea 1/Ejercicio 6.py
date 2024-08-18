"""Definir una función inversa() que calcule la inversión de una cadena. 
Por ejemplo,la cadena "estoy probando" deberia devolver la cadena "odnaborp yotse"""""


cadena_original =str(input("Ingrese la cadena de caracteres por favor: "))
def inversa(cadena):
    cadena_alreves = cadena[::-1] # Intento de rebanado-1 para invertir la cadena.
    return cadena_alreves

print(inversa(cadena_original))  


    
