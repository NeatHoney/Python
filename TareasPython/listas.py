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



personajes_frieren = [
{
"nombre": "Frieren",
"raza": "Elfo",
"clase": "Mago",
"edad": 1000,
"afiliacion": ["Grupo de los Cuatro Héroes", "Grupo de Frieren"]
},
{
"nombre": "Himmel",
"raza": "Humano",
"clase": "Héroe",
"edad": 76,
"afiliacion": ["Grupo de los Cuatro Héroes"]
},
{
"nombre": "Fern",
"raza": "Humano",
"clase": "Mago",
"edad": 19,
"afiliacion": ["Grupo de Frieren", "Magos de Primera Clase"]
},

{
"nombre": "Stark",
"raza": "Humano",
"clase": "Guerrero",
"edad": 18,
"afiliacion": ["Grupo de Frieren"]
},
{
"nombre": "Heiter",
"raza": "Humano",
"clase": "Sacerdote",
"edad": 100,
"afiliacion": ["Grupo de los Cuatro Héroes"]
},
{
"nombre": "Eisen",
"raza": "Enano",
"clase": "Guerrero",
"edad": 120,
"afiliacion": ["Grupo de los Cuatro Héroes"]
},
{
"nombre": "Sein",
"raza": "Humano",
"clase": "Sacerdote",
"edad": 28,
"afiliacion": ["Grupo de Frieren"]
},
{
"nombre": "Ubel",
"raza": "Humano",
"clase": "Mago",
"edad": 19,
"afiliacion": ["Magos de Primera Clase"]
},
{
"nombre": "Aura la Guillotina",
"raza": "Demonio",
"clase": "Mago",
"edad": 500,
"afiliacion": ["Siete Sabios de la Destrucción"]
},
{
"nombre": "Denken",
"raza": "Humano",
"clase": "Mago",
"edad": 78,
"afiliacion": ["Magos de Primera Clase", "Asociación Continental de Magia"]

},
{
"nombre": "Serie",
"raza": "Elfo",
"clase": "Mago",
"edad": 2000,
"afiliacion": ["Asociación Continental de Magia"]
},
{
"nombre": "Sense",
"raza": "Humano",
"clase": "Mago",
"edad": 28,
"afiliacion": ["Magos de Primera Clase", "Asociación Continental de Magia"]
}
]



"""
8. Muestra la edad media de los personajes humanos.
"""

suma = 0
cantidad = 0

for personaje in personajes_frieren:
    if personaje["raza"] == "Humano":
        suma += personaje["edad"]
        cantidad += 1

print("Edad media de los humanos:", suma / cantidad)


"""
9. Muestra el nombre y la raza de todos los personajes que sean magos de primera clase.
"""
for i in personajes_frieren:
    if "Magos de Primera Clase" in i["afiliacion"]:
        print(f"Nombre: {i["nombre"]}, Raza: {i["raza"]}")

"""
10. Muestra el nombre, la raza y la edad de los personajes del grupo de los cuatro héroes.
"""
for i in personajes_frieren:
    if "Grupo de los Cuatro Héroes" in i["afiliacion"]:
        print(f"Nombre: {i["nombre"]}, Raza: {i["raza"]}, Edad: {i["edad"]}")


"""
11. Inserta al final de la lista un nuevo personaje que tenga todos los campos con algún
valor con sentido (puedes inventártelos, pero que sean razonables).
"""
personajes_frieren.append({
    "nombre": "Gru",
    "raza": "Gigante",
    "clase": "Loco",
    "edad": 58,
    "afiliacion": ["Magos de Primera Clase"]
})

"""
12. Elimina todos los personajes cuya raza sea demonio.
"""
for i in personajes_frieren.copy():
    if "Demonio" in i["raza"]:
        personajes_frieren.remove(i)


for i in personajes_frieren:
    print(f"Nombre: {i['nombre']}, Raza: {i['raza']}")


"""
13. Añádele a todos los elfos la afiliación “Elfos Supervivientes del Examen de Python”
"""
for i in personajes_frieren:
    if i["raza"] == "Elfo":
        i["afiliacion"].append("Elfos Supervivientes del Examen de Python")

for i in personajes_frieren:
    if i["raza"] == "Elfo":
        print(f"Nombre: {i['nombre']}, Afiliación: {i['afiliacion']}")


"""
14. A todos los personajes que pertenezcan a la Asociación Continental de Magia,
quítales esa afiliación.
"""
for i in personajes_frieren:
    if "Asociación Continental de Magia" in i["afiliacion"]:
        i["afiliacion"].remove("Asociación Continental de Magia")



"""
15. Modifica la raza de todos los humanos que tengan 100 o más años a “Zombie”.
"""
for i in personajes_frieren:
    if i["edad"] >= 100 and i["raza"] == "Humano":
        i["raza"] == "Zombie"


