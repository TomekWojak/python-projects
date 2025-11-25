
# Podpunkt a
def oblicz_srednia_liczbe_pkt():
    punkty = []
    licznik = 1
    while True:
        try:
            n = int(input('Podaj liczbę studentów: '))
            break
        except ValueError:
            print('Podaj poprawną wartość!')
    while licznik <= n:
        try:
            l_punktow = float(input(f'Podaj liczbę punktów studenta {licznik}: '))
            licznik += 1

            if l_punktow < 0 or l_punktow > 100:
                continue
            punkty.append(l_punktow)
        except ValueError:
            print('Niepoprawna wartość')

    if(len(punkty) == 0):
        print('Żaden z punktów nie pasował do kryteriów')
        return

    srednia = sum(punkty) / len(punkty)

    print(f'Średnia liczba punktów w grupie wynosi {srednia}')

# oblicz_srednia_liczbe_pkt()


# Podpunkt b
def oblicz_srednia_liczbe_pkt_v2():
    punkty = []
    licznik = 1
    while True:
        try:
            n = int(input('Podaj liczbę studentów: '))
            break
        except ValueError:
            print('Podaj poprawną wartość!')
    while True:
        if licznik > n: break
        try:
            l_punktow = float(input(f'Podaj liczbę punktów studenta {licznik}: '))
            licznik += 1

            if l_punktow < 0 or l_punktow > 100:
                continue
            punkty.append(l_punktow)
        except ValueError:
            print('Niepoprawna wartość')

    if(len(punkty) == 0):
        print('Żaden z punktów nie pasował do kryteriów')
        return

    srednia = sum(punkty) / len(punkty)

    print(f'Średnia liczba punktów w grupie wynosi {round(srednia, 2)}')

# oblicz_srednia_liczbe_pkt_v2()