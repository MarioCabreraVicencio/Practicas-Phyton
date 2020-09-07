# Empareja una lista con una introducida por teclado.
def run():
    list = ["Matematicas", "Español", "Quimica"]
    scores = []
    for i in list:
        calif = int(input(f'Cual es tu calificación en {i}: ')) 
        scores.append(calif)
    for i in range(len(list)):
        print(f'Tu calificación en {list[i]} es de: {scores[i]}')

if __name__ == "__main__":
    run()