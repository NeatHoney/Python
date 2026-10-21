from datos import personajes

def ejercicio1():
    personajes.append({
        "nombre" : "Goku",
        "raza" : "Saiyan",
        "nivel_pelea" : 250000000,
        "tecnicas" : ["Golpe Seco", "Aliento Dragon", "Ataque Sorpresa"],
        "atributos" : {"fuerza":94, "defensa":88, "velocidad":95}
    })


mediaVelocidad = 0

def ejercicio2():
    sumaFuerza = 0
    sumaDefensa = 0
    sumaVelocidad = 0

    for personaje in personajes:
        sumaFuerza += personaje["atributos"][0]
        sumaDefensa += personaje["atributos"][1]
        sumaVelocidad += personaje["atributos"][2]

        
    mediaFuerza = sumaFuerza / len(personajes)
    mediaDefensa = sumaFuerza / len(personajes)
    mediaVelocidad = sumaFuerza / len(personajes)


    for personaje in personajes:
        if mediaFuerza and mediaDefensa and mediaVelocidad > 80:
            print(personaje)


def ejercicio3():
    for personaje in personajes:
        if personaje["atributos"][0] > mediaVelocidad:
            print(personaje)


def ejercicio4():
    for personaje in personajes:
        if "Big Bang Attack" in personaje["tecnicas"]:
            personaje["atributos"][0] + 10

    if personaje["atributos"][0] < 100:
        print("Personaje fuerza:", personaje["atributos"][0])
    else:
        print("Al añadir 10 ptos se pasa de 100")

def ejercicio5():
    fuerza_vegeta = 0
    for personaje in personajes:
        if personaje["nombre"] == "Vegeta":
            fuerza_vegeta = personaje["atributos"]["fuerza"]

    for personaje in personajes:
        if personaje["atributos"]["defensa"] < fuerza_vegeta and personaje["nombre"] != "Vegeta":
                print(personaje["nombre"], personaje["atributos"]["fuerza"])


def ejercicio6():
    for personaje in personajes.copy:
        if "Saiyan" in personaje["raza"]:
            print(personaje)
            personajes.remove(personaje)


    