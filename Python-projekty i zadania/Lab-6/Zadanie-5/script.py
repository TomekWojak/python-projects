import numpy as np

tab4_2d = np.random.rand(5, 5)

print("Macierz:\n", tab4_2d)
print("Max:", tab4_2d.max())
print("Min:", tab4_2d.min())

print("Max w wierszach:", tab4_2d.max(axis=1))
print("Max w kolumnach:", tab4_2d.max(axis=0))

print("Suma w wierszach:", tab4_2d.sum(axis=1))