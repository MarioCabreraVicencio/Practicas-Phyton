def password():
    print("Welcome to comparator of password")
    print()
    your_password = str(input("Write your password: "))
    # your_password = your_password.lower()
    # your_password = your_password.strip()
    original_password = str("Holasoymarioestudioenplatzi")

    if your_password == original_password:
        print("That is your correct password")
    else:
        print("This isn't your password")

def run():
    password()

if __name__ == "__main__":
    run()
