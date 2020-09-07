# Elimina archivos de una lista
def borrar():
    list = ["Mátematicas", "Historia", "Química"]
    for i in range(len(list)-1, -1, -1):
        dato = int(input("¿Cual fue tu calificación en número entero en: " + list[i] + "?" ))
        if dato > 5:
            list.pop(i)
    print(f'Tienes que repetir: {list}')

def run():
    borrar()
if __name__ == "__main__":
    run()