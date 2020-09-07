def run():
    edad = int(input(f'¿Cual es tu edad?: '))

    if edad <= 4:
        costo = 0
    elif edad <= 18:
        costo = 5
    else:
        costo = 10
    
    print(f'Debes de pagar: $ {costo}')

if __name__ == "__main__":
    run()