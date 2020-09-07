# En una lista ingresada por teclado, imprime el mayor y el menor.

# def run():
#     list = []
#     for i in range(3):
#         list_1 = float(input("Ingresa un valor a tu lista: "))
#         list.append(list_1)
#         # print(list)
#         mayor = list.sort()
#         # print(f'de menor a mayor: {list}')
#         mayor = list[0]
#         menor = list.sort(reverse=True)
#         # print(f' de mayor a menor: {list}')
#         menor = list[0]
#     print()
#     print(f'El valor menor es: {mayor}')
#     print()
#     print(f'El valor mayor es: {menor}')

# if __name__ == "__main__":
#     run()


# ingresando datos las veces que el usuario diga.

def run():
    list = []
    dato_1 = float(input("Ingresa el primer valor a tu lista: "))
    list.append(dato_1)
    while True:
        print("¿Deseas agregar otro valor? \n\t1 Si \n\t2 No")
        validador = int(input(": "))
        if validador == 2:
            break
        dato_2 = float(input("Ingresa otro valor a tu lista: "))
        list.append(dato_2)
    list.sort()
    menor = list[0]
    mayor = list[-1]
    print(f'\n El valor menor es: {menor}')
    print(f'\n El valor mayor es: {mayor}')

if __name__ == "__main__":
    run()

# Corregido por Luci.
# def run():
#     list = []
#     while True:
#         dato_1 = float(input("Ingresa el primer valor a tu lista: "))
#         list.append(dato_1)
#     # while True:
#         print("¿Deseas agregar otro valor? \n\t1 Si \n\t2 No")
#         validador = int(input(": "))
#         if validador == 2:
#             break
#         # dato_2 = float(input("Ingresa otro valor a tu lista: "))
#         # list.append(dato_2)
#     list.sort()
#     menor = list[0]
#     mayor = list[-1]
#     print(f'\n El valor menor es: {menor}')
#     print(f'\n El valor mayor es: {mayor}')

# if __name__ == "__main__":
#     run()