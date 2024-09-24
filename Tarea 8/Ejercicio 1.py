def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
    


n = int(input("Ingrese el numero: "))

print(f"El factorial de {n} es {factorial(n)}")
