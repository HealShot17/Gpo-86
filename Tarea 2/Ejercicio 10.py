'''Escriba una función es_bisiesto() que determine si un año determinado es un año
bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400'''


Dato = int(input("Ingrese un año: "))

def es_bisiesto(ano):

    if (ano % 4 == 0):
        if not (ano % 100 == 0):
            if (ano % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

 


if es_bisiesto(Dato):
    print(f"El año {Dato} es bisiesto.")
else:
    print(f"El año {Dato} no es bisiesto.")


