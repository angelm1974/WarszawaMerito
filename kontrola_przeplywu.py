import random
import os
a=random.randint(1,10)

# if a > 5:
#     print("a is greater than 5")
    
# print("koniec programu 1")

# if a==2:
#     print("a jest = 2")
# elif a>2 and a<5:
#     if a==3:
#         print("a jest = 3")
#     else:
#         print("a jest większe niż 2, ale mniejsze niż 5 i nie jest równe 3")
# elif a==8:
#     print("a jest = 8")
# else:
#     print("a nie jest ani 2, ani 3, ani 8")

# a=[1,2,3,4,5,0]

# for i in a:
#     if i%2==0:
#         print(f"{i} jest parzyste")
#     else:
#         print(f"{i} jest nieparzyste")


# zwierzeta = ['kot', 'pies', 'chomik', 'ryba', 'ptak']
# for zwierze in zwierzeta:
#     if zwierze == 'ryba':
#         continue
#     elif zwierze == 'chomik':
#         zwierzeta[2]='golden hamster'
       
#     print(f"Lubię {zwierze}")
# print(zwierzeta)


# for i in range(1,11):
#     print(i)


lista1=list(range(1,21))
# while lista1:
#     liczba=lista1.pop()
#     print(liczba)
#     if liczba==15:
#         break

# for i in lista1:
#     if i%3==0:
#         continue
#     print(i)

# while True:
#     liczba=random.randint(1,100)
#     print(liczba)
#     if liczba==50:
#         print("Wylosowano 50, koniec pętli")
#         break


# while True:
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print("Menu:")
#     print("1. Opcja 1\n2. Opcja 2\n3. Wyjście")
#     wybor=input("Wybierz opcję (1-3): ")
#     if wybor=='1':
#         print("Wybrano opcję 1")
#         input("Naciśnij Enter, aby kontynuować...")
#     elif wybor=='2':
#         print("Wybrano opcję 2")
#         input("Naciśnij Enter, aby kontynuować...")
#     elif wybor=='3':
#         print("Koniec programu")
#         break
#     else:
#         print("Nieprawidłowy wybór, spróbuj ponownie.")
#         input("Naciśnij Enter, aby kontynuować...")
#     print("Dalsza część pętli")
    
# print("Koniec programu 2")


# wartość = 5

# match wartość:
#     case 1:
#         print("Wartość to jeden")
#     case 2 | 3 | 4:
#         print("Wartość to dwa, trzy lub cztery")
#     case _ if wartość > 4 and wartość < 10:
#         print("Wartość jest większa niż cztery, ale mniejsza niż dzięć")
#     case _:
#         print("Wartość nie pasuje do żadnego przypadku")

# input_komenda = input("Podaj komendę (start, stop, pause): ")

# match input_komenda:
#     case 'start':
#         print("Uruchamianie programu...")
#     case 'stop':
#         print("Zatrzymywanie programu...")
#     case 'pause':
#         print("Wstrzymywanie programu...")
#     case _:
#         print("Nieznana komenda")
dane="abc"


match dane:
    case int():
        print("Dane są liczbą całkowitą")
    case str():
        print("Dane są łańcuchem znaków")
    case float():
        print("Dane są liczbą zmiennoprzecinkową")
    case _:
        print("Nieznany typ danych")

print(os.path.abspath(os.curdir))