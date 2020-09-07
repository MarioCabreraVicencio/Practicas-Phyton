def contribuyente():
    ingresos = float(input("¿A cuanto asienden tus ingresos mensuales?: "))
    edad = int(input("¿Cual es tu edad?: "))

    if ingresos >= 1000 and edad >= 16:
        print("Tu debes tributar.")
    else:
        print("Tu no debes tributar.")



def run():
    contribuyente()

if __name__ == "__main__":
    run()

