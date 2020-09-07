def run():
    print(f'¿Cual es tu puntuación? ')
    puntos = float(input("R: "))
    Cte = 2400.00

    if puntos == 0:
        nivel = "Inaceptable"
    elif puntos == 0.4:
        nivel = "Aceptable"
    else:
        nivel = "Meritorio"
    print(f'Tiene un nivel {nivel}, su bono es de $ {Cte * puntos}')

if __name__ == "__main__":
    run()

# bonificacion = 2400
# inaceptable = 0
# aceptable = 0.4
# meritorio = 0.6
# puntos = float(input("Introduce tu puntuación: "))
# # Clasifiación por niveles de rendimiento
# if puntos == inaceptable:
#     nivel = "Inaceptable"
# elif puntos == aceptable:
#     nivel = "Aceptable"
# elif puntos >= 0.6:
#     nivel = "Meritorio"
# else:
#     nivel = ""
# # Mostrar nivel de rendimiento
# if nivel == "":
#     print("Esta puntuación no es válida")
# else:
#     print("Tu nivel de rendimiento es %s" % nivel)
#     print("Te corresponde cobrar %.2f€" % (puntos * bonificacion))