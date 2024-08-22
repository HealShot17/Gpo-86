'''Hacer un programa que pida al usuario su fecha de nacimiento y luego imprima cuantos dıas han pasado
desde entonces.
'''
from datetime import datetime
fecha_nacimiento_str = input("Introduce tu fecha de nacimiento en el formato YYYY-MM-DD por favor: ")
fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d").date()
hoy = datetime.today().date()
diferencia = hoy - fecha_nacimiento
print(f"Han pasado {diferencia.days} días desde tu fecha de nacimiento.")
