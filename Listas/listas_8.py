# Dice sí una frase es un palindromo.
def run():
    frase = str(input("Escribe una frase: "))
    # Este replace me funciono y el .strip no me funciono. 
    frase = frase.replace(" ", "")
    # frase = frase.lower()
    frase_al_reves = frase[::-1]
    print(f'{frase_al_reves}')
    if frase == frase_al_reves:
        print(f'Es un palindromo')
    else:
        print("No es un palindromo.")

if __name__ == "__main__":
    run()