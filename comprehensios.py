# lista1=[]

# for i in range(20):
#     i=i*i
#     lista1.append(i)
# print(lista1)

# lista2=[i**2 for i in range(20)]
# print(lista2)

# dane=[1,2,3,4,5,6,7,8,9,10]
# parzyste=[{i:"parzysta"} for i in dane if i%2==0]
# print(parzyste)

# x=[1,2,3,4,5,6,7,8,9,10]
# y=[9,2,5,6,3,1,4,8,7,10]

# pary=[(i,j) for i in x for j in y if i>j]
# print(pary)
import random


# x=["A","B","C","D","E","F","G","H"]
# y=[1,2,3,4,5,6,7,8]

# pary=[{f"{i + str(j)}": random.choice(['skoczek', 'hetman', 'król','goniec c','goniec b','pion',''])} for i in x for j in y ]
# print(pary)

# lista1=[[j for j in range(5)] for i in range(3)]
# print(lista1)
# lista=[2,3,4,5,5,2,2,3,5,6,1,1,1,7,8,9,10]
# set1={i**2 for i in lista}
# print(set1)

text ="Python rządzi, Python radzi, Python nigdy Cię nie zdradzi"
# words=text.lower().replace(",","").replace(".","").split()
# print(set(words))

# words={text.lower().replace(",","").replace(".","") for text in text.split() if len(text)>4}
# print(words)

slownik={
    1:"papuga",
    2:"pies",
    3:"chomik",
    4:"papuga",
    5:"kot",
    6:"kot"    
}

odwrocony={value:key for key,value in slownik.items()}
print(odwrocony)