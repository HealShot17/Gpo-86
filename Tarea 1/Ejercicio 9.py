""" Definir una funcion generar n caracteres() que tome un entero n y
devuelva el carácter multiplicado por n.
Por ejemplo generar n caracteres(5,"x") deberia debolber "xxxxx"."""

n = int(input("Ingrese el número de repeticiones: "))

caracter = input("Ingrese el carácter a repetir: ")

def generar_n_caracteres(n, caracter):
    return caracter * n



resultado = generar_n_caracteres(n, caracter)

print(f"La cadena generada es: {resultado}")
