# Calcular el peso de un paquete.

def run():
    num_payasos = int(input("¿Cuantos payasos serán enviados en este paquete?: "))
    num_muñecas = int(input("¿Cuantas muñecas serán enviadas en este paquete?: "))

    peso_payasos = num_payasos * 0.112
    peso_muñecas = num_muñecas * 0.075 
 
    print(f'El pesos total por {str(num_payasos)} payasos es de: {str(peso_payasos)} kg, el peso total por {str(num_muñecas)} muñecas es de: {peso_muñecas} kg')
    print()
    print(f'El peso total del paquete a enviar es de: {str(peso_muñecas + peso_payasos)}kg.')
if __name__ == "__main__":
    run()
