def run():
    inversion = int(input("Ingresa el monto de tu inversión: "))
    tasa_interes = float(input("Ingresa la tasa de interes anual: "))
    años = int(input("Ingresa el periodo de la inversión: "))

    paso_uno = 1 + tasa_interes
    paso_dos = paso_uno ** años
    paso_tres = paso_dos * inversion
    paso_tres = round(paso_tres, 2)

    print(f'str(')
    


    print(f'Tu inversión inicial fue de: ${str(inversion)}')
    print(f'los intereses generados en el periodo de capitalizacion de {años} es de ')
    print(f'Tu capital es de: ${str(paso_tres)}')

if __name__ == "__main__":
    run()