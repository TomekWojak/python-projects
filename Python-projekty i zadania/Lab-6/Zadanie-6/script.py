import numpy as np

A = np.zeros((3, 3), dtype=int)
A[2, :] = 1
print("A:\n", A)

B = np.zeros((3, 3), dtype=int)
B[1:, 1] = 1
print("B:\n", B)

C = np.zeros((3, 3), dtype=int)
C[1:, :] = 1
print("C:\n", C)

D = np.zeros((3, 3), dtype=int)
D[0:2, [0, 2]] = 1
print("D:\n", D)

E = np.zeros((3, 3), dtype=int)
E[1:, 1:] = 1
print("E:\n", E)
