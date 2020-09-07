# Ingresa una palabra e imrpimela 10 veces.
def palabra():

    word = str(input("Ingresa una palabra: "))
    word = word.capitalize()
    # contador = 0
    for i in range(1, 11):
        print(f'{i}.- {word}')
        # contador += 1

if __name__ == "__main__":
    palabra()
