import json
import random as rnd
from datetime import datetime
import datetime
import csv
# with open("moj_tekst.txt",encoding="utf-8") as plik:
#     zawartosc = plik.read()

# # print(zawartosc)
# with open("dane.json", "r", encoding="utf-8") as plik:
#     dane = json.load(plik)

# rates = (dane['rates'])
# przetworzone = []
# for notowanie in rates:
#     # print(f" Numer notowania: {notowanie['no']}, \n\t-data notowania: {notowanie['effectiveDate']},\n\t-kurs: {notowanie['mid']}\n {50*'-'}")
#     przetworzone.append({'data': notowanie['effectiveDate'], 'kurs': notowanie['mid'], 'przygotowal': 'Jan Kowalski'})

# with open("przetworzone_dane.json", "w", encoding="utf-8") as plik_wyjsciowy:
#     json.dump(przetworzone, plik_wyjsciowy, ensure_ascii=False, indent=4)
# for i in range(100):
#     with open("dane_pralki.log", "a", encoding="utf-8") as plik:
#         # write a single line with ISO timestamp, a random event and a random value
#         plik.write(f"{i};{datetime.datetime.now().isoformat()};{rnd.choice(['START', 'STOP', 'BŁĄD'])};{rnd.randint(1, 80)}\n")
# suma = 0
# ilosc = 0
# with open("dane_pralki.log", encoding='utf-8') as plik:
#     csv_reader = csv.reader(plik, delimiter=';')
#     for row in csv_reader:
#         ilosc += 1
#         wynik = int(row[3])
#         suma += wynik
# print(f"Średnia wartość z {ilosc} pomiarów wynosi {suma/ilosc}")

with open("dane_pralki.log", encoding='utf-8') as plik:
    lines = plik.readlines()
    for line in lines:
        print(line.strip().split(";"))