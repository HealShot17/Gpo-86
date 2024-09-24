def fibonacci(n):
    # Caso base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Llamadas recursivas
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Ingrese el numero de la serie a buscar: "))

print(f"El numero {n} de la serie de fibonacci es {fibonacci(n)}")
