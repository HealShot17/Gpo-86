# 1 Algoritmo Secuencial para calcular la suma de una lista fija
lista = [3, 5, 7, 9]

# Inicializar la suma en 0
suma_total = 0

# Recorrer cada elemento de la lista y sumar su valor
for elemento in lista:
    suma_total += elemento

# Mostrar el resultado
print("La suma total es:", suma_total)


# 2 Función recursiva para calcular el factorial
def factorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:
        return n * factorial(n - 1)  # Llamada recursiva

# Calcular el factorial de 6
resultado = factorial(6)

# Mostrar el resultado
print("El factorial de 6 es:", resultado)


# 3 Implementación de Quicksort
def quicksort(arr):
    if len(arr) <= 1:  # Caso base: lista vacía o de un solo elemento
        return arr
    else:
        pivot = arr[0]  # Elegimos el primer elemento como pivote
        menores = [x for x in arr[1:] if x <= pivot]  # Elementos menores o iguales al pivote
        mayores = [x for x in arr[1:] if x > pivot]   # Elementos mayores al pivote
        return quicksort(menores) + [pivot] + quicksort(mayores)  # Llamadas recursivas

# Lista fija
lista = [10, 7, 8, 9, 1, 5]

# Ordenar la lista usando Quicksort
lista_ordenada = quicksort(lista)

# Calcular la suma de los elementos de la lista ordenada
suma_total = sum(lista_ordenada)

# Mostrar resultados
print("Lista ordenada:", lista_ordenada)
print("La suma de los elementos de la lista ordenada es:", suma_total)


# 4 Implementación de la búsqueda binaria
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2  # Calcular el índice medio
        if lista[medio] == objetivo:  # Verificar si el elemento medio es el objetivo
            return medio
        elif lista[medio] < objetivo:  # Si el objetivo está en la mitad derecha
            inicio = medio + 1
        else:  # Si el objetivo está en la mitad izquierda
            fin = medio - 1

    return -1  # El elemento no está en la lista

# 5 Lista ordenada y objetivo
lista = [1, 5, 7, 8, 9, 10]
objetivo = 8

# Realizar la búsqueda binaria
indice = busqueda_binaria(lista, objetivo)

# Mostrar el resultado
if indice != -1:
    print(f"El número {objetivo} está en la posición (índice): {indice}")
else:
    print(f"El número {objetivo} no se encuentra en la lista.")
    
    
# 6 Definición de la clase FiguraGeometrica
class FiguraGeometrica:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area_triangulo(self):
        # Fórmula para el área de un triángulo: (base * altura) / 2
        return (self.base * self.altura) / 2

# Crear una instancia de FiguraGeometrica con base=10 y altura=5
figura = FiguraGeometrica(base=10, altura=5)

# Calcular el área del triángulo
area = figura.area_triangulo()

# Mostrar el resultado
print(f"El área del triángulo con base={figura.base} y altura={figura.altura} es: {area}")



# 7 Crear y escribir en el archivo datos.txt
with open("datos.txt", "w") as archivo:
    archivo.write("3\n")
    archivo.write("4\n")
    archivo.write("5\n")

# Leer el archivo y calcular la suma de los números
suma = 0
with open("datos.txt", "r") as archivo:
    for linea in archivo:
        suma += int(linea.strip())  # Convertir cada línea a entero y sumar

# Mostrar el resultado
print(f"La suma de los números en el archivo es: {suma}")


# 8 Programa para usar el API
import requests

# URL de la API
url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    # Realizar una solicitud GET a la API
    response = requests.get(url)
    
    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        data = response.json()  # Convertir la respuesta en un diccionario
        post_id = data.get("id", 0)  # Obtener el valor del campo "id"
        resultado = post_id * 100  # Multiplicar el valor por 100
        print(f"El resultado de multiplicar el 'id' por 100 es: {resultado}")
    else:
        print(f"Error en la solicitud: Código {response.status_code}")
except Exception as e:
    print(f"Se produjo un error: {e}")

# 9 Estadistica Media 
# Lista fija
numeros = [2, 4, 4, 4, 5, 5, 7]

# Calcular la media
media = sum(numeros) / len(numeros)

# Mostrar el resultado
print(f"La media de la lista es: {media:.2f}")



# 10 Consulta en una lista 
# Lista de números
numeros = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# Usar un diccionario para contar las frecuencias
frecuencias = {}

# Contar las ocurrencias de cada número
for num in numeros:
    if num in frecuencias:
        frecuencias[num] += 1
    else:
        frecuencias[num] = 1

# Mostrar las frecuencias
for num, freq in frecuencias.items():
    print(f"El número {num} aparece {freq} veces.")

# Sumar las frecuencias
suma_frecuencias = sum(frecuencias.values())

# Mostrar la suma total de las frecuencias
print(f"La suma total de las frecuencias es: {suma_frecuencias}")




#Programa tkt
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Suma de Números")

# Función para realizar la suma y mostrar el resultado
def sumar():
    suma = 45 + 55
    etiqueta_resultado.config(text=f"Resultado: {suma}")

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="Resultado: ", font=("Arial", 14))
etiqueta_resultado.pack(pady=20)

# Botón para ejecutar la suma
boton_sumar = tk.Button(ventana, text="Sumar 45 + 55", command=sumar, font=("Arial", 12))
boton_sumar.pack()

# Ejecutar la aplicación
ventana.mainloop()
