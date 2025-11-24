liczby_pierwsze = []
liczba = 0

def jest_liczba_pierwsza(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


while True:
    jest_pierwsza = jest_liczba_pierwsza(liczba)
    if(jest_pierwsza): liczby_pierwsze.append(str(liczba))

    liczba += 1
    if(len(liczby_pierwsze) == 10):
        break

print(",".join(liczby_pierwsze))