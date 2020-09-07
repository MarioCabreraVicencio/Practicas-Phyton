# Compara una palabra introducida con una ya establecida.
def password():
    password = "estudioenplatzi"
    password_usuario = str(input("Escribe la contraseña correcta: "))

    while password_usuario != password:
        password_usuario = input("Escribe la contraseña correcta: ")
    print("This is the correct password")

def run():
    password()
if __name__ == "__main__":
    run()