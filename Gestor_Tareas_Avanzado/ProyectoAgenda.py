import datetime
from abc import ABC, abstractmethod

# Función principal del gestor de tareas
def gestor_de_tareas():
    tareas = []
    while True:
        print("\n--- Menú de Gestor de Tareas ---")
        print("1. Agregar tarea simple")
        print("2. Agregar tarea con fecha límite")
        print("3. Mostrar todas las tareas")
        print("4. Eliminar una tarea")
        print("5. Marcar tarea como completada")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_tarea_simple(tareas)
        elif opcion == "2":
            agregar_tarea_con_fecha(tareas)
        elif opcion == "3":
            mostrar_tareas(tareas)
        elif opcion == "4":
            eliminar_tarea(tareas)
        elif opcion == "5":
            marcar_tarea_completada(tareas)
        elif opcion == "6":
            print("Saliendo del gestor de tareas. ¡Hasta pronto!")
            break
        else:
            print("Intenta con una opción válida, por favor.")


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
        self.completada = False  # Atributo para marcar si la tarea está completada

    def marcar_completada(self):
        """
        Marca la tarea como completada.
        """
        self.completada = True

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
        estado = "Completada" if self.completada else "Pendiente"
        print(f"Tarea: {self.nombre} - Estado: {estado}")
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
        estado = "Completada" if self.completada else "Pendiente"
        print(f"Tarea: {self.nombre} - Estado: {estado}")
        print(f"Fecha límite: {self.fecha_limite[0]}-{self.fecha_limite[1]:02d}-{self.fecha_limite[2]:02d}")
        if self.etiquetas:
            print(f"Etiquetas: {', '.join(self.etiquetas)}")
        else:
            print("Sin etiquetas.")


# Función para agregar una tarea simple
def agregar_tarea_simple(tareas):
    nombre = input("Ingresa el nombre de la tarea: ")
    etiquetas = set(input("Ingresa las etiquetas separadas por comas: ").split(","))
    tarea = TareaSimple(nombre, etiquetas)
    tareas.append(tarea)
    print(f"Tarea '{nombre}' agregada con éxito.")


# Función para agregar una tarea con fecha límite
def agregar_tarea_con_fecha(tareas):
    nombre = input("Ingresa el nombre de la tarea: ")
    fecha_input = input("Ingresa la fecha límite (YYYY-MM-DD): ")
    fecha_limite = tuple(map(int, fecha_input.split("-")))
    etiquetas = set(input("Ingresa las etiquetas separadas por comas: ").split(","))
    tarea = TareaConFechaLimite(nombre, fecha_limite, etiquetas)
    tareas.append(tarea)
    print(f"Tarea '{nombre}' con fecha límite agregada con éxito.")


# Función para mostrar todas las tareas
def mostrar_tareas(tareas):
    if tareas:
        for i, tarea in enumerate(tareas):
            print(f"{i}.")
            tarea.mostrar_informacion()
            print("-" * 40)
    else:
        print("No hay tareas disponibles.")


# Función para eliminar una tarea
def eliminar_tarea(tareas):
    if tareas:
        mostrar_tareas(tareas)
        try:
            indice = int(input("Ingresa el número de la tarea que deseas eliminar (empezando desde 0): "))
            if 0 <= indice < len(tareas):
                tarea_eliminada = tareas.pop(indice)
                print(f"Tarea '{tarea_eliminada.nombre}' eliminada con éxito.")
            else:
                print("Índice fuera de rango. Intenta nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número.")
    else:
        print("No hay tareas para eliminar.")


# Función para marcar una tarea como completada
def marcar_tarea_completada(tareas):
    mostrar_tareas(tareas)
    if tareas:
        try:
            indice = int(input("Ingresa el número de la tarea que deseas marcar como completada (empezando desde 0): "))
            if 0 <= indice < len(tareas):
                tareas[indice].marcar_completada()
                print(f"Tarea '{tareas[indice].nombre}' marcada como completada.")
            else:
                print("Índice de tarea inválido.")
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número.")
    else:
        print("No hay tareas disponibles.")

def pruebas_gestor_de_tareas():
    # Lista de tareas para probar
    tareas = []
    
    # Prueba agregar tarea simple
    print("\n=== Prueba 1: Agregar Tarea Simple ===")
    tarea_simple = TareaSimple("Comprar leche", {"compras", "urgente"})
    tareas.append(tarea_simple)
    assert len(tareas) == 1, "Error al agregar tarea simple"
    assert tareas[0].nombre == "Comprar leche", "Nombre incorrecto en tarea simple"
    assert "compras" in tareas[0].etiquetas, "Error en las etiquetas de la tarea simple"
    print("Prueba de agregar tarea simple: PASÓ")
    
    # Prueba agregar tarea con fecha límite
    print("\n=== Prueba 2: Agregar Tarea con Fecha Límite ===")
    tarea_fecha = TareaConFechaLimite("Entregar proyecto", (2024, 9, 15), {"trabajo"})
    tareas.append(tarea_fecha)
    assert len(tareas) == 2, "Error al agregar tarea con fecha límite"
    assert tareas[1].nombre == "Entregar proyecto", "Nombre incorrecto en tarea con fecha límite"
    assert tareas[1].fecha_limite == (2024, 9, 15), "Fecha límite incorrecta"
    print("Prueba de agregar tarea con fecha límite: PASÓ")

    # Prueba mostrar tareas
    print("\n=== Prueba 3: Mostrar Tareas ===")
    mostrar_tareas(tareas)  # Esto imprime las tareas, así que no requiere assert, solo revisión visual

    # Prueba eliminar tarea
    print("\n=== Prueba 4: Eliminar Tarea ===")
    eliminar_tarea(tareas)  # Se elimina la primera tarea (Comprar leche)
    assert len(tareas) == 1, "Error al eliminar tarea"
    assert tareas[0].nombre == "Entregar proyecto", "Error al eliminar la tarea correcta"
    print("Prueba de eliminar tarea: PASÓ")

    # Prueba marcar tarea como completada
    print("\n=== Prueba 5: Marcar Tarea Como Completada ===")
    tareas[0].marcar_completada()  # Marca como completada la tarea restante
    assert tareas[0].completada is True, "Error al marcar tarea como completada"
    print("Prueba de marcar tarea como completada: PASÓ")

    print("\n=== Todas las pruebas han pasado ===")


# Ejecutar el programa
if __name__ == "__main__":
    pruebas_gestor_de_tareas()
    gestor_de_tareas()
