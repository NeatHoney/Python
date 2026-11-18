from datos import personajes

def ejercicio1():
    lista = [p["nombre"] for p in personajes if p["afiliacion"] == "Cuerpo de Exploración" and p["vivo"] == True]
    print(lista)


def ejercicio2():
    lista = [p["nombre"] for p in personajes if p["afiliacion"] == "Cuerpo de Exploración" and "Superviviencia" and "Sigilo" in p["habilidades"]]
    print(lista)


def ejercicio3():
    lista = [(p["nombre"], p["afiliacion"]) for p in personajes if p["afiliacion"] != "Cuerpo de Exploración"]
    print(lista)


def ejercicio4():
    lista = [f"{p["nombre"]} ({p["afiliacion"]})" for p in personajes if p["registro_combate"]["misiones_completadas"] >= 20]
    print(lista)


def ejercicio5():
    lista = [(p["nombre"], p["estatura_m"] * 100) for p in personajes if p["estatura_m"] > 1.70]
    print(lista)


def ejercicio6():
    lista = [h for p in personajes for h in p["habilidades"]]
    print(lista)


def ejercicio8():
    lista = [(p["nombre"], p["registro_combate"]["titanes_solo"]) for p in personajes]
    print(lista)


def ejercicio9():
    lista = [sum(p["estatura_m"] / len(personajes) for  p in personajes)]
    print(lista)
    

