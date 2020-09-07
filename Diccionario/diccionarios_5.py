# Agregar valores a llaves creadas y despues imprimirlas.
def run():
    materias = {"Matematics": 0, "Lenguage": 0, "Psicology": 0}
    credits = 0
    uno = float(input("¿Cual es tu calificación en Matemáticas?: "))
    dos = float(input("¿Cual es tu calificación en Lenguaje?: "))
    tres = float(input("¿Cual es tu calificación en Psicología?: "))

    materias["Matematics"] = uno
    materias["lenguage"] = dos
    materias["Psicology"] = tres
    for keys, values in materias.items():
        print(f'En {keys} tienes {values} cretidos.')
        credits += values
    print(f'El total de creditos acumulados es de: {credits}')
if __name__ == "__main__":
    run()