"""
7. Crea una lista de cadenas de texto con la forma "Nombre (Equipo)" para cada
jugador. Muéstrala.
"""
from datos import jugadores

lista = [f"{j["nombre"]} ({j["equipo"]})" for j in jugadores]
print(lista)

# Las llaves indican que dentro va una variable 
