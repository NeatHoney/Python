# numero = int(input("Introduce un número:")) control + c del barsa

# if numero > 0:
#     print("Positivo")
# elif numero < 0:
#     print("Negativo")
# else:
#     print("Cero")

# dia = input("Introduce un día: ").lower() # lower para cuando escribas en minuscula lo coga

# match dia:
#     case "miercoles" |"viernes":
#         print("Hay clase")
#     case "lunes" | "martes" | "jueves":   # la barra es: miercoles O viernes
#         print("No hay clase")
#     case _: # El barra baja es el default
#         print("Finde")


# numero = int(input("Introduce un número:"))

# match numero:
#     case x if x < 0:
#         print("Negativo")
#     case x if x > 0:
#         print("Positivo")
#     case _:
#         print("Cero")

# for i in range(1,10,2): # El tecer valor es por si quieres ir de salto en salto
#     print(i)

# for i in range(10,1,-1): # Si no pones el salto no te muestra , pones -1 para hacer el salto en negativo y descienda
#     print(i)


# juegos = [
#     "League of Legends",
#     "Fifa 26",
#     "Worl of Warcraft"
# ]

# for juego in juegos:
#     print(juego)


# juegos = [
#     {
#         "titulo" : "League of Legends",
#         "desarrollador" : "Riot Games",
#         "precio" : 0
#     },
#     {
#         "titulo" : "Fifa 26",
#         "desarrollador" : "EA Sports",
#         "precio" : 69.95
#     }
# ]

# for juego in juegos:
#     if juego["precio"] == 0:
#         print(juego["titulo"])

# palabra = "Hola mundo"

# for letra in palabra:
#     print(letra)

# contador = 1

# while contador <= 10:
#     print(contador)
#     contador += 1


# animales = ["Linde ibérico", "Quebrantahuesos", "Cabra montesa"]

# while animales:
#     animal = animales.pop(0) # Eliminar al primero 
#     print(animal)


numero = int(input("Introduce un número:"))

if numero >= 0 and numero <= 10:
    print("Ok")

    



