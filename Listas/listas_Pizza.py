# Armas tu pizza con los ingrecientes que quieras hasta que escojas que ya no quieres otro ingrediente
# def run():
#     print(f'Bienvenido a Mario´s pizza. \nArma tu pizza con los siguientes ingredientes: \n\t Pimiento \n\t Tofu \n\t Tocino \n\t Jamón \n\t Salchica')
#     # lista_ingredientes = ["Pimiento", "Tofu", "Tocino", "Jamón", "Salchica"]
#     ingredientes_escogidos = []
#     ingrediente_1 = str(input("¿Cual será el primer ingrediente de tu pizza?\n : "))
#     ingredientes_escogidos.append(ingrediente_1)
#     while True:
#         print("¿Desea otro ingrediente? \n\t1- Si \n\t2- No")
#         opcion = int(input(": ")) 
#         if opcion == 2:
#             break
#         ingrediente_n = str(input("¿Cual será el proximo ingrediente de tu pizza?\n: "))
#         ingredientes_escogidos.append(ingrediente_n)
#         # Tengo que corregir la impresion de la lista
#         print(f'Tu pizza lleva Tomate, Motzarella, {ingredientes_escogidos}')
# if __name__ == "__main__":
#     run()

# Armas tu pizza con solo 3 ingredientes.
def run():
    print(f'Bienvenido a Mario´s pizza. \nArma tu pizza con los siguientes ingredientes: \n\t Pimiento \n\t Tofu \n\t Tocino \n\t Jamón \n\t Salchicha \n Solo puedes escoger 3 ingredientes.')
    # lista_ingredientes = ["Pimiento", "Tofu", "Tocino", "Jamón", "Salchicha"]
    ingredientes_escogidos = []
    ingrediente_1 = str(input("¿Cual será el primer ingrediente de tu pizza?\n : "))
    ingredientes_escogidos.append(ingrediente_1)
    for i in range(2):
        print("¿Desea otro ingrediente? \n\t1- Si \n\t2- No")
        opcion = int(input(": ")) 
        if opcion == 2:
            break
        ingrediente_n = str(input("¿Cual será el proximo ingrediente de tu pizza?\n: "))
        ingredientes_escogidos.append(ingrediente_n)
        print(ingredientes_escogidos)
    print(f'Tu pizza lleva Tomate, Motzarella, {ingredientes_escogidos[0]}, {ingredientes_escogidos[1]} y {ingredientes_escogidos[2]}')
if __name__ == "__main__":
    run()