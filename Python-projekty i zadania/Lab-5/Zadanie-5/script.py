import pandas as pd
dane = {
    "nrAlbumu": [1,2,3,4,5],
    "imię": ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    "nazwisko": ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    "ocena": [4.5, 3.0, 5.0, 4.0, 2.5],
    "wiek": [22,21,24,23,25]
}

df = pd.DataFrame(dane)

# a)
print(f'{df[df["ocena"] > 4]} \n')

# b)
print(f'{df.sort_values(by="wiek")} \n')

# c)
srednia_ocena = df.groupby("ocena")["wiek"].mean()
print(f'{srednia_ocena} \n')

# d)
dane_2 = {
    "nrAlbumu": [2, 5],
    "ocena_poprawa": [4.0, 3.5]
}
dane_poprawa = pd.DataFrame(dane_2)
print(f'{dane_poprawa} \n')

dane_polaczone = pd.merge(df, dane_poprawa, on="nrAlbumu", how="left")
print(f'{dane_polaczone} \n')

# e)
dane_polaczone.to_csv("uczniowie-dane.csv", index=False, encoding="utf-8")

# f)
zmiany = pd.read_csv("uczniowie-dane.csv")
print(f'{zmiany} \n')

# g)
df.loc[len(df)] = [6, "Adam", "Kowalczyk", 4.0, 23]
print(f'{df} \n')

# h)
print(f'{df['ocena'].unique()} \n')

# i)
print((df["ocena"] == 5).sum())

