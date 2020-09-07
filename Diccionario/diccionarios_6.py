# Introduce por teclado datos (sin limite) a un diccionario y los imprime.
def run():
    person = {}
    more = 'Si'
    while more=='Si':
        key = input('¿Qué dato quieres introducir?: ')
        key = key.capitalize()
        value = input(key + ': ')
        value = value.capitalize()
        person[key] = value
        print(person)
        more = input('¿Quieres añadir más información (Si/No)? \n : ')
        more = more.capitalize()
    if more == 'No':
        print(f'Tu información es: {person}')

if __name__ == "__main__":
    run()