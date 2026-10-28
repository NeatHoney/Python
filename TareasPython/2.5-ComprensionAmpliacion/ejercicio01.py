"""
1. Muestra una lista con los títulos de las series que sean de Animación.
"""
from datos import series

lista = [j["titulo"] for j in series if "Animación" in j["generos"]]
print(lista)
