def run():
    num = int(input("Escribe un número entero: "))

    dividendo = num + 1
    ope = num * dividendo
    # print (f'dividendo')
    operacion = ope / 2

    print(f'La suma de 1 hasta {str(num)} es: {operacion}')

if __name__ == "__main__":
    run()