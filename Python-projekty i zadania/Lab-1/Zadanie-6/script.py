import random

CENA_PALIWA = 6.5
JEDNOSTKA_ZUZYCIA = 100

help(random.randint) # randint(a, b) method of random.Random instance, Return random integer in range [a, b], including both end points.

def oblicz_koszt_podróży():
    droga_losowa = random.randint(10, 100)

    przebyta_droga = float(input('Podaj przebytą drogę: ')  or droga_losowa)
    srednie_spalanie = float(input('Podaj średnie spalanie: ') or 0)
    cena_paliwa = float(input('Podaj aktualną cenę paliwa: ') or CENA_PALIWA)

    zuzycie_paliwa = przebyta_droga * srednie_spalanie / JEDNOSTKA_ZUZYCIA
    przewidywany_koszt = cena_paliwa * zuzycie_paliwa

    print(f'Dla przebytej drogi: {przebyta_droga}km, zużycie paliwa wynosi: {zuzycie_paliwa} litrów, a koszty szacowane są na {round(przewidywany_koszt, 2)} zł')

oblicz_koszt_podróży()

# Mamy tu jedną, uniwersalną funkcję, która łączy główne zadanie z zadaniem z podpunktu A. Funkcja pyta użytkownika o przebytą drogę, średnie spalanie oraz cenę paliwa.
# W przypadku, gdy użytkownik nie poda przebytej drogi - zostanie użyta losowa wartość. Tak samo, jeśli nie podano ceny paliwa - zostanie użyta cena przypisana na sztywno z zakresu globalnego.
