# Imprime una lista ingresada por teclado inversa a como fue agregada.
def run():
    # list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list = []
    for i in range(5):
        dato = int(input("Ingresa los numeros de tu lista: "))
        list.append(dato)
# Esto ordena una lista de mayor a menor
    list.sort()

    for i in range(len(list) -1, -1, -1):
        print(list[i], end=", ")

if __name__ == "__main__":
    run()