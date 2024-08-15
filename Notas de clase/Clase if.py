"""
#Estructuras de control
IF

if
    if x>5
            haz algo
        elif x>4
            haz algo mas
        elif x>5
            haz algo mas raro 
        else
            haz algo mas

While 
    while condicion True
           cidugi
           controldecondicion(sentinel/variablecentinela)
for
    for variable en objeto iterable:
           haz algo con la variable
    



"""
edad= int (input('Ingrese su edad: '))

if edad >= 18:
    print('Bienvenido a GitHub')
elif edad >= 16 and edad < 18:
    print("No puedes entrar hasta dentro de 2 años aprox ")
elif edad > 13 and edad < 16:
    print('No puedes entrar a este sitio')
else:   
    print("No deberias de tener acceso a internet")


x = 5
while x>0:
    print(x)
    x-=1

lista =["Hola","Mundo","como","estan"]

print(lista,"listasola")

for elemento in lista:
    print(elemento,"lista en for")

for elemento in lista:
    print(elemento)