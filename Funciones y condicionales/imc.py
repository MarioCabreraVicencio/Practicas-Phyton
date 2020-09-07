def run():
    altura = float(input("Ingresa tu altura en metros: "))
    peso = float(input("Ingresa tu peso en kilogramos: "))

    altura_cuadrado = altura**2
    imc = peso / altura_cuadrado
    imc = round(imc, 2)

    if imc >= 18.5 and imc <= 24.9:
        print(f'Su imc es de {imc}, usted esta en un rango saludable.')
    elif imc >= 25 and imc <= 29.9:
        print(f'Su imc es de {imc}, usted esta en un rango de sobre peso.')
    else:
        print(f'Su imc es de {imc}, usted esta en un rango de obesidad.')

if __name__ == "__main__":
    run()