
def run():
    dictionary = {}
    words = input("Introduce la lista de palabras y traducciones en formato palabra:traducción, palabra:traducción, ...: ")
    for i in words.split(','):
        key, value = i.split(':')
        dictionary[key] = value
        print(f'Diccionario: {dictionary}')
if __name__ == "__main__":
    run()
