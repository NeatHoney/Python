"""
2. Muestra los títulos de las series que sean de Fantasía o Misterio.
"""
from datos import series

print([j["titulo"] for j in series if "Fantasía" in j["generos"] or "Misterio" in j["generos"]])
