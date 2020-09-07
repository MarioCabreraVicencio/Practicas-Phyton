def run():
    renta = int(input("Ingresa el valor de tu renta anual: "))
# Al escribir rangos que se anteceden a sí mismos, python los respeta, por anto no es necesario 
# sobreescribir con AND el rango. ( renta >= 20000 and renta <= 35000)
    if renta < 10000:
        porcentaje = 5
    elif renta < 20000:
        porcentaje = 15
    elif renta < 35000: 
        porcentaje = 20
    elif renta < 60000:
        porcentaje = 30
    else:
        porcentaje = 45
    print(f'Tu impositivo es de {str(porcentaje)} %')

if __name__ == "__main__":
    run()
