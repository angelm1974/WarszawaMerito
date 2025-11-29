# moja_lista=[]
# moja_lista2=list()

# imiona = ["Anna", "Bartek", "Cezary", "Daria"]
# liczby = [1, 2, 3, 4, 5]
# mieszana = ["Ala", 3, "Ola", 7, True, 5.6]
# nested = [1, 2, [3, 4], imiona, [5, 6]]
# print(imiona[3])
# print(nested[3][1][-1])
# pizza=[]

# pizza1=input("Podaj składnik pizzy")
# pizza.append(pizza1)
# pizza2=input("Podaj składnik pizzy")
# pizza.append(pizza2)
# pizza3=input("Podaj składnik pizzy")
# pizza.append(pizza3)
# print(pizza)

# lista1 = [1, 2, 3]
# lista2 = [4, 5, 14,'Ala']
# # lista3=lista1+lista2
# lista1.extend(lista2)
# print(lista1)
# lista1.insert(3, "Ala")
# print(lista1)
# # lista1.remove("Ala")
# print(lista1.pop(6))
# print(lista1)

lista_petentow = ["Kowalski", "Nowak", "Wiśniewski", "Wójcik"]
lista_petentow[1] = "Kowalczyk"
lista_zalatwionych = []

while len(lista_petentow)>0:
    print(f"Załatwiam sprawę petenta: {lista_petentow[0]}")
    lista_zalatwionych.append(lista_petentow.pop(0))

print("Lista załatwionych petentów:")
print(lista_zalatwionych)
print("Lista petentów oczekujących:")
print(lista_petentow)