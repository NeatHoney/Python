"""
2. Crea una función llamada convertirTemperatura que reciba un número con
decimales y dos cadenas de caracteres. Las cadenas de caracteres posibles
serán "C", "K" y "F", que representan unidades de temperatura (Celsius,
Kelvin y Fahrenheit). La función devolverá, como número con decimales, el
resultado de convertir de la primera unidad que reciba la función a la
segunda. Por ejemplo, convertirTemperatura(10,"F","C") devolvería el
resultado de pasar 10 Fahrenheit a Celsius. Devuelve el resultado con dos
decimales, redondeando al valor más cercano.
"""


def convertirTemperatura(valor, origen, destino):
    # Paso 1: pasar el valor de la unidad de origen a Celsius
    if origen == "C":
        celsius = valor
    elif origen == "K":
        celsius = valor - 273.15
    else:  # "F"
        celsius = (valor - 32) * 5 / 9

    # Paso 2: pasar de Celsius a la unidad de destino
    if destino == "C":
        resultado = celsius
    elif destino == "K":
        resultado = celsius + 273.15
    else:  # "F"
        resultado = celsius * 9 / 5 + 32

    # Paso 3: devolver redondeado a 2 decimales
    return round(resultado, 2)


print(convertirTemperatura(10, "F", "C"))  # -12.22
print(convertirTemperatura(100, "C", "F"))  # 212.0
print(convertirTemperatura(0, "C", "K"))  # 273.15
print(convertirTemperatura(300, "K", "F"))  # 80.33
