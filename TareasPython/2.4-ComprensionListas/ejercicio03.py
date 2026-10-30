"""
3. Muestra una lista con los nombres de los jugadores que pertenecen al "FC
Barcelona".
"""
from datos import jugadores

lista = [j["nombre"] for j in jugadores if "FC Barcelona" in j["equipo"]]
print(lista)

