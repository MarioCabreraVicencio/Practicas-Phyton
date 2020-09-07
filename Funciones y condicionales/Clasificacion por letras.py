# abcedario[a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

def run():
    nombre = str(input("Escribe tu nombre: "))
    sexo = """ 
    1 Masculino.
    2 Femenino.
    ¿Cual es tu sexo? """

    opcion = int(input(sexo))

    if opcion == 1:
        if nombre > 'n':
            print("Perteneces al grupo A")
        elif nombre < 'n':
            print("Perteneces al grupo B")
    else:
        if nombre < 'm':
            print("Perteneces al grupo A")
        elif nombre > 'm':
            print("Perteneces al grupo B")

if __name__ == "__main__":
    run()



# name = input("¿Cómo te llamas? ")
# gender = input("¿Cuál es tu sexo (M o H)? ")
# if (gender == "M" and name.lower() < 'm') or (gender == "H" and name.lower() > 'n'):
#     group = "A"
# else:
#     group = "B"
# print("Tu grupo es " + group)