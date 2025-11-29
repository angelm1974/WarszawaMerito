pusta_tupla=()
print(type(pusta_tupla))  # <class 'tuple'>
tupla_liczb=(1,2,3,4,5)
print(tupla_liczb[2])  # 3
dane=("Ala", 3, True, 5.6)
# tuplaa[1]=4  # TypeError: 'tuple' object does not support item assignment
dane=list(dane)  # ['Ala', 3, True, 5.6]
print(type(list(dane)))  # <class 'list'>
dane[1]=4  # lista i wstawienei zadziała
print(dane)
dane=tuple(dane)  # z powrotem na tuplę
print(type(dane))  # <class 'tuple'>