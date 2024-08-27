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
#listaUnos =[[[1]*100]*100]*    #100 Cubo de datos
#print(listaUnos)    

tex = input("Ingrese un texto: ")
print(tex[::-1])


"""
class Prototipo:
        def __init__(self):
            print("Hola")
        def __str__(self):
            return "PrototipoX"


H = Prototipo()
print(H)
print(H.lorem().split(" "))     
print(len(H.lorem().split(" ")))   
print(tex.split(" "))
"""
tex1 = "Hola"
tex2 = "Mundo"
var1 = 20
#Contatenar
print(tex1+tex2+str(var1))

with open("dataser_modificado.vsv,r") as CSV:
    for line in CSV.readline():
        print(line)
