def run():
    lista = {}
    pregunta = str('Si')
    while pregunta == 'Si':
        articulo = str(input("¿Que necesitas comprar?: "))
        articulo = articulo.capitalize()
        costo = float(input(f'¿Que precio tiene el {articulo}?: '))
        lista[articulo] = costo
        pregunta = str(input("¿Deseas agregar mas articulos a la lista? \n Si \n No \n: "))
        pregunta = pregunta.capitalize()

    precio_total = 0
    print(f'Lista de compras.')
    if pregunta == 'No':
        for articulo, costo in lista.items():
            print(f'{articulo} \t {costo}')
            precio_total = costo + precio_total
        print(f'El total es ${precio_total}')


if __name__ == "__main__":
    run()