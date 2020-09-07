# Interes compuesto
def run():
    inversion = float(input("Ingresa la cantidad a invertir: "))
    interes = float(input("Ingresa la tasa de interes anual aplicable: "))
    años = int(input("Ingresa el periodo de la inversión: "))

    for i in range(años):
        # el (1 + interes {0.1} = 1.1, el uno suma el interes obtenido a la inversion. 
        # 100 * 0.1 = 10      100 * 1.1 = 110)
        inversion = inversion * (1 + interes)
        inversion = round(inversion, 2)

        print(f'Tu saldo en el periodo {i + 1} es de {inversion}')

if __name__ == "__main__":
    run()

# def suma(x, y):
# # Ingresar parámetros por teclado.
# # suma(input("x: "), input("y: "))

#     total = x + y
#     print(f'{total}')
#     return (total)

# a = suma(1, 2)
# b = suma(3, 4)
# c = suma(5, 6)
# d = a + b + c    
# print(f'este es el resultado: {d}')

# # suma(input("x: "), input("y: "))

# if __name__ == "__main__":
#     suma

