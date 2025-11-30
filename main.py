import funkcje_i_metody as fm
import moje_narzedzia.importy_danych as id
id.przedsaw_sie()
# pole = fm.oblicz_pole_prostokata(5.5, 3.3)
# print(f"Pole prostokąta wynosi: {pole}")

# fm.witacz("Heniek")

# print(fm.iloczyn(2))

# fm.n_argumentow(1, 2, 3, 4, 5, "Ala", "ma", "kota", [1, 2, 3])
# wynik = fm.y(3)
# print(f"Wynik y(3): {wynik}")

# print(f"Kwadraty liczb z listy y:{list(fm.kwadraty)}")
# print(fm.super_fn(5, lambda x: x**3))
# print(fm.super_fn("Ala", lambda s: s[::-1]))
# print(fm.super_fn([1,2,3,4], lambda lst: [i*10 for i in lst]))

liczby_calkowite=[-1, -2, -3, 4, 5, 6, 7, -8, 9, 10,1,2,3,8
                  ]
a=sorted(liczby_calkowite, key=lambda x: abs(x),reverse=True)

print(a)