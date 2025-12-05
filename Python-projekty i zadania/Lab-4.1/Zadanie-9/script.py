def obliczNtyWyrazCiagu(n):
    # F(n) = F(n-1) + F(n-2)
    if n == 0: return 0
    if n == 1: return 1

    return obliczNtyWyrazCiagu(n-1) + obliczNtyWyrazCiagu(n-2)

ntyWyrazCiagu = obliczNtyWyrazCiagu(10)
print(ntyWyrazCiagu)