def potencia(a, b):
    # Caso base: cualquier número elevado a 0 es 1
    if b == 0:
        return 1
    # Llamada recursiva: multiplica la base por la potencia recursiva
    else:
        return a * potencia(a, b - 1)


a = int(input("Ingrese el numero a elevar: "))
b = int(input("Ingrese el numero de veces que se elva: "))

print(f"{a} elevado a {b} es {potencia(a,b)}")