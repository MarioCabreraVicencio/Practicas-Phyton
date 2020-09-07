# Tablas de multiplicar.
def run():

# Muestra una lista con la tabla "n" del 1 al 10.

    # tabla = int(input("Ingresa la tabla de multiplicar que deseas observar: "))
    # for i in range(1, 11):
    #     print(i * tabla)

# Imprime una lista con las 10 tablas de mult, del 1 al "n" 
    tabla = int(input("Ingresa la tabla de multiplicar que deseas observar: "))

    for i in range(1, 11):
        for j in range(1, tabla + 1):
            # print(f'{i}*{j}= {i*j}, end="\t"')
            print(i*j, end="\t")
        print("")

if __name__ == "__main__":
    run()