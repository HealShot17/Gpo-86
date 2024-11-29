import tkinter as tk
from tkinter import messagebox
import requests
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Mostrar sugerencias de países
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


# Buscar información de un país
def buscar_pais(pais=None):
    pais = pais or entrada_pais.get().strip()
    if not pais or not pais.isalpha():
        messagebox.showwarning("Advertencia", "Introduce un nombre válido de país.")
        return

    url = f"https://restcountries.com/v3.1/name/{pais}"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()

        if datos and isinstance(datos, list):
            mostrar_info_pais(datos[0])
            guardar_datos_en_excel(datos[0])
        else:
            messagebox.showerror("Error", f"No se encontró información para '{pais}'.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"No se pudo conectar a la API: {e}")


# Mostrar información del país
def mostrar_info_pais(info):
    nombre = info.get("translations", {}).get("spa", {}).get("common", "No disponible")
    capital = info.get("capital", ["No disponible"])[0]
    region = info.get("region", "No disponible")
    subregion = info.get("subregion", "No disponible")
    poblacion = info.get("population", 0)
    area = info.get("area", 0)
    idiomas = ", ".join(info.get("languages", {}).values()) if "languages" in info else "No disponible"
    moneda = ", ".join([moneda["name"] for moneda in info.get("currencies", {}).values()]) if "currencies" in info else "No disponible"

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

    # Mostrar gráficos en la ventana
    mostrar_grafico_barras(poblacion, area)
    mostrar_grafico_pastel(idiomas)
    lista_sugerencias.pack_forget()


# Guardar datos en Excel
def guardar_datos_en_excel(info):
    nombre = info.get("translations", {}).get("spa", {}).get("common", "No disponible")
    capital = info.get("capital", ["No disponible"])[0]
    region = info.get("region", "No disponible")
    subregion = info.get("subregion", "No disponible")
    poblacion = info.get("population", "No disponible")
    area = info.get("area", "No disponible")
    idiomas = ", ".join(info.get("languages", {}).values()) if "languages" in info else "No disponible"
    moneda = ", ".join([moneda["name"] for moneda in info.get("currencies", {}).values()]) if "currencies" in info else "No disponible"

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
    try:
        df.to_excel("informacion_pais.xlsx", index=False)
        messagebox.showinfo("Éxito", "Datos guardados correctamente en Excel.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")


# Limpiar gráficos existentes
def limpiar_graficos():
    for widget in contenedor_graficos.winfo_children():
        widget.destroy()


# Mostrar gráficos en la ventana
def mostrar_grafico_barras(poblacion, area):
    limpiar_graficos()
    figura = Figure(figsize=(4, 3), dpi=100)
    ax = figura.add_subplot(111)
    ax.bar(["Población", "Área"], [poblacion, area])
    ax.set_title("Población y Área del País")
    ax.set_ylabel("Valor")

    canvas = FigureCanvasTkAgg(figura, contenedor_graficos)
    canvas.get_tk_widget().pack()
    canvas.draw()


def mostrar_grafico_pastel(idiomas):
    limpiar_graficos()
    figura = Figure(figsize=(4, 3), dpi=100)
    ax = figura.add_subplot(111)
    idioma_lista = idiomas.split(", ")
    idioma_count = {idioma: 1 for idioma in idioma_lista}
    ax.pie(idioma_count.values(), labels=idioma_count.keys(), autopct='%1.1f%%')
    ax.set_title("Distribución de Idiomas")

    canvas = FigureCanvasTkAgg(figura, contenedor_graficos)
    canvas.get_tk_widget().pack()
    canvas.draw()


# Seleccionar una sugerencia
def seleccionar_sugerencia(event):
    try:
        seleccion = lista_sugerencias.get(lista_sugerencias.curselection())
        entrada_pais.delete(0, tk.END)
        entrada_pais.insert(0, seleccion)
        buscar_pais(seleccion)
    except tk.TclError:
        return


# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Buscador de Información de Países")
ventana.geometry("700x800")

etiqueta = tk.Label(ventana, text="Introduce el nombre de un país:", font=("Arial", 12))
etiqueta.pack(pady=10)

entrada_pais = tk.Entry(ventana, font=("Arial", 12))
entrada_pais.pack(pady=5)
entrada_pais.bind("<KeyRelease>", actualizar_sugerencias)

boton_buscar = tk.Button(ventana, text="Buscar", command=buscar_pais, font=("Arial", 12), bg="lightblue")
boton_buscar.pack(pady=10)

lista_sugerencias = tk.Listbox(ventana, font=("Arial", 10), height=5)
lista_sugerencias.bind("<<ListboxSelect>>", seleccionar_sugerencia)

texto_resultado = tk.Text(ventana, wrap=tk.WORD, font=("Arial", 10), state=tk.DISABLED, height=10, width=70)
texto_resultado.pack(pady=10)

contenedor_graficos = tk.Frame(ventana)
contenedor_graficos.pack(pady=10)

ventana.mainloop()
