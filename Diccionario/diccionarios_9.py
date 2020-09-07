
def run():
    # diccionario = {"Folio": monto, "Folio": monto}
    diccionario = {}
    opcion = str("Si")
 
    while opcion == "Si":
        accion = int(input("¿Que desea hacer? \n\t 1 Agregar una nueva factura. \n\t 2 Pagar una factura. \n\t 3 Salir del programa. \n\t : "))
        if accion == 1:
            print("1. Agregar una nueva factura.")
            folio = int(input("Escribe el número de Folio: "))
            monto = float(input("¿Cual es el monto de la Factura?: "))
            diccionario[folio] = monto
            opcion = str(input("\n Desea realizar alguna otra acción? \n\t Si. \n\t No. \n\t : "))
            opcion = opcion.capitalize()

        elif accion == 2:
            print("2. Pagar una factura. ")
            print(f'Las facturas ingresadas son: {diccionario}')
            folio_factura = int(input("¿Que factura deseas pagar? \n Escribe su No. de Folio: "))
            pagar_factura = diccionario.get(folio_factura)
            print(f' El total a pagar es de: {pagar_factura}')
            print(f'Las facturas restantes son: {diccionario}')
            opcion = str(input("\n Desea realizar alguna otra acción? \n\t Si. \n\t No. \n\t : "))
            opcion = opcion.capitalize()
        else:
            print("Espero haberle sido de utilidad.")
    else:
        print("Espero haberle sido de utilidad.")

if __name__ == "__main__":
    run()