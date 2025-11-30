# moj_slownik = {
#     'kot': 'cat',
#     'pies': 'dog'
# }

# drugi={
#     1: 'jeden',
#     2: 'dwa',
#     3: 'trzy'
# }

# drugi[4]='cztery'
# print(drugi)

# moj_slownik['ryba']=["fish", "aquatic animal",12, True]
# moj_slownik['kot']=["feline", "small animal", 8, False]
# moj_slownik['pies']=["canine", "domestic animal", 10, True]
# moj_slownik['ptak']=["bird",  1]
# print(moj_slownik.get("koń", "Brak takiego klucza"))

# for key, value in moj_slownik.items():
#     try:
#         print(f"{key} - waga {value[2]} kg")
#     except IndexError:
#         print(f"{key} - brak informacji o wadze")

slownik1={
    'a': 1,
    'b': 2,
    'c': 3
}

slownik1['d']=4
slownik1['a']=10
r=slownik1.get('a', 5)
# print(r)
#a=list(slownik1.keys())
a=list(slownik1.values())
# print(a)
print(dir(dict))