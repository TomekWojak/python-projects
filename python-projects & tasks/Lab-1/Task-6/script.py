import random

CENA_PALIWA = 6.5
JEDNOSTKA_ZUZYCIA = 100

help(random.randint) # randint(a, b) method of random.Random instance, Return random integer in range [a, b], including both end points.

def oblicz_koszt_podróży():
    droga_losowa = random.randint(10, 100)

    przebyta_droga = int(input('Podaj przebytą drogę: ')  or droga_losowa)
    srednie_spalanie = int(input('Podaj średnie spalanie: '))
    cena_paliwa = int(input('Podaj aktualną cenę paliwa: ') or CENA_PALIWA)

    zuzycie_paliwa = przebyta_droga * srednie_spalanie / JEDNOSTKA_ZUZYCIA
    przewidywany_koszt = cena_paliwa * zuzycie_paliwa

    print(f'Zużycie paliwa wynosi: {zuzycie_paliwa} litrów, a koszty szacowane są na {round(przewidywany_koszt, 2)} zł')

oblicz_koszt_podróży()