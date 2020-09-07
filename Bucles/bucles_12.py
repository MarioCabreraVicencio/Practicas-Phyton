# Contabiliza el número de veces que aparece una letra en una frase.
def run():
    frase = str(input("Escribe una frase: "))
    letra = str(input("Escribe la letra a contar: "))
    contador = 0

    for i in frase:
        if i == letra:
            contador += 1
    print(f'La letra {letra} aparece {contador} en la frase.')

if __name__ == "__main__":
    run()