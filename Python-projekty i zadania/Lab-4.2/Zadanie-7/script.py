import datetime
# ostatnie laby: 29.11.2025 8:00
# kolokwium 14.02.2026
obecnaData = datetime.datetime.now()

def obliczCzasOdOstatnichLabow():
    dataOstatnichLabow = datetime.datetime(2025, 11, 29, 8)

    czasOdOstatnichLabow = obecnaData - dataOstatnichLabow
    dni = czasOdOstatnichLabow.days
    godziny = czasOdOstatnichLabow.seconds // 3600
    minuty = (czasOdOstatnichLabow.seconds % 3600) // 60

    print(f'Od ostatnich laboratoriów minęło {dni} dni, {godziny} godzin i {minuty} minut')

def obliczCzasDoKolokwium():
    dataKolokwium = datetime.datetime(2026, 2, 14, 16, 20)
    czasDoKolokwium = dataKolokwium - obecnaData
    dni = czasDoKolokwium.days
    miesiace = czasDoKolokwium.days // 30
    godziny = czasDoKolokwium.seconds // 3600
    minuty = (czasDoKolokwium.seconds % 3600) // 60

    print(f'Do kolokwium zostało {dni} dni, tj. {miesiace} miesiące, {godziny} godzin i {minuty} minut')


obliczCzasOdOstatnichLabow()
obliczCzasDoKolokwium()
