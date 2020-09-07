# Cuenta las veces que aparece cada letra.

def contador():
    frase = str(input(f'Escribe una frase: '))
    frase = frase.lower()
    # lista_vocales = ["a", "e", "i", "o", "u"]
    abcd = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


    # for i in lista_vocales:
    for i in abcd:
        contador = 0 
        for j in frase:
            if j == i:
                contador += 1
        # print(f'La vocal {i} aparece {contador} veces.')
        print(f'La letra {i} aparece {contador} veces.')

def run():
    contador()
if __name__ == "__main__":
    run()