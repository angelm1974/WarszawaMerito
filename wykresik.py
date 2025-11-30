
#konieczne zainstalowanie biblioteki matplotlib
# pip install matplotlib

import matplotlib.pyplot as plt


dane=[(1,5), (2,10), (3, 33), (4, 20), (5, 15), (6, 30)]

plt.plot(dane)
plt.title("Prosty wykres liniowy")
plt.xlabel("Oś X")
plt.ylabel("Oś Y")
plt.legend(["Dane 1"])
plt.grid()
plt.show()