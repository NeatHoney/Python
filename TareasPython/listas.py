"""
1. Muestra en una sóla línea el nombre y el peso del pokémon con más peso.
"""

pokemons = [
{
"nombre": "Bulbasaur",
"generacion": 1,

"categoria": "Semilla",
"tipos": ["Planta", "Veneno"],
"peso_kg": 6.9,
"altura_m": 0.7
},
{
"nombre": "Charizard",
"generacion": 1,
"categoria": "Llama",
"tipos": ["Fuego", "Volador"],
"peso_kg": 90.5,
"altura_m": 1.7
},
{
"nombre": "Squirtle",
"generacion": 1,
"categoria": "Tortuguita",
"tipos": ["Agua"],
"peso_kg": 9.0,
"altura_m": 0.5
},
{
"nombre": "Pikachu",
"generacion": 1,
"categoria": "Ratón",
"tipos": ["Eléctrico"],
"peso_kg": 6.0,
"altura_m": 0.4
},
{
"nombre": "Jigglypuff",
"generacion": 1,
"categoria": "Globo",
"tipos": ["Normal", "Hada"],
"peso_kg": 5.5,
"altura_m": 0.5
},
{
"nombre": "Eevee",
"generacion": 1,
"categoria": "Evolución",
"tipos": ["Normal"],
"peso_kg": 6.5,
"altura_m": 0.3
},
{
"nombre": "Lucario",
"generacion": 4,

"categoria": "Aura",
"tipos": ["Lucha", "Acero"],
"peso_kg": 54.0,
"altura_m": 1.2
},
{
"nombre": "Gardevoir",
"generacion": 3,
"categoria": "Envolvente",
"tipos": ["Psíquico", "Hada"],
"peso_kg": 48.4,
"altura_m": 1.6
},
{
"nombre": "Greninja",
"generacion": 6,
"categoria": "Ninja",
"tipos": ["Agua", "Siniestro"],
"peso_kg": 40.0,
"altura_m": 1.5
}
]


maximo = 0.0
nombreMax = ""

for i in pokemons:
    if i["peso_kg"] > maximo:
        maximo = i["peso_kg"]
        nombreMax = i["nombre"]

print(f"El pokemón que pesa más es {nombreMax} y pesa {maximo} Kg")


"""
2. Muestra la media de altura de todos los pokémons.
"""
sumaAlt = 0.0

for i in pokemons:
    sumaAlt += i["altura_m"]

mediaAlt = sumaAlt / len(pokemons)

print(f"La media de altura de los pokemons es {mediaAlt:.2f} m")


"""
3. Muestra el nombre y la altura de todos los pokémons que midan menos que la media.
"""

for i in pokemons:
    if i["altura_m"] < mediaAlt:
        print(f"{i["nombre"]} mide {i["altura_m"]} m")

"""
4. Muestra el nombre y los tipos de los pokémons que sean de tipo agua.
"""
for i in pokemons:
    if "Agua" in i["tipos"]:
        print(f"{i["nombre"]} es de tipo {i["tipos"]}")

"""
5. Muestra los pokémons que tengan un tipo que acabe en “a”.
"""
for i in pokemons:
    for tipo in i["tipos"]:
        if tipo[-1] == "a":
            print(f"{i["nombre"]}, {i["tipos"]}")
            break

# Versión con endswith
for i in pokemons:
    for tipo in i["tipos"]:
        if tipo.endswith("a"):
            print(f"{i["nombre"]}, {i["tipos"]}")
            break


"""
6. Inserta al final de la lista un nuevo pokémon que tenga todos los campos con algún
valor con sentido (puedes inventártelos, pero que sean razonables).
"""
pokemons.append({
    "nombre": "Mewtwo",
    "generacion": 1,
    "categoria": "Genético",
    "tipos": ["Psíquico"],
    "peso_kg": 122.0,
    "altura_m": 2.0
})

"""
7. Elimina todos los pokémons de tipo normal.
Para eliminar de una lista tienes tres opciones:
lista.remove(x)    # elimina el elemento con ese valor (el primero que encuentre)
lista.pop(2)       # elimina el de la posición 2 (sin número, el último)
del lista[2]       # igual que pop, pero sin devolver el elemento
"""
for i in pokemons.copy():
    if "Normal" in i["tipos"]:
        pokemons.remove(i)

for i in pokemons:
    print(i["nombre"])





