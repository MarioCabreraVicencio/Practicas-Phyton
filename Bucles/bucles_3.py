# Imprime todos los impares hasta el numero ingresado.
n = int(input("Introduce un número entero positivo: "))
# n+1 Es por que el rango no es inclusivo, sin el +1 la cuenta se queda en 8
for i in range(1, n+1, 2):

    print(i, end=", ")