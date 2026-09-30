""" 1. Pedir al usuario una nota numérica entera mediante un input y diga si la calificación
es Suspenso, Aprobado, Notable, Sobresaliente, o No válida (en caso de que la
entrada sea diferente a la esperada). Realizar una versión con IF y otra con MATCH."""

nota = int(input("Introduce una nota:"))

if nota >= 0 and nota < 5:
    print("Suspenso")
elif nota >= 5 and nota < 7:
    print("Aprobado")
elif nota >= 7 and nota < 9:
    print("Notable")
elif nota >= 9 and nota < 11:
    print("Sobresaliente")
else:
    print("No válida")


match nota:

    case n if n >= 0 and nota < 5:
        print("Suspenso")
    case n if n >= 5 and nota < 7:
        print("Aprobado")
    case n if n >= 7 and nota < 9:
        print("Notable")
    case n if n >= 9 and nota < 11:
        print("Sobresaliente")
    case _:
        print("No válida")


"""
2. Pedir al usuario dos valores por pantalla: el precio de un producto (float) y el tipo de
IVA (General, Reducido, Superreducido). Calcular el precio final del producto fruto
de sumarle el IVA en función de su tipo. Realizar una versión con IF y otra con
MATCH.
"""

precio = float(input("Introduce un precio:"))
tipo = int(input("Introduce el tipo (General 1, Reducido 2, Superreducido 3):"))

if tipo == 1:
    print(f"El iva General sería de: {precio * 1.21}")
elif tipo == 2:
    print(f"El iva Reducido sería de: {precio * 1.10}")
elif tipo == 3:
    print(f"El iva Superreducido sería de: {precio * 1.04}")


match tipo:
    case t if t == 1:
        print(f"El iva General sería de: {precio * 1.21}")
    case t if t == 2:
        print(f"El iva Reducido sería de: {precio * 1.10}")
    case t if t == 3:
        print(f"El iva Superreducido sería de: {precio * 1.04}")



"""
3. Pedir al usuario la edad de una persona y mostrar si es mayor o menor de edad. Si
la edad es menor a 0 mostrar un mensaje de error, y si es superior a 120 indicar que
es un vampiro.
 """

edad = int(input("Introduce la edad:"))

if edad < 0:
    print("Error...")
elif edad < 18:
    print("Eres menor de edad")
elif edad < 120:
    print("Eres mayor de edad")
elif edad >= 120:
    print("Eres un vampiro")


"""
4. A partir de 60 mm de lluvia acumulados en 12 horas se declara una alerta amarilla, y
a partir de 120 mm, una alerta roja. Pedir al usuario los milímetros de lluvia
acumulados y mostrar por pantalla si No hay alerta, Hay alerta amarilla o Hay
alerta roja. Realizar una versión con IF y otra con MATCH.
"""

agua = int(input("Introduce los mm de  agua:"))

if agua < 60:
    print("No hay alerta")
elif agua < 120:
    print("Hay alerta amarilla")
elif agua > 119:
    print("Hay alerta roja")


match agua:
    case a if a < 60:
        print("No hay alerta")
    case a if a < 120:
        print("Hay alerta amarilla")
    case a if a > 119:
        print("Hay alerta roja")


"""
5. Pedir al usuario dos números enteros y mostrar los números pares dentro de dicho
intervalo. Si el primer número es mayor que el primero se mostrará por pantalla un
mensaje de error. Realizar una versión con FOR y otra con WHILE.
"""

a = int(input("Introduce un número:"))
b = int(input("Introduce otro número:"))

if a > b:
    print("Error")
else:
    for i in range(a, b):
        if i % 2 == 0:
            print(i)


while b > a:
    for i in range(a, b):
        if i % 2 == 0:
            print(i)


"""
6. Supongamos que la contraseña para acceder es “12345”. Pedir al usuario la
contraseña por pantalla y, si es la correcta, mostrar un mensaje de bienvenida. Si la
contraseña introducida es incorrecta, volver a pedirla hasta que se introduzca
correctamente.
"""
contraseña = 12345
numero = 0

while numero != contraseña:
    numero = int(input("Introduce la contraseña:"))

print("Bienvenido al sistema")


"""
7. Dada la lista de videojuegos que se encuentra en el anexo I, muestra por pantalla
solo los videojuegos cuyo título empiece por M.
"""

videojuegos = ("Super Mario Bros", "New Super Mario Bros", "Mario vs Luigi", "Mario Kart")

for i in videojuegos:
    if i[0] == "M":
        print(i)

"""
8. Dada la lista de videojuegos que se encuentra en el anexo II, muestra por pantalla
solo los videojuegos que cuesten más de 20€.
"""

videojuegos = [

{"titulo": "The Legend of Zelda: BOTW", "consola": "Nintendo Switch", "precio": 59.99},
{"titulo": "Hollow Knight", "consola": "PC", "precio": 14.99},
{"titulo": "Stardew Valley", "consola": "PlayStation 4", "precio": 13.99},
{"titulo": "Assassin's Creed Shadows", "consola": "PlayStation 5", "precio": 69.99},
{"titulo": "Resident Evil: Requiem", "consola": "PlayStation 5", "precio": 79.99},
{"titulo": "Trails in the Sky 1st Chapter", "consola": "Nintendo Switch", "precio": 49.9}
]

for i in videojuegos:
    if i["precio"] > 20:
        print(i)



"""
9. Pedir al usuario un número entero y mostrar por pantalla si el número es primo o no.
"""

entero = int(input("Introduce un número entero:"))

if entero % 2 == 0:
    print(f"El número {entero} es primo")


"""
10. Pedir al usuario dos valores enteros y mostrar por pantalla todos los números primos
dentro de ese rango. Si el primer número es mayor que el primero se mostrará por
pantalla un mensaje de error.
"""

a = int(input("Introduce un número:"))
b = int(input("Introduce otro número:"))

if a > b:
    print("Error...")
else:
    for i in range(a, b):
        if i % 2 == 0:
            print(f"El número {i} es par")

            