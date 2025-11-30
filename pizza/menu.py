
# Dołączyć zabezpieczenie przed złymi danymi wejściowymi
def menu():
    print("Welcome to the Pizza Menu!")
    print("1. Skomponuj swoją pizzę")
    print("2. Wybierz pizze z menu")
    print("3. Koszyk")
    print("4. Zakończ")
    choice = int(input("Wybierz liczbe od 1 do 4: "))
    return choice