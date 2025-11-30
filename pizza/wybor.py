def otworz_json(nazwa_pliku):
    import json
    with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
        dane = json.load(plik)
    return dane

def zapisz_json(nazwa_pliku, dane):
    import json
    with open(nazwa_pliku, 'w', encoding='utf-8') as plik:
        json.dump(dane, plik, ensure_ascii=False, indent=4)

def przetwarzanie_menu():
    dane=otworz_json("menu.json")
    for index, pizza in enumerate(dane):
        print(f"{index + 1}. {pizza['nazwa']}")
    wybor = int(input("Wybierz numer pizzy z menu: "))
    if 1 <= wybor <= len(dane):
        print(f"Wybrałeś pizzę: {dane[wybor - 1]['nazwa']}")
    else:
        print("Nieprawidłowy wybór.")
    return dane[wybor - 1]