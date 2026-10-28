"""
1. Muestra una lista solo con los nombres de todos los futbolistas.
"""
from datos import jugadores

lista = [j["nombre"] for j in jugadores]
print(lista)
