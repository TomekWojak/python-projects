nazwaPliku = input('Podaj nazwę pliku: ') or 'Raport_maj.xlsx'

def sprawdzFormatPliku():
    formatToXlsx = nazwaPliku.endswith('.xlsx')

    if formatToXlsx:
        print('Tak')
    else:
        print('Nie')

sprawdzFormatPliku()