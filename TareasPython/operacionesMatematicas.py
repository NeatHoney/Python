"""
1. Pedir al usuario un número entero y calcular el sumatorio desde 1 hasta dicho
número (incluido). Si el número introducido es menor que 1, mostrar un mensaje de
error.
"""
numero = int(input("Introduce un número entero:"))

if numero < 1:
	print("Error: el número debe ser mayor o igual que 1")
else:
	suma = 0
	for i in range(1, numero + 1):
		suma += i

	print("El sumatorio es:", suma)



"""
2. Pedir al usuario un número entero y calcular el factorial desde 1 hasta dicho número
(incluido). Si el número introducido es menor que 1, mostrar un mensaje de error.
"""
numero = int(input("Introduce un número entero:"))

if numero < 1:
	print("Error: el número debe ser mayor o igual que 1.")
else:
	factorial = 1

	for i in range(1, numero + 1):
		factorial *= i

	print("El factorial es:", factorial)


"""
3. Pedir al usuario dos números enteros (base y potencia). Calcular el resultado de
elevar la base al exponente. Mostrar un error en caso de que la base sea menor que
1 o que la potencia sea menor que 0.
"""
base = int(input("Introduce la base:"))
potencia = int(input("Introduce la potencia:"))

if base < 1 or potencia < 0:
	print("Error: la base debe ser mayor o igual que 1 y la potencia debe ser mayor o igual que 0")

else:
	resultado = 1
	
	for i in range(potencia):
		resultado *= base

	print("El resultado es:", resultado)


"""
4. Pedir al usuario un número entero y añadir todos los números de la serie de
fibonacci desde 0 hasta ese número (incluido) a una lista. Mostrar dicha lista al
acabar. Si el número introducido es menor que 0, mostrar un mensaje de error.
"""
numero = int(input("Introduce un número entero: "))

if numero < 0:
    print("Error: el número debe ser mayor o igual que 0.")
else:
    fibonacci = []
    a = 0
    b = 1

    while a <= numero:
        fibonacci.append(a)
        a, b = b, a + b

    print("Serie de Fibonacci:", fibonacci)



"""
5. Pedir al usuario un número y mostrar el triángulo de pascal de ese número de filas.
En caso de que el número sea inferior a 1, mostrar un mensaje de error.
"""
filas = int(input("Introduce el número de filas: "))

if filas < 1:
    print("Error: el número de filas debe ser mayor o igual que 1.")
else:
    triangulo = []

    for i in range(filas):
        fila = [1]

        if i > 0:
            anterior = triangulo[i - 1]

            for j in range(len(anterior) - 1):
                fila.append(anterior[j] + anterior[j + 1])

            fila.append(1)

        triangulo.append(fila)

    for fila in triangulo:
        print(fila)

