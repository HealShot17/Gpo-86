import datetime
from abc import ABC, abstractmethod

# Función principal del gestor de tareas
def gestor_de_tareas():
    """
    Función principal para interactuar con el gestor de tareas.
    Ofrece un menú para agregar y mostrar tareas.
    """
    tareas = []
    while True:
        print("\n--- Menú de Gestor de Tareas ---")
        print("1. Agregar tarea simple")
        print("2. Agregar tarea con fecha límite")
        print("3. Mostrar todas las tareas")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_tarea_simple(tareas)
        elif opcion == "2":
            agregar_tarea_con_fecha(tareas)
        elif opcion == "3":
            mostrar_tareas(tareas)
        elif opcion == "4":
            print("Saliendo del gestor de tareas. ¡Hasta pronto!")
            break
        else:
            print("Intenta con una opcion valida, por favor.")

class Tarea(ABC):
    """
    Clase base abstracta que encapsula la información de una tarea genérica.
    """

    def __init__(self, nombre, etiquetas=None):
        """
        Inicializa una nueva tarea con un nombre y un conjunto opcional de etiquetas.

        Args:
            nombre (str): El nombre de la tarea.
            etiquetas (set, opcional): Un conjunto de etiquetas asociadas a la tarea. 
                                       Por defecto es un conjunto vacío.
        """
        self.nombre = nombre
        self.etiquetas = etiquetas if etiquetas is not None else set()

    @abstractmethod
    def mostrar_informacion(self):
        """
        Método abstracto para mostrar la información de la tarea.
        Debe ser implementado por las subclases.
        """
        pass


class TareaSimple(Tarea):
    """
    Clase para representar una tarea simple sin fecha límite.
    """

    def mostrar_informacion(self):
        """
        Muestra la información de la tarea simple.
        """
        print(f"Tarea: {self.nombre}")
        if self.etiquetas:
            print(f"Etiquetas: {', '.join(self.etiquetas)}")
        else:
            print("Sin etiquetas.")


class TareaConFechaLimite(Tarea):
    """
    Clase para representar una tarea con fecha límite.
    """

    def __init__(self, nombre, fecha_limite, etiquetas=None):
        """
        Inicializa una nueva tarea con fecha límite.

        Args:
            nombre (str): El nombre de la tarea.
            fecha_limite (tuple): La fecha límite en formato (YYYY, MM, DD).
            etiquetas (set, opcional): Un conjunto de etiquetas asociadas a la tarea. 
                                       Por defecto es un conjunto vacío.
        """
        super().__init__(nombre, etiquetas)
        self.fecha_limite = fecha_limite

    def mostrar_informacion(self):
        """
        Muestra la información de la tarea con fecha límite.
        """
        print(f"Tarea: {self.nombre}")
        print(f"Fecha límite: {self.fecha_limite[0]}-{self.fecha_limite[1]:02d}-{self.fecha_limite[2]:02d}")
        if self.etiquetas:
            print(f"Etiquetas: {', '.join(self.etiquetas)}")
        else:
            print("Sin etiquetas.")


# Función para agregar una tarea simple
def agregar_tarea_simple(tareas):
    """
    Solicita al usuario que ingrese los detalles de una tarea simple y la agrega a la lista de tareas.

    Args:
        tareas (list): Lista donde se almacenan las tareas.
    """
    nombre = input("Ingresa el nombre de la tarea: ")
    etiquetas = set(input("Ingresa las etiquetas separadas por comas: ").split(","))
    tarea = TareaSimple(nombre, etiquetas)
    tareas.append(tarea)
    print(f"Tarea '{nombre}' agregada con éxito.")

# Función para agregar una tarea con fecha límite
def agregar_tarea_con_fecha(tareas):
    """
    Solicita al usuario que ingrese los detalles de una tarea con fecha límite y la agrega a la lista de tareas.

    Args:
        tareas (list): Lista donde se almacenan las tareas.
    """
    nombre = input("Ingresa el nombre de la tarea: ")
    fecha_input = input("Ingresa la fecha límite (YYYY-MM-DD): ")
    fecha_limite = tuple(map(int, fecha_input.split("-")))
    etiquetas = set(input("Ingresa las etiquetas separadas por comas: ").split(","))
    tarea = TareaConFechaLimite(nombre, fecha_limite, etiquetas)
    tareas.append(tarea)
    print(f"Tarea '{nombre}' con fecha límite agregada con éxito.")

# Función para mostrar todas las tareas
def mostrar_tareas(tareas):
    """
    Muestra todas las tareas almacenadas en la lista.

    Args:
        tareas (list): Lista de tareas a mostrar.
    """
    if tareas:
        for tarea in tareas:
            tarea.mostrar_informacion()
            print("-" * 40)
    else:
        print("No hay tareas disponibles.")

# Ejecutar el programa
if __name__ == "__main__":
    gestor_de_tareas()

