def run():
    nombre = str(input("Bienvenido. \n ¿Escribe tu nombre? \n: "))
    nombre = nombre.capitalize()
    edad = int(input("Escribe tu edad: "))

    for i in range(edad):
        print(f'{nombre} has cumplido {i+1} años.')

if __name__ == "__main__":
    run()