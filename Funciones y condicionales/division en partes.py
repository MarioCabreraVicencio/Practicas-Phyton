def run():
    dividendo = float(input("Ingresa el dividendo: "))
    divisor = float(input("Ingresa el divisor: "))

    modulo = dividendo % divisor
    cociente = dividendo / divisor
    cociente = round(cociente, 2)

    print(f'Al dividir {dividendo} entre {divisor} obtenemos un residuo de {modulo} y un cociente de {cociente}')

if __name__ == "__main__":
    run()