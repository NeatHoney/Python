"""
3. Crea una función llamada calcularValorBruto, que reciba un número con
decimales (el precio de un producto) y una cadena de caracteres (que
representará el tipo de IVA aplicable). Las cadenas de caracteres posibles
serán GENERAL, REDUCIDO y SUPERREDUCIDO. La función devolverá el
resultado de sumar el IVA aplicable al valor neto del producto. Por ejemplo,
calcularValorBruto(10,"GENERAL") devolvería el resultado de sumar a los
10€ de valor neto, el porcentaje de IVA del tipo general (que es un 21%), lo
que daría 12,1€. Devuelve el resultado con dos decimales, redondeando
hacia arriba.
"""
import math

# Porcentaje de IVA de cada tipo
IVA = {
    "GENERAL": 21,
    "REDUCIDO": 10,
    "SUPERREDUCIDO": 4,
}


def calcularValorBruto(precio, tipoIva):
    bruto = precio * (1 + IVA[tipoIva] / 100)
    # Redondeo hacia arriba a 2 decimales: se pasa a céntimos, se sube con
    # ceil y se vuelve a euros. El round previo elimina el "ruido" de los
    # decimales en coma flotante (p. ej. 1210.0000000000002 -> 1210.0).
    return math.ceil(round(bruto * 100, 6)) / 100


print(calcularValorBruto(10, "GENERAL"))  # 12.1
print(calcularValorBruto(10, "REDUCIDO"))  # 11.0
print(calcularValorBruto(10, "SUPERREDUCIDO"))  # 10.4
print(calcularValorBruto(9.99, "GENERAL"))  # 12.09 (12.0879 sube)
