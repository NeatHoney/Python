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


conjunto = {1,2,3,3,4}
conjunto.add(7)
conjunto.remove(3)
print(conjunto)

def main():
    print("este es mi main")

if __name__ == "__main__":
    main()



def main():
    
    lista = ["Manzana", "Pera", "Melocoton"]
    lista2 = ["Kiwi", "Sandia", "Melon"]
    
    lista.extends(lista2)
    print(lista[-1])  # -1 Siempre te dice el último
    
    tupla = (3,5,7)
    print(tupla[0])
    
    inicio = int(input("Inicio:"))
    fin = int(input("Fin:"))
    salto = int(input("Salto:"))
    
    rango = range(inicio,fin,salto)
    print(rango)

if __name__ == "__main__":
    main()