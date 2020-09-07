# Imprime un triangulo con altura "n"
def triangulo():
    h = int(input("Ingresa un número entero que sea la altura de tu triangulo: "))
    for i in range(h):
        print("*" * (i+1))
        
def run():
    triangulo()
if __name__ == "__main__":
    run()