print ('Hola mundo')
print("Prueba")
lista=[1,2,3]
n=len(lista)
print(n)
y="Hola"

"""listas
    lista1 = list()
    lista2 = []
for i in range (2):
    lista1.append(input(f"Ingrese el lugar" {i+1}))
lista1.remove("6")
print(lista1.index("luis"))

a = int(input("Ingrese las filas: "))
b = int(input("Ingrese las columnas: "))

for i in range(a):
    listTemp =[]
    for j in range(b):
        listTemp.append(int(input(f"Ingrese el elemento de la fila {i+1} y la columnas {j+1}: ")))
    lista2.append(listTemp)

print()"""

#listaUnos =[1]*100             #Vector de datos
#listaUnos =[[1]*100]*100       #Lista de datos
listaUnos =[[[1]*100]*100]*    #100 Cubo de datos
print(listaUnos)      