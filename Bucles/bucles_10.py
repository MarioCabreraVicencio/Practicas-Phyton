# Indica si un número ingresado es primo o no lo es.

def primalidad():
    numero = int(input("Escribe un número: "))

    for i in range(2, numero + 1):
        operation = numero % i
        if operation == 0:
            break
    if i == numero: 
        print(f'El número {numero} es un número primo.')
    else:
        print(f'El número {numero} no es un número primo.')

def run():
    primalidad()
if __name__ == "__main__":
    run()