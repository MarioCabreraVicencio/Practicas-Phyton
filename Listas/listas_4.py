# Crear un lista de números por input y ordenarla de mayor a menor.
def run():
    list = []
    for i in range(5):
        datos = int(input("Ingresa un número: "))
        list.append(datos)
    for i in range(len(list)):
        list.sort()
        print(f'La lista es: {list[i]}')

if __name__ == "__main__":
    run()