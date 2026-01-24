import numpy as np

macierz = np.zeros((5, 5), dtype=int)

macierz[0, :] = 1
macierz[-1, :] = 1
macierz[:, 0] = 1
macierz[:, -1] = 1

def zamien_0_1(tab):
    return 1 - tab

odwrocona = zamien_0_1(macierz)
print(macierz)

print(odwrocona)
