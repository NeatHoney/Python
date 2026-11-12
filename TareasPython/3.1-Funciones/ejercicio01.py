"""
1. Crea una función llamada comprobarLetraDNI que reciba una cadena de
caracteres que representará al DNI de una persona y devuelva True si el DNI
es correcto y False si no lo es. Un DNI es correcto si tiene 8 dígitos enteros
seguidos de una letra (mayúscula o minúscula), y la letra es correcta. Para
conocer si la letra es correcta puedes consultar la web del Ministerio del
Interior.
https://www.interior.gob.es/opencms/es/servicios-al-ciudadano/tramites-y-gestiones/dni/calculo-del-digito-de-control-del-nif-nie/
"""

LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"

def comprobarLetraDNI(parametro1):
    # .isdigit() -> True si TODOS los caracteres de la cadena son dígitos (0-9)
    # .isalpha() -> True si TODOS los caracteres de la cadena son letras
    formatoCorrecto = (
        len(parametro1) == 9
        and parametro1[:8].isdigit()
        and parametro1[8].isalpha()
    )

    if formatoCorrecto:
        letraCalculada = LETRAS[int(parametro1[:8]) % 23]
        return parametro1[8].upper() == letraCalculada
    else:
        return False


print(comprobarLetraDNI("12345678Z"))  # True
print(comprobarLetraDNI("12345678z"))  # True
print(comprobarLetraDNI("12345678A"))  # False
print(comprobarLetraDNI("1234567Z"))   # False
print(comprobarLetraDNI("ABCDEFGHZ"))  # False
