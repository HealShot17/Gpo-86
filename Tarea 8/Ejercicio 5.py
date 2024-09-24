def suma_digitos(n):
    # Caso base: cuando el número es menor que 10, retorna el número (es el único dígito)
    if n < 10:
        return n
    # Llamada recursiva: suma el último dígito (n % 10) y llama de nuevo a la función con el resto (n // 10)
    else:
        return (n % 10) + suma_digitos(n // 10)

n = int(input("Ingrese el numero a sumar: "))
print(f"La suma de los numeros de {n} es {suma_digitos(n)}")