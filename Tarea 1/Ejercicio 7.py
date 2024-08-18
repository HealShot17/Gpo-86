"""Definir una función es palindromo() que reconoce palíndromos (es decir, palabras que tieneen 
el mismo aspecto escritas invertidas). Ejemolo: es palindromo ("radar") tendría que devolver True"""

entrada_usuario = str(input("Ingrese una palabra: "))
def es_palindromo(palabra):
    palabra = palabra.lower()
    palabra_reversa = palabra[::-1]
   
    return palabra == palabra_reversa




resultado = es_palindromo(entrada_usuario)

if resultado:
    print(f"La palabra '{entrada_usuario}' es un palíndromo.")
else:
    print(f"La palabra '{entrada_usuario}' no es un palíndromo.")
