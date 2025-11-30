import wybor as wb
koszyk = []


def uruchamianie_procedury(liczba):
    match liczba:
        case 1:
            print("Skomponuj swoją pizzę")
        case 2:
            print("Wybierz pizze z menu")
            koszyk.append(wb.przetwarzanie_menu())
        case 3:
            print("Koszyk")
            for pizza in koszyk:
                print(f"- {pizza['nazwa']}")
        case 4:
            print("Czy na pewno chcesz zakończyć(T/N)?")
            if input().upper() == 'T':
                print("Koniec programu")
                exit()
        case _:
            print("Nieprawidłowy wybór, spróbuj ponownie.")
# Dołączyć zabezpieczenie przed złymi danymi wejściowymi
