import tkinter as tk
import requests
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Mostrar sugerencias de países
def mostrar_sugerencias(sugerencias):
    lista_sugerencias.delete(0, tk.END)
    for sugerencia in sugerencias:
        lista_sugerencias.insert(tk.END, sugerencia)
    lista_sugerencias.pack(fill=tk.BOTH, expand=True)

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

    # Limpiar las gráficas anteriores antes de agregar nuevas
    limpiar_graficas()

    # Generar las gráficas de idioma y población
    generar_grafico_pastel(idiomas)
    generar_grafico_lineas()
    lista_sugerencias.pack_forget() 

# Limpiar las gráficas anteriores
def limpiar_graficas():
    # Elimina todos los widgets dentro del frame de gráficas
    for widget in frame_graficos.winfo_children():
        widget.destroy()

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

# Generar el gráfico de distribución de idiomas
def generar_grafico_pastel(idiomas):
    idioma_lista = idiomas.split(", ")
    idioma_count = {idioma: 1 for idioma in idioma_lista}
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.pie(idioma_count.values(), labels=idioma_count.keys(), autopct='%1.1f%%')
    ax.set_title("Distribución de Idiomas")
    
    # Agregar la gráfica a la ventana de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame_graficos)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Generar el gráfico de evolución de la población
def generar_grafico_lineas():
    anos = [2000, 2020]
    poblacion = [10_000_000, 15_000_000]
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.plot(anos, poblacion, marker='o')
    ax.set_xlabel("Año")
    ax.set_ylabel("Población")
    ax.set_title("Evolución de la Población")
    
    # Agregar la gráfica a la ventana de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=frame_graficos)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

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
ventana.geometry("1000x800")  # Tamaño más amplio para caber las gráficas y el contenido
ventana.configure(bg="#F0F0F0")  # Fondo suave para la ventana

# Frame para las entradas de información (izquierda)
frame_izquierda = tk.Frame(ventana, bg="#F0F0F0")
frame_izquierda.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)

etiqueta = tk.Label(frame_izquierda, text="Introduce el nombre de un país:", font=("Arial", 14), bg="#F0F0F0")
etiqueta.pack(pady=10)

entrada_pais = tk.Entry(frame_izquierda, font=("Arial", 12))
entrada_pais.pack(pady=5)
entrada_pais.bind("<KeyRelease>", actualizar_sugerencias)

boton_buscar = tk.Button(frame_izquierda, text="Buscar", command=buscar_pais, font=("Arial", 12), bg="lightblue")
boton_buscar.pack(pady=10)

# Lista desplegable para sugerencias
lista_sugerencias = tk.Listbox(frame_izquierda, font=("Arial", 10), height=5)
lista_sugerencias.bind("<<ListboxSelect>>", seleccionar_sugerencia)

texto_resultado = tk.Text(frame_izquierda, wrap=tk.WORD, font=("Arial", 10), state=tk.DISABLED, height=10, width=50)
texto_resultado.pack(pady=10)

# Frame para las gráficas (derecha)
frame_graficos = tk.Frame(ventana, bg="#F0F0F0")
frame_graficos.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.BOTH, expand=True)

ventana.mainloop()
