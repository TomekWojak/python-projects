import pandas as pd

dane = {
    "nrID": [1,2,3,4,5],
    "imię": ['Anna', 'Jan','Katarzyna','Tomasz','Michał'],
    "nazwisko": ['Kowalska','Nowak','Wiśniewska','Kaczmarek','Zieliński'],
    "stanowisko": ['Manager', 'Programista', 'Konsultant', 'Programista', 'Manager'],
    "wiek": [35,28,40,30,45],
    "pensja":[8000,4500,6000,5500,7000]
}

df = pd.DataFrame(dane)
pensja_wieksza_od_5000 = df[df["pensja"] > 5000]

# a)
print(f'{pensja_wieksza_od_5000} \n')

# b)
sortowanie_wg_wieku = df.sort_values(by="wiek")
print(f'{sortowanie_wg_wieku} \n')

# c)
srednia_pensja = df.groupby("stanowisko")["pensja"].mean()
print(f'{srednia_pensja} \n')

# d)
dane_2 = {
    "nrID": [2, 3],
    "nowe_stanowisko": ['Starszy Programista', 'Senior Konsultant'],
    "nowa_pensja": [6000, 7000]
}
dane_po_zmianie = pd.DataFrame(dane_2)

dane_polaczone = pd.merge(df, dane_po_zmianie, on="nrID")
print(dane_polaczone)

# e)
dane_polaczone.to_csv("pracownicy_zmiany.csv", index=False, encoding="utf-8")

# f)
zmiany = pd.read_csv("pracownicy_zmiany.csv")
print(zmiany)