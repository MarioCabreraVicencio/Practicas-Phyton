# ingresa una fruta y una cantidad y regresa cuanto hay que pagar por ella.
lista = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85}
lista_1 = ("Platano 1.35", "Manzana 0.80", "Pera 0.85")
for i in range(len(lista_1)):
    print(lista_1[i], end="\t")
fruta = str(input("\nWhat fruit do you want?: "))
fruta = fruta.capitalize()
if fruta in lista:
    peso = float(input("How much?: "))
    precio_en_lista = lista.get(fruta)
    print(f'precio {precio_en_lista}')
    precio_fruta = peso * precio_en_lista
    precio_fruta =  round(precio_fruta,2)
    print(f'Por {peso} kg de {fruta}, tienes que pagar ${precio_fruta} ')
else:
    print(f"Lo siento, {fruta} no esta dentro de la lista")