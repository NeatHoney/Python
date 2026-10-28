"""
3. Muestra los títulos de las series que tengan una nota igual o superior a 9 y que
además tengan 3 o más géneros.
"""
from datos import series

print([j["titulo"] for j in series if j["nota"] >= 9 and len(j["generos"]) >= 3])
