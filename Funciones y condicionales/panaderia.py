def barras_vendidas():
    venta = int(input("¿Cuantas barras frías se vendieron?: "))
    costo = 3.94 * 0.6
    total = costo * venta

    print(f'El costo de la barra fría es de ${str(costo)}')
    print(f'Usted debe pagar: {str(total)}')



def run():
    barras_vendidas()
if __name__ == "__main__":
    run()