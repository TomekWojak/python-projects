def obliczSrednia(*liczby):
    srednia = sum(liczby) / len(liczby) if len(liczby) != 0 else None

    return srednia

print(obliczSrednia(1,2,3,4,5))
print(obliczSrednia(123,456,789))
print(obliczSrednia())
