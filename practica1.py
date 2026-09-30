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

    







