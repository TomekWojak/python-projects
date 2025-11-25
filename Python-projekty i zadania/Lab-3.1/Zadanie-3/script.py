ulice = ['Jagodowa','Lipowa', 'Kwiatowa', 'Kasztanowa', 'Polna']

liczba_blokow = 5
liczba_lokali = 10
liczba_adresow = 0

for ulica in ulice:
    liczba_adresow += liczba_lokali * liczba_blokow

print(f'Łączna liczba adresów: {liczba_adresow}')