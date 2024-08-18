'''Construir un pequeño programa que convierta números binarios en enteros.'''

numero_binario = input("Ingrese un número binario: ")
def convertir_binario_a_entero(binario):
    
    try:
        entero = int(binario, 2)
        return entero
    except ValueError:
        print("Error: La cadena ingresada no es un número binario válido.")
        return None
resultado = convertir_binario_a_entero(numero_binario)


if resultado is not None:
    print(f"El número binario {numero_binario} se convierte a {resultado} en decimal.")





