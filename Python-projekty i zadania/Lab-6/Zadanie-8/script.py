import numpy as np

macierz = np.random.randint(0, 101, (5, 5))

print("Macierz:\n", macierz)

wieksze_20 = macierz[macierz > 20]
print("Liczba elementów > 20:", wieksze_20.size)

print("Średnia:", macierz.mean())
