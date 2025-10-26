import random

CENA_PALIWA = 6.5
SREDNIE_SPALANIE = 7
JEDNOSTKA_ZUZYCIA = 100

def oblicz_koszt_podróży():
    droga_losowa = random.randint(10, 100)

    przebyta_droga = float(input('Podaj przebytą drogę: ')  or droga_losowa)
    srednie_spalanie = float(input('Podaj średnie spalanie: ') or SREDNIE_SPALANIE)
    cena_paliwa = float(input('Podaj aktualną cenę paliwa: ') or CENA_PALIWA)

    zuzycie_paliwa = przebyta_droga * srednie_spalanie / JEDNOSTKA_ZUZYCIA
    przewidywany_koszt = cena_paliwa * zuzycie_paliwa

    print(f'Dla przebytej drogi: {przebyta_droga}km, zużycie paliwa wynosi: {zuzycie_paliwa} litrów, a koszty szacowane są na {round(przewidywany_koszt, 2)} zł')

oblicz_koszt_podróży()

# Mamy tu jedną, uniwersalną funkcję, która łączy główne zadanie z zadaniem z podpunktu A. Funkcja pyta użytkownika o przebytą drogę, średnie spalanie oraz cenę paliwa.
# W przypadku, gdy użytkownik nie poda przebytej drogi - zostanie użyta losowa wartość. Tak samo, jeśli nie podano ceny paliwa - zostanie użyta cena przypisana na sztywno z zakresu globalnego.
