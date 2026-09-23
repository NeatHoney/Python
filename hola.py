diccionario = {
    "nombre" : "Pepe",
    "apellido" : "López",
    "edad" : "18"
}

print(diccionario["edad"]) #Así solo muestra ese valor
print(diccionario) # Así muestra todo
diccionario["edad"] = 20 # Así cambias el valor

diccionario["direccion"] = "Calle Juan Carlos I" # Así añades un valor más a la lista
print(diccionario["direccion"])
print(diccionario) # Aquí se ve al final ya añadido



estudiante = [
    {
        "nombre" : "Joselin",
        "apellido" : "Flores",
        "modulos" : ["Acceso a datos", "Python", "Proyecto"]
    },

    {
        "nombre" : "Camilo",
        "apellido" : "Sesto",
        "modulos" : ["Acceso a datos", "Desarrollo de interfaces"]
    }
]


print(estudiante[0]["modulos"][0])
print(estudiante[1]["apellido"])
