def invertir_cadena(cadena):
    # Caso base: si la cadena está vacía o tiene un solo carácter
    if len(cadena) == 0:
        return cadena
    # Llamada recursiva: invierte el resto de la cadena y agrega el primer carácter al final
    else:
        return invertir_cadena(cadena[1:]) + cadena[0]

cadena = input("Ingrese una cadena: ")
print(f"El inverso de {cadena} es {invertir_cadena(cadena)}")
