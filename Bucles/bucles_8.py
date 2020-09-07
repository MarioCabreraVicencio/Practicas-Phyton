# Imprime una priramide de números.
def triangulo():
    n = int(input("Introduce la altura del triángulo (entero positivo): "))
    for i in range(1, n+1, 2):
        for j in range(i, 0, -2):
            print(j, end=" ")
        print("")

def run():
    triangulo()
if __name__ == "__main__":
    run()