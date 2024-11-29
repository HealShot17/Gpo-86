import tkinter as tk
import requests
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox


# Mostrar sugerencias de paises
def mostrar_sugerencias(sugerencias):
    lista_sugerencias.delete(0, tk.END) 
    for sugerencia in sugerencias:
        lista_sugerencias.insert(tk.END, sugerencia)
    lista_sugerencias.pack()

# Obtener sugerencias en español
def actualizar_sugerencias(event):
    pais = entrada_pais.get().strip()
    if len(pais) < 2:
        lista_sugerencias.pack_forget()
        return
    
    url = f"https://restcountries.com/v3.1/name/{pais}"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()
        
        sugerencias = [
            dato["translations"]["spa"]["common"]
            for dato in datos
            if "translations" in dato and "spa" in dato["translations"]
        ]
        mostrar_sugerencias(sugerencias)
    except requests.exceptions.RequestException:
        lista_sugerencias.pack_forget()

# Información detallada de un país
def buscar_pais(pais=None):
    pais = pais or entrada_pais.get().strip()
    if not pais:
        messagebox.showwarning("Advertencia", "Por favor, selecciona o introduce el nombre de un país.")
        return
    
    url = f"https://restcountries.com/v3.1/translation/{pais}"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()
        if datos:
            mostrar_info_pais(datos[0])
            guardar_datos_en_excel(datos[0])
        else:
            messagebox.showerror("Error", f"No se encontró información para '{pais}'.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"No se pudo conectar a la API. {e}")

# Mostrar la información
def mostrar_info_pais(info):
    nombre = info.get("translations", {}).get("spa", {}).get("common", "No disponible")
    capital = info.get("capital", ["No disponible"])[0]
    region = info.get("region", "No disponible")
    subregion = info.get("subregion", "No disponible")
    poblacion = info.get("population", 0)
    area = info.get("area", 0)
    idiomas = ", ".join(info.get("languages", {}).values()) if "languages" in info else "No disponible"
    moneda = ", ".join([moneda["name"] for moneda in info.get("currencies", {}).values()]) if "currencies" in info else "No disponible"

    es_valido, mensaje = validar_datos(poblacion, area)
    if not es_valido:
        messagebox.showerror("Error de validación", mensaje)
        return

    # Mostrar la información
    resultado = f"""
    Nombre: {nombre}
    Capital: {capital}
    Región: {region}
    Subregión: {subregion}
    Población: {poblacion}
    Área: {area} km²
    Idiomas: {idiomas}
    Moneda: {moneda}
    """
    texto_resultado.config(state=tk.NORMAL)
    texto_resultado.delete(1.0, tk.END)
    texto_resultado.insert(tk.END, resultado)
    texto_resultado.config(state=tk.DISABLED)

    # Generar las gráficas de cada pais
    generar_grafico_barras(poblacion, area)
    generar_grafico_pastel(idiomas)
    generar_grafico_lineas()
    generar_grafico_dispersion([poblacion], [area])
    lista_sugerencias.pack_forget() 

# ALmacenar los datos en Excel
def guardar_datos_en_excel(info):
    nombre = info.get("translations", {}).get("spa", {}).get("common", "No disponible")
    capital = info.get("capital", ["No disponible"])[0]
    region = info.get("region", "No disponible")
    subregion = info.get("subregion", "No disponible")
    poblacion = info.get("population", "No disponible")
    area = info.get("area", "No disponible")
    idiomas = ", ".join(info.get("languages", {}).values()) if "languages" in info else "No disponible"
    moneda = ", ".join([moneda["name"] for moneda in info.get("currencies", {}).values()]) if "currencies" in info else "No disponible"

    # Crear un DataFrame con los datos
    datos = {
        "Nombre": [nombre],
        "Capital": [capital],
        "Región": [region],
        "Subregión": [subregion],
        "Población": [poblacion],
        "Área (km²)": [area],
        "Idiomas": [idiomas],
        "Moneda": [moneda]
    }
    
    df = pd.DataFrame(datos)
    
    # Guardar en un archivo
    df.to_excel("informacion_pais.xlsx", index=False)
    messagebox.showinfo("Éxito", "Los datos se han guardado correctamente en el archivo Excel.")

# Generar los gráficos
def generar_grafico_barras(poblacion, area):
    plt.bar(["Población", "Área"], [poblacion, area])
    plt.ylabel("Valor")
    plt.title("Población y Área del País")
    plt.show()

def generar_grafico_pastel(idiomas):
    idioma_lista = idiomas.split(", ")
    idioma_count = {idioma: 1 for idioma in idioma_lista}
    plt.pie(idioma_count.values(), labels=idioma_count.keys(), autopct='%1.1f%%')
    plt.title("Distribución de Idiomas")
    plt.show()

def generar_grafico_lineas():
    anos = [2000, 2020]
    poblacion = [10_000_000, 15_000_000]
    plt.plot(anos, poblacion, marker='o')
    plt.xlabel("Año")
    plt.ylabel("Población")
    plt.title("Evolución de la Población")
    plt.show()

def generar_grafico_dispersion(poblaciones, areas):
    plt.scatter(areas, poblaciones)
    plt.xlabel("Área (km²)")
    plt.ylabel("Población")
    plt.title("Población vs. Área")
    plt.show()

# Validación de datos
def validar_datos(poblacion, area):
    if not isinstance(poblacion, (int, float)) or poblacion <= 0:
        return False, "Población no válida"
    if not isinstance(area, (int, float)) or area <= 0:
        return False, "Área no válida"
    return True, ""

# Seleccionar un país de las sugerencias
def seleccionar_sugerencia(event):
    seleccion = lista_sugerencias.get(lista_sugerencias.curselection())
    entrada_pais.delete(0, tk.END)
    entrada_pais.insert(0, seleccion)
    buscar_pais(seleccion)

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Buscador de Información de Países")
ventana.geometry("500x400")

etiqueta = tk.Label(ventana, text="Introduce el nombre de un país:", font=("Arial", 12))
etiqueta.pack(pady=10)

entrada_pais = tk.Entry(ventana, font=("Arial", 12))
entrada_pais.pack(pady=5)
entrada_pais.bind("<KeyRelease>", actualizar_sugerencias)

boton_buscar = tk.Button(ventana, text="Buscar", command=buscar_pais, font=("Arial", 12), bg="lightblue")
boton_buscar.pack(pady=10)

# Lista desplegable para sugerencias
lista_sugerencias = tk.Listbox(ventana, font=("Arial", 10), height=5)
lista_sugerencias.bind("<<ListboxSelect>>", seleccionar_sugerencia)

texto_resultado = tk.Text(ventana, wrap=tk.WORD, font=("Arial", 10), state=tk.DISABLED, height=10, width=50)
texto_resultado.pack(pady=10)

ventana.mainloop()
