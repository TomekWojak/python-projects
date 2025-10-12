import random

CENA_PALIWA = 6.5
def oblicz_srednie_spalanie():
    przebyta_droga = float(input('Podaj przebytą drogę: '))
    srednie_spalanie = float(input('Podaj średnie spalanie: '))

    przewidywane_zuzycie = przebyta_droga * srednie_spalanie / 100
    przywidywany_koszt_podrozy = przewidywane_zuzycie * CENA_PALIWA

    print(f'Przewidywane zużycie paliwa w Twoim przypadku wynosi: {przewidywane_zuzycie} litrów \nSzacowane koszta podróży wynoszą: {round(przywidywany_koszt_podrozy, 2)} PLN')

oblicz_srednie_spalanie()

help(random.randint) # randint(a, b) method of random.Random instance, Return random integer in range [a, b], including both end points.

def oblicz_koszty_eksploatacji():
    przebyta_droga = random.randrange(10, 100)

    srednie_spalanie = float(input('Podaj średnie spalanie: '))
    cena_paliwa = float(input('Podaj cenę paliwa za 1 litr: '))

    przewidywane_zuzycie = przebyta_droga * srednie_spalanie / 100
    przywidywany_koszt_podrozy = przewidywane_zuzycie * cena_paliwa

    print(f'Przewidywane zużycie paliwa: {przewidywane_zuzycie} litrów \nSzacowane koszta: {round(przywidywany_koszt_podrozy, 2)} PLN')

oblicz_koszty_eksploatacji()