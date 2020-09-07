# Imprime valores de un diccionarios llamados por teclado.
months = {1: "Enero", 2: "Febrero", 3: "Marzo"}
date = input("Escribe la fecha de hoy en formato dd/mm/aaaa: ")
date = date.split("/") 
print(f'Hoy es {date[0]} de {months[int(date[1])]} del {date[2]}')