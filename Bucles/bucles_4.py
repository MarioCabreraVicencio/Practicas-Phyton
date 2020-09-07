# Imprime la lista de numeros del n al 0
n = int(input("Introduce un número entero positivo: "))
# Como se hara una cuenta regresiva, se inicia en n hasta el 0, con pasos negativos.
for i in range(n,-1, -1):
    print(i, end=", ")