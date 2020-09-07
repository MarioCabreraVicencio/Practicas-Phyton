# imprime un string introducido de atras a delante en forma de lista y de renglon.

def run():
    word = str(input("Writte a word: "))
    # legth = len(word)
    for letra in (len(word) -1, -1, -1):
        print(letra, end=" ")
    print()
    print()
    for i in word:
        print(i)


if __name__ == "__main__":
    run()