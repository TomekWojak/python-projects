HASLO = 'pk47!jy0893'

def sprawdzJakoscHasla():
    sprawdzanaWartosc = "!" in HASLO

    if len(HASLO) >= 11 and sprawdzanaWartosc:
        print('Hasło jest poprawne')
    else:
        print('Hasło jest niepoprawne')

sprawdzJakoscHasla()