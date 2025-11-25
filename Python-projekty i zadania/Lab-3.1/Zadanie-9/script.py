def przywitaj_osobe(imie):
    print(f'Witaj {imie}')
przywitaj_osobe('Jan')

def wyswietl_wiek(wiek):
    print(f'Twój wiek to: {wiek}')
wyswietl_wiek(10)

def wyswietl_inicjaly(imie, nazwisko):
    print(f'{imie[0]}.{nazwisko[0]}')
wyswietl_inicjaly('Jan', 'Kowalski')

def pomnoz_string(str):
    print(f'\n{str}' * 5)
pomnoz_string('String')

def polacz_stringi(str1, str2):
    str3 = str1 + ' ' + str2
    print(str3)
polacz_stringi('Jan', 'Kowalski')

def polacz_stringi_v2(str1, str2):
    polowa = len(str1 + str2) // 2
    str3 = (str1 + str2)[:polowa]
    print(str3)

polacz_stringi_v2('Jan', 'Kowalski')

