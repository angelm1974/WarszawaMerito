
# a=123.4442

# a=round(a,2)
# print(a)
# print(type(a))

# lista_psow = ['Azor', 'Burek', 'Reksio', 'Azorek']

# # for i, nazwa in enumerate(lista_psow):
# #     print(f"{i+1}: {nazwa.upper()}")

# a="ala ma kota"
# n="Julek ma psa"

# x=" ".join([a,n])
# print(x)
# def piekne_drukowanie(tekst=None):
#     if tekst is None:
#         tekst = input("Podaj tekst do wydrukowania: ")
#     print("*" * (len(tekst) + 4))
#     print(f"* {tekst} *")
#     print("*" * (len(tekst) + 4))

# piekne_drukowanie("Witaj świecie!")

# def suma():
#     while True:
#         try:
#             a = int(input("Podaj pierwszą liczbę: "))
#             b = int(input("Podaj drugą liczbę: "))
#             return a + b
#         except ValueError:
#             print("Proszę podać poprawną liczbę.")


# wynik = suma()
# print(f"Wynik dodawania: {wynik}")

def oblicz_pole_prostokata(dlugosc: float, szerokosc: float) -> float:
    """Funkcja oblicza pole prostokąta.

    Args:
        dlugosc (float): Długość prostokąta.
        szerokosc (float): Szerokość prostokąta.

    Returns:
        float: Pole prostokąta.
    """
    return dlugosc * szerokosc
# pole = round(oblicz_pole_prostokata(4.4,4.2),2)

# print(f"Pole prostokąta wynosi: {pole}")


def witacz(imie: str = "Użytkowniku") -> None:
    """Funkcja wita się z użytkownikiem.
    Args:
        imie (str): Imię użytkownika.
    """
    print(f"Witaj, {imie}!")

def iloczyn(a: float, b: float =4) -> float:
    """Funkcja zwraca iloczyn dwóch liczb.

    Args:
        a (float): Pierwsza liczba.
        b (float): Druga liczba.

    Returns:
        float: Iloczyn liczb a i b.
    """
    if b<3:
        while True:
            try:
                b = int(input("Podaj drugą liczbę większą od 3: "))
                if b>=3:
                    break
            except ValueError:
                print("Proszę podać poprawną liczbę.")
    return a * b

def n_argumentow(*args) -> None:
    """Funkcja drukuje podane argumenty.

    Args:
        *args: Dowolna liczba argumentów.
    """
    suma = 0
    text=""
    for i, arg in enumerate(args):
        # print(f"Argument {i+1}: {arg}")
        if isinstance(arg, (int, float)):
            suma += arg
        elif isinstance(arg, str):
            text += arg + " "
            
    print(f"Suma liczb: {suma}")
    print(f"Połączony tekst: {text.strip()}")
    
y =lambda x: x*2

uv = lambda s: s.upper()
y=[1,2,3,4,5]
kwadraty = map(lambda x: x**2, y)

def super_fn(x,fn):
    return fn(x)