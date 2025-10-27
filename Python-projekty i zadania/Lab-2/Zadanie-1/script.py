def obsluzUzytkownika():
    while True:
        wartoscUzytkownika = input("Podaj liczbę zdobytych punktów: ")
        if not wartoscUzytkownika:
            print('Proszę podać jakąś wartość!')
            continue
        else:
            try:
                wynik = float(wartoscUzytkownika)
                sprawdzCzyZdano(wynik)
                break
            except ValueError:
                print('Podano niepoprawną wartość!')


def sprawdzCzyZdano(wynik):
    if wynik > 80:
        print('Gratulacje świetnego wyniku, zaliczasz egzamin w terminie zerowym')
    elif(wynik <= 80 and wynik >= 50):
        print('Gratulacje, zaliczasz egzamin, jeśli chcesz masz możliwość poprawy wyniku')
    else:
        print('Niestety, egzamin nie zaliczony, musisz podejść do niego ponownie')

obsluzUzytkownika()