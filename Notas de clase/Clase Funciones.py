"""
Funciones 
"""


#Funcion global
def imprimirNombre(nom):
    print("Hola Mr. "+str(nom))
    return


    



variable = lambda x,y: x**y
suma = lambda x,y: x+y
resta= lambda x,y: x-y
print(variable(2,10))



def abrirArchivo(ruta,nombre):
    try:
        with open (ruta+nombre,"x+") as fichero:
        print("Hola",file=fichero)


ruta = input("Ingrese la ruta del archivo")
nombre = input("Ingrese el nombre del archivo")


if abrirArchivo(ruta,nombre) == True:
    print("El archivo se abrio con exito")
else:
    print("El archivo no se pudo abrir")


def imprimirLista(lista,n=1,pow=1,sqr=False):
    for i in lista:
        if sqr and pow == 1 :
            sq = 2
            print(i**pow*n)
        else:
        print(i*n)

lista = range(7)

imprimirLista(lista)
imprimirLista(lista,7)
