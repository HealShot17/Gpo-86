import tkinter as tk
import requests
from tkinter import messagebox



# Función para mostrar las sugerencias en la lista desplegable
def mostrar_sugerencias(sugerencias):
    lista_sugerencias.delete(0, tk.END)  # Limpiar lista antes de agregar nuevas sugerencias
    for sugerencia in sugerencias:
        lista_sugerencias.insert(tk.END, sugerencia)
    lista_sugerencias.pack()  # Mostrar la lista de sugerencias
    
# Función para obtener sugerencias de países en español
def actualizar_sugerencias(event):
    pais = entrada_pais.get().strip()
    if len(pais) < 2:  # Esperar hasta que el usuario haya escrito al menos 2 letras
        lista_sugerencias.pack_forget()  # Ocultar la lista si hay menos de 2 caracteres
        return
    
    url = f"https://restcountries.com/v3.1/name/{pais}"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()
        
        # Filtrar las sugerencias en español
        sugerencias = [
            dato["translations"]["spa"]["common"]
            for dato in datos
            if "translations" in dato and "spa" in dato["translations"]
        ]
        mostrar_sugerencias(sugerencias)
    except requests.exceptions.RequestException:
        lista_sugerencias.pack_forget()  # Ocultar lista en caso de error

# Función para obtener información detallada de un país en español
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
        else:
            messagebox.showerror("Error", f"No se encontró información para '{pais}'.")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"No se pudo conectar a la API. {e}")

# Función para mostrar la información del país en español en la interfaz
def mostrar_info_pais(info):
    nombre = info.get("translations", {}).get("spa", {}).get("common", "No disponible")
    capital = info.get("capital", ["No disponible"])[0]
    region = info.get("region", "No disponible")
    subregion = info.get("subregion", "No disponible")
    poblacion = info.get("population", "No disponible")
    area = info.get("area", "No disponible")
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
    lista_sugerencias.pack_forget()  # Ocultar lista de sugerencias una vez seleccionado

# Función para seleccionar un país de las sugerencias
def seleccionar_sugerencia(event):
    seleccion = lista_sugerencias.get(lista_sugerencias.curselection())
    entrada_pais.delete(0, tk.END)
    entrada_pais.insert(0, seleccion)
    buscar_pais(seleccion)

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Buscador de Información de Países")
ventana.geometry("500x400")

etiqueta = tk.Label(ventana, text="Introduce el nombre de un país:", font=("Arial", 12))
etiqueta.pack(pady=10)

entrada_pais = tk.Entry(ventana, font=("Arial", 12))
entrada_pais.pack(pady=5)
entrada_pais.bind("<KeyRelease>", actualizar_sugerencias)  # Detectar cambios en la entrada

boton_buscar = tk.Button(ventana, text="Buscar", command=buscar_pais, font=("Arial", 12), bg="lightblue")
boton_buscar.pack(pady=10)

# Lista desplegable para sugerencias
lista_sugerencias = tk.Listbox(ventana, font=("Arial", 10), height=5)
lista_sugerencias.bind("<<ListboxSelect>>", seleccionar_sugerencia)

texto_resultado = tk.Text(ventana, wrap=tk.WORD, font=("Arial", 10), state=tk.DISABLED, height=10, width=50)
texto_resultado.pack(pady=10)

ventana.mainloop()
