paliwo = 100
paliwo_zużyte_na_s = 10
czas = 0

while paliwo > 0:
    paliwo -= paliwo_zużyte_na_s
    print(f'Pozostało {paliwo} litrów paliwa')
    czas += 1

    if(paliwo == 0): print('Koniec lotu')

print(f'Lot trwał {czas} sekund')