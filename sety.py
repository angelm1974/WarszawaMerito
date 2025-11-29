import csv

set1 = set()

# miasta = ['Warszawa', 'Kraków', 'Gdańsk', 'Warszawa', 'Poznań', 'Kraków']
# unikalne_miasta = set(miasta)
# print(unikalne_miasta)

with open('moj_tekst.txt', 'r', encoding='utf-8') as plik:
    zawartosc = plik.read()

zawartosc = zawartosc.lower()
zawartosc = zawartosc.replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace('\n', ' ')   
slowa = zawartosc.split()
slowa = set(slowa)
slowa =list(slowa)
slowa.sort(key=len)

print(slowa)
# print(f"Liczba unikalnych słów w pliku: {len(slowa)}")
# print("cia" in slowa)
# print("cia" in zawartosc)


csv_file = 'dane.csv'
with open(csv_file, 'w') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Słowo', 'Długość'])
    for slowo in slowa:
        writer.writerow([slowo, len(slowo)])
